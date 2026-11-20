"""Genera sitio/partes/idioma.html: el diccionario de en.py y el código que lo aplica.

Uso:  python sitio/i18n/generar.py     (y después  python sitio/build.py)

El español es la página tal como está escrita. El inglés se aplica en tres momentos:
  1. a la página recién montada, antes de que arranquen las secciones (I18N.node)
  2. a las listas de las que se dibujan las secciones (PROJECTS, BRANDS, TEAM, STEPS, SOCIAL, NEEDS, WHEN), que vuelven al español al cambiar
  3. a lo que se escribe después (contadores, mensajes), con un MutationObserver; las frases armadas pasan por REGLAS (RULES)
Los textos que viven en el CSS se cambian con reglas html[lang="en"] en el <style> de abajo.
"""
import json, sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from en import EN
D = json.dumps(EN, ensure_ascii=False, separators=(',', ':')).replace('</', '<\\/')
OUT = r'''<style>
/* the language switch inside the hero, next to the button */
.nav__end{display:flex;align-items:center;gap:6px}
.nav__lang{display:flex;color:var(--ink)}
.nav--dark .nav__lang{color:#fff}
.nav__lang button{min-width:40px;min-height:44px;padding:0 8px;border:0;background:none;color:inherit;font:500 13px/1 var(--font);letter-spacing:.02em;cursor:pointer;opacity:.5;transition:opacity 200ms ease}
.nav__lang button[aria-pressed="true"]{opacity:1}
@media (max-width:420px){.nav__lang button{min-width:32px;padding:0 5px}.nav .btn--sm{padding:0 14px}}
</style>
<script>
/* ===== Two languages. Spanish is the page as written; English is a dictionary applied to the page before its sections start,
   to the data the sections draw from, and to whatever they write afterwards ===== */
(() => {
  const D = __DICT__;
  const one = (s) => D[s] || s;
  /* sentences that are put together while the page runs */
  const RULES = [
    [/^Abrir vista previa de (.+)$/, (m) => `Open preview of ${m[1]}`],
    [/^Ver el trabajo con (.+)$/, (m) => `See the work with ${m[1]}`],
    [/^Ver en (.+)$/, (m) => `See on ${m[1]}`],
    [/^· (.+)$/, (m) => (D[m[1]] ? `· ${D[m[1]]}` : null)],
    [/^, (.+)$/, (m) => (D[m[1]] ? `, ${D[m[1]]}` : null)],
    [/^Recorrido con pantallas reales de (.+)\. Cuando esta página esté en su propio dominio, aquí se abre el sitio real y se navega sin salir\.$/, (m) => `A tour with real screens of ${m[1]}. Once this page is on its own domain, the real site opens here and you can browse it without leaving.`],
    [/^(.+): la fórmula de tu marca\.$/, (m) => `${m[1].split(' + ').map(one).join(' + ')}: your brand's formula.`],
    [/^Listo, (.+?)\. Pediste: (.+?)(?: · (.+))?\. En este prototipo la solicitud todavía no se envía\.$/, (m) => `Done, ${m[1]}. You asked for: ${m[2].split(', ').map(one).join(', ')}${m[3] ? ' · ' + one(m[3]) : ''}. In this prototype the request is not sent yet.`]
  ];
  const tr = (s) => {
    const k = s.replace(/\s+/g, ' ').trim(); if (k.length < 2) return null;
    let t = D[k];
    if (t === undefined) for (const [re, fn] of RULES) { const m = re.exec(k); if (m) { t = fn(m); break; } }
    if (t == null || t === k) return null;
    return s.match(/^\s*/)[0] + t + s.match(/\s*$/)[0];
  };
  const ATTR = /^(aria-label|placeholder|alt|title|data-ph)$/;
  const node = (n) => {
    if (LANG.cur !== 'en') return;
    if (n.nodeType === 3) { const t = tr(n.nodeValue); if (t !== null) n.nodeValue = t; return; }
    if (n.nodeType !== 1 || /^(SCRIPT|STYLE|TEMPLATE|TEXTAREA)$/.test(n.tagName) || n.classList.contains('proto-picker')) return;
    for (const a of n.attributes) if (ATTR.test(a.name) || (a.name === 'value' && /^(checkbox|radio)$/.test(n.type))) { const t = tr(a.value); if (t !== null) n.setAttribute(a.name, t); }
    for (let c = n.firstChild; c; c = c.nextSibling) node(c);
  };
  /* the lists the sections are drawn from: translated in place, and put back when Spanish returns */
  const sources = () => [window.PROJECTS, window.BRANDS, window.TEAM, typeof STEPS !== 'undefined' && STEPS, typeof SOCIAL !== 'undefined' && SOCIAL, typeof NEEDS !== 'undefined' && NEEDS, typeof WHEN !== 'undefined' && WHEN].filter(Boolean);
  const keep = new Map();
  const deep = (v, f) => { for (const k in v) { if (typeof v[k] === 'string') v[k] = f(v[k], k); else if (v[k] && typeof v[k] === 'object') deep(v[k], f); } };
  const SKIP = /^(id|img|tour|url|bg|fg|sym|s|z)$/;
  const data = (code) => sources().forEach((src) => {
    if (!keep.has(src)) keep.set(src, JSON.stringify(src));
    const es = JSON.parse(keep.get(src)); src.length = 0; es.forEach((x) => src.push(x));
    if (code === 'en') deep(src, (s, k) => (SKIP.test(k) ? s : D[s] || s));
  });
  const LANG = window.LANG = {
    cur: 'es',
    set(code) {
      if (code === LANG.cur || !/^(es|en)$/.test(code)) return;
      /* come back to the same place after the page is drawn again */
      const stage = document.getElementById('stage'), mid = innerHeight / 2; let k = 0, r = 0;
      stage.querySelectorAll('.v > section').forEach((s, i) => { const b = s.getBoundingClientRect(); if (b.top <= mid) { k = i; r = Math.min(1, Math.max(0, (mid - b.top) / b.height)); } });
      LANG.cur = code; document.documentElement.lang = code; data(code); chrome(code);
      if (window.REMOUNT) window.REMOUNT();
      requestAnimationFrame(() => requestAnimationFrame(() => {
        const s = stage.querySelectorAll('.v > section')[k]; if (!s || !k) return;
        const b = s.getBoundingClientRect(); scrollTo({ top: scrollY + b.top + r * b.height - innerHeight / 2, behavior: 'instant' });
      }));
    }
  };
  /* what lives outside the page (the preview window) is translated in place and remembers its Spanish */
  const outside = [];
  const chrome = (code) => {
    while (outside.length) { const [n, a, v] = outside.pop(); if (a) n.setAttribute(a, v); else n.nodeValue = v; }
    if (code !== 'en') return;
    const walk = (n) => {
      if (n.nodeType === 3) { const t = tr(n.nodeValue); if (t !== null) { outside.push([n, null, n.nodeValue]); n.nodeValue = t; } return; }
      if (n.nodeType !== 1 || /^(SCRIPT|STYLE|TEMPLATE|TEXTAREA)$/.test(n.tagName) || n.id === 'stage' || n.classList.contains('proto-picker')) return;
      for (const a of n.attributes) if (ATTR.test(a.name)) { const t = tr(a.value); if (t !== null) { outside.push([n, a.name, a.value]); n.setAttribute(a.name, t); } }
      for (let c = n.firstChild; c; c = c.nextSibling) walk(c);
    };
    walk(document.body);
  };
  /* every switch on the page shows the language that is on, and any of them changes it */
  const mark = (root) => root.querySelectorAll('[data-lang]').forEach((b) => b.setAttribute('aria-pressed', b.dataset.lang === LANG.cur));
  document.addEventListener('click', (e) => { const b = e.target.closest('[data-lang]'); if (b) LANG.set(b.dataset.lang); });
  window.I18N = { node: (root) => { mark(root); node(root); }, tr };
  /* whatever is written after the sections start (lists, counters, messages) is translated as it arrives */
  new MutationObserver((ms) => {
    if (LANG.cur !== 'en') return;
    for (const m of ms) {
      if (m.type === 'characterData') node(m.target);
      else if (m.type === 'attributes') { const v = m.target.getAttribute(m.attributeName), t = v && tr(v); if (t) m.target.setAttribute(m.attributeName, t); }
      else m.addedNodes.forEach(node);
    }
  }).observe(document.body, { subtree: true, childList: true, characterData: true, attributes: true, attributeFilter: ['aria-label', 'placeholder', 'alt', 'title', 'data-ph'] });
})();
</script>
'''
SALIDA = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'partes', 'idioma.html')
open(SALIDA, 'w', encoding='utf-8', newline='\n').write('<!-- GENERADO por i18n/generar.py a partir de i18n/en.py. No se edita a mano. -->\n' + OUT.replace('__DICT__', D))
print('partes/idioma.html:', len(OUT) + len(D), 'bytes,', len(EN), 'pares')
