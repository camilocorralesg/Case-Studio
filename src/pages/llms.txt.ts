/* /llms.txt: the short index of the site for assistants (llmstxt.org) */
import type { APIRoute } from 'astro';
import { corto } from '../datos/llms';

export const GET: APIRoute = ({ site }) =>
  new Response(corto((site ?? new URL('https://www.casestudio.com.co')).href), { headers: { 'Content-Type': 'text/plain; charset=utf-8' } });
