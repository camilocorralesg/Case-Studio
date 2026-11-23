"""python herramientas/compartir.py [--solo-iconos]
   -> lo que el sitio muestra fuera de sí mismo:
      - public/assets/og-case-studio.jpg (1200 x 630): la imagen que sale cuando se comparte el enlace (WhatsApp, redes, buscadores).
        Es el hero de verdad, de la página armada: el logo, el titular y la tabla con Ca y Se ya en su lugar; sin el menú, el
        apoyo ni los botones, que en una miniatura no se leen.
      - los iconos, dibujados con la marca del favicon (las dos casillas): public/favicon.svg, favicon-48.png,
        apple-touch-icon.png (180), icon-192.png e icon-512.png, y public/site.webmanifest.
   Se corre otra vez si cambian el hero, el titular o la marca."""
import asyncio, io, json, sys
from PIL import Image, ImageDraw
import comun
from playwright.async_api import async_playwright

PUB = comun.RAIZ / "public"
NOCHE, BLANCO = (2, 4, 10), (255, 255, 255)
SOLO = """.hx .nav__links,.hx .nav__end,.hx__pause,.skip,.b-copy .lead,.b-copy .acts,.proto-picker{display:none!important}
.hx .nav{padding-inline:44px;height:92px}.hx .logo{height:34px}
.v-tab .b-copy{top:92px;padding-top:26px}.v-tab .b-h1{font-size:74px}"""


def icono(lado, redondo=0.0):
    """La marca (dos casillas; la segunda, con su hueco) en blanco sobre la noche, centrada y con aire para que un recorte
    redondo o cuadrado no la toque."""
    k = 4
    im = Image.new("RGB", (lado * k, lado * k), NOCHE)
    d = ImageDraw.Draw(im)
    ancho = lado * k * .62
    u = ancho / 208
    x0, y0 = (lado * k - ancho) / 2, (lado * k - 100 * u) / 2
    for dx in (0, 108):
        d.rounded_rectangle([x0 + dx * u, y0, x0 + (dx + 100) * u, y0 + 100 * u], radius=12 * u, fill=BLANCO)
    d.rounded_rectangle([x0 + 122 * u, y0 + 14 * u, x0 + 194 * u, y0 + 86 * u], radius=5 * u, fill=NOCHE)
    return im.resize((lado, lado), Image.LANCZOS)


def iconos():
    svg = ('<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 -54 208 208"><style>.t{fill:#171717}.c{fill:#fff}'
           '@media (prefers-color-scheme:dark){.t{fill:#fff}.c{fill:#171717}}</style>'
           '<rect class="t" width="100" height="100" rx="12"/><rect class="t" x="108" width="100" height="100" rx="12"/>'
           '<rect class="c" x="122" y="14" width="72" height="72" rx="5"/></svg>\n')
    (PUB / "favicon.svg").write_text(svg, encoding="utf-8", newline="\n")
    for nombre, lado in (("favicon-48.png", 48), ("apple-touch-icon.png", 180), ("icon-192.png", 192), ("icon-512.png", 512)):
        icono(lado).save(PUB / nombre, optimize=True)
    manifiesto = {"name": "CaSe Studio", "short_name": "CaSe", "lang": "es", "start_url": "/", "display": "browser",
                  "background_color": "#02040a", "theme_color": "#02040a",
                  "icons": [{"src": "/icon-192.png", "sizes": "192x192", "type": "image/png"},
                            {"src": "/icon-512.png", "sizes": "512x512", "type": "image/png"},
                            {"src": "/icon-512.png", "sizes": "512x512", "type": "image/png", "purpose": "maskable"}]}
    (PUB / "site.webmanifest").write_text(json.dumps(manifiesto, ensure_ascii=False, indent=2) + "\n", encoding="utf-8", newline="\n")
    print("iconos: favicon.svg, favicon-48.png, apple-touch-icon.png, icon-192.png, icon-512.png, site.webmanifest")


async def tarjeta():
    async with async_playwright() as pw:
        b = await comun.navegador(pw)
        ctx = await b.new_context(viewport={"width": 1200, "height": 630}, device_scale_factor=1)
        page = await ctx.new_page()
        await comun.fuentes(page)
        await page.goto(comun.URL, timeout=120000)
        await comun.listo(page)
        await page.add_style_tag(content=SOLO)
        await page.evaluate("document.fonts.ready.then(() => dispatchEvent(new Event('resize')))")
        await page.wait_for_timeout(3600)            # la tabla ya está puesta y Ca y Se cayeron en su lugar
        png = await page.screenshot()
        await b.close()
    f = PUB / "assets" / "og-case-studio.jpg"
    Image.open(io.BytesIO(png)).convert("RGB").save(f, "JPEG", quality=88, optimize=True, progressive=True)
    print(f"{f.relative_to(comun.RAIZ)}: 1200 x 630, {f.stat().st_size // 1024} KB")


iconos()
if "--solo-iconos" not in sys.argv:
    asyncio.run(tarjeta())
