"""Arma el sitio en una sola página: sitio/index.html.

Uso:  python sitio/build.py        (antes, si cambió el diccionario de inglés:  python sitio/i18n/generar.py)

Cada archivo de partes/ trae su CSS (<style>), su plantilla (<template>) y su código (<script>).
Aquí se juntan en el orden de ORDEN: los estilos suben al <head> y lo demás queda en el <body>, uno tras otro.
El orden importa: lo que viene después puede pisar estilos de lo anterior, y color.html y menu.html
envuelven una función que define ensamble.html.
"""
import re
from pathlib import Path

AQUI = Path(__file__).parent
PARTES = AQUI / "partes"

ORDEN = [
    "logo",          # símbolos SVG del logo
    "base",          # piezas compartidas: raíz de la página, hero como momento de scroll, registro de secciones
    # --- las secciones, en el orden en que se leen
    "hero",
    "servicios",
    "rediseno",
    "visor",         # proyectos y marcas (los datos) y el visor que los abre sobre la página
    "proyectos",
    "marcas",
    "proceso",
    "redes",
    "nosotros",
    "cierre",
    "contacto",      # el formulario de opciones y su panel
    "frase-final",
    "ensamble",      # lo que se agrega al final: formulario, frase final y pie
    "pie",
    # --- lo que cruza varias secciones (va después de ellas porque ajusta sus estilos)
    "uniones",       # la luz que une una sección con la siguiente
    "color",         # secciones de otro color y el borde que las cambia con el scroll
    "menu",
    "idioma",        # GENERADO por i18n/generar.py: no se edita a mano
    "arranque",      # monta la página
]

FLECHA = ('<svg class="arr" viewBox="0 0 16 16" fill="none" aria-hidden="true"><path d="M3 8h10M9 4l4 4-4 4" '
          'stroke="currentColor" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round"/></svg>')
ICONOS = ('<svg class="i-pause" viewBox="0 0 16 16" aria-hidden="true"><rect x="4" y="3" width="2.6" height="10" rx="1" fill="currentColor"/>'
          '<rect x="9.4" y="3" width="2.6" height="10" rx="1" fill="currentColor"/></svg>'
          '<svg class="i-play" viewBox="0 0 16 16" aria-hidden="true"><path d="M5 3.2v9.6a.6.6 0 0 0 .9.5l7.6-4.8a.6.6 0 0 0 0-1L5.9 2.7a.6.6 0 0 0-.9.5z" fill="currentColor"/></svg>')

ENLACES = ('<nav class="nav__links" aria-label="Principal"><a href="#servicios">Servicios</a>'
           '<a href="#proyectos">Proyectos</a><a href="#redes">Redes</a><a href="#contacto">Contacto</a></nav>')

# La barra de arriba del hero: logo, enlaces, idioma y el botón principal.
NAV = ('<header class="nav nav--dark"><a class="nav__home" href="#top" aria-label="CaSe Studio, inicio">'
       f'<svg class="logo logo--dark" aria-hidden="true"><use href="#logo-cut"></use></svg></a>{ENLACES}'
       '<div class="nav__end"><div class="nav__lang" role="group" aria-label="Idioma"><button type="button" data-lang="es" aria-pressed="true" aria-label="Español">ES</button>'
       '<button type="button" data-lang="en" aria-pressed="false" aria-label="English">EN</button></div>'
       '<a class="btn btn--sm btn--white" href="#contacto">Empezar mi proyecto</a></div></header>')


def pausa(extra=""):
    cls = ("pause " + extra).strip()
    return f'<button class="{cls}" type="button" aria-label="Pausar animación">{ICONOS}</button>'


def llenar(s):
    """Reemplaza las marcas {{...}} que usan las partes."""
    s = s.replace("{{NAV_DARK}}", NAV).replace("{{ARR}}", FLECHA)
    s = re.sub(r"\{\{PAUSE:([\w\- ]+)\}\}", lambda m: pausa(m.group(1)), s)
    sobran = re.findall(r"\{\{[^}]*\}\}", s)
    assert not sobran, sobran
    return s


def main():
    cabecera = (PARTES / "cabecera.html").read_text(encoding="utf-8")
    estilos, cuerpo = [], []
    for nombre in ORDEN:
        parte = llenar((PARTES / f"{nombre}.html").read_text(encoding="utf-8"))
        estilos += re.findall(r"<style>.*?</style>", parte, flags=re.S)
        cuerpo.append(re.sub(r"<style>.*?</style>\s*", "", parte, flags=re.S))
    sobran = sorted(p.stem for p in PARTES.glob("*.html") if p.stem not in ORDEN and p.stem != "cabecera")
    assert not sobran, f"partes sin lugar en ORDEN: {sobran}"
    cabecera = cabecera.replace("</head>", "\n".join(estilos) + "\n</head>")
    html = cabecera + "\n<body>\n" + "\n".join(cuerpo)
    (AQUI / "index.html").write_text(html, encoding="utf-8", newline="\n")
    print(f"index.html: {len(html) / 1024:.1f} KB, {len(ORDEN) + 1} partes")


if __name__ == "__main__":
    main()
