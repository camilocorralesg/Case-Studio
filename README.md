# CaSe Studio

El sitio de CaSe Studio: sitios web, tiendas en línea, redes sociales y marca, hechos en Medellín por un mismo equipo.

Es una sola página, en español e inglés, construida alrededor de la tabla periódica: el nombre del estudio sale de **Ca**milo y **Se**bastián, que también son calcio y selenio.

Está hecho con [Astro](https://astro.build): un sitio estático que no le manda al navegador más JavaScript que el de sus propias animaciones.

## Verlo

```
npm install
npm run dev          # http://localhost:4321, se recarga al guardar
```

## Cambiarlo

Cada sección vive en un archivo de `src/partes/`. Antes de dar un cambio por bueno:

```
pip install -r herramientas/requirements.txt
python -m playwright install chromium
npm run revisar      # arma el sitio y corre las cinco revisiones
```

`npm run build` deja el sitio listo para publicar en `dist/`.

## Qué hay aquí

| Carpeta | Contenido |
|---|---|
| `src/` | El sitio: la página, sus partes, el layout, piezas pequeñas y el diccionario de inglés |
| `public/assets/` | Imágenes de los proyectos |
| `herramientas/` | Revisiones automáticas y capturas |
| `docs/` | Estado del proyecto, cómo está armado y el contenido real |
| `marca/` | Logos finalistas y la exploración de logos |
| `archivo/` | Las cinco propuestas de diseño que se exploraron, la bitácora y el sitio armado con Python que se usó hasta noviembre de 2026 |

Para trabajar con Claude Code, el contexto y las reglas están en `CLAUDE.md`.
