# CaSe Studio

Sitio web de CaSe Studio, un estudio de Medellín que hace sitios web, tiendas en línea, redes sociales y marca.
Los socios son Camilo Corrales (diseño y desarrollo) y Sebastián Vanegas (ventas); Catalina Vanegas maneja redes y contenido.
El nombre sale de **Ca**milo + **Se**bastián, que además son calcio y selenio. De ahí el concepto de todo el sitio: **la tabla periódica**.

**Responde siempre en español.**

## Dónde estamos

- El sitio es una sola página, en español e inglés. Todo lo que muestra es un elemento: servicios, proyectos, pasos, personas.
- Se llegó a este concepto ("Tabla") después de explorar cinco propuestas. Las otras cuatro (Cristal, Lámina, Señal, Tarjetas) están guardadas en un artefacto de claude.ai y sus fuentes en `archivo/`. **Aquí solo se trabaja Tabla.**
- Trabajo en curso: perfeccionar Tabla sección por sección. Decididos: el hero (destellos al azar sin nombre, sin servicios flotando) y Servicios (Escenario: la lista a un lado y un cuadro con la animación del servicio al frente, que cuenta su frase en pasos, sola y con su pausa desde el 22 de noviembre de 2026; después, la Fórmula (Con tu marca, 22 de noviembre de 2026): empieza siempre por Tú (119), los elementos caen de su fila a una bandeja y se funden con él, debajo sale lo que trae cada uno, y pasan a Contacto con "Pedir esta fórmula") y Rediseño (la misma panadería antes y después: se marcan sus problemas y casillas azules los corrigen hasta dejar el sitio nuevo) y Proyectos (la Rueda: los seis sitios en una rueda en 3D que se arrastra con el mouse, el dedo o el trackpad; al abrir uno, el sitio real se abre en vivo con su historia al lado, sin barra arriba desde el 22 de noviembre de 2026) y Marcas (un teléfono con el perfil real de Instagram de cada marca, que pasa solo de una a otra) y Proceso (la Ruta: una línea que el scroll dibuja lleva el elemento de "Tu marca" por cuatro estaciones, que aparecen solo cuando él llega; el lugar punteado de cada una está desde el comienzo, los pasos van sobre el papel sin tarjeta y al final el Tú sale por el extremo de la línea: Lugares, 22 de noviembre de 2026) y Redes (Historias: las seis partes del servicio como seis historias en un cubo que gira solo, como pasan las historias, con publicaciones reales de las marcas en cobalto). Nosotros se quitó (13 de noviembre de 2026): de Redes se pasa al Cierre; el equipo quedó en el pie hasta el 15 de noviembre, cuando el usuario pidió quitar los nombres de las personas. El Cierre también está decidido (Regreso): el logo se arma con el Tú en el medio y vuelve a la tabla periódica, con Ca al 20, Se al 34 y Tú al 119, el elemento que todavía no existe, y con su botón "Empezar mi proyecto": es el último llamado antes del formulario. Su final es Acercamiento (21 de noviembre de 2026): la cámara entra al período 8, el Tú queda grande con las casillas vecinas de fondo, y la frase y el botón ocupan el período nuevo, a su lado. Y Contacto (Una línea): una pantalla con los cuatro servicios para marcar como elementos y una sola barra con nombre, correo o WhatsApp y el botón; lo que se une en la Fórmula llega marcado. La Frase final (Crece, "Crece con CaSe.") se quitó el 17 de noviembre de 2026, a pedido del usuario: el Cierre ya era un buen llamado. Está en `archivo/secciones-quitadas/frase-final.astro`. Y Preguntas (Chat), entre Redes y el Cierre: las preguntas a un lado y un chat en un encuadre al otro; la que se toca entra al chat y CaSe responde en mensajes cortos, solo con lo que el sitio ya dice. Y el Pie (Frente): la tabla periódica es el menú, con las secciones y los servicios en sus casillas y Ca y Se en su lugar; al llegar, la cámara la levanta de frente, y debajo va el logo. En el celular el menú es Hoja: "Empezar mi proyecto" y una casilla "Menú" con la sección en la que vas, que abre una hoja con las ocho secciones con su nombre (15 de noviembre de 2026). También en el celular: la rueda de Proyectos pasa cada sitio como lo ve un teléfono (sus tiras `tour-<id>-cel*.webp`, de `herramientas/recorridos.py`; los seis, también Weed Honey desde el 16 de noviembre de 2026) y el pie es un mapa: la tabla pequeña con las casillas del estudio encendidas y, debajo, las secciones y los servicios con su nombre. Lo que muestra un servicio, un sitio o una marca va en un **encuadre** (`encuadre.astro`): un marco con la luz del hero que se mueve con el scroll, y las piezas flotando encima sin tablero. El 16 de noviembre de 2026 entró la ronda Acabado: los ajustes de la crítica en todo el sitio, sin cambiar secciones. El 22 de noviembre entraron los arreglos de la revisión del 21: las casillas de Marcas van en los azules del sitio (y en el celular la marca dice su nombre y su línea bajo el encuadre), Preguntas llega con la primera pregunta ya respondida, y la frase del Cierre y los pasos de Proceso siempre están al alcance del teclado y del lector de pantalla. Qué está decidido y qué falta: `docs/estado.md`.
- El 22 de noviembre de 2026 el usuario pidió menos movimiento atado al scroll: Servicios, Marcas y Redes dejaron de quedarse fijas (se cuentan solas, con pausa) y solo el hero, Rediseño, Proceso y el Cierre son momentos. Ese día entraron también el scroll suave (Lenis), las fuentes servidas desde el sitio, el arranque que pinta primero el hero y lo de buscadores y asistentes (datos estructurados, `robots.txt`, `sitemap.xml`, `llms.txt`).
- Está publicado en https://www.casestudio.com.co (Vercel, desde `main`). El formulario envía al WhatsApp del estudio, +57 310 872 3020 (23 de noviembre de 2026: "todo debería llegar allí"): abre WhatsApp con la solicitud escrita y el visitante la envía desde allí. El número sale también en el pie, los datos estructurados y `llms.txt`, y vive en `src/datos/sitio.json`. Falta el correo, que el usuario va a dar.

