"""python herramientas/cosechar.py [en]
   -> todos los textos que el sitio llega a mostrar (recorre la página a 1440 y a 390, usa el formulario y abre el visor).
      Sirve para revisar el diccionario de inglés. Con "en" los recoge en inglés. Deja la lista en herramientas/salida/textos-<idioma>.json"""
import asyncio, json, sys
import comun
from playwright.async_api import async_playwright
# Anota cada texto (y cada aria-label, placeholder, alt o title) en cuanto aparece en la página.
REC = r"""
(() => {
  const seen = window.__seen = new Map(); let n = 0;
  const ok = (s) => /[A-Za-zÁÉÍÓÚÑáéíóúñ¿¡]{2,}/.test(s);
  const add = (s, tag) => { s = s.replace(/\s+/g, ' ').trim(); if (s && ok(s) && !seen.has(s)) seen.set(s, tag + ':' + (n++)); };
  const skip = (el) => !el || el.closest('script,style,template,.proto-picker,svg defs');
  const walk = (node) => {
    if (node.nodeType === 3) { if (!skip(node.parentElement)) add(node.nodeValue, 't'); return; }
    if (node.nodeType !== 1 || skip(node)) return;
    for (const a of node.attributes) if (/^(aria-label|placeholder|alt|title|data-[a-z-]+)$/.test(a.name) && /[ áéíóúñ]/.test(a.value) && !/^(#|\.|http|assets)/.test(a.value)) add(a.value, '@' + a.name);
    for (const c of node.childNodes) walk(c);
  };
  walk(document.body);
  new MutationObserver((ms) => ms.forEach((m) => { if (m.type === 'characterData') walk(m.target); else if (m.type === 'attributes') walk(m.target); else m.addedNodes.forEach(walk); })).observe(document.body, { subtree: true, childList: true, characterData: true, attributes: true });
})();
"""
async def cosechar(b, ingles=False):
    out = {}
    for W, H in [(1440, 900), (390, 844)]:
        page, _ = await comun.pagina(b, W, H, reducido=True, ingles=ingles)
        await page.evaluate(REC); await comun.recorrer(page, 260, 45)
        await page.evaluate(comun.FORMULARIO); await comun.abrir_visor(page)
        for s, tag in await page.evaluate("[...window.__seen.entries()]"): out.setdefault(s, f"{W}:{tag}")
        await page.context.close()
    return out
async def main():
    ingles = len(sys.argv) > 1 and sys.argv[1] == 'en'
    async with async_playwright() as pw:
        b = await comun.navegador(pw); out = await cosechar(b, ingles); await b.close()
    destino = f"{comun.SALIDA}/textos-{'en' if ingles else 'es'}.json"
    json.dump(out, open(destino, 'w', encoding='utf-8'), ensure_ascii=False, indent=0)
    print(len(out), 'textos ->', destino)
if __name__ == '__main__':
    asyncio.run(main())
