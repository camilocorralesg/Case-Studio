# Herramientas

Revisan el sitio en un navegador de verdad (Chromium, con Playwright) y dejan capturas en `herramientas/salida/`.
Revisan `dist/`, lo que deja `npm run build`. Si nadie lo está sirviendo, lo sirven ellas mismas en el puerto 8765.

## Preparar

```
pip install -r herramientas/requirements.txt
python -m playwright install chromium
```

## La revisión completa

```
python herramientas/revisar.py            arma el sitio (npm run build) y corre las seis revisiones a la vez (también: npm run revisar)
python herramientas/revisar.py --sin-armar
```

Tarda entre uno y tres minutos y termina con un resumen. Cada revisión también se puede correr sola:

| Herramienta | Qué mira | Limpio es |
|---|---|---|
| `auditar.py` | A 1440, a 390 y con movimiento reducido: ids repetidos, un solo h1, nombres accesibles, alt, desborde horizontal, toques pequeños en celular, enlaces rotos, 11 secciones, errores de consola | `AUDITORÍA LIMPIA` |
| `lineas.py` | Líneas horizontales que cruzan toda la pantalla mientras se recorre el sitio, y sombras o luces cortadas en el borde entre dos secciones del mismo color | `LÍNEAS LIMPIO` |
| `bajo_menu.py` | Texto que se queda debajo del menú fijo a 1110, 1440, 1920 y 390 | `MENÚ LIMPIO` |
| `ida_y_vuelta.py` | Pasar a inglés y volver: misma sección, título traducido, nada en inglés al volver | `IDA Y VUELTA BIEN` |
| `idioma.py` | Lo que sigue en español con el sitio en inglés | `INGLÉS COMPLETO` |
| `contenido.py --comprobar` | Que `src/datos/contenido.json`, la copia de lo que dicen las secciones, esté al día. De ella salen el contenido sin JavaScript, los datos estructurados y `llms.txt` | `CONTENIDO AL DÍA` |

## El contenido para buscadores y asistentes

```
npm run contenido        arma, copia lo que dice el sitio a src/datos/contenido.json y vuelve a armar
```

Se corre después de cambiar un texto del sitio. El archivo no se edita a mano: el contenido se escribe una sola vez, en las partes.

## Cómo carga

```
python herramientas/carga.py                         tres cargas en un celular lento: primera pintura, pintura más grande, índice de velocidad, tareas largas y lo que se pidió por la red
python herramientas/carga.py --hoja carga.png        además, la película de la carga en salida/
python herramientas/carga.py --dist otra/carpeta     mide otro armado, para comparar antes y después
python herramientas/carga.py --computador --sin-freno
```

Imita lo que mide PageSpeed (un Moto G Power, 4G lenta, procesador cuatro veces más lento). Los números cambian mucho con lo ocupado que esté el equipo: para comparar un cambio se alternan el armado de antes y el de ahora. Los oficiales son los de PageSpeed sobre el sitio publicado.

## Ilustraciones

```
python herramientas/cobalto.py src/assets/rd-pan.jpg rd-pan
```

Las ilustraciones que el usuario genera con Nano Banana llegan con un azul parecido al de la marca, pero no el mismo. `cobalto.py` mide el azul de fondo, lo lleva a #1e55e0 sin tocar lo que no es azul (el pan, la madera, el vapor) y guarda `public/assets/NOMBRE-640.webp` y `NOMBRE-1024.webp`. El original se queda en `src/assets/`.

## Capturas

```
python herramientas/capturar.py hero.png 1440 900 3 480 ".hx|0;.hx|.3;.hx|.6"
python herramientas/capturar.py celular.png 390 844 4 300 ".hx|0;#servicios|.5;#proceso|.5;#contacto|.2"
python herramientas/capturar.py quieto.png 1440 900 2 720 "#redes|.5;.zb|.5" rm
python herramientas/capturar.py ingles.png 1440 900 2 720 ".hx|0;#contacto|.2" en
```

