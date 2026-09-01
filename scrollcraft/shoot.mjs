// Camina la página a cada posición de scroll y reporta lo que un screenshot
// suelto no puede ver: scroll muerto, cues que nunca llegan a opacidad plena.
import { chromium } from 'playwright-core';
import { mkdirSync } from 'node:fs';

const URL = process.argv[2] || 'http://localhost:4500/index-v2.html';
const OUT = process.argv[3] || 'lab/shots';
const W = Number(process.argv[4] || 1440);
const H = Number(process.argv[5] || 900);

mkdirSync(OUT, { recursive: true });

const browser = await chromium.launch({ executablePath: '/opt/pw-browsers/chromium-1194/chrome-linux/chrome', args: ['--no-sandbox'] });
const page = await browser.newPage({ viewport: { width: W, height: H }, deviceScaleFactor: 1 });

const errors = [];
page.on('pageerror', e => errors.push('pageerror: ' + e.message));
page.on('console', m => { if (m.type() === 'error') errors.push('console: ' + m.text()); });

await page.goto(URL, { waitUntil: 'networkidle' });
await page.waitForTimeout(900);

const docH = await page.evaluate(() => document.documentElement.scrollHeight);
const vh = H;
console.log(`doc=${docH}px  ~${(docH / vh).toFixed(1)} viewport-heights  viewport=${W}x${H}`);

const STEPS = Number(process.env.STEPS || 26);
const hashes = [];

for (let i = 0; i < STEPS; i++) {
  const y = Math.round((docH - vh) * (i / (STEPS - 1)));
  await page.evaluate(v => window.scrollTo({ top: v, behavior: 'instant' }), y);
  await page.waitForTimeout(320);
  const shot = await page.screenshot({ path: `${OUT}/${String(i).padStart(2, '0')}.png` });
  // hash barato para detectar scroll muerto
  let h = 0;
  for (let b = 0; b < shot.length; b += 997) h = (h * 31 + shot[b]) >>> 0;
  hashes.push({ i, y, h, size: shot.length });
}

// scroll muerto: dos posiciones consecutivas con el mismo aspecto
const dead = [];
for (let i = 1; i < hashes.length; i++) {
  if (hashes[i].h === hashes[i - 1].h && Math.abs(hashes[i].size - hashes[i - 1].size) < 400) {
    dead.push(`${hashes[i - 1].y}px → ${hashes[i].y}px`);
  }
}

// cues que nunca alcanzan opacidad plena en ninguna posición
const cueMax = {};
for (let i = 0; i < STEPS; i++) {
  const y = Math.round((docH - vh) * (i / (STEPS - 1)));
  await page.evaluate(v => window.scrollTo({ top: v, behavior: 'instant' }), y);
  await page.waitForTimeout(90);
  const cues = await page.evaluate(() =>
    [...document.querySelectorAll('[data-sc-cue]')].map((el, n) => ({
      k: (el.dataset.scCue + ' · ' + (el.closest('section')?.id || '?') + '#' + n),
      o: parseFloat(getComputedStyle(el).opacity || '1')
    }))
  );
  cues.forEach(c => { cueMax[c.k] = Math.max(cueMax[c.k] ?? 0, c.o); });
}
const faded = Object.entries(cueMax).filter(([, o]) => o < 0.9);

// contraste del texto pequeño más crítico, medido sobre la página compuesta
await page.evaluate(() => window.scrollTo(0, 0));
const traceCount = await page.evaluate(() => {
  window.scrollTo({ top: document.documentElement.scrollHeight, behavior: 'instant' });
  return new Promise(r => setTimeout(() => r(document.getElementById('trace-n')?.textContent), 800));
});

console.log('\n--- scroll muerto ---');
console.log(dead.length ? dead.join('\n') : 'ninguno');
console.log('\n--- cues que nunca llegan a opacidad plena ---');
console.log(faded.length ? faded.map(([k, o]) => `${o.toFixed(2)}  ${k}`).join('\n') : 'ninguno');
console.log('\n--- traza al final del recorrido ---');
console.log(`${traceCount} acciones registradas`);
console.log('\n--- errores ---');
console.log(errors.length ? [...new Set(errors)].join('\n') : 'ninguno');

await browser.close();
