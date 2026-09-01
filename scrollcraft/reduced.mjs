import { chromium } from 'playwright-core';
import { mkdirSync } from 'node:fs';
mkdirSync('lab/reduced', { recursive: true });
const b = await chromium.launch({ executablePath: '/opt/pw-browsers/chromium-1194/chrome-linux/chrome', args:['--no-sandbox'] });
const p = await b.newPage({ viewport: { width: 1440, height: 900 }, reducedMotion: 'reduce' });
await p.goto('http://localhost:4500/index-v2.html', { waitUntil: 'networkidle' });
await p.waitForTimeout(1200);
const docH = await p.evaluate(() => document.documentElement.scrollHeight);
for (const [n, f] of [['top',0],['peak',0.35],['close',0.88]]) {
  await p.evaluate(v => window.scrollTo({top:v, behavior:'instant'}), Math.round((docH-900)*f));
  await p.waitForTimeout(500);
  await p.screenshot({ path: `lab/reduced/${n}.png` });
}
console.log('traza:', await p.evaluate(() => document.getElementById('trace-n').textContent),
            '| mensajes visibles:', await p.evaluate(() => document.querySelectorAll('.msg.on').length));
await b.close();
