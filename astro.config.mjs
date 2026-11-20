// @ts-check
import { defineConfig } from 'astro/config';

/* A static site: astro build leaves the page in dist/, ready for any static host */
export default defineConfig({
  devToolbar: { enabled: false },
  build: { inlineStylesheets: 'never' }
});
