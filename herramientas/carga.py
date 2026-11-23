"""python herramientas/carga.py [--veces 3] [--hoja nombre.png] [--computador] [--sin-freno] [--dist carpeta]
   -> cómo carga la página en un celular lento, con las condiciones de PageSpeed: un Moto G Power, 4G lenta
      (150 ms de ida y vuelta, 1,6 Mbps) y un procesador cuatro veces más lento.
      Da la primera pintura (FCP), la pintura más grande (LCP), el índice de velocidad, las tareas largas,
      los saltos de diseño y qué se pidió por la red. Con --hoja deja la película de la carga en salida/.
   Sirve dist/ comprimido, como lo entrega el hospedaje (con --dist, otra carpeta: para comparar con un armado anterior).
   Con CASE_URL mide otra dirección.
   Los números sirven para comparar un cambio con el anterior en este equipo; los oficiales son los de PageSpeed."""
import asyncio, base64, functools, gzip, http.server, io, json, os, statistics, sys, threading
from pathlib import Path

RAIZ = Path(__file__).resolve().parents[1]
DIST = RAIZ / "dist"
SALIDA = Path(__file__).resolve().parent / "salida"
PUERTO = 8771
TEXTO = (".html", ".css", ".js", ".mjs", ".svg", ".txt", ".xml", ".json", ".webmanifest")
MOTO = dict(viewport={"width": 412, "height": 823}, device_scale_factor=1.75, is_mobile=True, has_touch=True,
            user_agent="Mozilla/5.0 (Linux; Android 11; moto g power (2022)) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/140.0.0.0 Mobile Safari/537.36")
# el freno de DevTools que usa Lighthouse para una 4G lenta: la latencia va por petición, por eso es 3,75 veces la de ida y vuelta
RED = dict(offline=False, latency=562.5, downloadThroughput=1474.56 * 1024 / 8, uploadThroughput=675 * 1024 / 8)
DURA = 7.0          # segundos que se mira la carga

try:
    sys.stdout.reconfigure(encoding="utf-8")
except Exception:
    pass


class Comprimido(http.server.SimpleHTTPRequestHandler):
    """dist/ con gzip en lo que es texto, como lo entrega un hospedaje."""
    protocol_version = "HTTP/1.1"
    memo = {}

    def do_GET(self):
        ruta = self.translate_path(self.path.split("?")[0])
        if os.path.isdir(ruta):
            ruta = os.path.join(ruta, "index.html")
        if not os.path.isfile(ruta):
            self.send_error(404)
            return
        ext = os.path.splitext(ruta)[1].lower()
        data = open(ruta, "rb").read()
        tipo = self.guess_type(ruta)
        self.send_response(200)
        if ext in TEXTO and "gzip" in self.headers.get("Accept-Encoding", ""):
            llave = (ruta, os.path.getmtime(ruta))
            if llave not in self.memo:
                self.memo[llave] = gzip.compress(data, 9)
            data = self.memo[llave]
            self.send_header("Content-Encoding", "gzip")
            tipo += "; charset=utf-8"
        self.send_header("Content-Type", tipo)
        self.send_header("Content-Length", str(len(data)))
        self.send_header("Cache-Control", "no-store")
        self.end_headers()
        self.wfile.write(data)

    def log_message(self, *a):
        pass


