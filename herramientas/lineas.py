"""python herramientas/lineas.py
   -> líneas horizontales duras que cruzan toda la pantalla mientras se recorre el sitio (a 1440 x 900).
   Termina con código 1 si encuentra alguna."""
import asyncio, sys, io
import comun
import numpy as np
from PIL import Image
from playwright.async_api import async_playwright
W, H = 1440, 900
async def main():
    async with async_playwright() as pw:
        b = await comun.navegador(pw)
        page, _ = await comun.pagina(b, W, H)
        total = await page.evaluate("document.documentElement.scrollHeight")
        hits = []; y = 0
        while y < total - H:
            await page.evaluate("y=>scrollTo({top:y,behavior:'instant'})", y); await page.wait_for_timeout(260)
            a = np.asarray(Image.open(io.BytesIO(await page.screenshot())).convert('L'), dtype=np.int16)
            d = np.abs(a[1:] - a[:-1])            # cambio de una fila de píxeles a la siguiente
            frac = (d > 9).mean(axis=1)           # parte del ancho que cambia en esa fila
            for r in np.where(frac > .97)[0]:
                if 8 < r < H - 8: hits.append((y, int(r), round(float(d[r].mean()), 1)))
            y += 610
        out = []
        for h in hits:                            # las filas vecinas cuentan como una sola línea
            if out and h[0] == out[-1][0] and h[1] - out[-1][1] <= 3: continue
            out.append(h)
        for (sy, r, m) in out[:40]:
            info = await page.evaluate("([sy,r])=>{scrollTo({top:sy,behavior:'instant'});const e=document.elementFromPoint(720,r+1),a=document.elementFromPoint(720,r-3);const n=x=>x?(x.closest('section,footer,.edge')||x).className.toString().slice(0,34):'';return n(a)+' / '+n(e)+' :: '+(e?e.className.toString().slice(0,30):'')}", [sy, r])
            print(f"  y={sy}+{r} Δ{m}  {info}")
        # 2. Lo que se corta en el borde de una sección: una sombra o una luz que pasa del borde de una sección fija termina en
        #    seco y deja una raya del ancho de lo que la proyecta, aunque no cruce toda la pantalla. Se mira cada borde entre dos
        #    piezas del mismo color, con el borde en la mitad de la pantalla.
        bordes = await page.evaluate("""() => [...document.querySelectorAll('#stage .v > *')].map((e, i, a) => {
            const n = a[i + 1]; if (!n) return null;
            const nom = (x) => x.id || x.className.toString().split(' ').pop();
            return { y: e.getBoundingClientRect().bottom + scrollY, mismo: getComputedStyle(e).backgroundColor === getComputedStyle(n).backgroundColor, nombre: nom(e) + ' / ' + nom(n) };
        }).filter(Boolean)""")
        cortes = []
        for bo in bordes:
            if not bo['mismo']: continue
            await page.evaluate("y=>scrollTo({top:y,behavior:'instant'})", max(0, round(bo['y'] - H / 2))); await page.wait_for_timeout(320)
            r = round(bo['y'] - await page.evaluate("scrollY"))
            if not 4 < r < H - 4: continue
            a = np.asarray(Image.open(io.BytesIO(await page.screenshot())).convert('RGB'), dtype=np.int16)
            d = np.abs(a[r + 1] - a[r - 2]).max(axis=1) > 4      # salto entre justo arriba y justo abajo del borde
            tramo, mejor, x0, desde = 0, 0, 0, 0
            for x, v in enumerate(d):
                tramo = tramo + 1 if v else 0
                if tramo == 1: desde = x
                if tramo > mejor: mejor, x0 = tramo, desde
            if mejor >= 80: cortes.append((bo['nombre'], x0, mejor))
        for (nombre, x0, largo) in cortes:
            print(f"  corte en el borde {nombre}: x={x0}..{x0 + largo}")
        await b.close()
    print('LÍNEAS', 'LIMPIO' if not out and not cortes else f'{len(out)} líneas de lado a lado, {len(cortes)} cortes en bordes')
    sys.exit(1 if out or cortes else 0)
asyncio.run(main())
