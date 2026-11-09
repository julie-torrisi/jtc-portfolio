const { chromium } = require('playwright');
(async()=>{const b=await chromium.launch();const p=await b.newPage({viewport:{width:1920,height:1080}});
const errs=[];p.on('pageerror',e=>errs.push(e.message));p.on('console',m=>{if(m.type()!=='log')errs.push(m.text())});p.on('requestfailed',r=>errs.push('FAIL '+r.url()));
await p.goto('http://localhost:8765/wall/v9.html',{waitUntil:'load'});
const ts=(process.argv[2]||'2').split(',').map(Number);let prev=0;
for(const t of ts){await p.waitForTimeout((t-prev)*1000);prev=t;await p.screenshot({path:`/home/claude/wall/frames/v9-${t}.png`});}
console.log(JSON.stringify(await p.evaluate(()=>window.__components)));console.log(errs.join('\n'));await b.close();})();