## Mapa

```
src/                   el sitio (Astro, estático)
  pages/index.astro    la página: el layout y las partes, en un orden que importa
  pages/*.ts           robots.txt, sitemap.xml, llms.txt y llms-full.txt, que salen del dominio y del contenido
  datos/               sitio.json (título, descripción y lugar, a mano) y contenido.json (copia de lo que dicen las secciones: no se edita)
  layouts/Base.astro   el <head>: fuentes, colores (:root), estilos base y funciones compartidas
  partes/              una parte por sección: su CSS, su plantilla y su código juntos
  components/          piezas que se repiten: Nav, Flecha, Pausa; Plano (el contenido escrito, para quien llega sin JavaScript) y Datos (schema.org)
  i18n/en.json         diccionario español -> inglés
  i18n/idioma.astro    el código que aplica el inglés
  assets/              originales de las ilustraciones que genera el usuario (Nano Banana)
public/assets/         imágenes de los proyectos (póster y recorrido de cada uno) y las ilustraciones ya en cobalto (herramientas/cobalto.py)
dist/                  GENERADO por npm run build. No se edita a mano
herramientas/          revisión automática y capturas (Python + Playwright). Ver herramientas/README.md
docs/                  estado.md, arquitectura.md, contenido.md
marca/                 logos finalistas y la exploración de logos
archivo/               las cinco propuestas originales, la bitácora, el sitio armado con Python (sitio-python/), que ya no se usa, y las secciones que se quitaron (secciones-quitadas/)
```

## Trabajar en el sitio

