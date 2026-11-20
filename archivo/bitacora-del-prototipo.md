# Referencia: artifact "CaSe Studio" (https://claude.ai/artifact/FUw6qEAqJaGxQcEv95qLeE)

Público, de otra cuenta (slug 75465d19-bfe6-4b15-8ec1-f6b63b059b9b). No se puede leer ni copiar con las
herramientas de artifacts (not found); sí se ve en el navegador integrado. El taller no alcanza ese host (403).
Archivos: index.html + videos/{akua,losduches,mimarte,neuralbi,weedhoney}.{mp4,jpg} (0,6 a 1,6 MB cada mp4).

## Cómo muestra los previews
- Tarjeta: marco de navegador (3 puntos + URL) con `<video class="clip" muted loop playsinline autoplay poster>`.
- Al abrir: hoja (sheet) con el mismo video + nota "Recorrido real del sitio, acelerado. Abre el sitio para
  navegarlo tú mismo." + ficha (sector, ubicación, tipo, idioma) + "Lo que construimos" + "Visitar sitio ↗".
- No hay iframe: el visor de artifacts bloquea iframes de otros sitios.

## Equipo (tab Nosotros)
- Camilo Corrales · Diseño y desarrollo · "Programación, diseño visual y construcción de cada sitio, desde la primera pantalla hasta el último detalle."
- Sebastián Vanegas · Ventas y relaciones comerciales · "Entiende el negocio de cada cliente, define qué debe lograr la web y acompaña el proyecto de principio a fin."
- Catalina Vanegas · Redes sociales y contenido · "Comunicadora social. Planea el contenido de cada marca, maneja su comunidad y cuida que cada publicación conecte con su público."
- Título: "Dos amigos desde la guardería, un mismo equipo." Historia: "Camilo + Sebastián = CaSe Studio." / "Uno lo diseña, el otro lo hace vender. Así nació CaSe Studio y así trabajamos con cada cliente."
- Hero: "Portafolio · Medellín" · "Webs que trabajan para tu negocio." · "Disponibles para nuevos proyectos"

## Servicios
Web: Sitios corporativos · Tiendas en línea · Landing pages de ventas · Menús y pedidos · Sitios bilingües · Mantenimiento
Redes: Manejo de redes sociales · Fotografía de producto · Parrilla de contenido · Community manager
Proceso: Conversamos · Diseñamos · Construimos · Lanzamos

## Marcas en redes (6)
Weed Honey (IG+TikTok @weedhoney.co) · Agilcash (IG+TikTok @agilcash.co) · La Miguería (IG @lamigueria, +280 mil seguidores)
· Speedo Colombia (IG @speedocolombia, +70 mil) · O'Neill Colombia (IG @oneillcolombia) · Graduados EAFIT (IG @graduadoseafit, +70.000 egresados)
Los datos completos (tag, lead, lo que hicimos, colores) están en parts/k05-portfolio.html (window.BRANDS).

## Proyectos web (5 en la referencia; NeuralNet no aparece aparte)
NeuralBI (tech) · Mimarte (ecom) · AKUA Residencia (real) · Weed Honey (ecom) · Los Duches (food). Datos en window.PROJECTS.

## Plan de esta ronda (11-nov, mañana)
1. Previews automáticos por tarjeta (tiras capturadas de los sitios, auto-scroll; video si el usuario pasa los MP4) y visor:
   en dominio real iframe navegable, en el artifact captura desplazable + ficha del proyecto.
2. Marcas de redes en el área de portafolio, distinto por tema (orden 2.5).
3. Formularios con opciones para elegir (servicios reales) en vez de describir, distinto por tema.
4. Frase final con motion tipo hero (después del formulario): "Camilo + Sebastián = CaSe Studio." / "Uno lo diseña, el otro lo hace vender."
5. Footers distintos por tema.