ESPIA = """
window.__m = { lcp: [], largas: [], cls: 0 };
new PerformanceObserver((l) => { for (const e of l.getEntries()) __m.lcp.push({ t: Math.round(e.startTime), area: e.size, el: e.element ? (e.element.tagName.toLowerCase() + '.' + String(e.element.className).split(' ').slice(0, 3).join('.')).slice(0, 70) : '', txt: e.element ? (e.element.textContent || '').trim().slice(0, 40) : '' }); }).observe({ type: 'largest-contentful-paint', buffered: true });
new PerformanceObserver((l) => { for (const e of l.getEntries()) __m.largas.push([Math.round(e.startTime), Math.round(e.duration)]); }).observe({ type: 'longtask', buffered: true });
new PerformanceObserver((l) => { for (const e of l.getEntries()) if (!e.hadRecentInput) __m.cls += e.value; }).observe({ type: 'layout-shift', buffered: true });
"""
LEER = """() => ({
  origen: performance.timeOrigin,
  fcp: Math.round((performance.getEntriesByName('first-contentful-paint')[0] || {}).startTime || 0),
  dcl: Math.round(performance.getEntriesByType('navigation')[0].domContentLoadedEventEnd),
  load: Math.round(performance.getEntriesByType('navigation')[0].loadEventEnd),
  html: performance.getEntriesByType('navigation')[0].transferSize,
  m: window.__m,
  red: performance.getEntriesByType('resource').map((r) => ({ n: r.name.replace(location.origin, '').slice(0, 78), ini: Math.round(r.startTime), fin: Math.round(r.responseEnd), kb: Math.round(r.transferSize / 102.4) / 10, tipo: r.initiatorType })),
  fuentes: [...document.fonts].filter((f) => f.status === 'loaded').map((f) => f.family + ' ' + f.weight).filter((v, i, a) => a.indexOf(v) === i)
})"""


def indice(cuadros, origen):
    """El índice de velocidad: cuánto tarda la pantalla en parecerse a como queda. Cada cuadro se compara con el último."""
    from PIL import Image, ImageChops, ImageStat
    ims = [(t, Image.open(io.BytesIO(d)).convert("L").resize((103, 206))) for t, d in cuadros]
    fin = ims[-1][1]
    blanco = Image.new("L", fin.size, 255)
    lejos = lambda im: ImageStat.Stat(ImageChops.difference(im, fin)).mean[0]
    base = lejos(blanco) or 1
    pasos = [(0.0, 0.0)] + [(max(0.0, t - origen), max(0.0, min(1.0, 1 - lejos(im) / base))) for t, im in ims]
    si = sum((1 - pasos[i][1]) * (pasos[i + 1][0] - pasos[i][0]) for i in range(len(pasos) - 1))
    llega = lambda q: next((round(t * 1000) for t, v in pasos if v >= q), None)
    return round(si * 1000), llega(.85), llega(.95)


