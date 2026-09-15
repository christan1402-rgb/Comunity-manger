// Arma la guía: contenido/*.md -> guia-instructor-atraccion-digital.html -> .pdf
// Uso: node plantilla/build.mjs            (desde academia/atraccion-digital)
//      node plantilla/build.mjs --solo-html
import fs from 'node:fs';
import path from 'node:path';
import { fileURLToPath } from 'node:url';
import { marked } from 'marked';

const HERE = path.dirname(fileURLToPath(import.meta.url));
const ROOT = path.resolve(HERE, '..');
const BASE = path.join(ROOT, 'guia-instructor-atraccion-digital');
const CSS = fs.readFileSync(path.join(HERE, 'estilos.css'), 'utf8');
const FRASE = 'Te ven. Te entienden. Te reservan.';

marked.use({ gfm: true, breaks: false });

function render(mdText) {
  const pre = mdText
    .replace(/\{lineas:(\d+)\}/g, (_, n) => '<div class="wline"></div>\n'.repeat(+n))
    .replace(/\{linea\}/g, '<span class="line"></span>')
    .replace(/\{salto\}/g, '<div class="pb"></div>');
  return marked.parse(pre)
    .replace(/\[ \]/g, '<span class="cb"></span>')
    .replace(/<table>(?=\s*<thead>(?:(?!<\/thead>)[^])*?<th[^>]*>(?:Qué vi|Evidencia))/g, '<table class="obs">');
}