## Estado (11-nov, ~10:40)
- HECHO: assets/tour-<id>.webp (tiras de 4 pantallas reales + 1) y pf-<id>.jpg nuevos; k05 con PROJECTS (ficha real), BRANDS, tourHTML/Tours, Viewer(i, from, list) con ficha; tours en las cinco secciones de proyectos.
- HECHO: parts/k12-brands.html (orden 2.5): Cristal lista+placa, Lámina sellos, Señal cintas, Tarjetas abanico, Tabla fichas.
- Validado en example.com: se dejan embeber Los Duches, NeuralNet, NeuralBI, AKUA y Mimarte; Weed Honey NO (CSP frame-ancestors 'none').
- PENDIENTE: parts/k11-finale.html (formularios con opciones, frase final Camilo + Sebastián = CaSe Studio, footers), harness (FINALE), auditoría, publicar con assets nuevos (tour-*.webp, pf-*.jpg).
- Publicado por última vez: versión 1794372823-fd4b (sin nada de esta ronda).

## Estado (11-nov, ~10:15 Bogotá) — PUBLICADO versión 1794409886-db02 (14 archivos propios)
- parts/k11-finale.html: formularios con opciones (Ask + FORMS por tema), frase final (tpl-ou, initOutro), footers (FOOT), window.FINALE(id, root, ct) llamado desde zz-harness.
- parts/k12-brands.html: sección #marcas (orden 2.5), un modo por tema.
- Orden por tema: hero, servicios, rediseño, proyectos, marcas, proceso, redes, cierre, contacto, frase final, footer (10 secciones + footer).
- Auditoría limpia en 1440, 390 y movimiento reducido (solo w2-w:18 conocido).
- Pendiente del usuario: los 5 MP4 del otro artifact (para cambiar tiras por video), correo/WhatsApp reales, si NeuralNet sigue como sexto proyecto, si quiere los nombres Camilo + Sebastián en la frase final, cabecera frame-ancestors de weedhoney.co.
- Herramientas: /tmp/cap.py (hojas de contacto por selector y progreso), /tmp/fm.py (llenar y enviar formularios), /tmp/vw.py (visor), /tmp/audit.py.

## Estado (11-nov, ~10:45 Bogotá) — PUBLICADO versión 1794411641-5199
- h02-cristal: el cristal del hero pasa por cinco formas (cuarzo, brillante, octaedro, cubo, icosaedro): FORMS, POS/NOR por forma, aA2/aN2 + uK en el shader, HOLD 4.4 s, MOVE 3 s. Copia anterior en old/h02-cristal-v-single-form.html.
- k13-fluid.html: máscaras en los brillos de cada stick, luz de unión entre secciones (--join en .v-cris/.v-tab/.v-tarj/.v-senal), Señal con base gris y azul como campo de luz, Tarjetas con proceso como tarjeta grande, Lámina con láminas enmarcadas.
- k14-footers.html: window.FOOT / FOOT_INIT. Cristal = nombre de vidrio en el horizonte (ref. Resend); Lámina = columnas + grabado del lago (ref. Blue Heritage); Señal = panel oscuro con la marca en el borde (ref. golf); Tarjetas = bento de tarjetas; Tabla = la tabla periódica como paisaje (ref. paisaje).
- k15-forms2.html: pasos numerados + panel vivo a la izquierda (Cristal anotaciones, Lámina talón, Señal barras de señal, Tarjetas mano en cascada, Tabla fórmula grande).
- Herramientas nuevas: /tmp/seams.py (todas las fronteras entre secciones), /tmp/hero.py (cristal en tiempos fijos), /tmp/ovf.py.
- Auditoría limpia en 1440, 390 y movimiento reducido.