```
npm run dev              sirve el sitio en http://localhost:4321 y se recarga al guardar
npm run build            arma dist/, lo que se publica
npm run revisar          arma y corre las seis revisiones; debe decir "bien" en todas
npm run contenido        después de cambiar un texto: vuelve a copiar lo que dice el sitio a src/datos/contenido.json
npm run carga            cómo carga en un celular lento (primera pintura, pintura más grande, tareas largas)
```

En el panel del navegador de Claude: `preview_start` con el nombre `case-studio` (`.claude/launch.json`).

Un cambio está terminado cuando:
1. `npm run revisar` termina con las seis en "bien".
2. Se miraron capturas del cambio a 1440 y a 390 de ancho, y con movimiento reducido (`herramientas/capturar.py`).
3. Todo texto nuevo tiene su par en `src/i18n/en.json`, y si cambió un texto del sitio se corrió `npm run contenido` (lo que leen los buscadores y los asistentes sale de esa copia; la revisión avisa si quedó vieja).
4. Si tocó algo que se ve (CSS, plantillas, canvas, movimiento, textos en pantalla), pasó el **chequeo de diseño** de abajo.

### Chequeo de diseño (obligatorio en todo cambio de UI)

Todo cambio que modifique la interfaz pasa por los dos skills antes de darse por terminado, sin que el usuario tenga que pedirlo:

1. **Impeccable** (instalado en `.claude/skills/impeccable`, con `npx impeccable install`). Se carga el skill *impeccable* y se sigue su preparación (`impeccable context`, y `craft-floor.md` antes de editar). Al terminar se corre su detector sobre la página armada: `.claude/skills/impeccable/scripts/impeccable detect dist/index.html` (en PowerShell, `impeccable.cmd`). Sobre los `.astro` solo corre reglas de texto. Lo que marca en Rediseño es a propósito: esa sección imita el estilo de IA para burlarse de él. Para cambios grandes, además, `/impeccable polish` o `/impeccable critique` sobre la sección.
2. **Taste** (*design-taste-frontend*). Se carga el skill y se revisa el cambio contra su lista anti-plantilla.

Lo que señalen se corrige o, si choca con una regla de diseño de este archivo, se le explica al usuario por qué se deja. Las reglas de este archivo ganan sobre las de los skills. En el resumen final se dice qué encontró cada chequeo.

El movimiento no se puede juzgar con capturas: se revisa el recorrido cuadro a cuadro y se le dice al usuario que lo mire en vivo.

## Reglas de diseño

Vienen de decisiones del usuario. No se negocian sin preguntarle.

1. **Premium y original.** Nada que parezca hecho por una IA sin criterio: degradados morados, tarjetas idénticas con icono, emojis, vidrio esmerilado por defecto, textos de relleno. La sección "Rediseño" del sitio se burla de eso mismo.
2. **Movimiento, con el scroll normal casi siempre** (22 de noviembre de 2026: el usuario dijo que había demasiado movimiento atado al scroll). Cuatro secciones son momentos, se quedan fijas en pantalla y el scroll las mueve (`.moment` y `moment()`): el hero, Rediseño, Proceso y el Cierre. Las demás pasan con el scroll como cualquier sección.
   - **Servicios, Marcas y Redes** se cuentan solas mientras están en pantalla (`showtime()`, en `comun.astro`), una vez: tienen su pausa, sus filas llevan a cualquier punto y al terminar descansan. Nada gira sin fin.
   - **Fórmula**, **Proyectos** y **Preguntas** siguen como estaban: algo que el visitante arma, una rueda que mueve y un chat que usa.
   - El movimiento que corre solo es tranquilo, y lo que dura más de 5 segundos tiene pausa.
   - El scroll de la página es suave (Lenis, `suave.astro`): se desliza y se asienta. Con movimiento reducido, o con el dedo en un celular, es el del navegador.
