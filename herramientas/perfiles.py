"""python herramientas/perfiles.py [cuenta ...]
   -> la captura del perfil de Instagram de cada marca que se muestra en el teléfono de Marcas (src/partes/marcas.astro).

   Por cada cuenta deja public/assets/ig/<cuenta>.webp (Instagram en español) y <cuenta>-en.webp (en inglés), a 780 px de ancho.
   - Si hay una captura hecha a mano en src/assets/ig/<cuenta>.png o .jpg (por ejemplo, desde el celular), usa esa para los dos
     idiomas. Así entra Weed Honey: su perfil es solo para adultos y Instagram no lo muestra sin una sesión iniciada.
   - Si no, abre el perfil público a tamaño de celular (390 px, a 3x), quita la ventana que invita a abrir la app y la barra de
     iniciar sesión, espera a que carguen las publicaciones y recorta el blanco que sobra abajo.
   Sin cuentas, hace las seis de BRANDS. Las capturas traen las cifras del día: se pueden volver a sacar cuando se quiera."""
import asyncio, io, sys
from pathlib import Path
import numpy as np
from PIL import Image
from playwright.async_api import async_playwright

RAIZ = Path(__file__).resolve().parents[1]
DESTINO = RAIZ / 'public' / 'assets' / 'ig'
MANUAL = RAIZ / 'src' / 'assets' / 'ig'
CUENTAS = ['weedhoney.co', 'agilcash.co', 'lamigueria', 'speedocolombia', 'oneillcolombia', 'graduadoseafit']
UA = 'Mozilla/5.0 (iPhone; CPU iPhone OS 17_5 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.5 Mobile/15E148 Safari/604.1'
LIMPIAR = """() => {
  [...document.querySelectorAll('body *')].forEach((e) => { const c = getComputedStyle(e); if (c.position === 'fixed' || c.position === 'sticky') e.remove(); });
  document.documentElement.style.overflow = 'auto'; document.body.style.overflow = 'auto';
}"""

try:
    sys.stdout.reconfigure(encoding='utf-8')
except Exception:
    pass


def guardar(im, nombre):
    """Recorta el blanco de abajo y guarda a 780 px de ancho, y a 480 (<nombre>-480.webp) para las pantallas que no son retina:
    el teléfono de Marcas mide unos 320 px, y cada pantalla toma el ancho que necesita (srcset)."""
    im = im.convert('RGB'); a = np.asarray(im).astype(int)
    filas = np.where((np.abs(a - 255).sum(axis=2) > 30).mean(axis=1) > .02)[0]
    if len(filas): im = im.crop((0, 0, im.width, int(filas.max()) + 1))
    im = im.resize((780, round(im.height * 780 / im.width)), Image.LANCZOS)
    DESTINO.mkdir(parents=True, exist_ok=True)
    im.save(DESTINO / nombre, quality=82, method=6)
    im.resize((480, round(im.height * 480 / 780)), Image.LANCZOS).save(DESTINO / nombre.replace('.webp', '-480.webp'), quality=80, method=6)
    return im.size


async def publica(b, cuenta, idioma):
    ctx = await b.new_context(viewport={'width': 390, 'height': 844}, device_scale_factor=3, is_mobile=True, has_touch=True, user_agent=UA,
                              locale='es-CO' if idioma == 'es' else 'en-US', extra_http_headers={'Accept-Language': 'es-CO,es;q=0.9' if idioma == 'es' else 'en-US,en;q=0.9'})
    pg = await ctx.new_page()
    await pg.goto(f'https://www.instagram.com/{cuenta}/', wait_until='domcontentloaded', timeout=60000)
    await pg.wait_for_timeout(5000)
    if 'restring' in (await pg.content()).lower() or 'restricted' in (await pg.content()).lower():
        await ctx.close(); return None
    await pg.evaluate(LIMPIAR)
    for y in (600, 1200, 1800, 0):   # the grid loads its pictures as they come into view
        await pg.evaluate(f'scrollTo(0, {y})'); await pg.wait_for_timeout(1200)
    await pg.evaluate(LIMPIAR); await pg.wait_for_timeout(1500)
    top = await pg.evaluate("(() => { const h = document.querySelector('main header') || document.querySelector('header'); return h ? Math.max(0, h.getBoundingClientRect().top + scrollY - 8) : 0; })()")
    png = await pg.screenshot(clip={'x': 0, 'y': top, 'width': 390, 'height': 1400}, full_page=True)
    await ctx.close()
    return Image.open(io.BytesIO(png))


async def main():
    cuentas = sys.argv[1:] or CUENTAS
    async with async_playwright() as pw:
        b = await pw.chromium.launch()
        for c in cuentas:
            hecha = next((p for p in (MANUAL / f'{c}.png', MANUAL / f'{c}.jpg', MANUAL / f'{c}.jpeg') if p.exists()), None)
            if hecha:
                im = Image.open(hecha)
                for n in (f'{c}.webp', f'{c}-en.webp'): tam = guardar(im, n)
                print(c, '| desde la captura hecha a mano', hecha.name, tam); continue
            for idioma in ('es', 'en'):
                im = await publica(b, c, idioma)
                if im is None: print(c, idioma, '| perfil restringido: hace falta una captura hecha a mano en', MANUAL); break
                print(c, idioma, '|', guardar(im, f'{c}.webp' if idioma == 'es' else f'{c}-en.webp'))
        await b.close()

asyncio.run(main())
