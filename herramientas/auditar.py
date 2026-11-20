"""python herramientas/auditar.py
   -> tres pasadas por el sitio (1440, 390 y movimiento reducido): ids repetidos, un solo h1, nombres accesibles, alt,
      desborde horizontal, toques pequeños en celular, enlaces rotos, número de secciones y errores de consola.
   Termina con código 1 si algo se aparta de lo esperado."""
import asyncio, json, sys
import comun
from playwright.async_api import async_playwright
ESPERADO = {"dupIds": [], "h1": 1, "noName": [], "noAlt": 0, "overflowX": 0, "small": [], "badLinks": [], "sections": comun.SECCIONES}
JS = """() => {
  const out = {};
  const ids = [...document.querySelectorAll('#stage [id]')].map(e => e.id); out.dupIds = [...new Set(ids.filter((x,i) => ids.indexOf(x) !== i))];
  out.h1 = document.querySelectorAll('#stage h1').length;
  /* the name a screen reader says: aria-label, aria-labelledby, or the text it can read (not what is aria-hidden or display:none);
     a name with no letters ("01") is no name */
  const said = (e) => {
    if (e.getAttribute('aria-label')) return e.getAttribute('aria-label');
    const lb = e.getAttribute('aria-labelledby'); if (lb) return lb.split(' ').map(id => (document.getElementById(id) || {}).textContent || '').join(' ');
    let t = ''; const walk = (n) => { for (const c of n.childNodes) { if (c.nodeType === 3) t += c.nodeValue; else if (c.nodeType === 1 && c.getAttribute('aria-hidden') !== 'true' && getComputedStyle(c).display !== 'none') { if (c.tagName === 'IMG') t += c.getAttribute('alt') || ''; else if (c.getAttribute('aria-label')) t += c.getAttribute('aria-label'); else walk(c); } } };
    walk(e); return t;
  };
  out.noName = [...document.querySelectorAll('#stage button, #stage a')].filter(e => !/\\p{L}/u.test(said(e)) && !e.closest('[aria-hidden=true]') && getComputedStyle(e).display !== 'none').map(e => (e.className || e.tagName) + ':' + said(e).trim().slice(0, 10)).filter((x,i,a)=>a.indexOf(x)===i).slice(0,5);
  out.noAlt = [...document.querySelectorAll('#stage img')].filter(e => !e.hasAttribute('alt')).length;
  out.overflowX = document.documentElement.scrollWidth - innerWidth;
  /* on the phone nothing to tap measures less than 40 px (rule 10), links inside running text aside */
  out.small = innerWidth < 500 ? [...document.querySelectorAll('#stage button, #stage a')].filter(e => { const r = e.getBoundingClientRect(), cs = getComputedStyle(e); return r.width && (r.width < 39.5 || r.height < 39.5) && cs.display !== 'inline' && !e.closest('[aria-hidden=true]') && cs.visibility !== 'hidden'; }).map(e => (e.className.split(' ')[0] || e.tagName) + ':' + Math.round(e.getBoundingClientRect().width) + 'x' + Math.round(e.getBoundingClientRect().height)).filter((x,i,a)=>a.indexOf(x)===i).slice(0,8) : [];
  out.badLinks = [...document.querySelectorAll('#stage a[href^="#"]')].filter(a => !document.querySelector('#stage ' + a.getAttribute('href'))).map(a => a.getAttribute('href')).filter((x,i,a)=>a.indexOf(x)===i);
  out.sections = [...document.querySelectorAll('#stage .v > section')].length;
  return out; }"""
async def main():
    mal = []
    async with async_playwright() as pw:
        b = await comun.navegador(pw)
        for ancho, alto, rm in [(1440, 900, False), (390, 844, False), (1440, 900, True)]:
            page, errs = await comun.pagina(b, ancho, alto, reducido=rm)
            H = await page.evaluate("document.documentElement.scrollHeight")
            # it looks twice: halfway down, with the fixed menu on screen, and at the end of the page
            for k in range(1, 15):
                await page.evaluate(f'scrollTo({{top:{H}*{k}/14,behavior:"instant"}})'); await page.wait_for_timeout(90)
                if k == 7: await page.wait_for_timeout(400); medio = await page.evaluate(JS)
            r = await page.evaluate(JS); nombre = f"{ancho}{' movimiento reducido' if rm else ''}"
            for k in ('noName', 'small'): r[k] = list(dict.fromkeys(medio[k] + r[k]))[:8]
            print(nombre, json.dumps(r, ensure_ascii=False), '| errores de consola:', errs or 'ninguno')
            if r != ESPERADO: mal.append(f"{nombre}: " + ', '.join(f"{k}={r.get(k)}" for k in ESPERADO if r.get(k) != ESPERADO[k]))
            if errs: mal.append(f"{nombre}: consola: {errs[0]}")
            await page.context.close()
        await b.close()
    print('AUDITORÍA', 'LIMPIA' if not mal else 'CON HALLAZGOS:'); [print('  -', m) for m in mal]
    sys.exit(1 if mal else 0)
asyncio.run(main())