def pelicula(cuadros, origen, destino):
    """Una hoja con la pantalla cada 250 ms de los primeros 5 segundos."""
    from PIL import Image, ImageDraw
    ims = [(t - origen, Image.open(io.BytesIO(d)).convert("RGB")) for t, d in cuadros]
    w, h = 150, int(150 * ims[-1][1].height / ims[-1][1].width)
    marcas = [i * .25 for i in range(21)]
    hoja = Image.new("RGB", (len(marcas) // 3 * (w + 6), 3 * (h + 22)), (255, 255, 255))
    d = ImageDraw.Draw(hoja)
    for k, m in enumerate(marcas[:len(marcas) // 3 * 3]):
        antes = [im for t, im in ims if t <= m]
        im = antes[-1] if antes else Image.new("RGB", ims[-1][1].size, (255, 255, 255))
        x, y = (k % (len(marcas) // 3)) * (w + 6), (k // (len(marcas) // 3)) * (h + 22)
        hoja.paste(im.resize((w, h)), (x, y + 18))
        d.text((x + 2, y + 3), f"{m:.2f} s", fill=(0, 0, 0))
    hoja.save(destino)


async def una(pw, url, computador, frenar, guardar):
    from playwright.async_api import Error
    b = await pw.chromium.launch(args=["--enable-unsafe-swiftshader", "--ignore-gpu-blocklist"])
    ctx = await b.new_context(**({"viewport": {"width": 1350, "height": 940}} if computador else MOTO))
    page = await ctx.new_page()
    await page.add_init_script(ESPIA)
    cdp = await ctx.new_cdp_session(page)
    await cdp.send("Network.enable")
    await cdp.send("Page.enable")
    if frenar:
        await cdp.send("Network.emulateNetworkConditions", RED)
        await cdp.send("Emulation.setCPUThrottlingRate", {"rate": 4})
    cuadros = []

    def cuadro(ev):
        cuadros.append((ev["metadata"]["timestamp"], base64.b64decode(ev["data"])))
        asyncio.ensure_future(cdp.send("Page.screencastFrameAck", {"sessionId": ev["sessionId"]}))

    cdp.on("Page.screencastFrame", cuadro)
    await cdp.send("Page.startScreencast", {"format": "jpeg", "quality": 55, "maxWidth": 412, "maxHeight": 940, "everyNthFrame": 1})
    await page.goto(url, wait_until="commit", timeout=120000)
    await page.wait_for_timeout(int(DURA * 1000))
    try:
        r = await page.evaluate(LEER)
    except Error as e:
        r = {"error": str(e)[:200]}
    await cdp.send("Page.stopScreencast")
    await b.close()
    if "error" in r or not cuadros:
        return r
    origen = r["origen"] / 1000
    cuadros = [c for c in cuadros if c[0] >= origen - .05]
    r["si"], r["v85"], r["v95"] = indice(cuadros, origen)
    r["cuadros"] = len(cuadros)
    if guardar:
        pelicula(cuadros, origen, guardar)
    return r


async def main():
    from playwright.async_api import async_playwright
    a = sys.argv[1:]
    veces = int(a[a.index("--veces") + 1]) if "--veces" in a else 3
    hoja = str(SALIDA / a[a.index("--hoja") + 1]) if "--hoja" in a else None
    url = os.environ.get("CASE_URL")
    if not url:
        carpeta = a[a.index("--dist") + 1] if "--dist" in a else str(DIST)
        srv = http.server.ThreadingHTTPServer(("127.0.0.1", PUERTO), functools.partial(Comprimido, directory=carpeta))
        threading.Thread(target=srv.serve_forever, daemon=True).start()
        url = f"http://127.0.0.1:{PUERTO}/"
    SALIDA.mkdir(exist_ok=True)
    res = []
    async with async_playwright() as pw:
        for i in range(veces):
            r = await una(pw, url, "--computador" in a, "--sin-freno" not in a, hoja if i == veces - 1 else None)
            if "error" in r:
                print("no se pudo medir:", r["error"])
                continue
            res.append(r)
    if not res:
        sys.exit(1)
    med = lambda k: round(statistics.median(k(r) for r in res))
    u = res[-1]
    lcp = lambda r: (r["m"]["lcp"] or [{"t": 0}])[-1]["t"]
    print(f"{url}  ·  {'computador' if '--computador' in a else 'Moto G Power'}{'' if '--sin-freno' in a else ', 4G lenta, procesador x4'}  ·  mediana de {len(res)}")
    print(f"  primera pintura (FCP)      {med(lambda r: r['fcp'])} ms      cada vez: {[r['fcp'] for r in res]}")
    print(f"  pintura más grande (LCP)   {med(lcp)} ms      cada vez: {[lcp(r) for r in res]}")
    print(f"  índice de velocidad        {med(lambda r: r['si'])} ms      cada vez: {[r['si'] for r in res]}")
    print(f"  85 % y 95 % de la pantalla {med(lambda r: r['v85'] or 0)} ms y {med(lambda r: r['v95'] or 0)} ms")
    print(f"  saltos de diseño (CLS)     {max(r['m']['cls'] for r in res):.3f}")
    print(f"  tareas largas              {u['m']['largas'] or 'ninguna'}  (inicio, duración en ms)")
    print(f"  HTML                       {u['html'] / 1024:.1f} KiB por la red · DOMContentLoaded {u['dcl']} ms · load {u['load']} ms")
    print("  el elemento del LCP:      ", " -> ".join(f"{e['el']} «{e['txt']}» a {e['t']} ms" for e in u["m"]["lcp"][-3:]))
    print(f"  fuentes cargadas:          {u['fuentes']}")
    print("  por la red (inicio a fin, KiB):")
    for x in sorted(u["red"], key=lambda x: x["ini"])[:18]:
        print(f"    {x['ini']:>5} a {x['fin']:>5} ms  {x['kb']:>6}  {x['tipo']:<8} {x['n']}")
    if hoja:
        print("  película:", hoja)


asyncio.run(main())