Cada cuadro es `selector|avance`: una sección y qué tanto de ella se ha recorrido, de 0 a 1. En las que se cuentan solas (Servicios, Marcas, Redes) el avance es el punto de lo que cuentan, y quedan en pausa ahí.
Los selectores de las secciones: `.hx` (hero), `#servicios`, `#rediseno`, `#proyectos`, `#marcas`, `#proceso`, `#redes`, `.zb` (cierre), `#contacto`, `.ft` (pie).

| Herramienta | Qué deja |
|---|---|
| `capturar.py` | Hoja de contactos con los estados del scroll que se le pidan |
| `bordes.py` | Cada cambio de color en cinco momentos del scroll |
| `costuras.py` | Una miniatura por cada frontera entre secciones |
| `formularios.py` | El formulario vacío con su aviso, con dos servicios marcados y enviado |
| `visor.py` | El detalle de un proyecto y el siguiente, en escritorio y en celular |
| `perfiles.py [cuenta ...]` | La captura del perfil público de Instagram de cada marca, en español y en inglés, a 780 y a 480 px, para el teléfono de Marcas (`public/assets/ig/`). Una captura hecha a mano en `src/assets/ig/<cuenta>.png` se usa en su lugar (así entra Weed Honey, que es solo para adultos y no se ve sin sesión) |
| `publicaciones.py` | Publicaciones reales recortadas de las capturas de Marcas y pasadas a duotono cobalto, para las historias de Redes (`public/assets/redes/`). Cuáles se usan está en la lista `USADAS`; se corre otra vez después de `perfiles.py` |
| `recorridos.py [id ...] [--celular \| --computador] [--muestra]` | Las tiras de cada proyecto: recorre su sitio real como un celular (390 × 844) y como un computador (1440 × 745), a 2x, y guarda `public/assets/tour-<id>-cel-390.webp`, `-cel.webp` (585) y `-cel-780.webp`, `tour-<id>.webp` (800) y `-1600.webp`, y `pf-<id>.jpg` (la primera pantalla a 320, para las miniaturas del detalle). Cada pantalla toma el ancho que necesita (`srcset`). Desde la segunda pantalla esconde las barras fijas del sitio (su menú arriba, un botón abajo), para que no se repitan. Rechaza las cookies que no son necesarias y no envía nada, salvo la verificación de edad de Weed Honey, que pasa con la fecha de un adulto de prueba (`EDAD`, autorizado por el usuario el 16 de noviembre de 2026). Si después de eso el sitio pone un aviso arriba (`AVISO`), lo esconde sin tocarlo. Con `--muestra` deja doce pantallas de un sitio en `salida/` para escoger sus puntos a mano (`PUNTOS`); con `--muestra=24`, las que se pidan |
| `cosechar.py [en]` | La lista de todos los textos que el sitio llega a mostrar, para repasar el diccionario |
| `compartir.py [--solo-iconos]` | La imagen que sale al compartir el enlace (`public/assets/og-case-studio.jpg`, el hero de la página armada) y los iconos con la marca (`favicon.svg`, los PNG y `site.webmanifest`) |

## Variables de entorno

| Variable | Para qué |
|---|---|
| `CASE_URL` | Revisar otra dirección en vez de servir `dist/` |
| `CASE_CHROME` | Usar otro Chrome o Chromium (ruta al ejecutable) |
| `CASE_SIN_GPU=1` | Abrir el navegador sin las opciones de GPU: con el equipo muy cargado lo cuelgan, y el sitio no usa WebGL |
| `CASE_SIN_RED=1` | Ya no hace falta: las fuentes las sirve el sitio (antes evitaba pedirlas a Google) |

## Lo que las herramientas no ven

El ritmo del movimiento. Una captura es un instante: que una animación se sienta bien solo se sabe mirándola en vivo.
