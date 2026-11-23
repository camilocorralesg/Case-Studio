/* /llms-full.txt: everything the site says, in one Markdown file, for assistants */
import type { APIRoute } from 'astro';
import { completo } from '../datos/llms';

export const GET: APIRoute = ({ site }) =>
  new Response(completo((site ?? new URL('https://www.casestudio.com.co')).href), { headers: { 'Content-Type': 'text/plain; charset=utf-8' } });
