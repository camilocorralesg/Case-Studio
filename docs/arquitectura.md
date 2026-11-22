# Cómo está armado el sitio

## De las partes a la página

El sitio es un proyecto de **Astro** (estático). `src/pages/index.astro` es la página: pone `src/layouts/Base.astro` (el `<head>`: fuentes, variables de color, estilos base y las funciones que usa todo lo demás) y adentro cada parte de `src/partes/`, en un orden que importa (ver abajo). `npm run build` deja el resultado en `dist/`; `npm run dev` lo sirve en `http://localhost:4321` y se recarga al guardar.

Las piezas que se repiten son componentes de `src/components/`: `Nav.astro` (la barra de arriba del hero), `Flecha.astro` (la flecha de los botones) y `Pausa.astro` (el botón de pausa, `<Pausa clase="..." />`).

Una parte típica trae tres cosas:

```astro
<style is:global> ... los estilos de la sección ... </style>
<template id="tpl-xx"> <section class="moment xx" id="nombre" style="--mh:320vh"> ... </section> </template>
<script is:inline> addSection('tabla', 'tpl-xx', 3, (root) => { ... return () => { /* limpiar */ }; }); </script>
```

Servicios ya escribe su contenido desde datos en el encabezado de Astro (`FAMS`, en `servicios.astro`): el HTML llega escrito y el inglés lo traduce al montar, como cualquier texto de una plantilla. Es el camino para las demás secciones (ver "Siguientes pasos del stack" en `estado.md`).

Los estilos son globales (`is:global`): Astro los junta en un solo CSS, en el orden de la página, así que una parte puede pisar a las anteriores. Los scripts son `is:inline`: corren en el orden en que aparecen y comparten funciones globales (`moment`, `drive`, `addSection`...). En HTML de una parte no se pueden escribir llaves `{ }` sueltas: Astro las lee como código.

**El orden de `index.astro` importa**: `color` y `menu` envuelven una función que define `ensamble`, e `idioma` y `arranque` van al final.

## Cómo se monta

Nada del contenido está escrito directamente en el `<body>`: está en plantillas, y `src/partes/arranque.astro` lo monta al cargar. Ahí también viven los enlaces internos: llevan el foco a su sección, y si la sección está a más de dos pantallas la página pasa por un velo de noche en lugar de recorrer el camino (`window.JUMP(y)`, que también usa el botón de volver arriba del pie en el celular). (Pasar cada sección a HTML que llegue ya escrito es el siguiente paso del stack: ver `docs/estado.md`.)

1. Clona la plantilla del hero (`tpl-tabla`, registrada con `VARIANTS.push` en `hero.astro`).
2. Le agrega las secciones registradas con `addSection('tabla', plantilla, orden, init)`, de menor a mayor `orden`.
3. Agrega el bloque de contacto (`tpl-contact`, en `arranque.astro`).
4. Si el idioma es inglés, traduce lo montado (`I18N.node`).
5. Llama al `init` del hero y al de cada sección. Cada `init` recibe la raíz y devuelve una función que limpia lo que prendió.
6. Llama a `window.FINALE`, que agrega lo que va después de las secciones.

`window.REMOUNT()` repite todo desde cero. Lo usa el cambio de idioma.

El orden de las secciones lo da el número de `addSection`:

