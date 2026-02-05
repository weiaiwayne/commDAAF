import puppeteer from 'puppeteer';
import { readFileSync } from 'fs';

const content = readFileSync('/root/.openclaw/workspace/projects/vibepolitics/PROJECT_SPEC.html', 'utf8');
const html = `<!DOCTYPE html>
<html>
<head>
<meta charset="utf-8">
<style>
body { font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif; line-height: 1.6; max-width: 900px; margin: 0 auto; padding: 20px; color: #333; }
h1 { color: #1a365d; border-bottom: 3px solid #3182ce; padding-bottom: 10px; }
h2 { color: #2c5282; margin-top: 2em; border-bottom: 1px solid #bee3f8; padding-bottom: 5px; }
h3 { color: #2b6cb0; }
h4 { color: #3182ce; }
table { border-collapse: collapse; width: 100%; margin: 1em 0; font-size: 0.9em; }
th, td { border: 1px solid #e2e8f0; padding: 10px 12px; text-align: left; }
th { background: #edf2f7; font-weight: 600; }
tr:nth-child(even) { background: #f7fafc; }
code { background: #edf2f7; padding: 2px 6px; border-radius: 3px; font-size: 0.9em; }
pre { background: #1a202c; color: #e2e8f0; padding: 16px; border-radius: 8px; overflow-x: auto; }
pre code { background: none; color: inherit; }
blockquote { border-left: 4px solid #3182ce; margin: 1em 0; padding-left: 1em; color: #4a5568; }
hr { border: none; border-top: 2px solid #e2e8f0; margin: 2em 0; }
strong { color: #1a202c; }
</style>
</head>
<body>${content}</body>
</html>`;

const browser = await puppeteer.launch({ headless: true, args: ['--no-sandbox'] });
const page = await browser.newPage();
await page.setContent(html, { waitUntil: 'networkidle0' });
await page.pdf({ 
  path: '/root/.openclaw/workspace/projects/vibepolitics/VibePolitics_Spec_v0.1.pdf',
  format: 'A4',
  margin: { top: '20mm', bottom: '20mm', left: '15mm', right: '15mm' },
  printBackground: true
});
await browser.close();
console.log('PDF created');
