"""11/2 · "First, ask if the moment needs a visual at all." donut legend: each label on one line beside its number; drop the "160 variants, by outcome" caption."""
import sys
src,dst=sys.argv[1:3]
t=open(src).read()
i=t.find('data-slide-id="pilot"');a=t.rfind('<section',0,i);b=t.find('</section>',i)
s=t[a:b]
cap='<figcaption class="dv-cap"><b>160 variants</b>, by outcome</figcaption>'
assert s.count(cap)==1; s=s.replace(cap,'')
t=t[:a]+s+t[b:]
css='''
/* 11/2 · pilot donut legend: label on one line beside its number (Julie) */
section[data-slide-id="pilot"] .dv-key span { white-space: nowrap; }
@media (max-width: 760px) { section[data-slide-id="pilot"] .dv-key span { white-space: normal; align-items: baseline; }
  section[data-slide-id="pilot"] .dv-key span b { white-space: nowrap; } }
'''
k=t.find('<body');last=t.rfind('</style>',0,k);t=t[:last]+css+t[last:]
open(dst,'w').write(t);print('ok')