## Estado (11-nov, ~11:30 Bogotá) — PUBLICADO versión 1794414494-3817
- Pedido nuevo del usuario: cambios de color por sección según el tema con transición atada al scroll (Lámina con una sección azul, Señal con secciones blancas) y quitar líneas divisoras (era .sv-rail, la barra de avance al pie de Servicios; eliminada en build.py y k00-common).
- parts/k16-tones.html: bordes de color (.edge, hermanos entre secciones; TONE por tema) + envoltorio de window.FINALE.
  Cristal = facetas SVG (marcas azul #1a55f2, proceso blanco #f5f8ff + palabra gigante .pl-big que se llena); Lámina = marea de tinta en semitono (canvas; marcas azul #1a5cf0);
  Señal = domo de luz con anillos (gradientes CSS; servicios, marcas y redes en blanco); Tabla = mosaico con silueta de tabla periódica y fichas Ca/Se (canvas; proceso blanco, cierre azul #1b55e8);
  Tarjetas = la tarjeta crece (.grows, --g) en proceso y cierre (cierre ahora azul).
- k13: brillos de unión con --jb/--jt (clases .tone, .tone-b0, .tone-t0 los apagan junto a un borde).
- Proceso real en los cinco temas (Conversamos, Diseñamos, Construimos, Lanzamos; STEPS en k06 y DK_ITEMS en build.py). Frases sin respaldo cambiadas por las de su página (hero Señal, hero Tarjetas, cierre Tarjetas).
- Hero Señal sin tramo vacío (tiempos .06–.46 / .12–.3 / .27–.52). Hero Cristal: guías dentro del marco, sin la línea inferior. Footer Tarjetas en celular: contacto y equipo a lo ancho.
- Herramientas: /tmp/edges.py OUT W H tema [tile] (cada borde en 5 posiciones), /tmp/one.py (un cuadro a tamaño real), /tmp/lines.py temas… (busca líneas horizontales de lado a lado), /tmp/map.py, /tmp/css.py.
- Oportunidades anotadas sin hacer: Servicios comparte estructura en Cristal/Lámina/Tarjetas; estado vacío del panel del formulario en Tarjetas y Tabla; menú fijo con sección activa (el nav solo vive en el hero); sección Nosotros; ES/EN.

## Estado (11-nov, ~11:40 Bogotá) — PUBLICADO versión 1794415010-d839
- k16-tones.html también lleva: Servicios distinto por tema (Tarjetas = 4 tarjetas 2×2 con la activa azul; Lámina = lámina al centro con los cuatro nombres alrededor, solo ≥861 px y sin movimiento reducido; Cristal sin la línea superior del marco),
  lámina de cierre de Lámina sin bordes rectos (máscara arriba y abajo, sin contorno), guías del hero Cristal dentro del marco.
- k15: estados vacíos del panel del formulario (Tarjetas = tres cartas fantasma en cascada; Tabla = "? + ? → Tm", arreglado last = null).
- Auditoría limpia (1440, 390, movimiento reducido); /tmp/lines.py sin líneas de lado a lado en ningún tema.
- Textos por confirmar con el usuario: Anuncios y Marca como servicios; descripciones de servicios con "cada semana" / "reporte semanal"; botón "Agendar llamada" lleva a un formulario (no hay agenda).
- Oportunidades sin hacer: menú fijo con sección activa; sección Nosotros; ES/EN; Servicios de Lámina en celular sigue siendo lista; variar la composición de Rediseño (misma estructura en los cinco).

## Estado (11-nov, ~12:50 Bogotá) — ronda 4 en curso (pedido: "Anuncios no, marca sí"; mejorar efectos del calendario de redes; cambiar texto de Agendar llamada; implementar TODAS las oportunidades: menú fijo, Nosotros, ES/EN, distinto por tema)
- HECHO: sin Anuncios en ningún tema; Marca como servicio (SV_ITEMS en build.py con dibujo nuevo en k00-common DRAW[3]; Tabla 4 fichas "Cuatro elementos"; Señal 4 palabras; hero Tarjetas con tarjeta "Tiendas en línea"; redes 6.º ítem = "Publicación"; formulario con grupo Marca → "Logo e identidad"; footer svc con "Marca e identidad").
- HECHO: botón "Empezar mi proyecto" en todos lados (antes Agendar llamada).
- HECHO: parts/k17-about.html (sección #nosotros, orden 4.5, window.TEAM): Cristal facetas, Lámina láminas-retrato en semitono, Señal tres señales con anillos, Tarjetas tarjetas que se reparten, Tabla recorrido de cámara por la tabla periódica (Ca, Se, Cv). Ahora son 11 secciones por tema.
- HECHO: parts/k18-menu.html (window.MENU, envuelve FINALE): Cristal riel de nodos + píldora; Lámina folio con índice desplegable; Señal píldora con barras de señal; Tarjetas tarjeta de pestañas con resaltado que se desliza; Tabla columna de elementos (fila arriba en celular). Botones ES/EN llaman window.LANG.set(code); sin window.LANG se ocultan (.no-lang).
- HECHO: calendario de Lámina (k08, sección sl): se imprime, se sellan piezas, anillos de reels, versiones IA, burbujas de comunidad, cursor "Hoy" que recorre el mes; mini calendario (.so-cal) con aparición y anillo de hoy.
- PENDIENTE: i18n ES/EN (parts/k19-i18n.html: diccionario + traducción del DOM al montar + MutationObserver; window.LANG = {cur, set}); verificar; publicar. Auditoría: patrón limpio ahora con "sections": 11.

## Estado (11-nov, ~13:00 Bogotá) — PUBLICADO versión 1794419799-7f1d (ronda 4 completa)
- i18n: web2/i18n/en.py (diccionario ES→EN, 341 pares) + web2/i18n/make.py genera parts/k19-i18n.html (¡regenerar con `python3 i18n/make.py` antes de build.py si cambia el diccionario!).
  window.LANG = {cur, set(code)}; window.I18N = {node, tr}; traduce el DOM antes de que arranquen las secciones (hook en zz-harness: I18N.node(root) y window.REMOUNT), los datos en sitio (PROJECTS, BRANDS, TEAM, STEPS, SOCIAL, NEEDS, WHEN) y lo que se escriba después (MutationObserver + RULES para frases armadas). Vuelve a la misma sección tras cambiar de idioma.
  Botones [data-lang] en el nav del hero (build.py nav → .nav__lang) y en cada menú fijo. Textos en CSS: reglas html[lang="en"]. Palabras del cierre: OU_SAY en k11. Canvas "Hablemos"/"Let's talk" en k07.
- Texto nuevo en español → agregar su par a i18n/en.py; comprobar con /tmp/left.py (lista lo que queda en español en EN) y /tmp/back.py (ida y vuelta).
- /tmp/cap.py acepta LANGX=en en el entorno para capturar en inglés. Auditoría: patrón limpio con "sections": 11.
- Pendiente del usuario: fotos del equipo para Nosotros (hoy monogramas Ca/Se/Cv); correo y WhatsApp reales; cuentas propias de redes; MP4 de los previews; fuente final; qué presentación de cada sección va al sitio final.
- Ideas sin hacer: variar la composición de Rediseño por tema; Servicios de Lámina en celular sigue como lista; etiqueta del riel de Cristal se cruza con las anotaciones del formulario.

## Estado (11-nov, ~14:40 Bogotá) — PUBLICADO versión 1794425914-cb9a
- Queja del usuario: el menú de Cristal (riel) quedaba encima del texto de las secciones (captura en Rediseño, ventana ~1110 px).
- Arreglo en k18-menu.html: el riel de Cristal vive en el margen (left = gutter/2), nombres plegados (panel de vidrio al pasar el cursor o con foco), nombre de la sección actual en vertical (.mn-vert);
  .v-cris{--gutter:clamp(30px,3.4vw,54px)} en ≥861 px para darle carril; en celular no hay riel: la píldora dice la sección (.mn-here, botón) y abre la lista.
  Tabla: menú = fila de elementos arriba en todos los anchos (antes columna a la derecha, tapaba contenido). Tarjetas: .st-stick con padding-top y tarjetas que se encogen en ventanas bajas.
- Herramienta nueva: /tmp/hit.py temas… (texto que queda debajo del menú a 1110, 1440, 1920 y 390; "stays under" = fijo ≥3 pasos). Único resto: la frase .sr-only del cierre (falso positivo).
