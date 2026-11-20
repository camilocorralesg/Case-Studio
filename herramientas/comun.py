"""Lo que comparten las herramientas: dónde está el sitio, cómo se sirve, cómo se abre el navegador y dónde quedan las capturas.

Variables de entorno (todas opcionales):
  CASE_URL      otra dirección para el sitio (por defecto se sirve dist/, lo que deja npm run build, en http://127.0.0.1:8765)
  CASE_CHROME   ruta a otro Chrome/Chromium (por defecto, el Chromium de Playwright)
  CASE_SIN_RED  si vale 1, no se piden las fuentes de Google (para trabajar sin conexión; se ven las de reserva)
"""
import functools, http.server, os, socket, sys, tempfile, threading
from pathlib import Path

AQUI = str(Path(__file__).resolve().parent)
RAIZ = Path(__file__).resolve().parents[1]
SITIO = RAIZ / "dist"          # lo que arma Astro (npm run build)
I18N = RAIZ / "src" / "i18n"
SALIDA = str(Path(AQUI) / "salida")
TMP = os.path.join(tempfile.gettempdir(), "case-studio")
os.makedirs(SALIDA, exist_ok=True)
os.makedirs(TMP, exist_ok=True)
PUERTO = 8765
URL = os.environ.get("CASE_URL", f"http://127.0.0.1:{PUERTO}/index.html")
SECCIONES = 11          # hero, servicios, fórmula, rediseño, proyectos, marcas, proceso, redes, preguntas, cierre y contacto

try:  # la consola de Windows no siempre habla UTF-8
    sys.stdout.reconfigure(encoding="utf-8")
except Exception:
    pass


class _Servidor(http.server.ThreadingHTTPServer):
    request_queue_size = 128     # las cinco revisiones piden a la vez; con la cola de 5 que trae por defecto, rechaza conexiones


class _Callado(http.server.SimpleHTTPRequestHandler):
    def log_message(self, *a):
        pass


def _servir():
    """Sirve dist/ en segundo plano si nadie lo está sirviendo ya."""
    if "CASE_URL" in os.environ:
        return
    with socket.socket() as s:
        s.settimeout(1)
        if s.connect_ex(("127.0.0.1", PUERTO)) == 0:
            return
    srv = _Servidor(("127.0.0.1", PUERTO), functools.partial(_Callado, directory=str(SITIO)))
    threading.Thread(target=srv.serve_forever, daemon=True).start()


_servir()

# Lleva el scroll a un punto de una sección: avance 0 = empieza, 1 = termina (las secciones altas se recorren con el scroll).
IR = "([s, p]) => { const m = document.querySelector('#stage ' + s); if (!m) return false; const top = m.getBoundingClientRect().top + scrollY; scrollTo({ top: top + Math.max(0, m.offsetHeight - innerHeight) * p, behavior: 'instant' }); return true; }"
# La sección que está en la mitad de la pantalla y qué tanto de ella se ha recorrido.
DONDE = "() => { const mid = innerHeight / 2; let id = '', r = 0; document.querySelectorAll('#stage .v > section').forEach((s) => { const b = s.getBoundingClientRect(); if (b.top <= mid) { id = s.id || s.className.split(' ').pop(); r = (mid - b.top) / b.height; } }); return [id, Math.round(r * 100) / 100]; }"


async def navegador(pw):
    exe = os.environ.get("CASE_CHROME")
    args = ["--enable-unsafe-swiftshader", "--ignore-gpu-blocklist"]
    if exe:
        return await pw.chromium.launch(executable_path=exe, args=args + ["--use-angle=swiftshader"])
    return await pw.chromium.launch(args=args)


async def fuentes(page):
    """Con CASE_SIN_RED=1 responde vacío a las fuentes de Google para no esperar por ellas."""
    if os.environ.get("CASE_SIN_RED") != "1":
        return

    async def vacio(route):
        await route.fulfill(status=200, body="", headers={"content-type": "text/css", "access-control-allow-origin": "*"})

    await page.route("https://fonts.googleapis.com/**", vacio)
    await page.route("https://fonts.gstatic.com/**", vacio)


async def listo(page):
    await page.wait_for_selector("#stage #proceso", state="attached", timeout=20000)


async def pagina(b, ancho=1440, alto=900, reducido=False, ingles=False, sin_ayudas=True):
    """Abre el sitio en una pestaña nueva y espera a que esté montado. Devuelve (page, errores).
    sin_ayudas esconde los selectores de trabajo (fuentes, opciones en revisión) para que no salgan en las capturas."""
    ctx = await b.new_context(viewport={"width": ancho, "height": alto}, reduced_motion="reduce" if reducido else "no-preference")
    page = await ctx.new_page()
    errores = []
    page.on("pageerror", lambda e: errores.append(str(e)[:200]))
    page.on("console", lambda m: errores.append(m.text[:200]) if m.type == "error" else None)
    await fuentes(page)
    # sola, la página carga en menos de un segundo; con las cinco revisiones abriendo navegadores a la vez en un equipo
    # ocupado puede pasar de los 30 s que espera Playwright por defecto, y eso no dice nada del sitio
    await page.goto(URL, timeout=120000)
    await listo(page)
    await page.wait_for_timeout(900)
    if ingles:
        await cambiar_idioma(page, "en")
    if sin_ayudas:
        await page.add_style_tag(content=".proto-picker{display:none!important}")
    return page, errores


async def cambiar_idioma(page, codigo):
    """Cambia de idioma y espera a que la página, que se vuelve a dibujar, regrese a su sitio."""
    await page.evaluate("c => window.LANG.set(c)", codigo)
    await listo(page)
    y = -1
    for _ in range(30):
        await page.wait_for_timeout(150)
        n = await page.evaluate("scrollY")
        if n == y:
            break
        y = n
    await page.wait_for_timeout(300)


# Usa el formulario como una persona: lo envía vacío, marca todas las opciones, escribe y lo envía.
FORMULARIO = """async () => {
  const f = document.querySelector('#stage form'); if (!f) return; const sub = f.querySelector('[type=submit]');
  sub && sub.click(); await new Promise(r => setTimeout(r, 250));
  for (const i of f.querySelectorAll('input[type=checkbox],input[type=radio]')) { i.click(); await new Promise(r => setTimeout(r, 25)); }
  const set = (el, v) => { el.value = v; el.dispatchEvent(new Event('input', {bubbles:true})); el.dispatchEvent(new Event('change', {bubbles:true})); };
  const n = f.querySelector('#c-name'), m = f.querySelector('#c-mail'); n && set(n, 'Ana'); m && set(m, 'ana@correo.example');
  await new Promise(r => setTimeout(r, 200)); sub && sub.click(); await new Promise(r => setTimeout(r, 400));
}"""


async def recorrer(page, paso=240, espera=40):
    total = await page.evaluate("document.documentElement.scrollHeight")
    y = 0
    while y < total:
        await page.evaluate("y => scrollTo({ top: y, behavior: 'instant' })", y)
        await page.wait_for_timeout(espera)
        y += paso


async def abrir_visor(page):
    """Abre el detalle de un proyecto (el botón "Ver proyecto" de la rueda) y lo cierra. Las marcas no tienen detalle."""
    for sel in ["#proyectos .ru-open"]:
        el = page.locator("#stage " + sel).first
        if await el.count():
            await el.evaluate("e => e.click()")
            await page.wait_for_timeout(700)
            await page.keyboard.press("Escape")
            await page.wait_for_timeout(300)
