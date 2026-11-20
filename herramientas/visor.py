"""python herramientas/visor.py
   -> abre el detalle de un proyecto y pasa al siguiente, a 1440 y a 390, y deja una hoja con el resultado en herramientas/salida/visor.png"""
import asyncio
import comun
from PIL import Image
from playwright.async_api import async_playwright
async def main():
    shots = []; errores = []
    async with async_playwright() as pw:
        b = await comun.navegador(pw)
        for (W, H) in [(1440, 900), (390, 844)]:
            page, errs = await comun.pagina(b, W, H)
            await page.evaluate("Viewer.show(3, null, PROJECTS)"); await page.wait_for_timeout(1500)
            f = f'{comun.TMP}/vw-{W}-a.png'; await page.screenshot(path=f); shots.append(f)
            if W > 1000:
                await page.keyboard.press('ArrowRight'); await page.wait_for_timeout(3300)
                f = f'{comun.TMP}/vw-{W}-b.png'; await page.screenshot(path=f); shots.append(f)
            await page.keyboard.press('Escape'); await page.wait_for_timeout(700)
            errores += errs; await page.context.close()
        print('errores:', errores or 'ninguno'); await b.close()
    ims = [Image.open(f).convert('RGB') for f in shots]
    tiles = [im.resize((640, 400), Image.LANCZOS) if im.width > 1000 else im.resize((185, 400), Image.LANCZOS) for im in ims]
    Wt = sum(t.width for t in tiles) + 8 * (len(tiles) - 1); s = Image.new('RGB', (Wt, 400), '#ff00ff'); x = 0
    for t in tiles: s.paste(t, (x, 0)); x += t.width + 8
    out = f'{comun.SALIDA}/visor.png'; s.save(out); print(out, s.size)
asyncio.run(main())
