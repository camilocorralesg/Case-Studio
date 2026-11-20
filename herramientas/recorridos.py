"""python herramientas/recorridos.py [id ...] [--celular | --computador] [--muestra]
   -> recorre cada proyecto de Proyectos en su sitio real y guarda sus tiras de pantallas en public/assets/: n pantallas
      repartidas por la página y la primera otra vez al final, para que la vuelta no salte.
      - celular (390 x 844, a 2x): tour-<id>-cel-390.webp, tour-<id>-cel.webp (585) y tour-<id>-cel-780.webp. La rueda usa la de
        390 o la de 585 según la pantalla; el detalle, la de 780.
      - computador (1440 x 745, a 2x): tour-<id>.webp (800) y tour-<id>-1600.webp. La rueda y el detalle eligen según la
        pantalla (2x en las retina). Y pf-<id>.jpg, la primera pantalla a 320, para las miniaturas del detalle.
      Sin bandera hace las dos. Deja hojas para mirarlas en herramientas/salida/recorridos-cel.png y recorridos-pc.png.

Los proyectos (id, dirección y cuántas pantallas) salen de window.PROJECTS en src/partes/visor.astro; con ids, solo esos.
Cada pantalla se ajusta al título de sección más cercano, para que no quede cortada a la mitad de una parte. Desde la segunda
pantalla se esconde la barra fija de arriba del sitio (su menú), que si no se repetiría en todas.
Si un sitio muestra un aviso de cookies, se rechazan las que no son necesarias. No se inicia sesión ni se envía nada, salvo la
verificación de edad de un sitio para adultos (EDAD), que se pasa con una fecha de prueba.
Con --muestra no guarda tiras: deja en herramientas/salida/muestra-<id>-<modo>.png doce pantallas repartidas por la página, para
escoger puntos a mano (PUNTOS, en fracciones de la página).
Lee la red: los sitios tienen que estar en línea."""
import asyncio, io, re, sys
from PIL import Image
import comun
from playwright.async_api import async_playwright

# lo que se imita: el ancho y alto de la pantalla, a 2x, y los anchos en que se guarda cada tira (el primero es el de src)
MODOS = {
    'cel': {'w': 390, 'h': 844, 'movil': True, 'ua': ('Mozilla/5.0 (iPhone; CPU iPhone OS 17_5 like Mac OS X) AppleWebKit/605.1.15 '
                                                      '(KHTML, like Gecko) Version/17.5 Mobile/15E148 Safari/604.1'),
            'anchos': {585: 'tour-{id}-cel.webp', 390: 'tour-{id}-cel-390.webp', 780: 'tour-{id}-cel-780.webp'}},
    'pc': {'w': 1440, 'h': 745, 'movil': False, 'ua': None,
           'anchos': {800: 'tour-{id}.webp', 1600: 'tour-{id}-1600.webp'}},
}
DPR = 2
POSTER = 320                     # la primera pantalla del computador, para las miniaturas de anterior y siguiente del detalle
# solo los botones que dicen que no: nunca se aceptan cookies por el usuario
NO = re.compile(r'^(rechazar( todas?| todo)?|solo (las )?(necesarias|esenciales)|denegar|no acepto|decline|reject( all)?|only necessary)$', re.I)
SALIDA = comun.RAIZ / 'public' / 'assets'
# puntos escogidos a mano para un sitio y un modo, en fracciones de lo que se puede bajar (0 = arriba): donde el reparto parejo cae
# a la mitad de una animación
PUNTOS = {('neuralnet', 'cel'): [0, .27, .727], ('neuralbi', 'cel'): [0, .182, .636, .727],
          # en el computador, NeuralNet hace crecer una esfera turquesa a la mitad: la portada, "Decisiones." y el tablero
          ('neuralnet', 'pc'): [0, .182, .636],
          # Weed Honey abre con una portada larga que se queda fija mientras cambian las latas y sus textos se cruzan: dos momentos
          # limpios de la portada, y después el producto y el cierre
          ('weedhoney', 'cel'): [0, .4545, .824, .909], ('weedhoney', 'pc'): [0, .4545, .909, 1]}
# sitios que piden la edad: se pasa con la fecha de un adulto de prueba, nunca la de una persona (el usuario lo autorizó el 16 de
# noviembre de 2026 para hacer el recorrido de Weed Honey)
EDAD = {'weedhoney': ('01', '01', '1990')}


def proyectos():
    src = (comun.RAIZ / 'src' / 'partes' / 'visor.astro').read_text(encoding='utf-8')
    return [(m['id'], m['url'], int(m['n'])) for m in re.finditer(r"\{ id: '(?P<id>[^']+)'[^}]*?url: '(?P<url>[^']+)', n: (?P<n>\d+)", src)]


