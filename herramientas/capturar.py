"""python herramientas/capturar.py SALIDA.png ANCHO ALTO COLUMNAS ANCHO_MINIATURA "selector|avance;selector|avance;..." [rm] [en]
   -> hoja de contactos con estados del scroll. Cada cuadro es una sección (selector CSS dentro de la página) y un avance
      de 0 a 1 dentro de ella. Ejemplo: ".hx|0;.hx|.3;.hx|.6;#servicios|.5". Si ANCHO_MINIATURA es igual a ANCHO, salen a tamaño real.
      rm = movimiento reducido · en = en inglés. La hoja queda en herramientas/salida/ si SALIDA no trae carpeta."""
import asyncio, os, sys
import comun
from PIL import Image
from playwright.async_api import async_playwright
out, W, H, cols, tw, spec = sys.argv[1], int(sys.argv[2]), int(sys.argv[3]), int(sys.argv[4]), int(sys.argv[5]), sys.argv[6]
extra = sys.argv[7:]
if not os.path.dirname(out): out = os.path.join(comun.SALIDA, out)
items = [x.split('|') for x in spec.split(';') if x]
async def main():
    shots = []
    async with async_playwright() as pw:
        b = await comun.navegador(pw)
        page, errs = await comun.pagina(b, W, H, reducido='rm' in extra, ingles='en' in extra)
        await page.wait_for_timeout(1500)                       # la entrada del hero
        for i, (sel, p) in enumerate(items):
            if not await page.evaluate(comun.IR, [sel, float(p)]): print('no existe', sel); continue
            await page.wait_for_timeout(750)
            f = f'{comun.TMP}/cap-{i}.png'; await page.screenshot(path=f); shots.append(f)
        print('errores:', errs or 'ninguno'); await b.close()
    th = round(tw * H / W); rows = -(-len(shots) // cols)
    s = Image.new('RGB', (cols * (tw + 8) - 8, rows * (th + 8) - 8), '#ff00ff')
    for k, f in enumerate(shots): s.paste(Image.open(f).convert('RGB').resize((tw, th), Image.LANCZOS), ((k % cols) * (tw + 8), (k // cols) * (th + 8)))
    s.save(out); print(out, s.size)
asyncio.run(main())