| Orden | Sección | Parte | Clases |
|---|---|---|---|
| (hero) | Hero | `hero.astro` | `.hx`, `.b-` |
| 1 | Servicios | `servicios.astro` (sus animaciones en `escenas.astro`, `window.SCN`) | `.f2` |
| 1.2 | Fórmula | `formula.astro` | `.fx` (la fila: `.fx-t`, los elementos, y `.fx-home`, sus lugares; la fórmula: `.fx-tray`, la bandeja, y `.fx-you`, el Tú; lo que trae: `.fx-gets`) |
| 1.5 | Rediseño | `rediseno.astro` | `.rd` |
| 2 | Proyectos | `proyectos.astro` (el detalle en `visor.astro`; las tiras, de `herramientas/recorridos.py`: `public/assets/tour-<id>.webp` y `-1600.webp` del computador, y `tour-<id>-cel-390.webp`, `-cel.webp` y `-cel-780.webp` del celular) | `.ru` (en el celular las pantallas son verticales y pasan la tira de celular; `.is-wide` es un sitio sin ella) |
| 2.5 | Marcas | `marcas.astro` (las capturas de los perfiles en `public/assets/ig`, con `herramientas/perfiles.py`) | `.mr` |
| 3 | Proceso | `proceso.astro` | `.pq` (la ruta: `.pq-map`, `.pq-stop`, `.pq-me`; en cada estación, `.pq-slot`, su lugar punteado, y `.pq-say`, su paso sobre el papel) |
| 4 | Redes | `redes.astro` (las publicaciones en cobalto en `public/assets/redes`, con `herramientas/publicaciones.py`; la historia "Contenido con IA" dibuja sus piezas con `PIECE`, sin publicaciones reales) | `.sm` (el cubo: `.sm-cube`; cada historia `.sm-f`, `.is-front` o `.is-side`, y `.is-cur` cuando empieza su dibujo) |
| 4.5 | Preguntas | `preguntas.astro` (las preguntas en `FAQ`, el saludo y el estado en `FAQ_SAY`) | `.fq` (la lista: `.fq-rows`, `.fq-row`, `.fq-el`; el chat: `.fq-chat`, `.fq-who`, `.fq-state`, `.fq-log`, mensajes `.fq-msg` `.fq-us` y `.fq-me`, enlaces `.fq-go`; en el celular, `.fq-quick` con `.fq-chip`) |
| 5 | Cierre | `cierre.astro` | `.zb` (la tabla: `.zb-view`, la ventana que la desvanece arriba y abajo cuando la cámara entra, `.zb-cam`, `.zb-grid`, `.zb-c`, `.zb-slot`; el logo y el Tú: `.zb-ca`, `.zb-se`, `.zb-you`, `.zb-gap`), `.zz-copy` (la frase y el botón, que el código pone al lado del Tú) |
| (fijo) | Contacto | `arranque.astro` + `contacto.astro` | `.contact` (una pantalla, el formulario en el centro), `.ck-` (los servicios: `.ck-need`, `.ck-c`; la barra: `.ck-bar`, `.ck-in`; la respuesta: `.ck-ok`) |
| (FINALE) | Pie | `pie.astro` | `.ft` (la tabla, que es el menú: `.ft-stage`, `.ft-plane`, `.ft-table`, `.ft-c`; las casillas del estudio: `.ft-l` con `.ft-nav`, `.ft-svc`, `.ft-ca`, `.ft-se`, `.ft-top`; el hueco: `.ft-gap`, `.ft-key`; el logo: `.ft-logo`, `.ft-mark`). En el celular la tabla se esconde y va `.ft-mob`: el mapa `.ft-map` (casillas `.ft-m`, encendidas con `.is-lit`, la que se toca con `.hot`), las listas `.ft-lists` (`.ft-row`, `.ft-el`), el contacto `.ft-mme` y `.ft-back` |

### FINALE: lo que se agrega al final

`ensamble.astro` define `window.FINALE(id, root, contacto)`: arma el formulario (`FORMS.tabla`) y agrega el pie. (La frase final se quitó el 17 de noviembre de 2026; su parte está en `archivo/secciones-quitadas/`.) El final queda: Cierre, Contacto y pie. Otras dos partes **envuelven** esa función para sumar lo suyo, por eso van después en `index.astro`:

- `color.astro` agrega los bordes de cambio de color.
- `menu.astro` agrega el menú fijo.

Cada una guarda la `FINALE` anterior, la llama y devuelve una limpieza que deshace lo propio y lo anterior.

## Un momento de scroll

Casi todas las secciones son un **momento**: la sección es alta (`--mh`, por ejemplo `320vh`) y su contenido se queda pegado a la pantalla mientras el scroll la recorre. Fórmula (`#formula`) y Proyectos (`#proyectos`) no lo son, por decisión del usuario: son secciones normales de una pantalla (`.fx-in`, `.ru-in`, `min-height:100svh`) que el scroll pasa de largo. Las fichas de Fórmula solo responden a toques y arrastres; la rueda de Proyectos entra una vez cuando se ve (`is-pre` → `is-in`, con un `IntersectionObserver`) y después la mueve el visitante (arrastre, flechas, sus elementos).

```html
<section class="moment xx" style="--mh:320vh"><div class="moment__stick"> ... </div></section>
```

```js
const parar = moment(seccion, (p) => { /* p va de 0 a 1 mientras la sección pasa */ });
```

`moment()` (en `Base.astro`) lee la posición una vez por cuadro y llama a la función con el avance. Devuelve cómo apagarlo. El hero es lo mismo con otras clases (`.hx`, `.hx__stick`, altura `--hh`) y usa `drive()`, que además maneja el dibujo en el lienzo, la pausa y el reposo.

Funciones a mano (en `src/layouts/Base.astro` y `src/partes/comun.astro`):

