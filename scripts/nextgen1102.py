"""11/2 · next-gen slide visual → Figma 4043:4741 (three tilted frameless screens) + no focus ring on the slide rail."""
import sys,re
src,dst=sys.argv[1:3]
t=open(src).read()
def rep(old,new):
    global t
    assert t.count(old)==1,(old[:70],t.count(old)); t=t.replace(old,new)
i=t.find('data-slide-id="next-gen"'); a=t.rfind('<section',0,i); b=t.find('</section>',i)
sec=t[a:b]
m=re.search(r'<div class="pv-devs reveal r3" style="--n:3">.*?</div></div>\n',sec,re.S)
assert m and 'rival3' in m.group(0)
fan='''<figure class="ng-fan reveal r3" aria-label="Rival comment sheets: Instagram, YouTube and TikTok.">
<div class="ng-ph" style="--x:21%;--y:51%;--r:6deg"><img src="img/rival1.webp" alt="Instagram’s comment sheet." loading="lazy" decoding="async" width="1185" height="2576"></div>
<div class="ng-ph" style="--x:49.6%;--y:51.8%;--r:-5deg"><img src="img/rival2.webp" alt="YouTube’s comment sheet." loading="lazy" decoding="async" width="1185" height="2576"></div>
<div class="ng-ph" style="--x:76.3%;--y:46.4%;--r:7deg"><img src="img/rival3.webp" alt="TikTok’s comment sheet." loading="lazy" decoding="async" width="1185" height="2576"></div>
<figcaption class="ng-caps" aria-hidden="true"><span style="--x:24.8%">Instagram</span><span style="--x:51.9%">YouTube</span><span style="--x:77.1%">TikTok</span></figcaption>
</figure>
'''
sec2=sec.replace(m.group(0),fan)
t=t[:a]+sec2+t[b:]
css='''
/* ===== 11/2 · next-gen rivals as Figma draws them (4043:4741): three frameless screens, tilted and overlapping. Tokens only. ===== */
section[data-slide-id="next-gen"] .split.pv-split { grid-template-columns: minmax(0, 698fr) minmax(0, 1079fr); }
.ng-fan { position: relative; margin: 0; width: 100%; max-height: 84svh; aspect-ratio: 1079 / 925; min-width: 0; justify-self: center; }
.ng-ph { position: absolute; left: var(--x); top: calc(var(--y) * 898 / 925); width: 33.9%; aspect-ratio: 366 / 791;
  transform: translate(-50%, -50%) rotate(var(--r)); border-radius: 11% / 5.1%; overflow: hidden; background: var(--void); box-shadow: var(--ck-elevation-2); }
.ng-ph img { display: block; width: 100%; height: 100%; object-fit: cover; object-position: top; max-width: none; }
.ng-caps { position: absolute; left: 0; right: 0; bottom: 0; height: 1.3em; }
.ng-caps span { position: absolute; left: var(--x); transform: translateX(-50%); font: 400 var(--meta)/1.3 var(--font-mono); letter-spacing: .08em; text-transform: uppercase; color: var(--mist); white-space: nowrap; }
@media (max-width: 1024px) { section[data-slide-id="next-gen"] .split.pv-split { grid-template-columns: minmax(0, 1fr); } .ng-fan { max-width: 640px; } }
/* 11/2 · slide rail: no focus ring around the pager (Julie) */
.srl .ck-pager-view:focus, .srl .ck-pager-view:focus-visible { outline: none; }
'''
j=t.find('<body'); last=t.rfind('</style>',0,j)
t=t[:last]+css+t[last:]
open(dst,'w').write(t); print('ok')
