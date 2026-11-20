"""python herramientas/bajo_menu.py
   -> texto que queda debajo del menú fijo a 1110, 1440, 1920 y 390 de ancho mientras se recorre la página.
      "se queda" = sigue debajo del menú al menos tres pasos de scroll seguidos (lo que pasa de largo no cuenta).
   Termina con código 1 si algo se queda debajo."""
import asyncio, sys
import comun
from playwright.async_api import async_playwright
JS = """() => {
  const nav = document.querySelector('#stage .mn'); if (!nav || !nav.classList.contains('is-in')) return null;
  const parts = [...nav.querySelectorAll('.mn-list a, .mn-now, .mn-side, .mn-top > *')].filter((e) => { const c = getComputedStyle(e); return c.visibility !== 'hidden' && c.display !== 'none' && +c.opacity > .05; }).map((e) => { const b = e.getBoundingClientRect(); b.k = e.className.toString().split(' ')[0] || 'enlace'; return b; }).filter((b) => b.width > 0 && b.height > 0);
  const hits = [];
  const texts = document.querySelectorAll('#stage .v > section :is(h1,h2,h3,h4,p,li,a,button,label,input,strong,small,figcaption,b,span)');
  for (const el of texts) {
    if (el.closest('.mn, .sr-only') || !el.childNodes.length && el.tagName !== 'INPUT') continue;
    if (![...el.childNodes].some((n) => n.nodeType === 3 && n.nodeValue.trim().length > 1) && el.tagName !== 'INPUT') continue;
    const c = getComputedStyle(el); if (c.visibility === 'hidden' || el.closest('[aria-hidden=true]')) continue;
    /* the opacity that is seen: the text's own times that of everything that holds it (a tile waiting at 0 hides its words) */
    let op = 1; for (let a = el; a && a !== document.body; a = a.parentElement) op *= +getComputedStyle(a).opacity;
    if (op < .2) continue;
    const r = document.createRange(); r.selectNodeContents(el);
    for (const b of r.getClientRects()) {
      if (b.width < 2 || b.bottom < 0 || b.top > innerHeight) continue;
      for (const m of parts) if (b.left < m.right - 1 && b.right > m.left + 1 && b.top < m.bottom - 1 && b.bottom > m.top + 1) { hits.push(m.k + '|' + (el.closest('section').id || el.closest('section').className.split(' ').pop()) + ':' + el.textContent.trim().slice(0, 22)); break; }
    }
  }
  return [...new Set(hits)];
}"""
async def main():
    mal = 0
    async with async_playwright() as pw:
        b = await comun.navegador(pw)
        for W, H in [(1110, 620), (1440, 900), (1920, 1000), (390, 844)]:
            page, _ = await comun.pagina(b, W, H)
            total = await page.evaluate("document.documentElement.scrollHeight"); y = 0; found = {}
            while y < total:
                await page.evaluate("y=>scrollTo({top:y,behavior:'instant'})", y); await page.wait_for_timeout(50)
                for h in (await page.evaluate(JS) or []): found[h] = found.get(h, 0) + 1
                y += int(H * .45)
            keep = sorted(((n, h) for h, n in found.items() if n >= 3), reverse=True); mal += len(keep)
            print(W, '| toca:', len(found), '| se queda bajo el menú:', [f"{h} x{n}" for n, h in keep[:9]] or 'nada')
            await page.context.close()
        await b.close()
    print('MENÚ', 'LIMPIO' if not mal else f'TAPA TEXTO en {mal} casos')
    sys.exit(1 if mal else 0)
asyncio.run(main())
