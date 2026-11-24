/* The site told in Markdown, for the assistants that read llms.txt (the short index) and llms-full.txt (everything).
   The words are the sections' own, from contenido.json; nothing is added that the site does not say. */
import S from './sitio.json';
import C from './contenido.json';

const seguido = (partes: string[]) => partes.map((p) => (/[.?!]$/.test(p) ? p : p + '.')).join(' ');
const wa = `https://wa.me/${S.whatsapp}`;
const cabeza = (base: string) => [`# ${S.nombre}`, '', `> ${S.resumen}`, '', `- Sitio: ${base}`, `- WhatsApp: [${S.whatsappVisible}](${wa})`, `- Correo: [${S.correo}](mailto:${S.correo})`, `- Lugar: ${S.ciudad}, Colombia`, '- Idiomas del sitio: español e inglés', ''];

export function corto(base: string) {
  const en = (ancla: string) => `${base}#${ancla}`;
  return [
    ...cabeza(base),
    '## Servicios',
    '',
    ...C.servicios.lista.map((s) => `- [${s.nombre}](${en('servicios')}): ${s.texto}`),
    '',
    '## Proyectos',
    '',
    ...C.proyectos.lista.map((p) => `- [${p.nombre}](${p.url}): ${p.tipo}. ${p.texto}`),
    '',
    '## Marcas con las que ha trabajado en redes',
    '',
    ...C.marcas.lista.map((m) => `- [${m.nombre}](${m.redes[0].url}): ${m.frase}`),
    '',
    '## Cómo trabaja',
    '',
    ...C.proceso.lista.map((p, i) => `- [${i + 1}. ${p.nombre}](${en('proceso')}): ${p.texto}`),
    '',
    '## Contacto',
    '',
    `- [${C.contacto.titular}](${en('contacto')}): ${C.contacto.apoyo}`,
    `- [WhatsApp ${S.whatsappVisible}](${wa}): todas las solicitudes llegan aquí`,
    `- [${S.correo}](mailto:${S.correo}): el correo del estudio`,
    '',
    '## Optional',
    '',
    `- [Todo el contenido del sitio](${base}llms-full.txt): servicios, proyectos, marcas, proceso, manejo de redes y preguntas, completos`,
    ''
  ].join('\n');
}

export function completo(base: string) {
  return [
    ...cabeza(base),
    `${C.hero.titular} ${C.hero.apoyo} ${C.hero.frase}`,
    '',
    '## Servicios',
    '',
    `${C.servicios.titular} ${C.servicios.apoyo}`,
    '',
    ...C.servicios.lista.flatMap((s) => [`### ${s.nombre}`, '', s.texto, '']),
    '## Rediseño',
    '',
    `${C.rediseno.titular} ${C.rediseno.apoyo}`,
    '',
    '## Proyectos',
    '',
    'Sitios hechos por el estudio.',
    '',
    ...C.proyectos.lista.flatMap((p) => [
      `### ${p.nombre}`,
      '',
      `- Tipo: ${p.tipo}`,
      `- Sitio: ${p.url}`,
      `- ${p.datos.join(' · ')}`,
      '',
      p.texto,
      '',
      'Lo que construimos:',
      '',
      ...p.hecho.map((h) => `- ${h}`),
      ''
    ]),
    `## ${C.marcas.titular}`,
    '',
    C.marcas.apoyo,
    '',
    ...C.marcas.lista.flatMap((m) => [
      `### ${m.nombre}`,
      '',
      ...m.redes.map((r) => `- ${r.red}: [${r.cuenta}](${r.url})`),
      '',
      m.texto,
      '',
      'Lo que hicimos:',
      '',
      ...m.hecho.map((h) => `- ${h}`),
      ''
    ]),
    `## ${C.proceso.titular}`,
    '',
    ...C.proceso.lista.map((p, i) => `${i + 1}. **${p.nombre}.** ${p.texto}`),
    '',
    `## ${C.redes.titular}`,
    '',
    C.redes.apoyo,
    '',
    ...C.redes.lista.map((r) => `- **${r.nombre}.** ${r.texto}`),
    '',
    `## ${C.preguntas.titular}`,
    '',
    ...C.preguntas.lista.flatMap((q) => [`### ${q.pregunta}`, '', seguido(q.respuesta), '']),
    '## Contacto',
    '',
    `${C.contacto.titular}. ${C.contacto.apoyo}`,
    '',
    `Formulario: ${base}#contacto (abre WhatsApp con la solicitud)`,
    `WhatsApp: [${S.whatsappVisible}](${wa})`,
    `Correo: [${S.correo}](mailto:${S.correo})`,
    ''
  ].join('\n');
}