| Función | Para qué |
|---|---|
| `range(p, a, b)` | Convierte un tramo del avance en 0..1. Con esto se reparte el scroll entre varios pasos |
| `easeIO(t)`, `easeOut(t)`, `lerp(a, b, t)`, `clamp01(v)` | Curvas e interpolación |
| `RM` | Verdadero si el visitante pidió menos movimiento |
| `FINE` | Verdadero si hay cursor de precisión (no táctil) |
| `pointer(el)` | Posición suavizada del cursor sobre un elemento |
| `drive({...})` | El motor del hero: reloj, pausa, avance del scroll |
| `copyOut(copy, say, p)` | El titular del hero se va y la frase de cierre llega |
| `markSprites()` | Las dos casillas del logo (Ca y Se) como imágenes para dibujar en el lienzo |
| `EL_Z`, `zOf(s)` | El número de cada elemento del sitio, por su símbolo en español (uno solo por cosa), y escrito con dos cifras |
| `MOTION.d(k)`, `MOTION.ease(k)` | Las duraciones (`--d-press` a `--d-scene`) y curvas (`--ease-out`, `--ease-io`) de `:root`, para las animaciones hechas desde el código |

### Movimiento reducido

Con `prefers-reduced-motion`, `.moment` deja de ser alta y `.moment__stick.is-flow` pasa a flujo normal. Cada `init` tiene que dejar su sección en el estado final cuando `RM` es verdadero (casi siempre `const p = RM ? 1 : p0`). El hero se queda en su primer cuadro.

## Lo que cruza varias secciones

| Parte | Qué hace |
|---|---|
| `encuadre.astro` | El marco que abre a la luz del hero detrás de lo que muestra un servicio, un sitio o una marca: `Encuadre.put(el, lado)` lo pone dentro de `el` (que aísla su apilamiento) y devuelve cómo quitarlo; `lado` refleja la luz para que cada sección la tenga desde otro lado (`'x'` Rediseño y Preguntas, `'y'` Marcas, `'xy'` Redes, nada en Servicios), con el borde de arriba siempre arriba. Cuatro campos de luz (cobalto, azul cielo, hielo y azul profundo) sobre la noche, con grano; se mueven con el avance de su sección (`--p`). Lo usan el escenario de Servicios (sin tablero: las tarjetas de cada escena flotan encima; `SCN.paint(cv, capas, true)` dibuja en modo noche, con sombras más hondas, las hojas de Marca desde el principio y cada paso centrado), la panadería de Rediseño y el teléfono de Marcas (el marco abraza al teléfono: su alto es el libre en la pantalla, `--fh`) |
| `uniones.astro` | La luz que cierra una sección abre la siguiente (`--join`, `--jb`, `--jt`), para que no haya cortes |
| `color.astro` | Las secciones de otro color (`TONE`: Servicios y Proceso en papel claro `#f4f7ff`, Cierre en azul). Entre dos secciones de distinto color inserta un `.edge`: un lienzo donde el color siguiente se arma casilla a casilla con el scroll |
| `formula.astro` → `contacto.astro` | La fórmula que el visitante arma después de Servicios vive en `window.FORMULA` (sobrevive al cambio de idioma) y se copia al formulario: marca cada servicio por su `data-sym` (Sw, Ti, Rs, Ma: los mismos símbolos de la Fórmula), que no cambia con el idioma. `window.FORMULA_SET` recuerda lo que marcó Servicios, para no deshacer nunca lo que el visitante marcó a mano. Si el visitante toca "Armar mi fórmula" con el ejemplo puesto, el ejemplo pasa a ser suyo y llega a Contacto. Contacto revisa que el contacto se pueda responder (`reachable()`: un correo o 7 dígitos) y, después de "Listo", no envía otra vez hasta que algo cambie |
| `menu.astro` | El menú fijo: en escritorio, una fila de casillas arriba; en el celular (hasta 860 px), "Empezar mi proyecto" y "Menú" con la casilla de la sección en la que vas (`.mn-top`, `.mn-open`, `.mn-here`), que abre una hoja con las ocho secciones con su nombre, el idioma arriba (`.mn-sh-lang`) y el botón (`dialog.mn-sheet`, casillas `.mn-c`; se cierra con la cruz, tocando afuera, con Escape o arrastrándola hacia abajo). Marca la sección que está en la mitad de la pantalla, se esconde en el hero y antes del pie. En Contacto y en la frase final su botón se aparta (`.cta-off`), para que el de ellas sea la única acción en pantalla. Sobre papel claro (`.on-light`) el botón pasa a tinta; desde 1200 px, junto a la fila va el nombre de la sección en la que vas (`.mn-now`, con el texto de su enlace) |
| `visor.astro` | Los datos de proyectos y marcas (`PROJECTS`, `BRANDS`), los recorridos (`Tours`; uno con `data-manual` solo corre cuando su dueño lo pide, `Tours.get`) y el detalle de un proyecto que se abre sobre la página (`Viewer.show(i, origen, lista, vuelta)`): crece desde la pantalla de la rueda y, al cerrar, `vuelta(j)` dice a qué nodo vuelve el proyecto en que terminó el visitante. Las marcas no abren detalle. El sitio real se abre en un `iframe` con `sandbox` cuando `LIVE` es verdadero: no dentro de claude.ai ni en `127.0.0.1` (donde las herramientas revisan `dist/` sin cargar sitios ajenos), sí en `localhost` (`npm run dev`) y en el dominio. Un sitio que no se deja mostrar (`embed: false`) queda en su recorrido. Cada tira sale de `tourHTML(p, clase, atributos, cel, sizes)`: sus anchos (`tourSrcset`, con `tour`, `tourHi`, `cel`, `celLo` y `celHi` de cada proyecto), cuánto se dibuja ahí (`sizes`), su ancho y alto, y `loading="lazy"`. El detalle toma la de 1600 o la de 780 |

