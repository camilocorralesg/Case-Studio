# Estado del proyecto

Última actualización: 22 de noviembre de 2026.

## Lo que hay

Una página con once secciones, en español e inglés, toda con el concepto de la tabla periódica:

| # | Sección | Qué hace | Parte |
|---|---|---|---|
| 1 | Hero | La tabla periódica como un piso de casillas que se arma al entrar; en reposo se encienden elementos al azar. Al bajar, la cámara sube, la tabla se hunde y Ca y Se se juntan como el logo | `hero.astro` |
| 2 | Servicios | Sobre papel claro, que se arma casilla a casilla al salir del hero. La lista de los cuatro a un lado; al otro, un cuadro grande con la animación del servicio que está al frente, que cuenta su frase en pasos. Desde el 22 de noviembre de 2026 no se queda fija: se cuenta sola mientras está en pantalla (unos seis segundos por servicio), con su pausa, y tocar una fila trae su servicio | `servicios.astro`, `escenas.astro` |
| 2b | Fórmula | Justo después, sobre el mismo papel (Con tu marca): la fórmula empieza siempre por Tú (119); los cuatro elementos esperan en una fila, cada uno con su lugar punteado, y al tocarlos o arrastrarlos caen a una bandeja y se funden con él, más grandes; debajo, lo que trae cada uno, con su frase de Servicios; "Pedir esta fórmula" lleva a Contacto con esas opciones marcadas | `formula.astro` |
| 3 | Rediseño | El mismo negocio, una panadería, antes y después: se marcan los problemas del sitio genérico y cada uno se corrige con casillas azules que lo deshacen; el resto se va en una ola y queda el sitio rediseñado | `rediseno.astro` |
| 4 | Proyectos | La Rueda: los seis sitios en una rueda en 3D sobre el piso de noche del hero, que se arrastra, se lanza y se mueve con sus elementos. "Ver proyecto" hace crecer la pantalla del frente hasta el detalle, donde el sitio real se abre en vivo con su historia al lado. El detalle no tiene barra arriba (22 de noviembre de 2026): dos casillas en la esquina, el ancho del sitio y salir | `proyectos.astro`, `visor.astro` |
| 5 | Marcas | Un teléfono, dentro de un encuadre con la luz del hero, muestra el perfil real de Instagram de cada marca y pasa solo de una a otra, con su pausa (22 de noviembre de 2026: lo pasaba el scroll, en una sección fija); al lado, las seis, con la del teléfono encendida; tocar una lleva el teléfono a su perfil. Las marcas no abren detalle | `marcas.astro` |
| 6 | Proceso | La Ruta, sobre papel claro (Lugares): una línea que el scroll dibuja lleva el elemento de "Tu marca" por cuatro estaciones; la ruta y el lugar punteado de cada una están desde el comienzo, y cada paso aparece, con su elemento encendido y su texto sobre el papel, solo cuando él llega; al final el Tú sale por el extremo de la línea | `proceso.astro` |
| 7 | Redes | Historias: las seis partes del servicio como seis historias en un cubo que gira solo, como pasan las historias, con su pausa (22 de noviembre de 2026: lo giraba el scroll, en una sección fija), dentro de un encuadre; cada una empieza su dibujo al quedar de frente; al lado, las seis, que llevan a cada historia | `redes.astro` |
| 8 | Preguntas | Chat: las siete preguntas a un lado, cada una con el elemento de la parte del sitio que la responde, y un chat en un encuadre al otro. La pregunta que se toca entra al chat y CaSe responde en mensajes cortos, al ritmo de quien escribe; en el celular las preguntas van dentro del chat, como respuestas rápidas | `preguntas.astro` |
| 9 | Cierre | Regreso, sobre azul: el logo se arma (Ca y Se, y Tú cae entre ellos) y vuelve a la tabla periódica, cada uno a su lugar real: Ca al 20, Se al 34 y Tú al 119, en un período 8 que se abre; después la cámara entra a ese período (Acercamiento): el Tú queda grande, con las casillas vecinas de fondo, y a su lado, en el período nuevo, "El elemento que falta es tu marca." y "Empezar mi proyecto": el último llamado antes del formulario | `cierre.astro` |
| 10 | Contacto | Una línea, en una pantalla: los cuatro servicios como elementos para marcar y una sola barra con nombre, correo o WhatsApp y "Enviar por WhatsApp", que abre WhatsApp con la solicitud escrita para el +57 310 872 3020 (23 de noviembre de 2026). Lo que el visitante une en la Fórmula llega marcado | `contacto.astro` |
| | Pie | Frente: la tabla periódica es el menú (las secciones y los servicios en sus casillas, Ca y Se en su lugar), con el contacto y la leyenda en su hueco; al llegar, la cámara la levanta de frente, y debajo el logo | `pie.astro` |

Además: un menú fijo que marca la sección (una fila de casillas arriba; en el celular, "Menú" con la sección en la que vas, que abre una hoja con las siete secciones), cambio de idioma que conserva el lugar de lectura, cambios de color que se arman como mosaico, y versión quieta para quien pide menos movimiento.

`python herramientas/revisar.py` pasa limpio.

## El hero (decidido el 11 de noviembre de 2026)

- **En reposo: destellos al azar.** Un elemento se enciende, se queda un momento y se apaga despacio; su luz alcanza a las casillas vecinas. Nunca hay más de tres a la vez y a veces pasa un rato sin ninguno, para que no parezca un metrónomo. Ca y Se no destellan: son el logo.
- **Sin servicios flotando** (W, Ti, Re, Mc quedaron descartados). Servicios y Redes siguen con sus símbolos de siempre (Sw, Ti, Rs, Ma).
- **La tabla se arma al entrar** y **la cámara alta** quedaron como estaban.
- Acabado: cada casilla tiene un brillo que cae desde su borde de arriba, un borde más claro arriba que abajo y, cuando se enciende, una luz desde adentro. El fondo tiene un horizonte azul detrás de la tabla, luz en el piso alrededor de Ca y Se, esquinas en sombra y un desvanecido al pie sin franjas. El bloque f dejó el tono lila y pasó a un azul acero.
- Se borraron `revision.html` y todas las ramas de opciones.

Hecho el 11 de noviembre de 2026, ya en Astro:
- **Ca y Se aterrizan de últimos.** La tabla se arma sin ellos; caen después con un pequeño asiento y su casilla se ilumina al recibirlos, con luz que alcanza a las vecinas. Los destellos empiezan cuando ya aterrizaron.
- **Los destellos al azar no llevan nombre** (decisión del usuario, 12 de noviembre). Solo el elemento que alguien toca o clica muestra su nombre en una etiqueta pequeña sobre la casilla, en el idioma de la página. Los 118 nombres están en `hero.astro`.
- **Un toque o un clic enciende la casilla** y muestra su nombre, también en celular. Con movimiento reducido la casilla queda encendida, quieta.
- **Un solo "Empezar mi proyecto"**: el de la barra se esconde mientras se ve el titular con su botón, y vuelve al bajar. Con movimiento reducido se queda visible.

Lo que queda por mejorar del hero:
1. **La tabla se corta a los lados a 1440** (Cs, Rn, Fr, Og). Medir la fila más cercana para que entre completa, o aceptar el corte como un piso que sigue.
2. **En celular las casillas no llevan símbolo** (miden menos de 26 px). Girar la tabla (periodos como columnas) duplica el tamaño.
3. La frase bajo el titular podría decir dónde está el estudio ("en Medellín").

## Rediseño (decidido el 12 de noviembre de 2026)