async def sin_cookies(page):
    for b in await page.query_selector_all('button, [role=button], a'):
        try:
            if NO.match((await b.inner_text()).strip()) and await b.is_visible():
                await b.click(timeout=2000)
                await page.wait_for_timeout(700)
                return True
        except Exception:
            pass
    return False


async def edad(page, pid):
    """La verificación de edad: día, mes y año en sus casillas, y su botón. Nada más del sitio se toca."""
    if pid not in EDAD:
        return False
    form = page.locator('form:has(input[placeholder="DD"])').first
    if not await form.count():
        return False
    for ph, v in zip(('DD', 'MM', 'AAAA'), EDAD[pid]):
        await form.locator(f'input[placeholder="{ph}"]').fill(v)
    await form.locator('[type=submit]').first.click()
    await page.wait_for_timeout(2500)
    return True


# la altura de la página y dónde empieza cada parte (secciones y títulos), para que cada pantalla arranque en una
MEDIR = """() => {
  const a = new Set();
  document.querySelectorAll('section, h1, h2').forEach((e) => { const r = e.getBoundingClientRect(); if (r.height > 0 && r.width > 0) a.add(Math.round(r.top + scrollY)); });
  return { h: Math.max(document.documentElement.scrollHeight, document.body.scrollHeight), anchors: [...a].sort((x, y) => x - y) };
}"""

# las barras fijas (fijas o pegajosas, a lo ancho y no muy altas) pegadas o casi pegadas al borde de arriba (su menú, también el que
# flota a unos píxeles) o al de abajo (un botón de compra o de contacto): desde la segunda pantalla se esconden, para que la tira
# muestre el sitio y no sus barras una y otra vez. También el círculo que sigue al cursor, que sin cursor queda flotando en la mitad
SIN_BARRA = """() => {
  let n = 0;
  for (const e of document.querySelectorAll('body *')) {
    const s = getComputedStyle(e);
    if (s.position !== 'fixed' && s.position !== 'sticky') continue;
    const r = e.getBoundingClientRect();
    if (!r.width || !r.height || r.bottom <= 0 || r.top >= innerHeight) continue;
    const bar = r.height < innerHeight * .25 && r.width > innerWidth * .5 && (r.top <= 24 || r.bottom >= innerHeight - 24);
    const cursor = s.pointerEvents === 'none' && r.width < 160 && r.height < 160 && parseFloat(s.borderTopLeftRadius) >= r.width * .4;
    if (bar || cursor) { e.style.setProperty('visibility', 'hidden', 'important'); n++; }
  }
  return n;
}"""


def puntos(h, H, anchors, n, fr=None):
    """n puntos de scroll repartidos por la página (el último antes del pie), cada uno movido al comienzo de la parte más
    cercana; los escogidos a mano (fr) se respetan tal cual."""
    span = max(0, h - H)
    if fr:
        return [round(f * span) for f in fr]
    out = [0]
    for i in range(1, n):
        t = round(i * span / n)
        near = [a for a in anchors if abs(a - t) < H * .45]
        p = min(near, key=lambda a: abs(a - t)) - 64 if near else t   # 64: lo que suele ocupar un menú fijo arriba
        p = max(0, min(span, p))
        if p - out[-1] < H * .6:                                        # dos pantallas casi iguales: se queda con la repartida
            p = t
        out.append(p)
    return out


async def bajar(page, H, y0, y):
    """baja de a poco hasta y, para que lo que carga al acercarse (imágenes, carruseles, lo que aparece al entrar) alcance a llegar"""
    step = H * .5 if y > y0 else -H * .5
    cur = y0
    while abs(y - cur) > abs(step):
        cur += step
        await page.evaluate('y => window.scrollTo({ top: y, behavior: "instant" })', round(cur))
        await page.wait_for_timeout(140)
    await page.evaluate('y => window.scrollTo({ top: y, behavior: "instant" })', y)


