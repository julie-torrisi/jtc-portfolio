"""11/2 · ending 36–46 from Figma 🎬 Stack · Master Deck (4003:1161). Finds slides by headline, asserts one match."""
import re,sys,html
sys.path.insert(0,'/home/claude')
from secs import top_sections, text
src,dst,arch=sys.argv[1:4]
t=open(src).read()
S=top_sections(t)
def head(a,b):
    m=re.search(r'<h[12][^>]*>(.*?)</h[12]>',t[a:b],re.S)
    return ' '.join(html.unescape(re.sub(r'<[^>]+>','',m.group(1))).split()) if m else ''
def find(prefix):
    hits=[(a,b) for a,b in S if head(a,b).startswith(prefix)]
    assert len(hits)==1,(prefix,len(hits)); return hits[0]
names={'ms':'Each milestone earned the next.','same':'Same content.','vp':'The VP of Engineering hesitated.','read':'Read the data, killed','ai':'AI and product didn’t share','four':'Four fires.','shipped':'What actually shipped.','live':'Still live in production.','pixel':'Every pixel defensible.','any':'Any discipline.','build':'Build once, ship everywhere.','fewer':'Fewer boxes.','thanks':'Thank you.'}
R={k:find(v) for k,v in names.items()}
# the block from VP (first moved) to Thank you must be contiguous top-level sections with only whitespace between
order_now=sorted(R.items(),key=lambda kv:kv[1][0])
start=R['vp'][0]; end=R['thanks'][1]
inblock=[(a,b) for a,b in S if a>=start and b<=end]
for (a,b),(c,d) in zip(inblock,inblock[1:]): assert not t[b:c].strip(),('gap',t[b:c][:80])
blk_keys=[k for k,(a,b) in order_now if a>=start]
assert set(blk_keys)=={'ms','vp','same','read','ai','four','shipped','live','pixel','any','build','fewer','thanks'},blk_keys
assert len(inblock)==len(blk_keys)
sec={k:t[a:b] for k,(a,b) in R.items()}
def rep(s,old,new,n=1):
    assert s.count(old)==n,(old[:60],s.count(old)); return s.replace(old,new)
# 36 Same content: Northstar phone → the north star SVG from Downloads (NORTHSTAR1.svg)
sec['same']=rep(sec['same'],'src="img/ns_z.webp" alt="North star comment sheet, same comments as every other milestone."','src="img/ns-northstar.svg" alt="North star comment sheet, same comments as every other milestone."')
# 37 VP: silk iris → halo (neighbour check)
sec['vp']=rep(sec['vp'],'data-silk="iris"','data-silk="halo"')
# 39 Four fires: velvet → halo (neighbour check)
sec['four']=rep(sec['four'],'<section class="slide ck-fit" data-dim=".4" data-silk="velvet"','<section class="slide ck-fit" data-dim=".4" data-silk="halo"')
# 40 Fewer boxes: Figma body + What I did; after phone → north star SVG
sec['fewer']=rep(sec['fewer'],'<p class="body reveal r3">The legacy sheet wrapped every comment in a grey bubble with its own byline and reaction row. The new sheet drops the bubbles, adds filters and pinning, and puts up and down votes on every row.</p>',
 '<p class="body reveal r3">Leadership didn’t have to take the redesign on taste. Every change traces to a job it serves: safety, clarity or control. It set the standard past comments: Feed followed the new comment action row when they simplified the action row under every post.</p>\n<p class="role in-pin reveal r3"><b>What I did</b><span>Designed every one of these changes and wrote the rationale leaders used to approve them.</span></p>')
sec['fewer']=rep(sec['fewer'],'src="img/ns_z.webp" alt="New comment sheet:','src="img/ns-northstar.svg" alt="New comment sheet:')
# 41 What actually shipped: feature row shows names only (Figma)
for sub in ['<span>73M daily views at launch · iOS test group drove 5x more pin volume than control</span>','<span>Led Phase 1 (shipped May 1, 2025), then handed off</span>']:
    sec['shipped']=rep(sec['shipped'],sub,'')