De la ronda de prototipos (https://claude.ai/artifact/CXS8xCDL1JKmV6YeK998dt) el usuario pidió una mezcla de **Revisión** y **Mosaico**, y que el sitio rediseñado se viera como un diseño excelente. Ya está en `rediseno.astro`:

- **Los dos sitios son la misma panadería, "Tu marca".** Antes: todos los hábitos de un sitio generado (degradado morado, emojis, "Desbloquea el poder de tu panadería", dos botones que brillan, sus productos vestidos de tarjetas "Innovador / Robusto / Potente"), y nunca dice cómo pedir. Después: fondo blanco, titular grande con "a las 7." en cobalto, "Hacer un pedido" y "Ver el menú", la ilustración del pan ocupando todo el lado derecho hasta los bordes, un pedido flotante encima ("Tu pedido · Pedir por WhatsApp"), "Recién salido" con el reloj que va de 06:48 a 07:00 mientras la penumbra se levanta del pan, y abajo a la izquierda una línea con lo de hoy ("Hoy: Masa madre, Croissant, Pan de queso"). Antes eran tres tarjetas iguales con icono: el mismo patrón que la nota 04 critica, por eso pasaron a ser una línea. Lo que funciona pasa de uno a otro: el nombre, los productos y pedir por WhatsApp.
- **La animación:** primero se marcan cuatro problemas sobre el sitio viejo (01 Emojis de relleno, 02 Promesa vaga, 03 Dos botones compiten, 04 Tarjetas iguales). Después cada uno se corrige en orden: casillas del azul de la marca tapan esa zona, el sitio viejo desaparece bajo ellas y al encogerse dejan ver el nuevo; la nota pasa a blanco y se va. Al final, el resto del sitio viejo se va en una ola de casillas de arriba a la izquierda hacia abajo a la derecha.
- **En celular** (hasta 600 px) los dos sitios se muestran como se ven en un celular: el cuadro es vertical (4:5), cada sitio tiene su versión de una columna y las casillas son 12 × 15. Así todo se lee; en horizontal el texto del sitio quedaba de 5 px.
- **Antes / Después** es un indicador del estado (un cuadrito azul junto al que está al frente). Antes eran dos píldoras que parecían botones y no hacían nada.
- Con movimiento reducido se ven los dos sitios quietos, el viejo pequeño y el nuevo grande; en celular, uno debajo del otro. El indicador no se muestra. En inglés se traducen los dos sitios y las notas.
- El pan es la ilustración que el usuario generó con Nano Banana. El original está en `src/assets/rd-pan.jpg`; `herramientas/cobalto.py` lleva su azul de fondo al cobalto de la marca (#3464ac → #1e55e0) sin tocar el pan, y la guarda en `public/assets/rd-pan-640.webp` y `rd-pan-1024.webp`. Este fue el prompt, por si hay que repetirla ("Recién salido" y "Tu pedido" van encima, a la izquierda):

  ```text
  Editorial illustration of one round sourdough loaf, freshly baked, with a single deep curved ear score and a light dusting of flour, sitting on a simple light-wood cutting board. Three thin wisps of steam rise from the crust. Crust in golden brown, warm amber and toasted chestnut tones, with fine texture; a few crumbs and a pinch of flour on the board. Background: flat cobalt blue (#1E55E0) with a large, soft morning-sun glow in the upper right (lighter blue #4F8DFF fading into the cobalt) and a gentle warm rim light on the right side of the loaf. Modern vector illustration, clean shapes, subtle gradients, premium bakery brand look, calm and minimal. Square 1:1 composition: the loaf large, in the lower right two thirds, slightly cropped by the right edge, the board cropped by the bottom edge; open blue space in the upper left and lower left for interface elements. No text, no logos, no hands, no people, no other props.
  ```

- Los prototipos quedan como archivo en sus artefactos.
- El cuadro no lleva resplandor azul debajo: Impeccable lo marca como gesto de IA y la luz propia de la sección basta. Redes ya no lo tiene (13 de noviembre de 2026); el aviso `dark-glow` que sigue en el detector sale de las casillas Ca y Se del pie (`pie.astro`, `0 0 30px 6px`), que no se han trabajado.

## Proyectos (decidido el 13 de noviembre de 2026)

Ronda de prototipos del 12 de noviembre de 2026: https://claude.ai/artifact/8giPsv9oQXTFftBTJRpWW2 (fuente en el scratchpad de esa sesión, carpeta `proyectos/`). Nada de esto está en `src/` hasta que el usuario elija. Las cuatro usan los datos reales de `visor.astro` y el mismo visor:

- **Bloque**: todos a la vista, con jerarquía. Un bloque de la tabla con fichas de distinto tamaño (Los Duches grande, NeuralNet ancha, NeuralBI y AKUA altas); el scroll las arma y cada elemento se abre en su sitio.
- **Índice**: todos a la vista, manda el texto. Lista grande con número, símbolo, nombre, tipo y lugar; al pasar el cursor, el sitio aparece junto a él. En celular cada fila lleva su primera pantalla.
- **Casos**: uno por uno, con su historia. Fichas que se apilan con el sitio, qué es, dónde, lo construido y los botones "Ver proyecto" y "Visitar sitio".
- **Zoom**: uno por uno, manda la imagen. La cámara entra en la tabla, se detiene en cada sitio con su nombre y su tipo, y al final vuelve al bloque completo.

Segunda ronda (12 de noviembre de 2026): https://claude.ai/artifact/BZWV9UDimJ25PmQiuiTU89 (fuente en la carpeta `proyectos2/` del scratchpad). Al usuario le gustó el **Índice**, pero con una animación de entrada en lugar de ir atado al scroll, y pidió carruseles. Ninguna de estas va fijada al scroll: la sección entra una vez cuando se ve y el visitante la mueve, así que la que se elija hace de Proyectos otra excepción a la regla 2, como Fórmula.

- **Índice**: la misma lista, que entra fila por fila al aparecer; cada elemento se enciende un instante al llegar.
- **Cinta**: tira que se desliza con el dedo, el trackpad, las flechas o arrastrando; el sitio del centro va al frente y sus vecinos esperan en los bordes.
- **Rueda**: carrusel en 3D; el del frente mira de frente y los demás giran hacia el fondo. Se arrastra, se lanza y se detiene en el sitio más cercano.
- **Mazo**: pila de sitios; el de adelante se lanza a un lado y pasa al fondo de la pila.
- **Marquesina**: dos filas que se deslizan solas, despacio y en sentidos contrarios; se detienen al pasar el cursor y tienen un botón de pausa.

**Elegida: la Rueda**, en pulido (12 de noviembre de 2026): https://claude.ai/artifact/PTD2mo5QAaopTM41MrSnuA (fuente en la carpeta `rueda/` del scratchpad; el selector compara "Pulida" con "Antes"). El usuario pidió quitar el aspecto de terminal de los sitios y rehacer por completo el detalle: que el sitio se expanda del todo, con color, diseño y los tonos del hero.

- **Los sitios en la rueda** son pantallas limpias: sin barra de navegador, bordes redondeados, un filo de luz, el brillo de las casillas del hero arriba y un reflejo suave en el piso. El del frente se para en una luz azul. Abajo, el elemento del frente encendido como los del hero, su nombre, tipo y lugar, los elementos para ir a cualquiera y "Ver proyecto".
- **El detalle**: la pantalla del frente crece desde la rueda (en la misma pantalla del sitio que estaba mostrando) hasta llenar el alto de la pantalla, y se recorre pantalla por pantalla (avanza sola hasta que se toca; los números al lado marcan cuál se ve). Al lado, la historia: el elemento grande encendido, sector y lugar, nombre, tipo, el texto, los datos, lo que se construyó, "Visitar sitio" y los proyectos vecinos para seguir sin cerrar. Detrás, la tabla de noche del hero: casillas tenues, algunas que se encienden despacio, luz azul abajo y esquinas en sombra. Al cerrar, la rueda queda en el último proyecto visto y la pantalla vuelve a su lugar. En celular es una hoja que se baja entera: el elemento y el nombre, el sitio completo y después la historia.
- **Detalle en vivo** (segunda vuelta, mismo artefacto, variante "En vivo"): el usuario pidió mejorar más el detalle y que el sitio se pudiera visitar en vivo desde ahí. El sitio real se abre en vivo dentro del detalle y se navega; mientras carga se ve su recorrido y el sitio aparece encima. Arriba, una barra flotante (no un marco de navegador): "En vivo", la dirección con su elemento, volver a cargar, abrir en pestaña nueva y ver a todo el ancho (la historia se aparta). La historia va en un panel a la derecha con la luz del hero: elemento, sector y lugar, nombre, tipo, texto, datos en filas, lo que se construyó, "Visitar sitio" y los vecinos. Al cerrar, el sitio en vivo se descarga.
- **Tercera vuelta** (13 de noviembre de 2026): el usuario pidió quitar los contadores ("01 / 06", en el detalle y en la rueda), quitar el indicador "En vivo", que la barra no fuera una cápsula y menos texto en la descripción. Quedó así: una sola barra arriba de todo el detalle, con esquinas suaves y la superficie de las casillas del hero (a la izquierda el elemento del sitio con su nombre y dirección; a la derecha volver a cargar, abrir en pestaña nueva, ver a todo el ancho y cerrar). El panel dice lo justo: el elemento, el nombre, el tipo, la primera frase del texto del proyecto (recortada, no reescrita), sector, lugar y tipo de sitio en etiquetas, "Lo que construimos" plegado, "Visitar sitio" y los vecinos con la imagen de su sitio. La barra de desplazamiento del sitio en vivo (blanca en Windows) queda escondida tras el borde, sin cortar el sitio. El número pequeño dentro de cada elemento se dejó (regla 8).
- Cinco de los seis sitios se dejan mostrar dentro de otra página. Weed Honey lo bloquea (`frame-ancestors 'none'` y `X-Frame-Options: DENY`) y queda en su recorrido con "Abrir en pestaña nueva". Dentro de claude.ai ningún sitio puede mostrarse en vivo, así que el artefacto muestra los recorridos; la prueba en vivo se sirve en local (`servir.py` en la carpeta `rueda/` del scratchpad, http://127.0.0.1:8790/index.html).
- **Ya en el sitio** (13 de noviembre de 2026): el usuario eligió **la Rueda con el detalle "En vivo"**. Reemplazó a la cuadrícula de `proyectos.astro` y al visor viejo de `visor.astro` (el de la barra de navegador). Lo que se decidió al llevarla:
  - Proyectos no va fijada al scroll (otra excepción de la regla 2 en `CLAUDE.md`, como Fórmula): entra una vez cuando se ve.
  - Solo corre el recorrido del sitio del frente, y solo mientras la rueda está en pantalla y el detalle cerrado.
  - El sitio en vivo va en un `iframe` con `sandbox` (scripts, mismo origen, formularios y ventanas nuevas; no puede mover la página de arriba). `LIVE` ahora deja `localhost` (para verlo con `npm run dev`) y sigue dejando fuera `127.0.0.1`, donde `npm run revisar` revisa sin cargar sitios ajenos. Al cerrar o al pasar a un sitio que no se deja mostrar, el sitio en vivo se descarga.
  - **Marcas** abre el mismo detalle: la barra con su elemento en sus colores y su cuenta, la marca como un elemento grande en sus colores (número, símbolo, nombre y sus cuentas) en lugar del sitio, y al lado su historia corta, "Lo que hicimos" plegado, "Ver en Instagram" (y TikTok) y las marcas vecinas. Al cerrar, la marca vuelve a su casilla aunque se haya navegado a otra.
  - Mientras el detalle está abierto, la página guarda el lugar de su barra de desplazamiento, así lo de atrás no se mueve y la pantalla vuelve justo a su sitio.
  - En celular el escenario de la rueda mide lo que la pantalla del frente y su reflejo, para que el nombre quede justo debajo.
  - La sombra larga de cada pantalla va en una capa aparte: dibujada con la pantalla, se repintaba en cada cuadro mientras corre el recorrido. Sin GPU (Chromium de las herramientas) la rueda va lenta a 1440; en un navegador normal hay que mirarla en vivo.
  - `bajo_menu.py` ahora mira la opacidad real de cada texto (la suya por la de lo que lo contiene): las casillas de Marcas esperan invisibles bajo el menú antes de caer y las contaba.
  - Las capturas de los sitios miden 800 px de ancho; con capturas de 1600 px el recorrido se vería más nítido a pantalla completa.

## Marcas (decidido el 13 de noviembre de 2026: Perfil)

Ronda de prototipos del 13 de noviembre de 2026: https://claude.ai/artifact/E8162NzEwHnwb2gGHqt2wh (fuente en la carpeta `marcas/` del scratchpad de esa sesión; `armar.py` arma la página con el `<head>` del sitio y el detalle real de `visor.astro`). Nada de esto está en `src/` hasta que el usuario elija. Hoy Marcas es un titular y seis casillas que caen con el scroll durante dos pantallas y media; lo que se hizo con cada marca solo se ve al abrirla. Las cuatro van fijadas al scroll (regla 2), usan solo lo que está en `contenido.md` y abren el mismo detalle de Proyectos:

- **Periodo**: una a la vez. Cada marca llega grande con su frase, sus cuentas y lo que se hizo; al seguir bajando se encoge hasta su casilla en un periodo de seis. Al final queda la fila completa con "We + Ag + Mi + Sp + O' + Ea".
- **Capítulos**: el scroll mueve de lado una cinta donde cada marca ocupa un panel del alto de la pantalla en sus colores, con su símbolo gigante y su historia al lado.
- **Perfil**: un teléfono muestra el perfil de cada marca (su elemento como foto, la cuenta, su frase y una cuadrícula hecha con sus colores, sin publicaciones inventadas) y el scroll pasa de una a otra; al lado, la lista de las seis con la del teléfono encendida. Al usuario le gustó esta; pidió que el teléfono mostrara cómo se ve de verdad cada perfil en Instagram. Ya muestra una captura real del perfil público de cada marca a tamaño de celular (tomadas el 13 de noviembre de 2026, sin la ventana que invita a abrir la app), en la carpeta `marcas/ig/` del scratchpad. Falta **Weed Honey**: Instagram lo muestra como "Perfil restringido" (contenido para adultos) y solo se ve con sesión iniciada, así que sigue con el perfil dibujado en sus colores hasta tener una captura hecha desde la cuenta. Las capturas traen las cifras reales del día (La Miguería 289 mil seguidores, Speedo 71,4 mil, O'Neill 10,6 mil, Graduados EAFIT 7.618, Agilcash 380).
- **Directorio**: las seis en tipografía grande, todas a la vista; la fila que el scroll pone al frente se abre y dice qué se hizo.
- **Actual**: la sección como está hoy, para comparar.

## El encuadre (decidido el 13 de noviembre de 2026: luz con el scroll)

El usuario mostró una referencia (piezas de interfaz flotando dentro de un marco redondeado con una atmósfera detrás) y pidió llevar esa idea a las zonas que muestran sitios, marcas y animaciones, con los colores del hero y sin nubes. Prototipo del 13 de noviembre de 2026, montado sobre el sitio armado: https://claude.ai/artifact/WDbbRqVutxpwK4rwfM4bZj (fuente en la carpeta `encuadre/` del scratchpad de esa sesión). Se prueba en Servicios y en Rediseño.

- **Segunda vuelta** (pedida por el usuario): en Servicios ya no hay tablero blanco; las tarjetas de cada animación (el navegador, la tienda, el carrito, el calendario, el teléfono) flotan solas sobre el fondo. En Marca, que dejaba piezas sueltas, las dos hojas de la guía están desde el principio (la izquierda con el logo y los colores, la derecha cuando llegan las tipografías) y las sombras de las tarjetas son más hondas para despegarse de la noche. En el prototipo esto se hace ajustando `escenas.astro` sobre lo armado; si se elige, va a `src/` con una bandera.
- Rediseño: la panadería flota dentro de un marco algo más grande que ella.
- Fondos, todos con los colores del hero (noche, cobalto, azul cielo, hielo):
  - **Degradado vivo**: cuatro campos de luz que derivan despacio (26 a 38 segundos), con grano fino.
  - **Luz con el scroll**: los mismos campos, movidos por el avance de la sección (regla 2); quietos cuando la página está quieta.
  - **Degradado y casillas**: el degradado con la retícula tenue de la tabla y algunas casillas que se encienden.
  - **Piso del hero**: un cuadro del propio hero como imagen.
  - **Actual**, para comparar.
- El usuario generó con Nano Banana dos ilustraciones de piso con nubes; prefiere sin nubes. Se le dieron tres prompts sin nubes.

## Ya en el sitio: Perfil y el encuadre (13 de noviembre de 2026)

- **El encuadre** (`encuadre.astro`), con la luz que sigue el scroll, va detrás del escenario de Servicios, de la panadería de Rediseño y del teléfono de Marcas. Lo que va dentro queda centrado, con el mismo margen por los cuatro lados.
- **Servicios** ya no tiene tablero blanco: las tarjetas de cada escena flotan sobre el encuadre. `escenas.astro` dibuja en modo noche: sombras más hondas, las hojas de la guía de Marca desde el principio, y Sitios web y Tiendas mueven su composición para que cada paso quede en el centro. Las imágenes quietas de movimiento reducido no cambian.
- **Marcas** es la variante Perfil, con las capturas reales en `public/assets/ig/` (en español y en inglés, para que la interfaz de Instagram siga el idioma del sitio), sacadas con `herramientas/perfiles.py`. El sitio mira al armarse qué capturas hay.
- **Weed Honey**: Instagram lo marca como "Perfil restringido" (para adultos) y solo se ve con sesión; su TikTok pide resolver un captcha. Su perfil sale de una captura que el usuario tomó desde la app del celular (la original en `src/assets/ig/weedhoney.co-original.webp`; `weedhoney.co.png` es la misma sin la barra de estado ni la de navegación, procesada con `python herramientas/perfiles.py weedhoney.co`). Está en la app en inglés, así que su teléfono dice "followers" también con el sitio en español. Cada captura cubre la pantalla del teléfono desde arriba.

- **Ajuste del 13 de noviembre de 2026** (pedido por el usuario): el encuadre de Marcas abraza al teléfono (su alto es el que queda libre, el teléfono ocupa el 86 % y el marco va en el medio de su columna), el teléfono es más grande y lleva la isla de la cámara y un brillo en el vidrio, y la lista se ajusta al alto de la pantalla para caber en laptops bajas. Las marcas ya no abren el detalle: tocar una lleva el teléfono a su perfil. El detalle (`visor.astro`) quedó solo para proyectos.

## Proceso (decidido el 13 de noviembre de 2026: Ruta V2)

Ronda de prototipos del 13 de noviembre de 2026: https://claude.ai/artifact/VWFwZ1eVK5oCUTa2n1qBD1 (fuente en la carpeta `proceso/` del scratchpad de esa sesión; `armar.py` monta cada variante en lugar de Proceso sobre el sitio armado). Nada de esto está en `src/` hasta que el usuario elija. Hoy Proceso son cuatro casillas iguales que se llenan de azul una tras otra. Las cuatro van fijadas al scroll, sobre el papel claro, y usan solo los cuatro pasos de `contenido.md` (sin plazos ni cifras):

- **Taller**: el mismo sitio de "Tu marca" pasa por los cuatro pasos dentro de un encuadre con la luz del hero: notas de la conversación (tu negocio, tus clientes, qué debe lograr la web), boceto con su estilo, el sitio construido con su versión de celular y publicado, con "Seguimos contigo". A la izquierda del encuadre, el paso y su texto; arriba, los cuatro elementos.
- **Ruta**: una línea que se dibuja con el scroll lleva el elemento de "Tu marca" por cuatro estaciones, como un mapa de metro; al llegar, la estación se enciende y cuenta su paso. En celular la línea baja en zigzag.
- **Transmutación**: una sola casilla grande cambia de estado; su número sube de 01 a 04, el símbolo rueda de Cn a La y se va encendiendo hasta quedar como las del hero. Al lado, la serie Cn → Di → Cs → La y el texto del paso.
- **Capas**: cuatro losas con forma de elemento caen una sobre otra en perspectiva y arman la torre del proyecto; la de arriba se enciende. Al lado, la lista de pasos con el actual abierto.
- **Actual**, para comparar.

Segunda ronda (13 de noviembre de 2026): https://claude.ai/artifact/MELM6veWnxYiiTAdxFFdAq (fuente en la carpeta `proceso2/` del scratchpad). Al usuario le gustaron **Ruta** y **Capas**; pidió una V2 mucho mejor de cada una y tres ideas nuevas:

- **Ruta V2**: el mapa sobre una retícula tenue de casillas; la línea más gruesa, con un degradado azul; las estaciones empiezan como casillas vacías marcadas y se llenan encendidas cuando "Tu marca" entra en ellas; el texto de cada paso aparece en una tarjeta blanca. En celular la ruta baja por la izquierda y las tarjetas van a la derecha, sin cruces.
- **Capas V2**: losas mejor terminadas que caen con un pequeño asentamiento; al lado de la torre, el nombre de cada losa derecho, en columna, unido a ella con una línea en codo; a la izquierda, el paso actual en grande.
- **Escalera** (nueva): las cuatro losas son una escalera que sube y "Tu marca" salta de un escalón al siguiente; cada escalón se enciende al pisarlo y lleva su nombre encima.
- **Tablero** (nueva): el piso de la tabla del hero en perspectiva; la ruta se enciende casilla por casilla y las cuatro estaciones se levantan del piso al llegar.
- **Ensamble** (nueva): vista explotada de plano técnico; las cuatro capas empiezan separadas con sus nombres y el scroll las junta en un solo bloque, encendiendo la del paso actual.

- **Ya en el sitio** (13 de noviembre de 2026): el usuario eligió **Ruta V2** y pidió que los elementos fueran completamente invisibles hasta que el cursor (el elemento de "Tu marca" que recorre la línea) llegara a ellos. Quedó así: al principio solo se ven la línea punteada, tenue, y el cursor; al llegar a una estación, su elemento aparece con un pequeño rebote y una onda que se abre una vez, y su tarjeta entra un instante después. Las cuatro estaciones son una lista ordenada, así que un lector de pantalla las lee completas aunque todavía no se vean. Con movimiento reducido la ruta está dibujada y las cuatro estaciones, quietas. Detalle técnico: al armar, el optimizador de CSS descarta `translate` cuando la misma regla tiene `transform`; las tarjetas se posicionan solo con `transform`.

## Redes (decidido el 13 de noviembre de 2026: Historias)

Ronda de prototipos del 13 de noviembre de 2026: https://claude.ai/artifact/TTUrT3PACuFALxX59KLYuA (fuente en la carpeta `redes/` del scratchpad de esa sesión; `armar.py` monta cada variante en lugar de Redes sobre el sitio armado, `verificar.py` la recorre a 1440, 390 y quieta). Nada de esto está en `src/` hasta que el usuario elija. Hoy Redes es una molécula: seis elementos que se enlazan al del centro y la descripción del que está activo. Las cuatro van fijadas al scroll, sobre la noche, cuentan las seis partes de `contenido.md` con su "Nuestro plus" y tienen el índice de los seis (botones de 44 px que llevan a cada parte):

- **Mes**: un mes de tus redes como tabla periódica, dentro del encuadre. Cada día es un elemento (el número es el día) y las seis partes actúan sobre el mismo mes: se marcan los días con su formato (Rl, Ft, Pz), se llenan de fotos, los reels y piezas se mueven, aparecen piezas hechas con IA junto a las originales, llegan respuestas y los días se publican en orden.
- **Historias**: las seis partes como seis historias en el cubo que el scroll gira, como pasan las historias de una a otra. Las barras de arriba se llenan con el scroll; cada historia tiene un dibujo propio (el calendario, el visor de la cámara, un elemento en movimiento sobre su línea de tiempo, variantes que se abren, la conversación, el perfil). Tocar a la derecha pasa a la siguiente, a la izquierda a la anterior.
- **Pieza**: una publicación de "Tu marca", la panadería de Rediseño (su ilustración y sus textos), pasa por las seis manos: el post vacío con su retícula y su día (jueves, 7:00), la foto que se revela, sus capas que se separan en 3D mientras corre una línea de tiempo, tres variantes que se abren detrás, la conversación al lado y, al final, el post entra en su lugar del perfil, "Publicado".
- **Espectro**: el elemento de "Tu marca" entra en Rs como una sola luz y sale en seis, del hielo al cobalto; cada una cae en su parte, que se enciende de su color. Los caminos están desde el principio, punteados y tenues.
- **Actual**, para comparar.

Mes e Historias usan publicaciones reales de las seis cuentas de Marcas, recortadas de sus capturas de perfil (`public/assets/ig/`) y pasadas a duotono cobalto para que quepan en el blanco, negro y azul. Mes y Pieza cuentan algo parecido a lo que ya muestra la animación de Redes en Servicios (el mes se llena, se publica, alguien comenta); Historias y Espectro no lo repiten. Textos nuevos para revisar: la frase bajo el título de cada variante, los formatos (Reel, Foto, Pieza), los días de la semana y "Publicado". Ninguna lleva el resplandor bajo el elemento del centro que hoy marca el detector (`dark-glow`).

- **Ya en el sitio** (13 de noviembre de 2026): el usuario eligió **Historias** y pidió ver qué mejoras ameritaba. Quedó con:
  - cada historia empieza su dibujo cuando llega al frente (la que espera en el costado del cubo está como antes de empezar), y la primera solo cuando la sección se ve; al volver hacia atrás, la que se va queda terminada;
  - Motion graphics va con el scroll: el elemento recorre su arco y el cabezal su línea de tiempo mientras se baja, sin nada que se repita solo (el detector marcaba el vaivén como marquesina);
  - en Community management, cada mensaje recibe su respuesta (antes había unos puntos de "escribiendo" que latían sin parar);
  - flechas a los lados de la historia en computador; en el celular se toca la historia (derecha, siguiente; izquierda, anterior);
  - "Nuestro plus" también en la lista, la luz de cada historia en otro lugar y los días del calendario con su formato (Rl, Ft, Pz);
  - las publicaciones en cobalto salen de `herramientas/publicaciones.py`, que las recorta de las capturas de Marcas; si se rehacen las capturas, se corre otra vez.
  Con movimiento reducido se ven las seis historias terminadas, una al lado de otra, y a la izquierda las seis partes con su texto. La frase bajo el título quedó "Lo que hacemos en tus redes, en seis historias."

## Nosotros (quitada el 13 de noviembre de 2026)

Después de ver esta ronda, el usuario decidió quitar la sección: Redes pasa directo al Cierre y el menú tiene siete casillas. El equipo sigue en el pie (símbolo, número y nombre de cada uno). La parte se guardó en `archivo/secciones-quitadas/nosotros.astro` por si vuelve; sus textos están en `docs/contenido.md`.


Ronda de prototipos del 13 de noviembre de 2026: https://claude.ai/artifact/TJ8VC6p5e3WzAdxhiXgGj7 (fuente en la carpeta `nosotros/` del scratchpad de esa sesión; `armar.py` monta cada variante en lugar de Nosotros sobre el sitio armado, `verificar.py` la recorre a 1440, 390 y quieta). Nada de esto está en `src/` hasta que el usuario elija. Hoy Nosotros es una cámara que recorre la tabla y se detiene en Ca, Se y Cv con una tarjeta al lado. Las cuatro usan solo `TEAM` y los textos de siempre ("Dos amigos desde la guardería, un mismo equipo."), no repiten el nombre Ca + Se = CaSe (eso lo cuentan Cierre y la Frase final) y siguen con monogramas mientras no haya fotos:

- **Mosaico**: la tabla periódica se vuelve una pantalla de puntos; sus casillas, con los huecos llenos, escriben Ca, luego Se, luego Cv, en una ola que cruza la tabla. Al final vuelve a ser la tabla, con Ca y Se encendidos y Cv en uno de sus huecos vacíos. Al lado, la persona de turno; al principio y al final, los tres.
- **Tríptico**: los tres lado a lado en paneles altos con la luz del hero. El scroll abre uno a la vez (su símbolo crece, entran su rol y su texto) y los otros se angostan a su nombre en vertical; al principio y al final quedan iguales. Donde está el símbolo puede ir el retrato cuando haya fotos.
- **Bloques**: la guardería como bloques de juguete. Ca y Se empiezan pequeños, uno al lado del otro, y crecen; cada uno se enciende cuando se cuenta; después Cv cae encima y los tres quedan como un solo equipo. Bloques en 3D, con el elemento en la cara del frente y su número al costado.
- **Retratos**: uno a la vez, en un marco de retrato con la luz del hero. El símbolo, enorme, rueda de Ca a Se y a Cv con su número; al lado el nombre sube desde su línea. Cuando haya fotos, la foto va en el marco.
- **Actual**, para comparar.

## Cierre (decidido el 14 de noviembre de 2026: Regreso)

Ronda de prototipos del 14 de noviembre de 2026: https://claude.ai/artifact/Eh3QsTfQPmjJgyPpwK3FaB (fuente en la carpeta `cierre/` del scratchpad de esa sesión; `armar.py` monta cada variante en lugar del Cierre sobre el sitio armado, `verificar.py` la recorre a 1440, 390 y quieta y prueba a escribir un nombre en Tu elemento). Nada de esto está en `src/` hasta que el usuario elija. Hoy el Cierre es el logo (Ca y Se) con un hueco punteado donde cae la casilla "Tú", y después "El elemento que falta es tu marca." con "Empezar mi proyecto", sobre azul. Las cuatro siguen sobre ese azul (llevan la clase `.zb`, así que el mosaico de color las une con Redes y con Contacto), con el mismo titular y el mismo botón; el elemento del visitante sigue siendo "Tú" (en Proceso y Redes es "Tm", que además es el símbolo real del tulio, por eso aquí no se usa):

- **119**: la tabla periódica real, completa, se enciende elemento por elemento del 1 al 118 (un contador arriba dice el número y el símbolo). Después se abre el período 8 debajo del 7 y la cámara entra a su primer puesto, el elemento 119, que todavía nadie ha creado: ahí queda "Tú, Tu marca", y llegan el titular y el botón. Usa un dato real (la tabla llega hasta el 118) que no está en `contenido.md`.
- **Reunión**: vuelven todos los elementos que la página mostró (servicios, proyectos, marcas, pasos del proceso y partes de redes), desordenados, y arman una tabla, una familia por fila con su nombre al final. Ca y Se empiezan juntos, como el logo, y se separan para dejar el puesto del medio de la primera fila, donde cae "Tú".
- **Tu elemento**: Ca y Se con tu casilla en el medio; el scroll los junta y enciende la tuya. Debajo del titular hay un campo, "El nombre de tu marca" (texto nuevo): al escribirlo, la casilla toma su símbolo como las marcas de la página ("Panadería La Espiga" da "Pa") y su nombre. El nombre todavía no pasa al formulario de Contacto.
- **Escala**: el logo, pequeño, en el centro, con tu casilla entre Ca y Se. El scroll hace crecer la tuya hasta ocupar toda la pantalla, con la luz del hero adentro; Ca y Se salen por los lados y queda un póster con el "Tú" gigante, el titular y el botón.
- **Actual**, para comparar.

Segunda ronda (14 de noviembre de 2026): https://claude.ai/artifact/HHTEZQuBR1NCnjdpoiUs1v (fuente en la carpeta `cierre2/` del scratchpad). El usuario pidió juntar el cierre actual con 119: primero se arma el logo como hoy (Ca y Se entran por los lados y Tú cae en el puesto del medio) y después los tres regresan a la tabla periódica, cada uno a su lugar real: Ca al 20, Se al 34 y Tú al 119, en el período 8 que se abre. Es el camino de vuelta del hero, donde la tabla termina en el logo. Tú lleva el 01 mientras es parte del logo y pasa a 119 al llegar. Tres coreografías, más 119 y la actual para comparar:

- **Regreso**: con el logo armado en el centro, la tabla aparece alrededor, desde el medio hacia afuera, y los tres vuelan a su lugar; cada aterrizaje enciende un anillo de casillas alrededor, como el golpe de Ca y Se en el hero, y la tabla se enciende desde el Tú. Al lado del 119 aparece "119 · Tu marca". Al final se ve la tabla entera, con los tres marcados, y debajo el titular y el botón.
- **Cuenta**: el logo se arma y se achica en el centro mientras detrás la tabla se enciende del 1 al 118, con el contador arriba. Cuando la cuenta pasa por el 20, Ca vuela a su lugar; al pasar por el 34, Se. Tú se queda solo donde estaba el logo hasta el 118; entonces se abre el período 8, Tú entra al 119 y la cámara se acerca, mientras el resto de la tabla se apaga un poco y llegan el titular y el botón.
- **Piso**: el hero al revés. El logo se arma de pie; la tabla se tiende debajo como un piso en perspectiva y los tres caen acostados en sus casillas, cada uno con su anillo de luz; junto al 119 se levanta "119 · Tu marca", la cámara sube un poco y el titular y el botón llegan arriba del piso.

- **Ya en el sitio** (14 de noviembre de 2026): el usuario eligió **Regreso** y pidió pulir lo que hiciera falta antes de llevarlo. Quedó así:
  - Ca y Se son la marca misma (el SVG del logo, con las letras caladas), no casillas dibujadas, y se ven desde el primer momento, con el puesto vacío entre ellos: al llegar a la sección ya se entiende que falta algo;
  - mientras baja al período 8, el Tú cuenta su número del 01 al 119;
  - mientras vuelan, las tres piezas se separan del azul con una sombra suave que desaparece al aterrizar;
  - cada aterrizaje enciende un anillo de casillas alrededor, la tabla se enciende desde el Tú y junto a él aparece "119 · Tu marca" (texto nuevo, con su par en inglés);
  - la tabla toma la altura que deja el titular, sin números en las casillas (a ese tamaño no se leen); en el celular la tabla y el titular quedan juntos en el centro, y Ca y Se entran desde menos lejos;
  - la sección mide 260vh (340vh hasta el 16 de noviembre de 2026) y termina con una pausa para leer. Su botón salió ese día: antes
    del formulario va uno solo, el de la frase final. Con movimiento reducido es una pantalla quieta con todo en su lugar.
  Se quitaron de `color.astro` las reglas del cierre anterior (`.zb-slot`, `.zb-you`), que habrían pisado a las nuevas. Los prototipos de las dos rondas siguen en sus artefactos.

### Ronda de prototipos del 19 de noviembre de 2026: el 119 en grande

**Elegida el 21 de noviembre de 2026: A · Acercamiento.** Ya está en `cierre.astro`. Al llevarla al sitio cambió en tres cosas frente al prototipo:
- **Las casillas grandes se desvanecen hacia arriba y hacia abajo** a medida que la cámara entra (`.zb-view`, `--mk`). En el prototipo el borde de la sección las cortaba, y eso choca con la regla 6 cuando llega Contacto.
- **Hay una sola luz.** La que estaba en el centro de la tabla viaja con la cámara hasta el Tú (`--gx`, `--gy`, `--ga`); el prototipo sumaba un segundo halo detrás del Tú. El botón la hace más fuerte (`--hot`) y enciende un anillo de hielo alrededor de la casilla.
- **La etiqueta "119 Tu marca" junto a la casilla se quitó**, porque el Tú grande ya lo dice.

El Cierre mide ahora 300vh (antes 260vh). Con movimiento reducido es su último cuadro: la cámara ya en el período nuevo.

Prototipo: https://claude.ai/artifact/TNs29Hgb4MynvEJMKoGNfQ. Las fuentes están en la carpeta `cierre/` del scratchpad de esa sesión:
- `variantes.js` y `variantes.css`: las variantes;
- `armar.py`: las monta sobre `dist/` y saca la página del artefacto;
- `verificar.py`: recorre cada variante a 1440, 390 y 1880, quieta y en inglés.

Nada de esto está en `src/` hasta que el usuario elija. Es el sitio completo con un selector abajo a la derecha (en el celular, una píldora con las letras) y abre en el comienzo del Cierre. El enlace elige la variante: `#cierre-a`, `#cierre-b`, `#cierre-c` o `#cierre-actual`.

Hoy el Tú termina como la casilla más pequeña de la pantalla. Las tres repiten el Cierre de hoy hasta que el Tú cae en el 119 y la tabla se enciende desde él. Después cada una tiene su final, y "El elemento que falta es tu marca." con "Empezar mi proyecto" llega al lado del Tú (debajo en el celular, y en C encima):
- **A · Acercamiento**: la cámara entra al período 8. El Tú queda del tamaño de las casillas vecinas, que quedan de fondo, apagadas y enormes (Fr, Ra, Ac arriba, los lantánidos abajo). La frase ocupa el período nuevo, a su derecha, que estaba vacío.
- **B · Ficha**: la tabla sube y se aleja. El Tú sale de su casilla hacia el visitante y crece hasta ser la ficha grande, y su lugar en la tabla queda vacío, punteado y con luz.
- **C · Piso**: la tabla se acuesta como el piso del hero, girando sobre el 119. El Tú se levanta sobre su casilla, con un charco de luz a sus pies, y Ca y Se quedan en el piso, en blanco. Las filas lejanas se apagan. El sitio termina como empezó.
- **Actual**, para comparar.

En las tres:
- el Tú lleva el 119 desde que aparece;
- el botón enciende la casilla (un anillo de hielo y más luz detrás);
- con movimiento reducido cada una es su último cuadro, quieto;
- el Cierre pasa de 260vh a 300vh para que el final tenga su tramo.

## Contacto (decidido el 14 de noviembre de 2026: Una línea)

Ronda de prototipos del 14 de noviembre de 2026: https://claude.ai/artifact/9dwtZyJu2f9MkoU5K9APw9 (fuente en la carpeta `contacto/` del scratchpad de esa sesión; `armar.py` cambia la función que arma el formulario, `FORMS.tabla`, por la de la variante elegida, y `verificar.py` marca tres opciones y un plazo, escribe nombre y contacto y envía, a 1440, 390 y quieta). Entonces Contacto era el titular a la izquierda con una fórmula que se arma (? + ? → Tm) y, a la derecha, las doce opciones como elementos, el plazo, el nombre y el contacto. Contacto no se queda fija ni va atada al scroll (es un formulario). Las cuatro conservan los mismos campos (las opciones con su símbolo, el plazo, el nombre y el contacto), así que la Fórmula de Servicios sigue marcando aquí lo que el visitante une, y dicen lo mismo al faltar algo y al enviar:

- **Carta**: el pedido como una oración que se escribe sola: "Hola, soy … Necesito … Lo quiero … Escríbanme a …". El nombre y el contacto se escriben en la oración; las opciones de abajo la llenan con sus propias frases ("un sitio corporativo", "manejo de redes"), cada una con su símbolo. Textos nuevos: las cuatro partes de la oración y "elige lo que necesitas", "elige cuándo", "tu nombre", "tu correo o WhatsApp".
- **Pasos**: una pregunta a la vez (01 qué necesitas, 02 para cuándo, 03 a quién le respondemos), con los tres pasos a un lado y, debajo de cada uno, lo que ya se respondió; cualquiera lleva de vuelta a su paso. Textos nuevos: "Seguir al paso 2", "Seguir al paso 3" y "Volver".
- **Ficha 119**: después del Cierre, el elemento 119 tiene su ficha. "Tú, Tu marca" llena sus datos mientras se llena el formulario (Necesita, Para, De, Responder a: textos nuevos) y se enciende cuando está completa; en computador la ficha acompaña al formulario mientras se baja.
- **Reacción**: la fórmula de hoy, grande y en el centro: cada elemento que se toca vuela desde su lugar hasta ella, y el resultado, Tú (119), brilla un poco más con cada uno.
- **Actual**, para comparar.

En esta ronda se encontró que el selector de las páginas de prueba volvía a armar la página en el mismo cuadro del primer armado, y eso arrancaba dos veces las secciones (en las rondas anteriores pudo duplicar animaciones en los artefactos; el sitio no lo hace). Quedó corregido en el `armar.py` de esta ronda.

Segunda ronda (14 de noviembre de 2026): https://claude.ai/artifact/KzoynZgGRXtdkD9wUXMqkc (fuente en la carpeta `contacto2/` del scratchpad). El usuario pidió algo más normal: mucho más minimalista y sencillo, sin tantas opciones, pero que se vea muy bien. Las cuatro usan el mismo formulario corto: los cuatro servicios como elementos para marcar (Sw Sitios web, Ti Tiendas en línea, Rs Redes sociales, Ma Marca), nombre, correo o WhatsApp, en dos de ellas un mensaje opcional, y "Enviar solicitud". Sin plazo y sin las doce opciones. Tienda, redes y marca llevan el símbolo que busca la Fórmula de Servicios, así que lo que el visitante une allá se sigue marcando aquí; para sitios web habría que sumarlo a la Fórmula al llevarlo. Texto nuevo: "Mensaje (opcional)".

- **Columna**: todo centrado en una columna angosta, con aire; el botón a todo el ancho.
- **Mitades**: el titular grande a la izquierda (con el correo de muestra abajo) y el formulario a la derecha, como el contacto de un estudio.
- **Una línea**: lo más corto: los cuatro servicios y una sola barra con nombre, contacto y el botón; sin mensaje.
- **Encuadre**: el formulario en una tarjeta que flota sobre la luz del hero (`encuadre.astro`), como las piezas de Servicios y de Marcas.
- **Actual**, para comparar.

Detalle técnico: la clase `.mn` ya es del menú fijo (se esconde hasta que aparece); un formulario con esa clase quedaba invisible. Las variantes usan el prefijo `ck-`.

- **Ya en el sitio** (14 de noviembre de 2026): el usuario eligió **Una línea**, pidió quitar la línea "También puedes escribirnos a hola@casestudio.example" y pulir lo que hiciera falta antes de llevarlo. Quedó así:
  - Contacto ocupa una pantalla entera, con el formulario en el centro: cada "Empezar mi proyecto" llega a verlo completo;
  - los cuatro servicios son elementos para marcar (Sw, Ti, Rs, Ma, con su número); el marcado se pone azul, con su símbolo en una casilla blanca;
  - una sola barra con Nombre, Correo o WhatsApp y "Enviar solicitud"; en el celular la barra se apila, cada campo muestra su propio borde (como los servicios, para que se vea dónde escribir) y el botón va a todo el ancho;
  - mientras Contacto está en pantalla, el botón "Empezar mi proyecto" del menú se aparta: llevaría a donde el visitante ya está, y así "Enviar solicitud" es la única acción;
  - el titular, la bajada y la respuesta reparten sus líneas para no dejar una palabra sola (en inglés quedaba "steps." sola);
  - si falta algo, se marca donde está (los servicios con un anillo, el campo con su borde) y abajo se dice lo primero que falta; los campos quedan atados a ese aviso para los lectores de pantalla;
  - los avisos y la respuesta van en el azul claro de la paleta, no en verde; al enviar, una casilla azul con un visto acompaña "Listo, … Pediste: …";
  - el autocompletado del navegador respeta los colores de la barra, y el campo del contacto no corrige ni pone mayúsculas (en el celular su tecla dice enviar);
  - la Fórmula de Servicios marca aquí los cuatro servicios con sus mismos símbolos, Sitios web incluido; solo desmarca lo que ella marcó, y al cambiar la fórmula toca solo lo que cambió (antes volvía a marcar un servicio que el visitante había desmarcado a mano);
  - se fueron el plazo, las doce opciones, la línea del correo y sus textos en `en.json`. El correo de muestra queda solo en el pie.
  Contacto no se queda fija ni va atada al scroll (es un formulario). Los prototipos de las dos rondas siguen en sus artefactos.

## Frase final (decidido el 15 de noviembre de 2026: Crece; quitada el 17 de noviembre de 2026)

**Quitada el 17 de noviembre de 2026**, a pedido del usuario: el Cierre ("El elemento que falta es tu marca.") ya era un buen llamado. La parte está en `archivo/secciones-quitadas/frase-final.astro`. Lo de abajo queda como registro.

Ronda de prototipos del 14 de noviembre de 2026: https://claude.ai/artifact/DEij9LwtHT1RMqWFzQgP4E (fuente en la carpeta `frase/` del scratchpad de esa sesión; `armar.py` monta cada variante en lugar de la frase final sobre el sitio armado y `verificar.py` la recorre en seis momentos del scroll a 1440 y 390, quieta y en inglés). Nada de esto está en `src/` hasta que el usuario elija. Hoy la frase final abre con una pantalla vacía (el primer 15 % del scroll no muestra nada), termina con la frase apagada a gris y la ecuación "Ca milo + Se bastián" compite con ella. Las cuatro son un momento atado al scroll que ya se lee al llegar, y con movimiento reducido muestran su último estado, quieto y completo:

- **Sujetos**: los dos sujetos de la frase se vuelven los dos elementos: "Uno" se convierte en Ca y "el otro" en Se, cada uno con su nombre debajo, y queda "Ca lo diseña, Se lo hace vender." ("se lo hace vender" sigue siendo español). Las dos líneas empiezan en el mismo borde, así que Ca y Se quedan uno encima del otro, como una columna de la tabla. En inglés: "Ca designs it, Se makes it sell."
- **Por dentro**: el logo, en el centro, se abre en las dos personas que lo forman: cada casilla crece hasta ser una casilla de elemento grande con su número, su nombre (Camilo Corrales, Sebastián Vanegas) y su mitad de la frase.
- **Firma**: la página se despide como una carta: la frase, los dos que la firman, cada uno con su elemento, y el logo completo de lado a lado, que sube desde abajo con el scroll.
- **Notas**: el marcador azul de Servicios pasa por cada mitad de la frase y cada una recibe su nota, un elemento, explicada abajo como nota al pie: "Calcio. Camilo Corrales, diseño y desarrollo." y "Selenio. Sebastián Vanegas, ventas y relaciones comerciales." (los datos salen de `contenido.md`).
- **Actual**, para comparar.

Los textos nuevos de cada variante tienen su inglés escrito en el prototipo; pasarían a `en.json` al llevar la elegida. Con movimiento reducido el escenario de la frase deja de quedarse fijo y toma el alto de lo que tiene: Por dentro y Firma, que reparten sus piezas por toda la pantalla, conservan una pantalla propia.

Segunda ronda (14 de noviembre de 2026): https://claude.ai/artifact/H4nDHbTq7chBfPHBLbsZXb (fuente en la carpeta `frase2/` del scratchpad). El usuario pidió que la frase sea un llamado a la acción bacano e inspirador, sin nuestros nombres y con CaSe; le gustaron Sujetos y Notas y pidió adaptarlas, más ideas nuevas. La frase de las cuatro es "Crece con CaSe.", escrita toda con elementos reales: C·Re·Ce (carbono 6, renio 75, cerio 58), C·O·N (carbono 6, oxígeno 8, nitrógeno 7) y Ca·Se (calcio 20, selenio 34). En inglés, "Soar with CaSe." (S·O·Ar · W·I·Th · Ca·Se), que también se escribe con elementos. Las cuatro terminan en "Empezar mi proyecto", que lleva a Contacto, y Ca y Se van con los colores del logo:

- **Escrita** (Sujetos adaptada): la frase llega escrita y cada palabra se vuelve los elementos que la forman, una tras otra, cada uno con su nombre debajo. En el celular, una palabra por línea.
- **Notas** (adaptada): el marcador azul pasa por cada palabra y cada una recibe su nota; abajo, como notas al pie, los elementos con que está escrita ("Carbono, renio y cerio.", "Carbono, oxígeno y nitrógeno.", "Calcio y selenio, el nombre del estudio.").
- **Crece**: la frase, ya en elementos, llega pequeña y crece con el scroll: cada elemento más grande que el anterior, una escalera que termina en CaSe. En el celular, una palabra por línea y cada línea más grande.
- **Desfile**: los elementos pasan enormes, cada uno con su número y su nombre, y al final la vista se aleja y queda la frase entera con el botón.

- **Ya en el sitio** (15 de noviembre de 2026): el usuario eligió **Crece**, pidió quitar los nombres de los elementos y pulir lo que hiciera falta. Quedó así:
  - cada elemento lleva solo su número y su símbolo;
  - la escalera es más empinada (cada escalón casi un cuarto más grande) y los espacios crecen con ella;
  - el último escalón es el logo: Ca y Se del mismo tamaño, lado a lado, y llegan juntos;
  - la fila guarda desde el comienzo el alto de su último escalón, así que los elementos crecen hacia arriba desde una línea quieta y el botón no se mueve;
  - mientras la frase está en pantalla, el "Empezar mi proyecto" del menú se aparta (como en Contacto) y el de la frase es la única acción;
  - en el celular y en tabletas angostas (menos de 800 px de contenido), una palabra por línea y cada línea más grande.
  Los elementos salen de `OU_SAY` (español e inglés), que elige idioma con `LANG.cur`; la frase completa para lectores de pantalla tiene su par en `en.json`.

Otras frases que también se escriben solo con elementos, por si se quiere cambiar: "Cosas bacanas nacen con CaSe." (Co·S·As Ba·Ca·Na·S Na·Ce·N C·O·N Ca·Se) y "Escala con CaSe." (Es·Ca·La C·O·N Ca·Se). Al llevarla, el "Empezar mi proyecto" del menú se aparta en la frase final, como en Contacto, para que no se repita.

## Pie (decidido el 15 de noviembre de 2026: Frente)

Ronda de prototipos del 15 de noviembre de 2026: https://claude.ai/artifact/UevwmwuhSMiRDCmrFYRsqr (fuente en la carpeta `pie/` del scratchpad de esa sesión; `armar.py` cambia `FOOT.tabla` y `FOOT_INIT.tabla` por los de la variante elegida, y `verificar.py` captura el pie entrando, casi al final y entero, a 1440, 1024 y 390, quieto y en inglés). Nada de esto está en `src/` hasta que el usuario elija. El usuario pidió hacerlo "más increíble". Las cuatro llevan el mismo contenido (el logo, el correo de muestra, el lugar, "Disponibles para nuevos proyectos", las secciones, los cuatro servicios, el equipo y volver arriba) y arrancan en el mismo oscuro de la frase final, así que no aparece ninguna raya entre las dos. De paso corrigen tres cosas del pie actual: el punto verde de "Disponibles" (fuera de la paleta) pasa a un cuadrito azul; "Servicios" lista los cuatro servicios en vez de cinco renglones; la flecha de volver arriba es un dibujo y no el carácter ↑.

- **Tabla**: el pie es la tabla periódica, períodos 1 a 5, con los símbolos reales como textura. El estudio ocupa casillas: Ca y Se en su lugar real, Catalina (Cv, 03) en el del litio, los cuatro servicios después del calcio (Ti, Tiendas, en el del titanio), Contacto en el del cobalto (Co), las secciones en el período 5 y volver arriba en la esquina del helio. El logo y el contacto van en el hueco de la tabla, donde los afiches ponen el título. Las casillas entran por número atómico a medida que llega el pie; cada casilla del estudio se enciende al pasar el puntero. Entre 861 y 1200 px las casillas muestran solo el símbolo; en el celular quedan solo las del estudio, en cuatro columnas.
- **Firma**: columnas cortas y debajo el logo completo de lado a lado, que sube desde abajo cuando se acaba la página.
- **Piso**: vuelve el piso del hero, vivo: la tabla entera acostada, Ca y Se encendidos en su lugar, los destellos al azar del hero (uno a la vez, solo con el pie en pantalla) y las casillas que se encienden bajo el puntero. Al llegar, el piso se levanta.
- **Ficha**: el estudio como la ficha de un elemento: el logo con sus dos números (20 · 34) y al lado sus propiedades, como una hoja de datos (contacto, estado, servicios, equipo y secciones), que entran una tras otra con el scroll.
- **Actual**, para comparar.

Textos nuevos: "Estado" (Ficha); los demás ya tienen su par en `en.json`.

Segunda ronda (15 de noviembre de 2026): https://claude.ai/artifact/5Dr7Kj54RqJUNsg61gyHrC (fuente en la carpeta `pie2/` del scratchpad). El usuario pidió algo como Piso combinado con la primera versión de Ficha, muy creativo. Las cuatro juntan el piso vivo (la tabla acostada, con Ca y Se encendidos en su lugar real y los destellos del hero) con la ficha del estudio (20 · 34, el logo, "CaSe Studio") y su hoja de datos; cambian en cómo se relacionan los dos:

- **Levanta**: Ca y Se se despegan del piso (acostados, luego de pie) y vuelan a la ficha, donde quedan como su logo; en el piso quedan sus dos casillas vacías. Después aparecen la ficha y su hoja de datos.
- **Enlace**: cada dato de la ficha es una casilla real del piso, como en la Tabla de la primera ronda (Camilo en Ca, Sebastián en Se, Catalina en el litio, los servicios después del calcio con Ti en el titanio, las secciones en el período 5, Contacto en el cobalto, volver arriba en el helio). Al pasar el puntero o el foco por un dato, su casilla se enciende en la tabla; al llegar, cada fila marca sus casillas a medida que entra. Aquí no hay destellos al azar: las luces del piso significan algo.
- **Reverso**: la ficha tiene dos caras. Sobre el piso, el scroll la voltea del elemento (20 · 34, el logo, el nombre) a su hoja de datos, cuando la ficha ya está a la vista. Solo se puede tocar la cara que mira al visitante; con movimiento reducido se ven las dos caras, una encima de la otra.
- **Cámara**: la ficha está dibujada sobre el piso, en el hueco de la tabla. Al llegar, la cámara sube: el piso se levanta hasta que la ficha se lee de frente; debajo, la hoja de datos en dos columnas. Todo el pie cabe en una pantalla, para que al final de la página la ficha se vea entera. En el celular el piso queda pequeño y la ficha va plana, encima de los datos.

Tercera ronda (15 de noviembre de 2026): https://claude.ai/artifact/VshMjwnLdsJ2Wnx77mzCL7 (fuente en la carpeta `pie3/` del scratchpad). El usuario la describió así: el efecto de cámara, pero sobre la tabla, donde los elementos están en sus casillas y así sirve de menú de navegación; abajo, el logo de CaSe muy bonito; muy profesional y creativo. Las tres comparten la tabla: la tabla periódica real, períodos 1 a 5, con sus símbolos tenues como textura, el estudio en sus casillas como en la Tabla de la primera ronda (las secciones y los servicios son enlaces, el equipo se muestra, volver arriba va al helio) y tres familias de color con su leyenda, como una tabla de verdad: Secciones (azul oscuro con borde), Servicios (azul) y Equipo (blanco). En el hueco de la tabla, el contacto y la leyenda. Los destellos del hero caen en las casillas que son solo tabla. Al llegar, la cámara levanta la tabla hacia el visitante; debajo, el logo real, tan ancho como la tabla. El pie mide casi una pantalla (905 px a 1440). En el celular, la tabla es una cuadrícula plana de las casillas del estudio, en cuatro columnas, con el contacto y la leyenda arriba.

- **Frente**: la cámara levanta la tabla hasta dejarla casi de frente, como un menú; el logo sube desde abajo cuando se acaba la página.
- **Mosaico**: la tabla queda un poco más inclinada y el logo se arma debajo con casillas pequeñas, sin orden, como llegan los cambios de color de la página; cuando está completo, el dibujo pasa a ser el logo real.
- **Ola**: las casillas se ponen de pie una por una, por número atómico, y la tabla se vuelve el menú; después el logo: Ca y Se se ponen de pie de últimos y "Studio" entra a su lado. Usa el logo real partido en tres con `viewBox`.

Texto nuevo: "Secciones" (la leyenda); "Servicios" y "Equipo" ya tienen su par.

- **Ya en el sitio** (15 de noviembre de 2026): el usuario eligió **Frente**, pidió quitar los nombres de las personas y mejorarlo al llevarlo. Quedó así:
  - sin personas: Ca y Se quedan en su lugar como los elementos del nombre (Calcio, Selenio) y la casilla de Catalina se fue (el litio vuelve a ser solo tabla); la leyenda dice Secciones, Servicios y CaSe;
  - la cámara termina del todo de frente y suelta el 3D, así el texto del menú se lee nítido;
  - en el celular el menú sigue su orden (las secciones, los servicios y volver arriba al final); Ca y Se no van ahí, porque el nombre es el logo de abajo;
  - se quitaron del pie el punto verde, el carácter ↑ y la lista de cinco "servicios"; del diccionario salieron los textos del pie anterior que nada usa (Explorar, Equipo, los roles y los renglones viejos de servicios), y entraron "Calcio" y "Selenio".

## Revisión completa del sitio (15 de noviembre de 2026)

Una crítica de diseño de todo el sitio (Impeccable: 23 de 36, `.impeccable/critique/`) dejó dos problemas de prioridad 1:
- **el celular**: el menú sin nombres, casillas de menos de 40 px y ningún camino a Contacto a la vista;
- **el largo**: 37,5 pantallas, y Marcas y Redes son la misma escena.

El usuario eligió empezar por el celular y poner la frase final antes de Contacto. Ya en el sitio:
- **El final**: Cierre, frase final, Contacto y pie. El botón de la frase baja al formulario y el pie queda justo después de él.
- **Más cortas**: Redes pasó de 6 a 3,8 pantallas de scroll y Proceso de 4,2 a 3.
- **El menú en el celular**: cada casilla mide 40 px y dice su nombre a quien usa lector de pantalla. El idioma es una sola casilla, la del otro idioma.

### Ronda "Celular y Redes" (prototipos, 15 de noviembre de 2026)

Artefacto: https://claude.ai/artifact/PrBDpdcCoMrvFZb1YCD1Dv. Seis variantes, que esperan la elección del usuario:

1. **Botón fijo**: en el celular, "Empezar mi proyecto" queda fijo abajo y la fila de secciones sigue arriba.
2. **Hoja**: arriba a la derecha van "Empezar mi proyecto" y una casilla "Menú" con la sección en la que vas. La casilla abre una hoja con las siete secciones y su nombre, el idioma y el botón. Abajo no queda nada.
3. **Barra**: abajo, una barra con la sección en la que vas (abre la misma hoja) y el botón. Arriba no queda nada.
4. **Cierre de cerca**: en el celular, Ca, Se y Tú llegan a sus casillas más grandes (41 px en vez de 18), como bajo una lupa, y "119 · Tu marca" se lee.
5. **Redes al centro**: en el computador, el título arriba, la historia en el centro y las seis partes en fila debajo, como un período.
6. **Actual**: el sitio como está.

Con Botón fijo y Barra, Servicios, Marcas y Redes dejan libre la franja de abajo en el celular, para que el botón no tape su texto. En Redes al centro la historia queda más pequeña: 283 px de ancho a 1440, contra 370 hoy.

- **Ya en el sitio** (15 de noviembre de 2026): el usuario eligió **Hoja**. El Cierre y Redes quedan como estaban. Al llevarla:
  - la hoja se cierra con la cruz, tocando afuera, con Escape o arrastrándola hacia abajo; si el arrastre es corto, vuelve a su lugar;
  - al cerrarse, el foco vuelve a "Menú";
  - la casilla de arriba y la hoja marcan la sección en la que vas, como la fila del escritorio (las de antes en azul, la actual en blanco);
  - el botón de arriba se aparta en Contacto y en la frase final, como el del escritorio;
  - `bajo_menu.py` ahora también revisa la barra del celular.

### Recorridos de celular (15 de noviembre de 2026)

`herramientas/recorridos.py` recorre el sitio real de cada proyecto como un celular (390 × 844) y guarda su tira en `public/assets/tour-<id>-cel.webp`. Son pantallas repartidas por la página y otra vez la primera al final, como las de computador. Ya están Los Duches, NeuralNet, NeuralBI, AKUA y Mimarte. En NeuralNet y NeuralBI los puntos se escogieron a mano (`PUNTOS`), porque el reparto parejo caía a la mitad de una animación.

**Weed Honey** pide confirmar la edad con una fecha de nacimiento antes de entrar. No se llenó sin permiso, así que sigue solo con su tira de computador.

### Ronda "Recorridos y pie" (prototipos, 15 de noviembre de 2026)

Artefacto: https://claude.ai/artifact/Egsu8KA9wN6Rd4p66G3WRc. Todo es en el celular; el escritorio no cambia.

1. **Rueda en teléfono**: las pantallas de la rueda se paran como teléfonos (195 × 422 px la del frente, contra 296 × 153 hoy) y pasan el recorrido de celular. El detalle también lo muestra, a todo el ancho. Weed Honey, sin el suyo, queda con su pantalla de computador acostada en medio del teléfono.
2. **Solo el detalle**: la rueda queda como está; al abrir un proyecto, el recorrido es el de celular.
3. **Pie: mapa**: arriba, la tabla entera pequeña, como un mapa con las casillas del estudio encendidas en su lugar (se prenden una tras otra al llegar). Debajo, las secciones y los servicios con su nombre y su número de la tabla; tocar uno enciende su casilla en el mapa. Después, el contacto, "Volver arriba" y el logo.
4. **Pie: ordenado**: el pie de hoy sin el hueco de arriba. Primero el contacto, con el correo más grande. Luego las secciones (seis, en tres columnas) y los servicios (cuatro, en dos), cada grupo con su nombre y sus números desde 01. "Volver arriba" es un botón.
5. **Actual**: el sitio como está.

En el detalle, el recorrido solo se ve donde el sitio en vivo no carga: en los prototipos, en Weed Honey y mientras un sitio tarda. En el dominio publicado, el detalle abre el sitio real.

- **Ya en el sitio** (15 de noviembre de 2026): el usuario eligió **Rueda en teléfono** y **Pie: mapa**. Al llevarlos:
  - la rueda y el detalle cambian de tira si el ancho cruza el del celular (una tableta que gira, una ventana que se angosta), también con el detalle abierto;
  - Weed Honey, mientras no tenga su recorrido de celular, queda acostado en medio del teléfono sobre sus propios colores, desenfocados y oscuros, en vez de un hueco negro;
  - en el pie, el mapa enciende sus casillas la primera vez que se ve y se lee quieto con movimiento reducido. "Volver arriba" es un botón de 48 px, y el pie de escritorio (Frente) no cambia;
  - los datos de cada proyecto dicen si tiene recorrido de celular (`cel` en `PROJECTS`), y el inglés no los traduce.

### Ronda "Preguntas" (prototipos, 15 de noviembre de 2026)

El usuario pidió un FAQ que funcione como un chat: cada pregunta que se toca entra al chat y se responde ahí, en mensajes cortos. Artefacto: https://claude.ai/artifact/Gigm2uXc7pGeBYnLhtCrWq. Va entre Redes y el Cierre, en el encuadre, con CaSe Studio arriba ("Disponibles para nuevos proyectos").

1. **Chat**: las siete preguntas en una lista, cada una con su elemento (el de la parte del sitio que la responde: Sv, Fm, Pc, Rd, Rs, La, Py), y el chat al lado. Si se toca otra mientras responde, lo que faltaba llega de una vez y sigue la nueva.
2. **Elementos**: las preguntas son casillas de un período; la que se toca vuela al chat y se vuelve la pregunta.
3. **Al scroll**: la sección se queda fija y el scroll va haciendo las preguntas una tras otra; tocar una salta a su respuesta. Con movimiento reducido se lee la conversación entera.

En el celular las preguntas van dentro del chat, como respuestas rápidas. Las respuestas solo dicen lo que el sitio ya dice: los servicios, el proceso, el rediseño, las redes, que te enseñamos a usar el sitio, y los proyectos y las marcas. No hay preguntas sobre precios, tiempos, propiedad del sitio ni rondas de cambios hasta que el usuario dé esas respuestas.

- **Ya en el sitio** (15 de noviembre de 2026): el usuario eligió **Chat** y pidió mejorarlo antes de llevarlo. Quedó así:
  - cada mensaje tarda según su largo, como alguien que escribe, y mientras tanto el estado de arriba dice "Escribiendo…" (sin puntitos animados);
  - una pregunta ya hecha no se repite: el chat vuelve a su respuesta y la marca;
  - cuatro respuestas terminan en la parte del sitio que las muestra: "Armar mi fórmula", "Ver el proceso", "Ver el rediseño" y "Ver proyectos";
  - en el celular, después de cada pregunta las respuestas rápidas se corren a la primera que falta;
  - "Preguntas" (Pr, en inglés Qs) es la séptima casilla del menú y del pie (en el lugar 42 de la tabla), así que la sección se marca a sí misma. En la hoja del celular el idioma pasó arriba, junto a la cruz, y las ocho secciones quedan en dos filas;
  - en escritorio angosto (861 a 980 px) la fila del menú se alinea a la izquierda, para no tocar el botón;
  - todo en inglés: las preguntas, las respuestas y el saludo salen de `FAQ` y `FAQ_SAY`, que traduce `sources()`;
  - no se queda fija ni se ata al scroll, como Fórmula y Proyectos: el visitante la usa.

## Crítica del 16 de noviembre de 2026 y ronda "Acabado"

Crítica completa con los dos skills, sin cambiar secciones, para el acabado premium de Apple. Impeccable usó dos evaluaciones aisladas: revisión de diseño, y detector con evidencia del navegador.
- Resultado: 24/36, Aceptable, a un punto de Bueno. Archivada en `.impeccable/critique/`; la anterior fue 23/36.
- Taste: textos sin fallas; rendimiento rápido, con 6 fallas, todas de imágenes.

Problemas prioritarios:
- **[P1]** en escritorio, el botón del menú es blanco sobre papel claro: 1,07:1 en unas 9 pantallas;
- **[P1]** el ejemplo de la Fórmula no llega a Contacto, porque `commit()` se sale con el ejemplo puesto;
- **[P2]** números de casillas de 6 a 9,5 px, y símbolos blancos sobre casilla encendida a 3,3:1;
- **[P2]** el menú de escritorio habla en códigos;
- **[P2]** el sistema se desvió: seis cobaltos casi iguales, 10 radios, 19 duraciones y el foco en seis colores.

Otros hallazgos:
- el © queda pegado al logo, porque `.ft p{margin:0}` le gana a `.ft-legal`;
- Servicios llega con el escenario vacío;
- "x" pasa como contacto y se puede enviar dos veces;
- 12 imágenes sin carga diferida y ninguna con ancho y alto.

Artefacto: https://claude.ai/artifact/PD2HFiGJZUY26VXjYYzhKk. Siete vistas: Todo, cinco grupos y Actual.
1. **Menú y botones**:
   - sobre papel claro, el botón del menú pasa a tinta y el idioma conserva su borde;
   - junto a la fila, el nombre de la sección en la que vas (desde 1200 px);
   - el idioma contra el borde, sin hueco cuando el botón se aparta;
   - los botones principales a peso 600 y el fantasma más tenue;
   - los enlaces del hero en el centro real.
2. **Casillas y números**:
   - ningún número por debajo de 9,5 px, con cifras tabulares;
   - las casillas "hechas" del menú en un azul más hondo;
   - la luz de las casillas encendidas más alta y más suave, para que el símbolo blanco se lea;
   - las filas de Servicios que esperan atenúan su texto y no su elemento;
   - el © del pie con aire, y los nombres del pie en una línea de símbolos.
3. **Escenas**:
   - Servicios llega ya dibujado y sigue desde ahí;
   - el chat de Preguntas mide 600 px de alto;
   - cada encuadre con su luz desde otro lado (Rediseño, Marcas, Redes y Preguntas);
   - la frase del hero se parte bien y la indicación de la Fórmula va bajo su título.
4. **Celular**:
   - los botones del hero apilados al mismo ancho;
   - el detalle sin los números 1 a 4 encima del sitio, y su nota sobre fondo sólido;
   - las respuestas rápidas se desvanecen en el borde.
5. **Formulario**:
   - "Armar mi fórmula" con el ejemplo puesto lleva el ejemplo a Contacto;
   - un error se distingue del foco: anillo blanco y etiqueta marcada;
   - el contacto se revisa (un correo, o un número de 7 dígitos o más) con "Revisa el correo o el número para poder responderte.";
   - después de "Listo", no se puede enviar otra vez hasta cambiar algo.

Propuesto pero sin prototipo, porque no se ve en una captura:
- imágenes con carga diferida, ancho y alto, a 2x para pantallas retina, y tiras sin la barra fija de cada sitio;
- tokens de color, para dejar un solo cobalto y quitar `--calcio` y `--ok`;
- una sola física de movimiento, con duraciones y curvas como variables.

### Ya en el sitio: Acabado completo (16 de noviembre de 2026)

El usuario eligió "Todo": los cinco grupos están en `src`. Quedó así:
- **Menú** (`menu.astro`):
  - el botón en tinta sobre papel claro, con su hover;
  - el nombre de la sección en `.mn-now`, que toma el texto de su enlace, ya traducido;
  - el idioma con `order:2`.
  - Distinto del prototipo: el botón conserva su desvanecido al apartarse en Contacto. El `display:none` no hacía falta, porque el idioma ya queda contra el borde.
  - Las casillas "hechas" de la hoja del celular usan el mismo azul hondo que la fila.
- **Botones y barra del hero** (`Base.astro`):
  - peso 600 en los principales;
  - el fantasma al 88 %, blanco con el hover;
  - la barra en tres columnas desde 861 px, con el logo a la izquierda sin estirarse.
- **Números**:
  - cada parte con su tamaño: ninguno por debajo de 9,5 px, en cifras tabulares;
  - la luz nueva de las casillas encendidas en `.lit` (detalle y rueda), Redes, Preguntas y los puntos de la rueda;
  - Proceso conserva la suya, porque sus elementos son grandes.
- **Servicios**:
  - el primer servicio arranca en un quinto de su animación;
  - las filas que esperan atenúan su título. Con movimiento reducido, todas se leen en tinta.
- **Encuadre**: `Encuadre.put(el, lado)`. Servicios queda como se dibuja; Rediseño y Preguntas `'x'`; Marcas `'y'`; Redes `'xy'`.
- **Celular**: el detalle esconde los números en su propio corte, 900 px, y no en 860.
- **Contacto**:
  - `reachable()` pide un correo completo (algo@algo.algo) o 7 dígitos;
  - después de "Listo", el botón queda con `aria-disabled` hasta que algo cambie.
- **Pie**:
  - `.ft .ft-legal`: entre 28 y 44 px en escritorio y 28 px en el celular;
  - los nombres del pie en una línea de símbolos desde 1201 px.

Revisión:
- `npm run revisar`: cinco "bien".
- El detector: los mismos 10 de antes (7 falsos de relleno, 2 de la parodia de Rediseño, 1 del encuadre).
- copy-lint: 0 fallas.
- perf:
  - las 6 fallas de imágenes de siempre;
  - más tareas largas a 1440 por la carga del equipo. El sitio anterior, medido en el mismo momento, dio 105 contra 94 del nuevo.

### Ya en el sitio: imágenes, un solo cobalto y una sola física (16 de noviembre de 2026)

El usuario pidió las tres mejoras sin prototipo y el recorrido de Weed Honey.

**Imágenes**
- Las tiras se volvieron a capturar con `herramientas/recorridos.py`, que ahora hace celular y computador a 2x:
  - celular a 390, 585 y 780;
  - computador a 800 y 1600;
  - `pf-<id>.jpg` a 320, para las miniaturas del detalle, que antes llegaban a 5x.
- Cada `<img>` dice sus anchos (`srcset`), cuánto se dibuja (`sizes`), su ancho y alto, y carga al acercarse (`loading="lazy"`):
  - la rueda toma 800 o 1600 en el computador, y 390 o 585 en el celular;
  - el detalle toma 1600 o 780. Antes se veía a 0,8x en el computador.
- Desde la segunda pantalla se esconden las barras fijas de cada sitio: el menú flotante de Los Duches y los botones de abajo de NeuralBI y Mimarte.
- Puntos escogidos a mano:
  - NeuralNet en computador (portada, "Decisiones." y el tablero), porque a la mitad crece una esfera turquesa;
  - Weed Honey en los dos (dos momentos limpios de su portada fija, el producto y el cierre).
- Los perfiles de Instagram de Marcas tienen versión de 480 (`perfiles.py` la deja al lado). `publicaciones.py` no la toma.
- La ilustración de Rediseño tiene ancho y alto.

**Weed Honey**
- Ya tiene recorrido de celular: su verificación de edad se pasa con la fecha de un adulto de prueba (01/01/1990), con permiso del usuario.
- Así, los seis proyectos se ven en el celular como los ve un teléfono.

**Un solo cobalto** (`Base.astro`, `:root`):
- Las variables:
  - `--cobalt` (#1e55e0), lo que se elige, se une o está hecho;
  - `--cobalt-deep`, el cuerpo de una casilla encendida;
  - `--night`, `--cell`, `--deep`, `--sky`, `--ice`, `--frost`, `--lab` y `--focus`, cada azul con su papel;
  - sus canales, para las transparencias: `rgba(var(--cobalt-rgb),.2)`.
- El brillo del hero (`--glow-rgb`, #1e6bff) es la luz y no una superficie: sigue siendo más luminoso que el cobalto, para que la luz que une las secciones no se apague.
- 262 colores escritos a mano en los estilos pasaron a estas variables.
- Los cobaltos casi iguales se unieron al cobalto:
  - el fondo del Cierre, que era #1b55e8;
  - los servicios del pie, que eran #1b4fd6;
  - la burbuja de Redes;
  - el "Nuestro plus";
  - el punto de las listas del detalle.
- Las casillas "hechas" quedaron de `--cobalt` a `--cobalt-deep`.
- Salieron las variables sin uso: `--calcio`, `--ok`, `--selenio`, `--action`, `--blue`, `--blue-2`, `--ice-2`, `--steel`, `--abyss`, `--muted`, `--hair`, `--night-2` y `--dot`.
- El foco:
  - un solo azul sobre la noche (`--focus`) y el cobalto sobre el papel;
  - antes eran seis colores.
- `color.astro` escribe sus colores a mano porque los compara como texto, pero son los mismos valores.

**Una sola física**
- Siete duraciones en `:root`: `--d-press` 90, `--d-hover` 150, `--d-fade` 200, `--d-state` 260, `--d-move` 440, `--d-enter` 560 y `--d-scene` 720 ms.
- Las 26 duraciones del CSS pasaron a ellas (156 valores). Los retrasos de coreografía se quedaron como estaban.
- La curva de ida y vuelta, `--ease-io`, que no se usaba, ahora va en lo que cambia entre dos estados: el pliegue de las filas de Servicios y el ancho del detalle.
- Las animaciones hechas desde el código leen las mismas variables con `MOTION.d('state')` y `MOTION.ease('out')` (en `Base.astro`):
  - abrir y cerrar el detalle;
  - el nombre de la rueda;
  - el destello de una pregunta repetida;
  - el cierre de la hoja del menú.

## Segunda crítica del 16 de noviembre de 2026, y lo que se llevó

Otra crítica con el mismo método: dos evaluaciones aisladas, la revisión de diseño (A) y el detector con el navegador (B).
- Resultado: **25/36**, Aceptable, a un punto de Bueno. Tendencia 23 → 24 → 25. Archivada en `.impeccable/critique/`.
- El punto ganado es la prevención de errores (el contacto se revisa y no se reenvía).
- La consistencia sigue en 2, ya no por el desvío del sistema sino por la identidad de los elementos.
- El detector dio los mismos 10 hallazgos en el CLI. En el navegador dio 89 y 60, casi todos decisiones (la parodia, el encuadre, los números atómicos).

Problemas que señaló:
- [P1] el formulario llegaba en la pantalla 33 de 35, después de tres finales;
- [P1] la historia "Contenido con IA" mostraba publicaciones reales de Speedo Colombia con la etiqueta "IA";
- [P2] los símbolos y números no son estables (Weed Honey es Wh y We; "Mi" son Mimarte y La Miguería; los números cambian por lista), y entre 861 y 1199 px ni el menú ni el pie muestran nombres;
- [P2] con teclado el menú va al final (después del pie), no hay "Saltar al contenido", la hoja abre con el foco en el idioma y la rueda no tiene pausa;
- [P2] el botón de la Fórmula no hacía lo que decía.

El usuario eligió atacar "Largo y finales", con los arreglos rápidos primero. Además decidió dos cosas:
- **Historia de IA:** esas publicaciones no se hicieron con IA, así que la historia se dibuja.
- **Fórmula:** el botón dice "Pedir esta fórmula" y el primer toque suma sobre el ejemplo.

### Ya en el sitio (16 de noviembre de 2026)

**Arreglos rápidos**
- Los números de la frase final, de 8 a 9,5 px como mínimo, en cifras tabulares.
- "Tu marca" bajo el Tú se leía "Tumarca": `.zb-you em` heredaba el espaciado del símbolo grande. Ahora tiene `letter-spacing:0`.
- Con movimiento reducido, el mosaico de color se dibuja completo (`draw(1)`, antes `.66`): el borde con la silueta de la tabla y Ca y Se en su lugar.
- La luz de las casillas encendidas es un solo token, `--lit` (`Base.astro`). La usan:
  - el detalle y la rueda;
  - Redes, Preguntas y Proceso, que se había quedado con la luz vieja y daba 2,98:1;
  - la marca del recorrido del detalle;
  - el día del calendario de Redes.

**Historia de IA**
- Sus cuatro piezas, la de atrás y las tres que se abren en abanico, ahora se dibujan: un disco, la marca "Tm" y dos líneas de texto, en otros colores y otra composición en cada una (`PIECE` en `redes.astro`).
- Ninguna publicación real lleva la etiqueta "IA".
- `speedocolombia-3` y `-9` salieron de `USADAS` (`publicaciones.py`), y sus archivos quedaron fuera de `public/`.

**Fórmula**
- El botón dice "Pedir esta fórmula" (en inglés "Request this formula").
- El primer toque ya no borra el ejemplo: suma o quita sobre él, y la etiqueta "Ejemplo" se va.
- "Armar mi fórmula" se queda en Preguntas, donde lleva a la Fórmula.

**Largo y finales**
- Los momentos fijos se acortaron, sin quitar ninguno:

  | Momento | Antes | Ahora |
  |---|---|---|
  | Servicios | 440vh | 340vh |
  | Marcas | 420vh | 300vh |
  | Redes | 380vh | 300vh |
  | Rediseño | 340vh | 260vh |
  | Cierre | 340vh | 260vh |
  | Frase final | 220vh | 160vh |

  La crítica proponía 140vh para la frase final. Se dejó en 160vh para que su escalera se alcance a leer.
- Resultado a 1440:
  - la página pasó de 35,1 a 29,9 pantallas;
  - Contacto, de la pantalla 33,1 a la 27,9;
  - el primer proyecto, de la 12,4 a la 10,6.
- A 390, la página pasó de 34,5 a 29,3 pantallas.
- Llegar a la pantalla 24, como estimó la crítica, dejaría unos 25vh por historia o por marca.
- El Cierre ya no tiene botón: antes del formulario va uno solo, el de la frase final. Mientras tanto, el del menú fijo sigue a la vista.

### Ya en el sitio: símbolos, nombres y teclado (16 de noviembre de 2026)

El usuario pidió los dos frentes que quedaban ("Ambos").

**Un solo símbolo y un solo número por cosa**
- `EL_Z` en `Base.astro` le da a cada elemento su número, por su símbolo en español, y `zOf(s)` lo escribe con dos cifras.
- La regla:
  - lo que vive en la tabla del pie lleva su número de ahí: Ca 20, Se 34, los servicios del 21 al 24, Contacto 27 y las secciones Sv 37, Rd 38, Py 39, Mc 40, Pc 41 y Pr 42. Redes es el servicio Redes sociales: Rs 23, también en inglés (antes era "So" en el menú);
  - los clientes llevan una sola cuenta, primero los proyectos y después las marcas: Ld 01, Nn 02, Nb 03, Ak 04, Wh 05, Mi 06, Ag 07, Lm 08, Sp 09, O' 10 y Ea 11. Weed Honey es Wh en las dos secciones (antes era We en Marcas) y La Miguería pasó a Lm (antes compartía "Mi" con Mimarte);
  - "Tu marca" es Tú 119 en todas partes: el elemento que recorre Proceso, el de Motion graphics en Redes, la marca dibujada en las escenas de Servicios y en las piezas de IA, y el del Cierre. En inglés es You. Antes era "Tm", que además es el tulio en la tabla del hero;
  - lo que vive en una sola lista conserva su número ahí: los pasos de Proceso del 01 al 04, las historias de Redes del 01 al 06 y Fm 02 en Preguntas.
- **Dónde se ve el cambio:**
  - el menú y la hoja muestran 37, 38, 39, 40, 41, 23, 42 y 27;
  - Servicios, la Fórmula y Contacto, del 21 al 24;
  - en Preguntas, cada pregunta lleva el número de lo que la responde.

**Nombres**
- El nombre de la sección en la que vas (`.mn-now`) se ve desde 861 px:
  - hasta 980 px, a la derecha de la fila, que ahí está pegada a la izquierda;
  - de 981 a 1199 px, a la izquierda de la fila, para no chocar con el botón;
  - desde 1200 px, a la derecha.
- **Nombres del pie entre 861 y 1200 px:** no caben dentro de la casilla (mide unos 49 px a 1024). Salen encima de ella al pasar el cursor o con el foco, como en la fila del menú.
- **Desde 1201 px:** los nombres del pie miden 11 px (antes 10,5).

**Teclado**
- **Orden de tabulación:**
  - el primer enlace es "Saltar al contenido" (en inglés "Skip to content"): está fuera de la vista hasta que tiene el foco y lleva al titular del hero, que tiene `tabindex="-1"`;
  - el menú fijo va primero en el DOM, justo después de ese enlace: antes 75 de 88 paradas pasaban antes de llegar a él.
- **Enlaces internos:** llevan el foco a su sección, no solo el scroll (`arranque.astro`). La sección con el foco no muestra anillo, porque no es un control.
- **Hoja del celular:** abre con el foco en la sección en la que vas. Antes lo tenía en el idioma, y un Enter cambiaba de idioma.
- **Rueda de Proyectos:** tiene pausa (`Pausa`, junto a las flechas). Detiene el recorrido del sitio del frente hasta que se vuelve a tocar, y no se ve con movimiento reducido.
- **Rediseño:** los titulares de las dos maquetas son párrafos, para que no entren al esquema de títulos.

### Ya en el sitio: observaciones menores (17 de noviembre de 2026)

El usuario pidió todas menos la de Weed Honey.
- **Barra del hero:** el idioma va contra el borde y el botón antes (`order:2`, como en el menú fijo). Mientras el botón se aparta, su lugar queda en el medio de la barra y no hay hueco a la derecha de ES/EN.
- **Cierre:** Ca y Se llevan detrás una casilla del azul de la sección (`.zb-back`). Las letras de Ca están caladas y Se es un contorno, y sobre la tabla encendida se veían In, Sn, Sb y Pb a través de ellas. En reposo se ven igual.
- **Rediseño:**
  - la etiqueta de la nota 03 ("Dos botones compiten") va al lado de los botones, y ya no sobre el subtítulo de la parodia;
  - hasta 860 px va encima de ellos, a la derecha;
  - en el celular va debajo de los botones, y la 04 debajo de las tarjetas, para que no compartan franja;
  - entre 601 y 860 px las etiquetas de las notas pasaron a 10,5 px y su número a 10, porque estaba en 9 y rompía la regla 8.
- **Textos pequeños:**
  - "Nuestro plus" y "Ejemplo" pasaron de 11 a 12 px;
  - "tu fórmula", de 12 a 13 px;
  - las etiquetas del formulario, de 12,5 a 13 px.
- **Barra del detalle:** cada herramienta muestra su nombre, el mismo de su `aria-label` (ya traducido), debajo de ella al pasar el cursor o con el foco.

Sigue pendiente de la crítica: Marcas abre con las dos cuentas más pequeñas (Weed Honey y Agilcash), y la captura de Weed Honey está en inglés y con sesión iniciada. Necesita una captura del usuario.

### Ya en el sitio: barrido del 17 de noviembre de 2026

El usuario pidió un barrido con Impeccable y Taste, quitar la Frase final, revisar la distribución en todos los anchos, poder arrastrar la rueda sin usar las flechas, alinear el encuadre de Redes y subir las animaciones de Servicios. Dos agentes revisaron una copia del sitio: uno el diseño, sección por sección, y otro los márgenes de 390 a 2560, con capturas y medidas (en el scratchpad de la sesión, `barrido/A` y `barrido/B`).

**La Frase final se quitó** (ver su sección). El Cierre recupera su botón "Empezar mi proyecto" y es el último llamado. El botón del menú fijo se oculta en el Cierre y en Contacto, que ya tienen el suyo.

**Anchos**:
- **Redes y Marcas**: el encuadre llena su columna hasta la medianil derecha, como en Servicios, Rediseño y Preguntas. Antes iba centrado con un tope: a 1880 de ancho le faltaban 131 px (Redes) y 288 px (Marcas) para la medianil. En Marcas esto deshace lo pedido el 13 de noviembre ("el encuadre abraza al teléfono, en el medio de su columna"): si el usuario lo prefiere así, se vuelve.
- **Redes, hasta 860 px**: el título y la fila de elementos empiezan en la medianil; a 768 iban centrados.
- **Proceso**: las tarjetas miden 180 px como mínimo (antes 220). A 768 y 1024 se salían de la medianil y dos se montaban.
- **Preguntas**: un mensaje no pasa de 36em, unos 70 caracteres por línea. Desde 1920 había líneas de 95 a 111.
- **Servicios**: la frase va bajo el título en todos los anchos. Desde 1680 saltaba a la esquina derecha, hasta 1000 px lejos del título.

**La rueda de Proyectos**:
- **Se agarra en cualquier parte, también sobre la pantalla.** Con el mouse, la imagen del recorrido empezaba su propio arrastre y la rueda se movía 3 px y volvía.
- **Una vez que se mueve, guarda el puntero.** Soltar fuera de la ventana también la suelta.
- **El trackpad la gira** con el deslizamiento lateral, y la rueda del mouse con Shift. Al levantar los dedos se asienta en el sitio más cercano.
- **Un lanzamiento fuerte pasa hasta tres sitios.** Al agarrarla cede un poco (escala ,985), y mientras gira las pantallas se inclinan con la velocidad (hasta 5°) y se enderezan al asentarse.
- **Al entrar gira medio sitio hasta su lugar**, para mostrar que gira.
- **Una pantalla nunca está vacía:**
  - su póster va de fondo mientras llega el recorrido, que entra con un fundido;
  - las tiras del frente y sus vecinas se piden pantalla y media antes de verse;
  - el detalle también abre con el póster detrás.

**Saltos largos**: un enlace que va a más de dos pantallas no recorre el camino. La página se apaga un instante a la noche y abre en la sección (`JUMP`, en `arranque.astro`). "Ver proyectos" cruzaba 9.500 px de momentos fijos en un segundo.

**Servicios, las cuatro escenas** (`escenas.astro`):
- **Sitios web**:
  - el primer servicio llega como una página que carga (su ventana, la barra de dirección con la línea de carga y la forma de sus partes), y el primer tramo de scroll la carga; antes llegaba ya armada y "Cargan rápido" se contaba con un cuadro quieto;
  - el botón cede bajo el dedo;
  - en el WhatsApp escribe un "Cliente nuevo" con sus tres puntos antes del mensaje.
- **Tiendas**:
  - el carrito salta cuando el producto cae en él;
  - "Pagar" pasa por un anillo, el visto y un destello;
  - un punto de luz lleva la venta por la línea al inventario;
  - la cámara se corre antes de que entre el inventario, que antes entraba cortado por el borde;
  - el inventario es más grande: su número pasa de 6 a 5 y la unidad vendida sale con "−1".
- **Redes**:
  - cada día se enciende cuando le cae su pieza;
  - las publicaciones brillan al subir al perfil;
  - "Publicado" lleva su visto;
  - la respuesta tiene sus tres puntos.
- **Marca**:
  - las cuatro casillas se funden con un destello y el Tú tiene su número, 119, desde que existe;
  - los colores salen del logo a su lugar;
  - "Aa" gana peso al llegar;
  - la hoja de la derecha se abre desde el lomo;
  - el uso incorrecto tiembla antes de su cruz;
  - en el celular la cámara sale cuando se abre la hoja y llega con la tipografía ya puesta.

**Reglas que se cumplían a medias**:
- **Regla 8**: en el Cierre y en la escena de Marca el Tú contaba del 01 al 119 mientras caía. Ahora lleva el 119 desde el comienzo.
- **Mono solo para números y datos.** Pasaron a la sans:
  - "Secciones" y "Servicios" del pie y de la hoja del menú;
  - la marca "IA" de las piezas de Redes;
  - el nombre de "119 Tu marca" del Cierre (el número sigue en mono);
  - en las escenas, "WhatsApp", "Llegó desde tumarca.com", "Calendario de contenido", los días de la semana, "Instagram · TikTok", "Publicado", "Guía de marca" y "Usos".
- **"Nuestro plus" ya no es una píldora cobalto**: es una palabra en el azul del cielo junto al nombre, y en la historia, una línea propia bajo el título.
- **El foco en el hero es `--focus`**: era el cobalto sobre la noche.

**Marcas**: la fila encendida despliega su línea, con la cifra real de cada cuenta (280 mil seguidores, 70 mil, 70.000 egresados), como la frase de un servicio en Servicios. Antes solo se veía con movimiento reducido.

**Chequeos**:
- **`npm run revisar`**: las cinco en "bien".
- **Detector de Impeccable**: los mismos de siempre.
  - `cramped-padding` en las secciones a sangre: falso positivo, porque los márgenes medidos coinciden con la medianil.
  - La parodia de Rediseño: a propósito.
  - El halo de la luz del encuadre.
- **Taste copy-lint**: 0 FAIL. Los WARN son los números atómicos del menú y del pie, que son el concepto.
- **Taste perf** se corrió con el equipo casi sin memoria libre y dio tareas largas, igual que en otras rondas: hay que repetirlo con el equipo libre.

**Lo que el barrido propone y no se hizo** (son decisiones del usuario):
- **Cierre**: que el 119 sea lo más grande de la pantalla al final. La cámara entra al período 8, la tabla se oscurece y la casilla del Tú crece con el botón pegado a ella; hoy el Tú termina como una casilla más.
- **Fórmula**: a 1440 la composición queda a medias (la zona al centro, Ti y Ma solos a la derecha, el lado izquierdo y el tercio de abajo vacíos) y dice lo mismo tres veces. La dirección propuesta:
  - los cuatro elementos en columna a la izquierda;
  - a la derecha, una casilla grande donde caen;
  - debajo, el compuesto y, por cada elemento, su frase de Servicios.
- **Proceso**: abre casi vacío (una línea tenue y un Tú pequeño en la esquina). La dirección propuesta:
  - el Tú grande al empezar;
  - cada estación deja un objeto dibujado en lugar de una tarjeta blanca;
  - unos 220vh en lugar de 300.
- **Redes**: Estrategia y Community management son esqueletos (barras grises, siglas). Se pueden dibujar los tres canales reales del texto (comentarios, mensajes y reseñas) con su estado de respondido.
- **La misma composición cinco veces** (texto a un lado, encuadre al otro: Servicios, Rediseño, Marcas, Redes y Preguntas). Se pueden centrar Redes y Preguntas, como ya están en el celular.
- **Textos** (no se cambian sin el usuario):
  - "Proyectos" podría ser "Seis sitios en vivo.";
  - "Hablemos de tu proyecto" podría ser "Cuéntanos qué necesita tu marca.";
  - en el hero, "Juntamos lo que tu marca necesita en un solo equipo." repite el lead, y "en Medellín" cabe en él;
  - Preguntas no responde precio, tiempos, de quién queda el sitio ni qué pasa después: faltan las respuestas del usuario.
- **El reflejo bajo las pantallas de la rueda**, que es el gesto del cover flow.
- **Las casillas de Antes/Después de Rediseño**, que parecen tocables y no lo son.
- **Las fichas de Marcas en los colores de cada cliente** (Weed Honey es 05 en azul noche en Proyectos y 05 beige en Marcas).
- **Mensaje**: Rediseño se burla del estilo de IA y en Redes "Contenido con IA" es "Nuestro plus". Es tensión de mensaje: decide el usuario.
- **El largo**: 29,9 pantallas a 1440. Se puede recortar un 15–25 % del alto en Proceso, Marcas y el final del Cierre.

### Análisis del 21 de noviembre de 2026, arreglos y prototipos

El usuario eligió Acercamiento para el Cierre y pidió otro análisis del sitio, prototipos de mejoras y quitar los patrones de IA que quedaran. El análisis siguió el método de crítica de Impeccable: dos revisores aislados sobre una copia congelada del sitio, uno de diseño (sin ver detectores ni críticas anteriores) y otro de evidencia medida. Sus archivos están en el scratchpad de la sesión (`analisis/A` y `analisis/B`).

**Veredicto del revisor de diseño**: donde la tabla hace trabajo (hero, Cierre y pie) el sitio es de autor; en el medio, cinco secciones repiten "lista de casillas + marco oscuro" y el concepto baja a viñeta. Heurísticas de Nielsen: 23 de 36 (la 7 no aplica). Lo más bajo: reconocer antes que recordar (1), porque el menú habla en símbolos; lo más alto: recuperarse de errores (4), por el formulario.

**Evidencia medida**:
- **Detector estático de Impeccable**: los 10 de siempre (7 falsos positivos de relleno, 2 de la parodia de Rediseño y la luz del encuadre).
- **Detector dentro del navegador, a 1440**: 52 hallazgos.
  - De la parodia de Rediseño o de sus maquetas en miniatura: los 5 resplandores, el texto degradado y 8 textos pequeños.
  - Números de elemento a 10 px (18): cumplen la regla 8 del proyecto, que permite hasta 9,5 px.
  - Luces del encuadre (4): decididas.
  - **Reales**: 10 textos con poco contraste (los números sobre casillas encendidas, a 3,3–3,9:1, y las casillas de Marcas en colores de cliente, hasta 2,6:1) y un azul escrito a mano en la luz de Proyectos.
- **Taste copy-lint**: 0 FAIL; los 2 avisos son los números atómicos, que son el concepto.
- **Azules escritos a mano**: 148 usos de 52 colores fuera de `:root`. La regla 5 pide variables. Los más repetidos: `#eef3ff` (13), `rgba(160,196,255,…)` (12), `rgba(170,204,255,…)` (9), `#8fb0ff`, que ya es `--frost` (8), y `#b3bfd3` (8). **Pendiente**: una pasada que los vuelva variables, verificada con capturas idénticas antes y después.

**Arreglos aplicados el 22 de noviembre de 2026**:
- **Marcas**:
  - las casillas van en los azules del sitio (marino en reposo, encendida la del teléfono). Llevaban los colores de cada cliente: era lo único de la página fuera del blanco, negro y azul, con contraste de hasta 2,6:1, y Weed Honey era azul en Proyectos y beige aquí. Dentro del teléfono cada marca conserva sus colores;
  - en el celular, bajo el encuadre, van el nombre y la línea de la marca que está en el teléfono (`.mr-cap`). Antes solo se veían seis símbolos;
  - para un lector de pantalla, cada fila describe su marca con su línea (`aria-describedby`).
- **Menú fijo**: espera a que la última frase del hero salga de la pantalla. Entraba encima de ella durante unos 160 px de scroll (regla 7).
- **Cierre**: la frase y el botón ya no se sacan de la página con `visibility`: el lector de pantalla los lee siempre y el teclado llega al botón en cualquier punto; al recibir el foco, el Cierre va a su final. Mientras no se ven, el puntero no los puede tocar.
- **Proceso**: las tarjetas de los pasos solo se ocultan a la vista (opacidad), así el lector de pantalla lee los cuatro.
- **Números sobre casillas encendidas**: blancos, y `--lit` un poco más hondo arriba, para pasar de 4,5:1.
- **Preguntas**:
  - llega con el saludo y la primera pregunta ya respondida, quietos (llegaba con dos burbujas en un marco de 600 px);
  - responde en la mitad del tiempo (una respuesta de cinco mensajes tardaba 5,2 s).
- **Fórmula**: "Ejemplo" y "tu fórmula" dejan el mono, y "Ejemplo" deja de ser una píldora.
- **Proyectos**: la luz del escenario usa `--glow-rgb`.
- **Tarjeta del enlace**: se agregaron las etiquetas `og:` y `twitter:card` (sin imagen todavía).
- **Observadores**: los tres que despiertan animaciones (`onVisible`, Fórmula y Redes) leen el último aviso del lote. Si llegaban dos juntos, por un salto justo después de armar la página, se quedaban con el viejo: en la Fórmula las casillas no salían de la esquina.

**Elegidas el 22 de noviembre de 2026: Fórmula B · Con tu marca y Proceso A · Lugares.** Ya están en `formula.astro` y `proceso.astro`. Frente a los prototipos:
- **Fórmula**: la cara del Tú es una variable, `--you-face`, que comparten el Cierre y la Fórmula. Los textos nuevos están en `en.json` ("Toca los elementos que tu marca necesita o arrástralos a la fórmula." y "Esto es un ejemplo: toca un elemento y la fórmula es tuya."); salieron "tu fórmula", "Ejemplo" y "Todos los elementos de tu marca en internet.", que ya no se usan. El primer toque sigue conservando el ejemplo.
- **Proceso**: los pasos se ocultan solo a la vista (opacidad), para que el lector de pantalla lea los cuatro en cualquier punto del scroll; el prototipo usaba `visibility`.

**Prototipos** (las fuentes están en la carpeta `proto/` del scratchpad de la sesión; las fuentes están en la carpeta `proto/` del scratchpad de la sesión, con `armar.py`, que las monta sobre `dist/`):
- **Fórmula**: https://claude.ai/artifact/3Vwbx6rDCvjjYQu9BpsEHH. Los elementos esperan en una fila, cada uno con su lugar punteado, y caen a una bandeja donde se funden, más grandes, como las dos casillas del logo. Debajo, lo que trae cada uno: su frase de Servicios. El título va centrado y el ejemplo se ve en contorno hasta el primer toque.
  - **A · Caída**: la fórmula son los elementos elegidos.
  - **B · Con tu marca**: la fórmula empieza siempre por Tú (119) y lo elegido se une a él.
- **Proceso**: https://claude.ai/artifact/6uYZA3HeUjb27W6dG4mfRf. La Ruta se queda. El Tú sale grande, cada estación tiene su lugar punteado desde el comienzo, los pasos van sobre el papel sin tarjeta, y al final el Tú sale lanzado por el extremo de la línea. Pasa de 300vh a 240vh.
  - **A · Lugares**: cada paso aparece cuando el Tú llega, como hoy.
  - **B · Una a la vez**: la estación que el Tú alcanza se abre en grande con su frase, y las que ya pasó quedan como casillas pequeñas con su nombre (la dirección que propuso el revisor).

**Decisiones que quedan con el usuario**:
- **El primer toque en la Fórmula.** Hoy conserva el ejemplo (decisión del 16 de noviembre): quien toca solo Tiendas termina con Sitios web, Redes y Tiendas marcados en Contacto. El revisor lo marcó como riesgo. La alternativa: que el primer toque reemplace el ejemplo.
- **Contacto como fórmula** (propuesta del revisor): en lugar de cuatro tarjetas iguales, el Tú del Cierre unido en grande a lo elegido, con la misma bandeja de la Fórmula, y la barra debajo.
- **El menú con nombres**: hoy son ocho símbolos y solo se nombra la sección actual; el revisor propone el nombre bajo cada casilla, como en el pie.
- **Los marcos medio vacíos**: Redes muestra una historia de 370 px en un marco de 907, y Marcas a 1880 un teléfono de 337 en 1.168. El revisor propone alternar el lado del marco y que el contenido lo llene.
- **Preguntas en el celular**: las siete van en una tira horizontal; el revisor propone una lista vertical.
- Siguen pendientes de antes: el reflejo de la rueda, las casillas de Antes/Después de Rediseño, y precio y tiempos en Preguntas.

### Publicación en Vercel y revisión de seguridad (22 de noviembre de 2026)

El sitio se publica en Vercel como una sola aplicación de Astro (`vercel.json`, `.vercelignore`, Node 24 en `package.json`). Antes de publicar se revisó que nada quedara expuesto:

- **Llaves y secretos**: ninguno, ni en los archivos, ni en el historial de git, ni dentro de los dos zip. El sitio no llama a ningún servidor ni guarda nada en el navegador. `npm audit` no encuentra vulnerabilidades.
- **Datos personales**: los correos son de muestra y los commits usan la dirección `noreply` de GitHub. Las imágenes del sitio no traen metadatos. La captura de Weed Honey no muestra de quién es la cuenta que la tomó.
- **Lo que se publica**: `dist/` tiene la página, su hoja de estilos y las imágenes de `public/assets/`; sin mapas de código ni archivos de trabajo. El visor abre los sitios de los clientes en un marco aislado, y los enlaces que abren pestaña llevan `noopener`.
- **Arreglos**: salió de git `archivo/sitio-python/.impeccable/hook.cache.json` (una caché con una ruta del computador; sigue en el historial); `.gitignore` cubre esas cachés en cualquier carpeta, `.env` y `.vercel/`; y `vercel.json` manda cabeceras de seguridad (ver `docs/arquitectura.md`, "Publicación").
- **Queda con el usuario**: el repositorio de GitHub es público, así que cualquiera ve `CLAUDE.md`, `docs/`, `archivo/` y `marca/`, con los nombres del equipo que se quitaron del sitio. Y el código de la página nombra claude.ai en un comentario y en la condición `LIVE` de `visor.astro`.

### Rendimiento, scroll suave, buscadores y menos scroll fijo (22 de noviembre de 2026)

El usuario trajo el informe de PageSpeed del sitio publicado (95 en rendimiento en celular: primera pintura y pintura más grande en 2,0 s, índice de velocidad 4,6 s; SEO 91) y pidió mejorarlo, sumar posicionamiento para buscadores y asistentes, scroll suave tipo Lenis, capturas nuevas de Weed Honey, el detalle sin la barra de arriba y, al final, menos movimiento atado al scroll.

**Carga.** Medido con `herramientas/carga.py` (un Moto G Power con 4G lenta y el procesador cuatro veces más lento, alternando el armado de antes y el de ahora): la primera pintura pasó de unos 2,5 s a 1,4 s y la pintura más grande de unos 3,9 s a 2,0 s. Lo que cambió:
- Las fuentes las sirve el sitio (antes Google Fonts: otra conexión y una hoja que frenaba la primera pintura); la de texto se pide por adelantado.
- La hoja de estilos va dentro de la página (medido: 1,39 s contra 1,79 s con la hoja aparte).
- El hero se pinta antes de preparar las otras diez secciones, que despiertan después, de a pocas. Antes todo se preparaba antes de la primera pintura: en un celular lento, más de un segundo de pantalla en blanco.
- Los scripts se minifican al armar (de 218 a 138 KB; de paso los comentarios ya no viajan en la página).
- Nada hace una transición hacia su primer estado al cargar, y el botón de la barra del hero ya no aparece un instante antes de esconderse.

**Scroll suave** (Lenis, `suave.astro`): la rueda desliza la página y la deja asentarse. Dos números lo gobiernan, `LERP` (0,085) y `WHEEL` (0,9). El dedo en el celular y el movimiento reducido usan el scroll del navegador.

**Buscadores y asistentes.** Dirección canónica, imagen para compartir (`public/assets/og-case-studio.jpg`, el hero de verdad), iconos y manifiesto, datos estructurados (el estudio y sus cuatro servicios, la página, las preguntas, los proyectos y las marcas), `robots.txt`, `sitemap.xml`, `llms.txt` y `llms-full.txt`. El contenido también llega escrito en el HTML para quien no corre JavaScript (los rastreadores de los asistentes no lo corren). El título quedó "CaSe Studio | Sitios web, tiendas, redes y marca en Medellín". Los dos enlaces del detalle que PageSpeed marcaba sin destino ya lo tienen o salieron con la barra.

**El detalle de un proyecto** ya no tiene la barra de arriba; quedan dos casillas en la esquina (el ancho del sitio y salir). Salieron "volver a cargar" y "abrir en pestaña nueva": la segunda ya está en "Visitar sitio".

**Weed Honey.** Su sitio cambió por completo. Tiras y póster nuevos: la portada "Soda con CBD", lo que trae cada lata, un sabor y la tienda. El sitio muestra un aviso arriba después de la verificación de edad; la herramienta lo esconde sin tocarlo.

**Menos scroll fijo.** La página medía 28 pantallas de alto a 1440 y ahora 22. Servicios, Marcas y Redes pasan con el scroll normal y se cuentan solas (`showtime()`); siguen fijas el hero (2,5 pantallas), Rediseño (2,6), Proceso (2,4) y el Cierre (3).

**Queda con el usuario:**
- Mirar en vivo el scroll suave y las tres secciones que ahora corren solas: el ritmo no se juzga con capturas.
- El formulario no envía y no hay correo ni WhatsApp reales: es lo que más pesa ahora que el sitio está publicado y se va a posicionar.
- Si "el banner superior" que pidió quitar era otra cosa que la barra del detalle.
- Si Rediseño (2,6 pantallas fijas) también pasa a scroll normal.
- Confirmar los textos del proyecto Weed Honey frente a su sitio nuevo ("Tabla nutricional e ingredientes por producto" es el que no se pudo comprobar).
- PageSpeed también lista, sin puntaje, una política de contenido completa, HSTS con subdominios, aislamiento de origen y Trusted Types: son decisiones de dominio y van con el envío del formulario.

### El WhatsApp del estudio (23 de noviembre de 2026)

El usuario dio el WhatsApp, +57 310 872 3020, y pidió que todo llegue allí. El formulario abre WhatsApp con la solicitud escrita (los servicios marcados, el nombre y cómo responder); el botón dice "Enviar por WhatsApp" para que el visitante sepa qué va a pasar. El número reemplaza al correo de muestra en el pie y está en los datos estructurados, el contenido sin JavaScript y `llms.txt`. En 127.0.0.1 el formulario no abre WhatsApp (las herramientas lo llenan).

## Pendiente del usuario

- Decidir si el repositorio de GitHub sigue público o pasa a privado (Vercel publica igual desde uno privado).
- El correo del estudio: va al pie, a los datos estructurados y a `llms.txt` cuando llegue.

- Si se quieren preguntas de precios, tiempos, propiedad del sitio o rondas de cambios en Preguntas, dar sus respuestas.

- El correo del estudio (el WhatsApp ya está desde el 23 de noviembre de 2026).
- Las cuentas de redes del propio estudio, para el pie.
- Revisar el inglés. Una traducción para mirar con cuidado: "Nuestro plus" como "Our edge".
- Cerrar el logo definitivo (`marca/`).
- Los cinco videos de recorrido de los proyectos, si se quieren en vez de las tiras de pantallas.

## Stack

**Decidido el 11 de noviembre de 2026: Astro** (estático, TypeScript estricto), en lugar de Next: el sitio es una página de presentación sin sesión ni datos por usuario, Astro no le carga React al visitante y el código de canvas pasó tal cual. El armado con Python quedó en `archivo/sitio-python/`.

Hecho: el proyecto Astro en la raíz (`src/`, `public/`), las partes como componentes, el inglés en `src/i18n/en.json`, las herramientas revisando `dist/` y `npm run dev` para trabajar.

Siguientes pasos del stack, en orden:
1. **Git.** El usuario crea el repositorio el 12 de noviembre de 2026; desde ahí se suben los cambios.
2. **HTML que llega escrito.** Hoy las secciones están en `<template>` y se montan con JavaScript al cargar. Pasarlas a markup de Astro hace que el contenido llegue escrito (mejor para buscadores y para la primera pintura) y deja el JavaScript solo para el movimiento.
3. **Una URL por idioma** (`/` y `/en/`) con el i18n de Astro, con título y descripción en inglés, en vez de traducir la página en el navegador.
4. **Código en módulos TypeScript.** Las funciones compartidas (`moment`, `drive`, `pointer`) y el lienzo del hero como módulos, en vez de scripts globales.
5. **Fuentes servidas desde el sitio** (Fontsource o la API de fuentes de Astro) en vez de Google Fonts, cuando se confirme la combinación.
6. **Envío del formulario** (un endpoint o un servicio de formularios) y **dominio**. El hospedaje es Vercel (22 de noviembre de 2026); cuando el formulario tenga a dónde enviar, se escribe la política de contenido completa en `vercel.json` con ese destino. El visor ya está listo para abrir los sitios reales en su dominio (`LIVE` en `visor.astro`).

## Siguiente

El plan del usuario es perfeccionar Tabla sección por sección. El hero quedó decidido; lo que sigue del hero está arriba. **Servicios** (decidido el 12 de noviembre de 2026): de la segunda ronda de prototipos el usuario eligió **Escenario**, con Reacción después, y pidió animaciones con una narración que se entienda y sin AI slop. Ya está en el sitio y reemplazó a Familias + Laboratorio:

- **La lista** (izquierda): número, símbolo y nombre de cada servicio; el que está al frente se enciende y dice su frase.
- **El escenario** (derecha): un cuadro grande con la animación del servicio al frente, llevada por el scroll. Debajo del dibujo no hay texto: la frase del servicio, en la lista, está partida donde la animación cambia de paso, y el tramo que se está contando se pone en tinta con un marcador azul que corre bajo él con el scroll ("Cargan rápido," → "se leen bien en el celular" → "y llevan a tu cliente a escribirte."). La frase es el guion; así se cumple también la regla de Taste de no poner textos bajo una imagen. Las cuatro cuentan cada una su frase para "Tu marca", la marca del visitante (el mismo Tm de Contacto):
  - Sitios web: la página de "Tu marca" carga pieza por pieza, pasa al celular, el visitante toca "Escríbenos por WhatsApp" y te llega su mensaje: en tu WhatsApp escribe un "Cliente nuevo", y abajo dice "Llegó desde tumarca.com".
  - Tiendas: "Agregar" lleva el producto al carrito, "Pagar" termina en "Pago aprobado" y el inventario conectado baja una unidad.
  - Redes: el calendario de este mes (los días reales) recibe fotos, videos y textos; pasan al perfil @tumarca, quedan publicados y alguien pregunta "¿Tienen envíos?" y recibe respuesta.
  - Marca: cuatro casillas se vuelven el logo Tú (119, desde que existe) con su nombre, llegan los colores con nombre y valor, las dos tipografías, y la guía muestra el uso correcto y el incorrecto.
- Las palabras dentro de los dibujos son palabras de interfaz, en el idioma de la página, sin insignias. Desde el 17 de noviembre de 2026 hay dos señales que antes no estaban, y solo donde cuentan una causa: el esqueleto de la página mientras carga (en Sitios web, se va en cuanto llega el contenido) y los tres puntos de "escribiendo" justo antes de un mensaje. Los mensajes de ejemplo ("Hola, quiero hacer un pedido.", "¿Tienen envíos?", "Sí, te escribimos por DM.") son de una marca hipotética, no de clientes; el usuario puede pedir que se cambien.
- En celular el escenario va arriba y una cámara sigue el paso que se cuenta, para que sus palabras se lean. Con movimiento reducido no hay escenario: cada fila muestra su dibujo completo y quieto.
- El tablero tiene una sombra corta que se apaga dentro de la sección. La de antes medía 80 px, la sección la cortaba en su borde y al llegar Fórmula quedaba una raya bajo el tablero. `lineas.py` ahora busca esos cortes en cada borde entre secciones del mismo color.
- **La fórmula** (sección propia, `#formula`): no está atada al scroll ni se queda fija (el usuario lo pidió el 12 de noviembre de 2026: está solo para que el visitante agregue algo si quiere). Es una sección normal de una pantalla. Abre con un ejemplo marcado como tal (Sw + Rs); el primer toque lo borra. Lo que el visitante une pasa a Contacto: Tiendas marca "Tienda en línea", Redes "Manejo de redes", Marca "Logo e identidad", y Sitios web hace que la fila Web pregunte el tipo de sitio. Nunca se deshace lo que el visitante marcó a mano, y la fórmula se conserva al cambiar de idioma.
- Sigue faltando un caso real de Marca, si algún día se quiere mostrar trabajo real en vez de "Tu marca".

### Servicios: lo que la frena hoy

- Cuatro tarjetas iguales en fila: el patrón que la regla 1 y Impeccable señalan.
- Al voltear, el símbolo desaparece: nunca se ven el elemento y su descripción juntos.
- El titular promete "Tú eliges la fórmula", pero aquí no se elige nada; la elección vive en Contacto.
- 460vh de scroll para cuatro frases.
- No lleva a ninguna parte: ni a Redes, ni a Rediseño, ni a los proyectos de cada servicio.

### Servicios: las opciones que se consideraron (11 de noviembre de 2026)

1. **Familias.** Cada elemento se abre en su grupo de cuatro, sacados de su propio texto: Sitios web (Sitio corporativo, Landing de ventas, Menú y pedidos, Rediseño), Tiendas (Catálogo, Carrito, Pagos, Inventario), Redes (Calendario, Fotos, Videos, Textos), Marca (Logo, Colores, Tipografías, Guía). Cuatro columnas de cuatro: un bloque de la tabla.
2. **Laboratorio.** Los elementos se tocan para armar la fórmula aquí mismo, y "Armar mi fórmula" lleva a Contacto con esas opciones ya marcadas.
3. **Elemento y prueba.** Una pantalla por servicio con su caso real (Sitios: AKUA, NeuralBI. Tiendas: Mimarte, Weed Honey. Redes: La Miguería, Agilcash). Marca no tiene caso en `contenido.md`. Se cruza con Proyectos y Marcas.
4. **La ecuación.** Un momento tipográfico: "Sw + Ti + Rs + Ma → CaSe" de lado a lado; el scroll abre cada término en su frase y la flecha se cierra en el logo.
5. **Ficha técnica.** Cada servicio como una ficha de elemento completa: qué incluye, con qué se combina y un proyecto real. Suma 1 y 3.
6. **Pulir lo actual.** Volteo con símbolo y texto juntos, grosor real, selección y menos scroll.

Se eligió 1 + 2. Las demás direcciones se prototiparon el 12 de noviembre con el skill *prototype* en un artefacto de claude.ai, para ver qué más puede salir: https://claude.ai/artifact/SUDetRRyosowfTWuVeonQ5 (teclas 1 a 5 o flechas para cambiar de variante, R para reiniciar). Son cinco: Ecuación (tipográfica), Lista (filas en vez de tarjetas), Caso (cada servicio con su proyecto real), Ficha (la más densa) y Reacción (se juntan elementos para formar la fórmula). Ninguna toca `src/`; si alguna gana, se integra y el artefacto queda como archivo.

**Segunda ronda (12 de noviembre de 2026)**, pedida por el usuario: Servicios como lista, con una animación 2D por servicio en el lenguaje de la marca y menos texto; la lista solo muestra y la elección pasa después, en el componente Reacción de la primera ronda. Artefacto: https://claude.ai/artifact/68vCPcC7hNE1vZK6KSrsSc (teclas 1 a 4 o flechas, R reinicia). Las cuatro animaciones son las mismas en todas las variantes, llevadas por el scroll y sin cifras ni textos de relleno:
- Sitios web: la página carga casilla a casilla, se vuelve celular y llega un mensaje del cliente.
- Tiendas: un producto pasa del catálogo al carrito, el pago se aprueba y sale una unidad del inventario.
- Redes: el mes se llena de fotos, videos y textos, se publican y la comunidad comenta.
- Marca: cuatro casillas se vuelven el logo, llegan los colores y las tipografías, y todo queda en una guía.

Las variantes cambian dónde vive la animación: Escenario (lista a un lado, un cuadro grande al otro), Filas (la fila activa se abre con su animación adentro), Elemento (la casilla misma se abre y se vuelve el dibujo, en azul marino) y Mosaico (el dibujo hecho de casillas, como los cambios de color del sitio). Reacción tiene menos texto que en la primera ronda: la fórmula, los nombres y "Armar mi fórmula".

