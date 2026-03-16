// checkout.uz CORS Proxy — Node.js (Render.com uchun)
// render.com ga deploy qilish uchun

const express = require('express');
const fetch   = require('node-fetch');
const app     = express();

app.use(express.json());
app.use((req, res, next) => {
  res.header('Access-Control-Allow-Origin', '*');
  res.header('Access-Control-Allow-Headers', 'Content-Type, Authorization');
  if (req.method === 'OPTIONS') return res.sendStatus(200);
  next();
});

app.all('/*', async (req, res) => {
  const url  = 'https://checkout.uz' + req.path + (req.url.includes('?') ? req.url.slice(req.url.indexOf('?')) : '');
  const opts = { method: req.method, headers: req.headers };
  if (req.method !== 'GET') opts.body = JSON.stringify(req.body);
  delete opts.headers.host;
  const r    = await fetch(url, opts);
  const data = await r.json();
  res.status(r.status).json(data);
});

app.listen(process.env.PORT || 3000, () => console.log('Proxy ishga tushdi!'));