3. **En el hero no hay luces ni barridos que crucen de lado a lado.** El usuario pidió quitar la que había.
4. **Contenido ancho, márgenes delgados** (`--gutter`).
5. **Blanco, negro y azul.** Los colores son variables de `:root` en `src/layouts/Base.astro`, con un solo cobalto (`--cobalt`) y cada otro azul con su papel (`--night`, `--cell`, `--deep`, `--cobalt-deep`, `--sky`, `--ice`, `--frost`, `--lab`, `--focus`; sus transparencias con `rgba(var(--cobalt-rgb),.2)`). En los estilos no se escribe un azul a mano: se usa su variable. El foco es `--focus` sobre la noche y el cobalto sobre el papel.
6. **Sin líneas divisorias horizontales.** Una sección pasa a la siguiente con luz compartida (`uniones.astro`) y un cambio de color llega como un mosaico que se arma (`color.astro`), nunca como una raya. Tampoco se corta nada en el borde de una sección: una sombra o una luz que pasa del borde de una sección fija deja una raya del ancho de lo que la proyecta. Lo verifica `herramientas/lineas.py`.
7. **El menú fijo no tapa texto.** Lo verifica `herramientas/bajo_menu.py`.
8. **Cada sección cuenta lo suyo como elementos**: símbolo grande, número pequeño, nombre. Si algo nuevo no encaja en esa idea, se replantea. El número nunca baja de 9,5 px, en cifras tabulares: se atenúa con el color, no con el tamaño (ronda Acabado, 16 de noviembre de 2026). Cada cosa tiene un solo símbolo y un solo número en todo el sitio, los de `EL_Z` en `Base.astro`:
   - lo que vive en la tabla del pie lleva su número de ahí;
   - los clientes comparten una cuenta del 01 al 11;
   - "Tu marca" es Tú 119;
   - lo demás va por su lugar en su lista.
   Un símbolo nuevo no repite uno que ya existe.
9. **Movimiento reducido**: con `prefers-reduced-motion` todo se lee quieto y completo.
10. **Celular**: se revisa a 390 de ancho; nada para tocar mide menos de 40 px.

El diseño se trabaja con los skills *impeccable* y *design-taste-frontend* (ver "Chequeo de diseño"). Para comparar direcciones distintas de una pieza está el skill *prototype* de Emil Kowalski (`.claude/skills/prototype`, se invoca a mano): las variantes viven aparte (un artefacto de claude.ai o una página de prueba) y nunca en `src/` hasta que el usuario elige una.

## Reglas de texto

- Español de Colombia, de tú. Frases llanas y concretas.
- Sin "no es X, es Y", sin listas de negaciones, sin preguntas que se contestan solas.
- Sin raya (—) en textos cortos.
- **Nada inventado**: ni cifras, ni clientes, ni testimonios. Solo lo que está en `docs/contenido.md` o lo que el usuario diga.
  Una publicación real de un cliente nunca se presenta como hecha con IA: la historia "Contenido con IA" de Redes se dibuja (16 de noviembre de 2026).
- Botones con verbo y objeto: "Empezar mi proyecto", "Ver proyectos", "Armar mi fórmula". No se usa "Agendar llamada".
- Los servicios son cuatro: sitios web, tiendas en línea, redes sociales y marca. **Anuncios no es un servicio.**
- Para textos de marketing se usa el skill *copywriting* si está instalado.
- El inglés es traducción de Claude: el usuario todavía no lo ha revisado.

## Reglas técnicas

