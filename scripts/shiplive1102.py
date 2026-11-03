"""11/2 · What actually shipped: no DM footnote/asterisk; feature label sits as close to its row as the platform line does to the metrics. Still live in production: composer GIF centred top-to-bottom against the copy."""
import sys
src,dst=sys.argv[1:3]
t=open(src).read()
def rep(old,new):
    global t
    assert t.count(old)==1,(old[:60],t.count(old)); t=t.replace(old,new)
rep('<b>Sharing via DM<sup class="fn-mark" aria-hidden="true">*</sup></b>','<b>Sharing via DM</b>')
rep('<span class="fn"><sup class="fn-mark">*</sup>DM: direct message.</span>','')
rep('<p class="meta reveal r4" style="margin-top:clamp(20px,3vw,44px)">Features I designed end to end · all shipped</p>',
    '<p class="meta bp-feat reveal r4" style="margin-top:clamp(20px,3vw,44px)">Features I designed end to end · all shipped</p>')
css='''
/* 11/2 · shipped + live fixes (Julie) */
.bp-ship .stack > .meta.bp-feat { margin-bottom: 0; }
.ns-fig > figure.ns-a { align-self: center; }
'''
k=t.find('<body');last=t.rfind('</style>',0,k);t=t[:last]+css+t[last:]
open(dst,'w').write(t);print('ok')
