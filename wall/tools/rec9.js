const { chromium } = require('playwright');
(async()=>{const b=await chromium.launch();
const ctx=await b.newContext({viewport:{width:1920,height:1080},recordVideo:{dir:'/tmp/vid',size:{width:1920,height:1080}}});
const p=await ctx.newPage();await p.goto('http://localhost:8765/wall/v9.html',{waitUntil:'load'});
await p.waitForTimeout(32000);await ctx.close();await b.close();})();
