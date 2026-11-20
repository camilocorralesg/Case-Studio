"""python herramientas/costuras.py [ANCHO_MINIATURA]
   -> una miniatura por cada frontera entre secciones (a 1440 x 900), para buscar cortes duros.
      Deja la hoja en herramientas/salida/costuras.png"""
import asyncio, sys
import comun
from PIL import Image
from playwright.async_api import async_playwright
TW = int(sys.argv[1]) if len(sys.argv) > 1 else 236
async def main():
    tiles = []
    async with async_playwright() as pw:
        b = await comun.navegador(pw)
        page, errs = await comun.pagina(b)
        ys = await page.evaluate("[...document.querySelectorAll('#stage .v > section, #stage .v > footer')].slice(1).map(s => Math.round(s.getBoundingClientRect().top + scrollY))")
        for y in ys:
            await page.evaluate("(y)=>scrollTo({top:y-innerHeight/2,behavior:'instant'})", y); await page.wait_for_timeout(420)
            f = comun.TMP + '/costura.png'; await page.screenshot(path=f); tiles.append(Image.open(f).convert('RGB').resize((TW, round(TW * 900 / 1440)), Image.LANCZOS))
        print('errores:', errs or 'ninguno'); await b.close()
    th = round(TW * 900 / 1440); cols = 6; rows = -(-len(tiles) // cols)
    s = Image.new('RGB', (cols * (TW + 6) - 6, rows * (th + 6) - 6), '#ff00ff')
    for k, t in enumerate(tiles): s.paste(t, ((k % cols) * (TW + 6), (k // cols) * (th + 6)))
    out = f'{comun.SALIDA}/costuras.png'; s.save(out); print(out, s.size)
asyncio.run(main())
