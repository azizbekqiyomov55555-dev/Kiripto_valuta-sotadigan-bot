// render.com uchun proxy server (Node.js)
// 1. render.com ga kiring
// 2. New Web Service yarating
// 3. Bu kodni index.js ga joylashtiring

const express = require("express");
const fetch = require("node-fetch");
const app = express();
app.use(express.json());
app.use((req,res,next)=>{
  res.header("Access-Control-Allow-Origin","*");
  res.header("Access-Control-Allow-Headers","*");
  if(req.method==="OPTIONS") return res.sendStatus(200);
  next();
});
app.all("/*",async(req,res)=>{
  const url="https://checkout.uz"+req.path;
  const r=await fetch(url,{method:req.method,headers:{...req.headers,host:"checkout.uz"},body:req.method!=="GET"?JSON.stringify(req.body):undefined});
  const d=await r.json();
  res.status(r.status).json(d);
});
app.listen(process.env.PORT||3000);
