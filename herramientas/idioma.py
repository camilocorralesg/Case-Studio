"""python herramientas/idioma.py [rm]
   -> lo que sigue en español después de pasar el sitio a inglés (recorre la página, usa el formulario y abre el visor).
      Dos señales: un texto que es entrada del diccionario (src/i18n/en.json) y sigue igual, o un texto con
      palabras o tildes del español. No cuenta nombres propios (La Miguería, Sebastián, Medellín...) ni símbolos.
   rm = movimiento reducido. Termina con código 1 si queda algo sin traducir."""
import asyncio, json, re, sys
import comun
from cosechar import REC
from playwright.async_api import async_playwright
PARES = json.loads((comun.I18N / 'en.json').read_text(encoding='utf-8'))   # el diccionario: si un texto de la izquierda sigue en pantalla, no se tradujo
RM = len(sys.argv) > 1 and sys.argv[1] == 'rm'
SIN_TRADUCIR = {k for k, v in PARES.items() if k != v}
ES = re.compile(r"[áéíóúñ¿¡]|\b(de|del|la|las|el|los|y|tu|tus|con|para|que|una|un|por|en|lo|se|su|al|es|más|sin|mi)\b", re.I)
OKNAMES = re.compile(r"^(Los Duches|La Miguería|Sebastián Vanegas|Medellín.*|Laureles, Medellín|La Pilarica, Medellín|.*@.*|© .*|AKUA.*|Graduados EAFIT|.*Medellín\.?|hola@.*|.*NeuralBI.*|O'Neill Colombia|Speedo Colombia|Tú)$")
NOMBRES = re.compile(r"La Miguería|Los Duches|Sebastián|bastián|Medellín|Catalina|Camilo|CaSe Studio|O'Neill|La Pilarica")      # "bastián": la frase final parte el nombre en Se + bastián
FORMULA = re.compile(r"^[A-Z][a-z']?( \+ [A-Z][a-z']?)+$")
def sospechoso(s):
    if s in SIN_TRADUCIR: return True
    if len(s) <= 3 or FORMULA.match(s) or OKNAMES.match(s) or re.fullmatch(r"[a-z ]{8,}", s): return False
    return bool(ES.search(NOMBRES.sub('', s)))
async def main():
    async with async_playwright() as pw:
        b = await comun.navegador(pw)
        page, errs = await comun.pagina(b, reducido=RM, ingles=True)
        await page.evaluate(REC); await comun.recorrer(page)
        await page.evaluate(comun.FORMULARIO); await comun.abrir_visor(page)
        got = await page.evaluate("[...window.__seen.keys()]"); await b.close()
    bad = [s for s in got if sospechoso(s)]
    print(len(got), 'textos,', len(bad), 'en español'); [print('  -', s[:150]) for s in bad]
    print('errores:', errs or 'ninguno')
    print('INGLÉS', 'COMPLETO' if not bad and not errs else f'FALTAN {len(bad)} textos')
    sys.exit(1 if bad or errs else 0)
asyncio.run(main())
