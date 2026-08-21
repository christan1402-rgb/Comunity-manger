// Convierte un informe HTML en PDF A4 listo para enviar.
// Uso: node scripts/render-pdf.mjs informes/2026-07-29.html
import pw from '/opt/node22/lib/node_modules/playwright/index.js';
const { chromium } = pw;
import fs from 'fs';
import path from 'path';

const src = process.argv[2];
if (!src) { console.error('Uso: node scripts/render-pdf.mjs <archivo.html>'); process.exit(1); }
const abs = path.resolve(src);
if (!fs.existsSync(abs)) { console.error('No existe:', abs); process.exit(1); }
const out = abs.replace(/\.html$/, '.pdf');

const CHROME = ['/opt/pw-browsers/chromium-1194/chrome-linux/chrome',
                '/opt/pw-browsers/chromium/chrome-linux/chrome']
               .find(p => fs.existsSync(p));

const browser = await chromium.launch({
  ...(CHROME ? { executablePath: CHROME } : {}),
  args: ['--no-sandbox', '--disable-dev-shm-usage'],
});
const page = await browser.newPage({ viewport: { width: 1000, height: 1400 }, deviceScaleFactor: 2 });
await page.goto('file://' + abs, { waitUntil: 'networkidle' });
await page.pdf({ path: out, format: 'A4', printBackground: true,
                 margin: { top: 0, bottom: 0, left: 0, right: 0 } });

// Vistas previas para revisar el diseño antes de enviar.
const n = await page.locator('section.page').count();
const dir = path.join(path.dirname(abs), '.previews');
fs.mkdirSync(dir, { recursive: true });
for (let i = 0; i < n; i++) {
  await page.locator('section.page').nth(i).screenshot({ path: path.join(dir, `pg${i + 1}.png`) });
}
await browser.close();
console.log(`PDF: ${out} (${fs.statSync(out).size} bytes, ${n} páginas)`);
console.log(`Vistas previas: ${dir}/pg1..${n}.png — revísalas antes de enviar.`);