async def recorrer(b, modo, pid, url, n, muestra=False):
    M = MODOS[modo]
    W, H = M['w'], M['h']
    opts = {'viewport': {'width': W, 'height': H}, 'device_scale_factor': DPR, 'locale': 'es-CO', 'reduced_motion': 'no-preference'}
    if M['movil']:
        opts.update(is_mobile=True, has_touch=True, user_agent=M['ua'])
    ctx = await b.new_context(**opts)
    page = await ctx.new_page()
    try:
        await page.goto(url, wait_until='domcontentloaded', timeout=90000)
        try:
            await page.wait_for_load_state('networkidle', timeout=12000)
        except Exception:
            pass
        await page.wait_for_timeout(2500)
        gate = await edad(page, pid)
        await page.wait_for_timeout(1500)                               # la entrada del sitio
        cookies = await sin_cookies(page)
        m = await page.evaluate(MEDIR)
        if muestra:
            pos = [round(i * max(0, m['h'] - H) / 11) for i in range(12)]
        else:
            pos = puntos(m['h'], H, m['anchors'], n, PUNTOS.get((pid, modo)))
        shots, y0, barras = [], 0, 0
        for i, y in enumerate(pos):
            await bajar(page, H, y0, y); y0 = y
            await page.wait_for_timeout(2400)                           # lo que aparece al llegar y las imágenes que cargan tarde
            if i:
                barras = max(barras, await page.evaluate(SIN_BARRA))
            shots.append(await page.screenshot())
        return shots, {'alto': m['h'], 'puntos': pos, 'cookies': cookies, 'edad': gate, 'barras': barras}
    finally:
        await ctx.close()


def guardar(shots, modo, pid):
    """cada ancho de la tira, de las capturas a 2x (la pantalla de vuelta al final); en el computador, también el póster"""
    M = MODOS[modo]
    full = [Image.open(io.BytesIO(s)).convert('RGB') for s in shots]
    full.append(full[0])
    out = []
    for w, name in M['anchos'].items():
        h1 = round(M['h'] * w / M['w'])
        strip = Image.new('RGB', (w, h1 * len(full)))
        for i, im in enumerate(full):
            strip.paste(im.resize((w, h1), Image.LANCZOS), (0, i * h1))
        f = SALIDA / name.format(id=pid)
        strip.save(f, 'WEBP', quality=76 if w <= 800 else 72, method=6)
        out.append((f, strip))
    if modo == 'pc':
        f = SALIDA / f'pf-{pid}.jpg'
        full[0].resize((POSTER, round(M['h'] * POSTER / M['w'])), Image.LANCZOS).save(f, 'JPEG', quality=82, optimize=True, progressive=True)
        out.append((f, None))
    return out


def muestra_hoja(shots, modo, pid):
    M = MODOS[modo]
    w = 195 if modo == 'cel' else 300
    ims = [Image.open(io.BytesIO(s)).convert('RGB').resize((w, round(M['h'] * w / M['w']))) for s in shots]
    cols = 6 if modo == 'cel' else 4
    rows = -(-len(ims) // cols)
    out = Image.new('RGB', (cols * (w + 6) - 6, rows * (ims[0].height + 6) - 6), (255, 255, 255))
    for i, im in enumerate(ims):
        out.paste(im, ((i % cols) * (w + 6), (i // cols) * (im.height + 6)))
    out.save(comun.SALIDA + f'/muestra-{pid}-{modo}.png')
    print(f'{pid} ({modo}): muestra en herramientas/salida/muestra-{pid}-{modo}.png (doce pantallas, de 0 a 1 en pasos de 1/11)')


async def main():
    muestra = '--muestra' in sys.argv
    modos = [m for m, flag in (('cel', '--celular'), ('pc', '--computador')) if flag in sys.argv] or ['cel', 'pc']
    quiero = {a for a in sys.argv[1:] if not a.startswith('--')}
    todos = [p for p in proyectos() if not quiero or p[0] in quiero]
    async with async_playwright() as pw:
        b = await pw.chromium.launch()
        for modo in modos:
            hechas = []
            for pid, url, n in todos:
                try:
                    shots, info = await recorrer(b, modo, pid, url, n, muestra)
                except Exception as e:
                    print(f'{pid} ({modo}): no se pudo recorrer ({str(e)[:160]})')
                    continue
                if muestra:
                    muestra_hoja(shots, modo, pid)
                    continue
                files = guardar(shots, modo, pid)
                hechas.append(files[0][1])
                print(f"{pid} ({modo}): {len(shots)} pantallas + la primera | alto {info['alto']} px | puntos {info['puntos']}"
                      f" | edad: {'pasada con fecha de prueba' if info['edad'] else 'no pide'} | cookies rechazadas: {'sí' if info['cookies'] else 'no había'}"
                      f" | barras escondidas: {info['barras']} | " + ', '.join(f'{f.name} {f.stat().st_size // 1024} KB' for f, _ in files))
            if hechas:
                w = 200
                small = [im.resize((w, round(im.height * w / im.width))) for im in hechas]
                hoja = Image.new('RGB', (len(small) * (w + 10) - 10, max(s.height for s in small)), (255, 255, 255))
                for i, s in enumerate(small):
                    hoja.paste(s, (i * (w + 10), 0))
                hoja.save(comun.SALIDA + f'/recorridos-{modo}.png')
                print('hoja:', comun.SALIDA + f'\\recorridos-{modo}.png', hoja.size)
        await b.close()


asyncio.run(main())
