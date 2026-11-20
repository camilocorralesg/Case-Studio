# Archivo

Lo que hubo antes de quedarse con Tabla.

## Las cinco propuestas

Antes de elegir, se construyeron cinco versiones completas del sitio, cada una con su propia idea visual:

| Propuesta | Idea |
|---|---|
| Cristal | Un cristal hecho de puntos de luz dentro de un marco de plano |
| Lámina | Una lámina impresa en dos tintas azules que cobra vida |
| Señal | Un campo de luz azul y letras que se ordenan |
| Tarjetas | Los servicios como cartas sobre fondo blanco |
| Tabla | La tabla periódica. **La elegida** |

- **Para verlas funcionando**: están guardadas en el artefacto "CaSe Studio" de claude.ai, con un selector para pasar de una a otra: https://claude.ai/artifact/4tPRvLJSuVAznqVdKRAMwD
- **Sus fuentes**: `prototipo-cinco-temas.zip`. Adentro, `build.py` arma `index.html` a partir de `parts/`. Es el mismo sistema de este repositorio antes de separar Tabla.

De ahí se puede rescatar una idea de otra propuesta, pero no se trabaja sobre ese código.

## La bitácora

`bitacora-del-prototipo.md` son las notas de trabajo de las rondas en que se construyeron las cinco propuestas: qué pidió el usuario en cada una, qué se decidió y por qué. Sirve para entender de dónde viene una decisión. Describe el prototipo de cinco temas, no el estado actual: para eso está `docs/estado.md`.

## Secciones que se quitaron

`secciones-quitadas/` guarda las partes que estuvieron en el sitio de Tabla y el usuario decidió quitar. Están tal como quedaron el día que salieron; para volver a usar una, se copia a `src/partes/` y se suma a `src/pages/index.astro` y al menú (`src/partes/menu.astro`).

| Parte | Qué era | Se quitó |
|---|---|---|
| `nosotros.astro` | Nosotros: la cámara recorre una tabla y se detiene en Ca, Se y Cv, con el texto de cada uno. Define `window.TEAM` | 13 de noviembre de 2026 |