- El stack es **Astro** (estático, TypeScript estricto). Se eligió sobre Next porque el sitio es una página de presentación, sin sesión ni datos por usuario: Astro no carga React y el código de canvas pasa tal cual. Si el sitio crece hacia una aplicación (portal de clientes, pagos), se puede sumar React como isla o replantear.
- Las partes usan `<style is:global>` y `<script is:inline>`: los estilos se juntan en el orden de la página y los scripts comparten funciones globales. En el HTML de una parte no van llaves `{ }` sueltas (Astro las lee como código).
- El orden de `src/pages/index.astro` importa: los estilos de una parte pueden pisar los de las anteriores, y `color` y `menu` envuelven la función que define `ensamble`.
- Los textos que una sección dibuja desde código salen de listas (`PROJECTS`, `BRANDS`, `STEPS`, `SOCIAL`, `NEEDS`, `FAQ`, `FAQ_SAY`). El inglés las traduce en su sitio: si se agrega una lista nueva hay que sumarla a `sources()` en `src/i18n/idioma.astro`. Lo que dibujan los lienzos (los nombres de los elementos en el hero, las palabras de las animaciones de Servicios en `escenas.astro`) elige idioma con `LANG.cur`; los tramos de la frase de cada servicio sí pasan por el diccionario.
- El movimiento tiene una sola física (16 de noviembre de 2026): siete duraciones en `:root` (`--d-press` 90, `--d-hover` 150, `--d-fade` 200, `--d-state` 260, `--d-move` 440, `--d-enter` 560, `--d-scene` 720 ms) y dos curvas (`--ease-out` para lo que llega, `--ease-io` para lo que va y vuelve entre dos estados). En el CSS no se escribe una duración a mano; las animaciones hechas desde el código usan `MOTION.d('state')` y `MOTION.ease('out')`. Los retrasos de coreografía sí van a mano.
- Teclado: el primer enlace es "Saltar al contenido", el menú fijo va primero en el DOM y un enlace interno lleva el foco a su sección (`arranque.astro`). Un enlace que va a más de dos pantallas no recorre el camino: la página pasa un instante por la noche y abre en la sección (`JUMP`), para no cruzar los momentos fijos a toda velocidad. Lo que corre solo más de 5 segundos tiene pausa (el hero y la rueda de Proyectos).
- Toda imagen lleva su ancho y alto, `loading="lazy"` si no está en la primera pantalla, y sus anchos con `srcset` y `sizes` para que cada pantalla tome 2x de lo que muestra y no más.
- Fuentes (elegidas por el usuario el 11 de noviembre de 2026): Schibsted Grotesk para titulares, texto y símbolos (`--head`, `--font`, `--sym`) e IBM Plex Mono para números atómicos y datos (`--mono`). Las sirve el propio sitio (paquetes de Fontsource, `Base.astro`): no se pide nada a Google. Los símbolos de los elementos siempre usan `var(--sym)`, nunca un nombre de fuente escrito. No se usan Geist, Space Grotesk, Plus Jakarta Sans ni Poppins.
- La carga (22 de noviembre de 2026): la hoja de estilos va dentro de la página, los scripts se minifican al armar (`astro.config.mjs`; los nombres de arriba de cada script no cambian, porque se comparten) y el hero se pinta antes de preparar las demás secciones, que despiertan después de a pocas (`arranque.astro`). La página dice que terminó con `window.MOUNTED`. Mientras se arma, nada hace una transición hacia su primer estado (`.is-booting`).
- Mover la página desde el código: `window.GO(y)` para un tramo corto y `window.JUMP(y)` para uno largo; los dos usan el scroll suave si está. El detalle de un proyecto lo detiene mientras está abierto, y lo que tiene scroll propio lleva `data-lenis-prevent`.
- Buscadores y asistentes: el título, la descripción y el lugar están en `src/datos/sitio.json`; de `src/datos/contenido.json` salen el contenido escrito para quien llega sin JavaScript (`Plano.astro`), los datos estructurados (`Datos.astro`), `llms.txt` y `llms-full.txt`. Ahí también está el WhatsApp del estudio (`whatsapp`, `whatsappVisible`), que la página toma de `window.CONTACTO`; el correo se agrega cuando el usuario lo dé.
- Cómo está armada la página por dentro: `docs/arquitectura.md`.

## Lo que no se hace

- No se hace commit ni push sin que el usuario lo pida.
- No se tocan los otros repositorios de `My Repos`.
- No se generan imágenes con Higgsfield. Si hace falta una imagen se le entrega al usuario el prompt completo para Nano Banana (estilo vectorial o ilustrado) y él la genera.
- No se publica el correo personal del usuario ni datos de contacto reales hasta que él los entregue. Entregado: el WhatsApp +57 310 872 3020 (23 de noviembre de 2026).