sec['shipped']=rep(sec['shipped'],'<span>Shipped</span>','',2)
# 42 Any discipline: silk iris → velvet (neighbour check)
sec['any']=rep(sec['any'],'<section class="slide" data-dim=".3" data-silk="iris">','<section class="slide" data-dim=".3" data-silk="velvet">')
# 44 NEW · Designed for comments. Adopted by Feed.
feed='''<section class="slide fd-slide" data-dim=".4" data-silk="halo" aria-label="Precedent: Feed adopted the comment action row and icons.">
<div class="split fd-split">
<div class="stack">
<p class="meta reveal">Precedent</p>
<h2 class="d-l reveal r2">Designed for comments. <span class="b">Adopted</span> by <span class="l">Feed.</span></h2>
<p class="body reveal r3">Feed took its icon modernization from the comment redesign and cut the action row under every post from as many as 4 lines to 2.</p>
<p class="role in-pin reveal r3"><b>What I did</b><span>Designed the comment action row and its icons. When Feed simplified the action row under every post, they built on my design.</span></p>
</div>
<figure class="fd-fig reveal r3">
<div class="fd-card"><img src="img/feed-post.svg" alt="A Facebook Feed post with the redesigned action row: Like, Comment, Send and Share on one line, with the comment redesign's icon style." width="375" height="222" loading="lazy" decoding="async"><ul class="mco mco-r"><li style="--y:44%">Feed<span>Took its icon style from the comments redesign.</span></li></ul></div>
<figcaption class="meta">Feed UFI redesign</figcaption>
</figure>
</div>
<div class="notes"><b>Talk track · voice-over only</b><ul><li>Feed went from as many as 4 lines to 2 under every post. Product constraints ruled out 1, so never say Feed went to one line.</li></ul></div>
</section>'''
# 45 NEW · The goal was never to just redesign comments.
goal='''<section class="slide center gl-slide" data-dim=".45" data-silk="bloom" aria-label="Result: the goal was to make great conversations the default, forever.">
<div class="stack gl-stack">
<p class="meta reveal">Result</p>
<h2 class="d-l reveal r2">The goal was never to just redesign comments. The goal was to make great conversations the default, forever.</h2>
<p class="body reveal r3">Three things I do consistently well that make great work inevitable:</p>
<ol class="gl-list reveal r3">
<li><b>Turn fragmented work into one system that ships.</b><span>Scattered teams become partners working toward the same goal.</span></li>
<li><b>Build the operating rhythm that protects the work from organizational chaos.</b><span>Decisions stay made, even when the org changes around them.</span></li>
<li><b>Make products other teams want to build on.</b><span>Adoption is a choice, not a mandate.</span></li>
</ol>
</div>
</section>'''
new_order=['ms','same','vp','read','four','fewer','shipped','any','live','FEED','GOAL','thanks']
# 'same' sits before start? it is inside the block (VP came first). Rebuild block.
parts=[]
for k in new_order:
    parts.append(feed if k=='FEED' else goal if k=='GOAL' else sec[k])
newblk='\n\n'.join(parts)
archived={k:t[R[k][0]:R[k][1]] for k in ('ai','pixel','build')}
t2=t[:start]+newblk+t[end:]
css='''
/* ===== 11/2 · Ending 36–46 from Figma "🎬 Stack · Master Deck" (Julie). Tokens only. ===== */
.baf-copy .role, .fd-slide .role { grid-template-columns: minmax(0, 1fr); gap: var(--ck-space-2); margin-top: clamp(16px, 3svh, 40px); max-width: 52ch; }
.fd-slide .split.fd-split { grid-template-columns: minmax(0, 1fr) minmax(0, 1fr); }
.fd-fig { margin: 0; display: grid; justify-items: center; gap: var(--ck-space-5); min-width: 0; }
.fd-card { position: relative; width: min(100%, clamp(280px, 25vw, 480px)); }
.fd-card > img { display: block; width: 100%; height: auto; max-width: 100%; border-radius: var(--ck-radius-s); box-shadow: var(--ck-elevation-2); }
.fd-fig figcaption { text-align: center; }
.gl-stack { justify-items: center; max-width: min(100%, 1240px); margin-inline: auto; }
.gl-slide .d-l { max-width: 28ch; text-wrap: balance; }
.gl-slide .body { max-width: none; color: var(--dusk); }
.gl-list { margin: 0; padding: 0; list-style: none; counter-reset: gl; display: grid; gap: var(--ck-space-5); }
.gl-list li { counter-increment: gl; display: grid; gap: var(--ck-space-1); font-size: var(--caption); color: var(--mist); }
.gl-list li b { font-weight: 500; color: var(--neutral-50); }
.gl-list li b::before { content: counter(gl) ". "; }
.gl-list li span { color: var(--dusk); }
@media (max-width: 1024px) { .fd-slide .split.fd-split { grid-template-columns: minmax(0, 1fr); } }
'''
i=t2.find('</style>'); j=t2.find('<body')
last=t2.rfind('</style>',0,j); assert last>0
t2=t2[:last]+css+t2[last:]
open(dst,'w').write(t2)
open(arch,'w').write('<!-- ARCHIVE · removed from the master ending, 11/2 (Julie: "any additional slides left over should be archived"). Base master v1793661108-d472. Restore by pasting a section back. -->\n'+'\n\n'.join(f'<!-- {names[k]} -->\n{v}' for k,v in archived.items()))
print('ok',len(t),'->',len(t2))
