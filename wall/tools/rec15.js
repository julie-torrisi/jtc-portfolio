const { chromium } = require('playwright');
(async()=>{const b=await chromium.launch();
const ctx=await b.newContext({viewport:{width:1920,height:1080},recordVideo:{dir:'/tmp/vid15',size:{width:1920,height:1080}}});
const p=await ctx.newPage();const errs=[];p.on('pageerror',e=>errs.push(e.message));
await p.goto('http://localhost:8765/wall/'+(process.argv[2]||'v12.html'),{waitUntil:'load'});
await p.waitForTimeout(33000);console.log(JSON.stringify(await p.evaluate(()=>window.__components)));console.log(errs.join('\n'));await ctx.close();await b.close();})();