## El inglés

`src/i18n/en.json` es un diccionario: texto en español exacto, texto en inglés. `src/i18n/idioma.astro` lo carga y lo aplica en tres momentos:

1. **Al montar**: recorre lo recién montado y cambia textos y atributos (`aria-label`, `placeholder`, `alt`, `title`) antes de que arranquen las secciones.
2. **En las listas**: `PROJECTS`, `BRANDS`, `STEPS`, `SOCIAL` y `NEEDS` se traducen en su sitio y vuelven al español al cambiar de idioma.
3. **Después**: un `MutationObserver` traduce lo que las secciones escriben más tarde. Las frases que se arman con datos ("Listo, Laura. Pediste: ...") pasan por `RULES` en `idioma.astro`.

`LANG.set('en')` cambia el idioma: recuerda en qué sección y a qué altura está el lector, vuelve a montar la página y regresa a ese punto.

Lo que el lienzo del hero dibuja no pasa por el diccionario: los símbolos son iguales en los dos idiomas y los nombres de los 118 elementos están en las dos listas de `NAMES`, en `hero.astro`, que se elige con `LANG.cur`.

Para agregar un texto: escribirlo en español en la parte y agregar el par en `en.json`. Si una sección dibuja desde una lista nueva, sumarla a `sources()` en `idioma.astro`. `herramientas/idioma.py` avisa si algo se quedó en español.

## Publicación

El sitio se publica en Vercel como una sola aplicación de Astro (`vercel.json`): arma con `npm run build` y sirve `dist/`, nada más. `.vercelignore` deja por fuera lo que no hace falta para armar (`herramientas/`, `archivo/`, `marca/`, `docs/`) y `engines` en `package.json` fija Node 24.

`vercel.json` también manda estas cabeceras con cada respuesta:

| Cabecera | Para qué |
|---|---|
| `X-Content-Type-Options: nosniff` | El navegador no adivina el tipo de un archivo. |
| `X-Frame-Options: SAMEORIGIN` y `frame-ancestors 'self'` | Ninguna otra página puede mostrar el sitio dentro de un marco. Si algún día hace falta (un generador de maquetas, por ejemplo), se cambia aquí. |
| `Referrer-Policy: strict-origin-when-cross-origin` | A otros sitios solo se les dice el dominio, nunca la dirección completa. |
| `Permissions-Policy` | El sitio no usa cámara, micrófono, ubicación ni pagos, y los sitios que abre el visor tampoco pueden pedirlos. |
| `base-uri 'self'; object-src 'none'` | No se cargan complementos ni se cambia la base de los enlaces. |

Todavía no hay una política de contenido completa (`script-src`, `connect-src`): los scripts van escritos en la página y el formulario no envía. Se escribe cuando el formulario tenga a dónde enviar y el dominio sea el definitivo.

El visor abre los sitios de los clientes en un marco aislado (`sandbox`, sin `allow-top-navigation`): corren, pero no pueden sacar al visitante de la página. El sitio no guarda nada en el navegador ni llama a un servidor, así que no usa llaves; si llega a usarlas van en las variables de entorno de Vercel, nunca en git (`.env` y `.vercel/` están en `.gitignore`).

## Ayudas de trabajo que no son parte del sitio

Hoy no hay ninguna. Si se vuelve a poner una (un selector para comparar opciones en pantalla), lleva la clase `proto-picker`: el inglés no la traduce y las herramientas la esconden al capturar.

## Rastros del prototipo

El código viene de un prototipo que comparaba cinco temas. Se limpió para dejar solo Tabla, pero quedan nombres de entonces: el id `'tabla'` en `addSection` y `VARIANTS`, la clase raíz `.v-tab`, sufijos como `contact--tabla` o `rd--tab`. No estorban; si se renombran, hay que hacerlo en todas las partes a la vez y volver a correr la revisión.
