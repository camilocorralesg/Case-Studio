/* /robots.txt: everything may be read, by search engines and by the assistants' crawlers, which are named so the choice is
   on record; and where the sitemap and the text for assistants are */
import type { APIRoute } from 'astro';

const ASISTENTES = ['GPTBot', 'OAI-SearchBot', 'ChatGPT-User', 'ClaudeBot', 'Claude-SearchBot', 'Claude-User', 'PerplexityBot', 'Perplexity-User', 'Google-Extended', 'Applebot-Extended', 'CCBot'];

export const GET: APIRoute = ({ site }) => {
  const base = (site ?? new URL('https://www.casestudio.com.co')).href;
  const texto = [
    'User-agent: *',
    'Allow: /',
    '',
    ...ASISTENTES.map((a) => `User-agent: ${a}`),
    'Allow: /',
    '',
    `Sitemap: ${base}sitemap.xml`,
    '',
    `# El sitio en texto, para asistentes: ${base}llms.txt y ${base}llms-full.txt`,
    ''
  ].join('\n');
  return new Response(texto, { headers: { 'Content-Type': 'text/plain; charset=utf-8' } });
};