// Parte el markdown en trozos por encabezado (# o ##). Cada trozo conserva su nivel y título.
function chunks(src) {
  const out = [];
  let cur = { level: 0, title: '', body: [] };
  for (const ln of src.split('\n')) {
    const m = ln.match(/^(#{1,2}) (.+)$/);
    if (m) { out.push(cur); cur = { level: m[1].length, title: m[2].trim(), body: [] }; }
    else cur.body.push(ln);
  }
  out.push(cur);
  return out.filter((c) => c.level || c.body.join('').trim());
}

const slideRe = /^Diapositiva (\d+)\. (.+?) · (\d+) min$/;
const anexoRe = /^Anexo ([A-Z])\. (.+)$/;

function article(kind, kicker, title, minutes, body) {
  const min = minutes ? `<span class="min">${minutes} min</span>` : '';
  return `<article class="${kind}"><header><div class="row"><span class="k">${kicker}</span>${min}</div><h2>${title}</h2></header>${render(body)}</article>`;
}

function separator(num, title, introHtml, cols, foot = 'HERNANDEZ Academia') {
  return `<section class="dark sep${num ? '' : ' anexos'}"><div class="top"><div class="kick">${num ? 'Clase' : 'Material para imprimir'}</div><div class="num">${num || 'Anexos'}</div><h1>${title}</h1>${introHtml}</div><div class="cols">${cols}</div><div class="foot">${foot}</div></section>`;
}

function buildClass(cs) {
  const head = cs[0];
  const m = head.title.match(/^Clase (\d)\s*·\s*(.+)$/);
  if (!m) throw new Error('Encabezado de clase inválido: ' + head.title);
  const [, num, title] = m;
  const bodyHtml = render(head.body.join('\n'));
  const hilo = bodyHtml.match(/<p>Hilo:\s*(.*?)<\/p>/s);
  const rest = bodyHtml.replace(hilo ? hilo[0] : '', '').replace(/<p>Antes de empezar<\/p>/, '');
  const slides = cs.slice(1).map((c) => {
    const s = c.title.match(slideRe);
    if (!s) throw new Error('Título de diapositiva inválido: ' + c.title);
    return { n: +s[1], title: s[2], min: +s[3], body: c.body.join('\n') };
  });
  const total = slides.reduce((a, s) => a + s.min, 0);
  const idx = slides.map((s) => `<li><span>${s.n}. ${s.title}</span><span class="m">${s.min} min</span></li>`).join('');
  const cols = `<div><h3>Antes de empezar</h3>${rest}</div><div class="idx"><h3>${slides.length} diapositivas</h3><ul>${idx}</ul><div class="total"><span>Total</span><span>${total} de 120 min</span></div></div>`;
  const sep = separator(num, title, hilo ? `<p class="hilo">${hilo[1]}</p>` : '', cols);
  const body = slides.map((s) => article('slide', `Diapositiva ${s.n}`, s.title, s.min, s.body)).join('');
  return { html: sep + `<section class="doc">${body}</section>`, slides: slides.length, minutes: total, list: slides };
}

function buildIntro(cs) {
  const parts = cs.map((c) => {
    if (c.level === 1) return `<h1 class="pagetitle">${c.title}</h1>${render(c.body.join('\n'))}`;
    return `<h2>${c.title}</h2>${render(c.body.join('\n'))}`;
  });
  return `<section class="doc">${parts.join('')}</section>`;
}

function buildAnexos(cs) {
  const head = cs[0];
  const items = cs.slice(1).map((c) => {
    const a = c.title.match(anexoRe);
    if (!a) throw new Error('Título de anexo inválido: ' + c.title);
    return { letra: a[1], title: a[2], body: c.body.join('\n') };
  });
  const idx = items.map((a) => `<li><span>${a.title}</span><span class="m">${a.letra}</span></li>`).join('');
  const cols = `<div>${render(head.body.join('\n'))}</div><div class="idx"><h3>${items.length} anexos</h3><ul>${idx}</ul></div>`;
  const sub = (head.title.split('·')[1] || '').trim();
  const sep = separator(0, sub, '', cols);
  const body = items.map((a) => article('anexo', `Anexo ${a.letra}`, a.title, 0, a.body)).join('');
  return sep + `<section class="doc">${body}</section>`;
}

function cover(slides) {
  return `<section class="dark cover"><div></div><div class="mid"><img src="assets/logo-atraccion-digital.png" alt="Taller Atracción Digital"><div class="kick">Guía del instructor</div><p class="meta">4 clases · 120 minutos por clase · ${slides} diapositivas</p><h1 class="frase">${FRASE}</h1></div><div class="foot"><span class="g">HERNANDEZ Academia</span><span class="w">Somos el estándar</span></div></section>`;
}

const dir = path.join(ROOT, 'contenido');
const files = fs.readdirSync(dir).filter((f) => f.endsWith('.md')).sort();
let body = '', slides = 0, intro = '';
const resumen = [], mapa = [];
for (const f of files) {
  const cs = chunks(fs.readFileSync(path.join(dir, f), 'utf8'));
  if (/^Clase /.test(cs[0].title)) {
    const r = buildClass(cs); body += r.html; slides += r.slides;
    resumen.push(`${f}: ${r.slides} diapositivas, ${r.minutes} min`);
    mapa.push({ num: cs[0].title.match(/^Clase (\d)/)[1], title: cs[0].title.split('·')[1].trim(), slides: r.list, minutes: r.minutes });
  }
  else if (/^Anexos/.test(cs[0].title)) body += buildAnexos(cs);
  else intro = buildIntro(cs);
}
const mapaHtml = mapa.map((c) => `<div><h3>Clase ${c.num} · ${c.title}</h3><table class="mapa"><tbody>${c.slides.map((s) => `<tr><td class="n">${s.n}</td><td>${s.title}</td><td class="c">${s.min} min</td></tr>`).join('')}<tr class="tot"><td></td><td>Total</td><td class="c">${c.minutes} min</td></tr></tbody></table></div>`).join('');
intro = intro.replace('</section>', `<h2>Mapa de las ${slides} diapositivas</h2><p>Los títulos son los de cada diapositiva. Sirven para armar las láminas después: lo que se proyecta es el título, lo que se dice está en cada nota.</p><div class="mapa2">${mapaHtml}</div></section>`);
body = intro + body;
const html = `<!doctype html>
<html lang="es"><head><meta charset="utf-8"><title>Guía del instructor · Taller Atracción Digital</title>
<style>${CSS}</style></head><body>${cover(slides)}${body}</body></html>`;
fs.writeFileSync(BASE + '.html', html);
console.log(resumen.join('\n'));
console.log(`HTML: ${BASE}.html (${slides} diapositivas)`);

if (process.argv.includes('--solo-html')) process.exit(0);

const pwMod = await import('/opt/node22/lib/node_modules/playwright/index.js').catch(() => import('playwright'));
const pw = pwMod.chromium ? pwMod : pwMod.default;
const CHROME = ['/opt/pw-browsers/chromium-1194/chrome-linux/chrome', '/opt/pw-browsers/chromium/chrome-linux/chrome'].find((p) => fs.existsSync(p));
const browser = await pw.chromium.launch({ ...(CHROME ? { executablePath: CHROME } : {}), args: ['--no-sandbox', '--disable-dev-shm-usage'] });
const page = await browser.newPage();
await page.goto('file://' + BASE + '.html', { waitUntil: 'networkidle' });
await page.evaluate(() => document.fonts.ready);
await page.pdf({ path: BASE + '.pdf', preferCSSPageSize: true, printBackground: true });
await browser.close();
console.log(`PDF: ${BASE}.pdf (${(fs.statSync(BASE + '.pdf').size / 1024).toFixed(0)} KB)`);
