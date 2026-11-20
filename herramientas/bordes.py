"""python herramientas/bordes.py [ANCHO ALTO [ANCHO_MINIATURA]]
   -> cada cambio de color del sitio (los bordes que arma color.html) en cinco posiciones del scroll.
      Deja la hoja en herramientas/salida/bordes-<ancho>.png"""
import asyncio, sys
import comun
from PIL import Image
from playwright.async_api import async_playwright
W, H = (int(sys.argv[1]), int(sys.argv[2])) if len(sys.argv) > 2 else (1440, 900)
tw = int(sys.argv[3]) if len(sys.argv) > 3 else 300
US = [.16, .34, .5, .68, .9]
async def main():
    async with async_playwright() as pw:
        b = await comun.navegador(pw)
        page, errs = await comun.pagina(b, W, H)
        n = await page.evaluate("document.querySelectorAll('#stage .edge').length"); shots = []
        for i in range(n):
            for u in US:
                await page.evaluate("([i,u])=>{const e=document.querySelectorAll('#stage .edge')[i];const top=e.getBoundingClientRect().top+scrollY;scrollTo({top:top-innerHeight+u*(innerHeight+e.offsetHeight),behavior:'instant'})}", [i, u])
                await page.wait_for_timeout(520)
                f = f'{comun.TMP}/ed-{i}-{int(u*100)}.png'; await page.screenshot(path=f); shots.append(f)
        print('bordes:', n, '| errores:', errs or 'ninguno'); await b.close()
    th = round(tw * H / W); cols = len(US); rows = max(1, n)
    s = Image.new('RGB', (cols * (tw + 6) - 6, rows * (th + 6) - 6), '#ff00ff')
    for k, f in enumerate(shots): s.paste(Image.open(f).convert('RGB').resize((tw, th), Image.LANCZOS), ((k % cols) * (tw + 6), (k // cols) * (th + 6)))
    out = f'{comun.SALIDA}/bordes-{W}.png'; s.save(out); print(out, s.size)
asyncio.run(main())
