"""python herramientas/ida_y_vuelta.py
   -> con movimiento normal y reducido: va a "Proceso", pasa a inglés y vuelve a español.
      Comprueba que el lector siga en la misma sección en las dos direcciones, que el título cambie de idioma
      y que al volver no quede ningún texto en inglés.
   Termina con código 1 si algo falla."""
import asyncio, re, sys
import comun
from playwright.async_api import async_playwright
EN = re.compile(r"\b(the|and|your|we|with|for|you|our|what|how|start|see|of)\b", re.I)
TEXTOS = """() => { const out = new Set(); const w = document.createTreeWalker(document.body, NodeFilter.SHOW_TEXT); let n; while ((n = w.nextNode())) { const p = n.parentElement; if (p && !p.closest('script,style,template,.proto-picker')) { const s = n.nodeValue.replace(/\\s+/g, ' ').trim(); if (s.length > 2) out.add(s); } } return [...out]; }"""
TITULO = "document.querySelector('#stage #proceso h2').textContent.trim()"
mismo = lambda a, b: a[0] == b[0] and abs(a[1] - b[1]) < .06
async def main():
    mal = []
    async with async_playwright() as pw:
        b = await comun.navegador(pw)
        for rm in (False, True):
            page, errs = await comun.pagina(b, reducido=rm); nombre = 'movimiento reducido' if rm else 'movimiento normal'
            await page.evaluate(comun.IR, ['#proceso', .4]); await page.wait_for_timeout(600)
            antes = set(await page.evaluate(TEXTOS)); d0 = await page.evaluate(comun.DONDE); t0 = await page.evaluate(TITULO)
            await comun.cambiar_idioma(page, 'en'); d1 = await page.evaluate(comun.DONDE); t1 = await page.evaluate(TITULO)
            await comun.cambiar_idioma(page, 'es'); d2 = await page.evaluate(comun.DONDE); t2 = await page.evaluate(TITULO)
            sobra = sorted(s for s in set(await page.evaluate(TEXTOS)) - antes if EN.search(s))
            lang = await page.evaluate("document.documentElement.lang")
            fallas = []
            if not mismo(d0, d1): fallas.append(f"al pasar a inglés salta de {d0} a {d1}")
            if not mismo(d0, d2): fallas.append(f"al volver queda en {d2} y estaba en {d0}")
            if t1 == t0: fallas.append("el título de Proceso no cambió de idioma")
            if t2 != t0: fallas.append(f"el título volvió como «{t2}»")
            if lang != 'es': fallas.append(f"html lang quedó en {lang}")
            if sobra: fallas.append(f"queda inglés: {sobra[:6]}")
            if errs: fallas.append(f"errores: {errs[0]}")
            print(nombre, '|', d0, '->', d1, '->', d2, '|', t0, '/', t1, '|', 'bien' if not fallas else fallas)
            mal += [f"{nombre}: {f}" for f in fallas]
            await page.context.close()
        await b.close()
    print('IDA Y VUELTA', 'BIEN' if not mal else 'FALLA:'); [print('  -', m) for m in mal]
    sys.exit(1 if mal else 0)
asyncio.run(main())
