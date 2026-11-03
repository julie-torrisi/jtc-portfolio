"""11/2 · milestone notes show on laptop-size windows; Fewer boxes shows the real screens (no ASSET placeholders)."""
import sys,re
src,dst=sys.argv[1:3]
t=open(src).read()
def rep(old,new,n=1):
    global t
    assert t.count(old)==n,(old[:70],t.count(old)); t=t.replace(old,new)
# 1 · milestone callouts: hide only where there is truly no room (tablet/phone or very short screens)
rep('@media (max-width: 1180px), (max-height: 700px) { .mco { display: none; } }',
    '@media (max-width: 1023px), (max-height: 540px) { .mco { display: none; } }')
# 2 · Fewer boxes: drop the placeholder overlay on both phones (real screens, as in Figma)
i=t.find('<section class="slide baf"'); j=t.find('</section>\n',t.find('class="baf-stage"',i))
j=t.find('</section>',j+10)  # end of .baf section (stage is a nested section)
sec=t[i:j]
svgs=re.findall(r'\n\s*<svg viewBox="0 0 375 812" preserveAspectRatio="none" aria-hidden="true">.*?</svg>',sec,re.S)
assert len(svgs)==2,len(svgs)
for s in svgs: sec=sec.replace(s,'')
t=t[:i]+sec+t[j:]
css='''
/* 11/2 · milestone notes at laptop sizes (Julie: "the notes are important") */
@media (max-width: 1440px) { .mco { width: clamp(120px, 12.3vw, 236px); } .mco li { font-size: clamp(12px, .9vw, 17px); } }
@media (min-width: 1024px) and (min-height: 541px) and (max-width: 1366px), (min-width: 1024px) and (min-height: 541px) and (max-height: 860px) {
  .mco { display: flex; flex-direction: column; justify-content: center; gap: var(--ck-space-3); }
  .mco li { position: static; } }
'''
k=t.find('<body'); last=t.rfind('</style>',0,k); t=t[:last]+css+t[last:]
open(dst,'w').write(t); print('ok')
