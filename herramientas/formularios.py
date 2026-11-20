"""python herramientas/formularios.py [ANCHO ALTO]
   -> llena y envía el formulario de contacto y deja tres cuadros: vacío con su aviso, con dos servicios marcados y enviado.
      Deja la hoja en herramientas/salida/formulario-<ancho>.png"""
import asyncio, sys
import comun
from PIL import Image
from playwright.async_api import async_playwright
W, H = (int(sys.argv[1]), int(sys.argv[2])) if len(sys.argv) > 2 else (1440, 900)
async def main():
    shots = []
    async with async_playwright() as pw:
        b = await comun.navegador(pw)
        page, errs = await comun.pagina(b, W, H)
        async def foto(n):
            await page.evaluate("(H)=>{const c=document.querySelector('#stage .contact');const r=c.getBoundingClientRect();scrollTo(0,scrollY+r.top+Math.max(0,(r.height-H))/2)}", H); await page.wait_for_timeout(500)
            f = f'{comun.TMP}/fm-{n}.png'; await page.screenshot(path=f); shots.append(f)
        await page.evaluate("document.querySelector('#stage .contact').scrollIntoView({block:'start'})"); await page.wait_for_timeout(500)
        await page.locator('#stage .contact__form button[type=submit]').click(); await page.wait_for_timeout(500); await foto('vacio')
        await page.evaluate("(vals)=>{[...document.querySelectorAll('#stage .ck-c input')].filter(i=>vals.includes(i.value)).forEach(i=>i.click())}", ['Tiendas en línea', 'Redes sociales']); await foto('opciones')
        await page.fill('#stage #c-name', 'Laura'); await page.fill('#stage #c-mail', 'laura@panaderia.example')
        await page.locator('#stage .contact__form button[type=submit]').click(); await page.wait_for_timeout(900); await foto('enviado')
        print('errores:', errs or 'ninguno'); await b.close()
    tw = 640 if W > 1000 else 300; th = round(tw * H / W)
    s = Image.new('RGB', (3 * (tw + 8) - 8, th), '#ff00ff')
    for k, f in enumerate(shots): s.paste(Image.open(f).convert('RGB').resize((tw, th), Image.LANCZOS), (k * (tw + 8), 0))
    out = f'{comun.SALIDA}/formulario-{W}.png'; s.save(out); print(out, s.size)
asyncio.run(main())
