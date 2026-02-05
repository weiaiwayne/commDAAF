import fs from 'fs';
import puppeteer from 'puppeteer';
import { marked } from 'marked';

const inputFile = process.argv[2];
const outputFile = process.argv[3] || inputFile.replace(/\.md$/, '.pdf');

const md = fs.readFileSync(inputFile, 'utf8');
const html = `
<!DOCTYPE html>
<html>
<head>
  <meta charset="UTF-8">
  <style>
    body {
      font-family: 'Georgia', serif;
      line-height: 1.6;
      max-width: 800px;
      margin: 0 auto;
      padding: 40px;
      font-size: 11pt;
    }
    h1 { font-size: 24pt; margin-top: 0; }
    h2 { font-size: 18pt; margin-top: 24pt; }
    h3 { font-size: 14pt; margin-top: 18pt; }
    h4 { font-size: 12pt; margin-top: 14pt; }
    code { background: #f4f4f4; padding: 2px 6px; border-radius: 3px; font-size: 10pt; }
    pre { background: #f4f4f4; padding: 16px; border-radius: 4px; overflow-x: auto; }
    pre code { padding: 0; }
    blockquote { border-left: 3px solid #ccc; margin-left: 0; padding-left: 16px; color: #666; }
    table { border-collapse: collapse; width: 100%; margin: 16px 0; }
    th, td { border: 1px solid #ddd; padding: 8px; text-align: left; }
    th { background: #f4f4f4; }
  </style>
</head>
<body>
${marked(md)}
</body>
</html>
`;

const browser = await puppeteer.launch({ headless: true, args: ['--no-sandbox'] });
const page = await browser.newPage();
await page.setContent(html, { waitUntil: 'networkidle0' });
await page.pdf({ path: outputFile, format: 'A4', margin: { top: '1in', bottom: '1in', left: '1in', right: '1in' } });
await browser.close();
console.log('Created:', outputFile);
