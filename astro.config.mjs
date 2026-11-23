// @ts-check
import { defineConfig } from 'astro/config';
import { readFile, readdir, writeFile } from 'node:fs/promises';
import { fileURLToPath } from 'node:url';
import { minify } from 'terser';

/* The scripts of the page are written in the parts to be read, and Astro leaves them as they are (is:inline). Once the site is
   built, each one is made small: its comments and spaces go, and the names inside its functions get short. The names at the top
   of each script stay, because the scripts share them (toplevel: false). A script that cannot be made small stays as written. */
const aligerar = () => ({
  name: 'aligerar',
  hooks: {
    /** @param {{ dir: URL, logger: { info: (m: string) => void, warn: (m: string) => void } }} o */
    'astro:build:done': async ({ dir, logger }) => {
      const raiz = fileURLToPath(dir);
      for (const nombre of (await readdir(raiz)).filter((f) => f.endsWith('.html'))) {
        const html = await readFile(raiz + nombre, 'utf8');
        const partes = [];
        let fin = 0, antes = 0, despues = 0;
        /* only the page's own scripts: the ones with a type (the data for search engines, the modules) are left alone */
        for (const m of html.matchAll(/<script>([\s\S]*?)<\/script>/g)) {
          let corto = m[1];
          try {
            corto = (await minify(m[1], { ecma: 2020, module: false, toplevel: false, compress: { passes: 2 }, format: { comments: false } })).code ?? m[1];
          } catch (e) {
            logger.warn(`${nombre}: un script se queda como está (${e instanceof Error ? e.message : e})`);
          }
          partes.push(html.slice(fin, m.index), '<script>', corto, '</script>');
          fin = (m.index ?? 0) + m[0].length;
          antes += m[1].length; despues += corto.length;
        }
        partes.push(html.slice(fin));
        await writeFile(raiz + nombre, partes.join(''));
        logger.info(`${nombre}: scripts de ${(antes / 1024).toFixed(0)} a ${(despues / 1024).toFixed(0)} KB`);
      }
    }
  }
});

/* A static site: astro build leaves the page in dist/, ready for any static host.
   The stylesheet travels inside the page (inlineStylesheets): the first paint waits for one file, not two. */
export default defineConfig({
  site: 'https://www.casestudio.com.co',
  devToolbar: { enabled: false },
  build: { inlineStylesheets: 'always' },
  integrations: [aligerar()]
});
