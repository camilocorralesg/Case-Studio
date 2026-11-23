"""python herramientas/contenido.py [--comprobar]
   -> lee de la página armada (dist/) lo que el sitio dice: titulares, servicios, proyectos, marcas, pasos, redes y preguntas,
      y lo guarda en src/datos/contenido.json. De ese archivo sale lo que no se dibuja en pantalla: el texto para quien llega sin
      JavaScript (buscadores y asistentes que no lo corren), los datos estructurados, llms.txt y llms-full.txt.
      Así el contenido se escribe una sola vez, en las partes; este archivo es su copia y no se edita a mano.
      Con --comprobar no escribe: dice si la copia quedó vieja y termina con código 1 (lo usa la revisión completa).
   Después de cambiar un texto del sitio: npm run build, python herramientas/contenido.py y npm run build otra vez
   (o npm run contenido, que hace las tres cosas)."""
import asyncio, json, sys
import comun
from playwright.async_api import async_playwright

DESTINO = comun.RAIZ / "src" / "datos" / "contenido.json"
LEER = """() => {
  const t = (s, r = document) => { const e = r.querySelector(s); return e ? e.textContent.replace(/\\s+/g, ' ').trim() : ''; };
  const S = '#stage ';
  return {
    hero: { titular: [...document.querySelectorAll(S + '#b-h1 .ln')].map((l) => l.textContent.trim()).join(' '), apoyo: t(S + '.hx .lead'), frase: t(S + '.hx__say') },
    servicios: { titular: t(S + '#f2-h'), apoyo: t(S + '#servicios .lead'),
      lista: [...document.querySelectorAll(S + '#servicios .f2-row')].map((r) => ({ simbolo: t('.f2-el b', r), nombre: t('h3', r), texto: t('.f2-fold p', r) })) },
    formula: { titular: t(S + '#fx-h'), apoyo: t(S + '#formula .lead') },
    rediseno: { titular: t(S + '#rd-h'), apoyo: t(S + '#rediseno .lead') },
    proyectos: { titular: t(S + '#ru-h'),
      lista: PROJECTS.map((p) => ({ id: p.id, simbolo: p.sym, nombre: p.name, tipo: p.kind, url: p.url, texto: p.lead, datos: p.facts.filter(Boolean), hecho: p.feats })) },
    marcas: { titular: t(S + '#mr-h'), apoyo: t(S + '#marcas .lead'),
      lista: BRANDS.map((b) => ({ simbolo: b.sym, nombre: b.name, redes: b.nets.map(([red, cuenta, url]) => ({ red, cuenta, url })), frase: b.tag, texto: b.lead, hecho: b.did })) },
    proceso: { titular: t(S + '#pq-h'), lista: STEPS.map((s) => ({ simbolo: s.s, nombre: s.t, corto: s.c, texto: s.d })) },
    redes: { titular: t(S + '#sm-h'), apoyo: t(S + '#redes .sm-lead'), lista: SOCIAL.map(([nombre, texto, plus]) => ({ nombre, texto, plus: !!plus })) },
    preguntas: { titular: t(S + '#fq-h'), lista: FAQ.map((f) => ({ simbolo: f.s, pregunta: f.q, respuesta: f.a.filter((x) => typeof x === 'string') })) },
    cierre: { titular: t(S + '#zb-h') },
    contacto: { titular: t(S + '#contact-h'), apoyo: t(S + '#contacto .lead'), opciones: NEEDS.map(([nombre, simbolo]) => ({ nombre, simbolo })) }
  };
}"""


def vacios(d, ruta=""):
    """Las claves que llegaron sin texto: la página cambió de forma y hay que ajustar LEER."""
    if isinstance(d, dict):
        return [x for k, v in d.items() for x in vacios(v, f"{ruta}.{k}" if ruta else k)]
    if isinstance(d, list):
        return ([ruta] if not d else []) + [x for i, v in enumerate(d) for x in vacios(v, f"{ruta}[{i}]")]
    return [ruta] if d == "" else []


async def main():
    async with async_playwright() as pw:
        b = await comun.navegador(pw)
        page, errs = await comun.pagina(b)
        dato = await page.evaluate(LEER)
        await b.close()
    faltan = vacios(dato)
    if faltan:
        sys.exit("CONTENIDO: llegaron vacíos " + ", ".join(faltan[:8]) + ". La página cambió de forma: ajustar LEER en herramientas/contenido.py.")
    nuevo = json.dumps(dato, ensure_ascii=False, indent=2) + "\n"
    viejo = DESTINO.read_text(encoding="utf-8") if DESTINO.exists() else ""
    if "--comprobar" in sys.argv:
        if nuevo != viejo:
            a, b2 = (json.loads(viejo) if viejo else {}), dato
            cambian = [k for k in b2 if a.get(k) != b2[k]]
            print("La copia del contenido quedó vieja en:", ", ".join(cambian) or "(el archivo no existe)")
            print("Lo que sale de ella (texto sin JavaScript, datos estructurados, llms.txt) no dice lo mismo que el sitio.")
            sys.exit("CONTENIDO VIEJO: correr npm run contenido")
        print("CONTENIDO AL DÍA")
        return
    DESTINO.parent.mkdir(parents=True, exist_ok=True)
    DESTINO.write_text(nuevo, encoding="utf-8", newline="\n")
    print(f"{DESTINO.relative_to(comun.RAIZ)}: {'sin cambios' if nuevo == viejo else 'actualizado'} · "
          f"{len(dato['proyectos']['lista'])} proyectos, {len(dato['marcas']['lista'])} marcas, {len(dato['preguntas']['lista'])} preguntas")


asyncio.run(main())
