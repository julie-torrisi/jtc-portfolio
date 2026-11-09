import json,os
os.chdir('/home/claude/jtc-portfolio/wall')
m=json.load(open('bp/meta.json'))
s=open('src.html').read().replace('__META__',json.dumps(m,separators=(',',':')))
open('index.html','w').write(s)
