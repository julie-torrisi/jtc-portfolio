"""11/2 · four fixes: Risk label sits close to its line; CEO directive note at footnote size; pillars venn centred between copy and rail, legend lines breathe; no XFN footnote on the influence slide."""
import sys
src,dst=sys.argv[1:3]
t=open(src).read()
def rep(old,new,n=1):
    global t
    assert t.count(old)==n,(old[:60],t.count(old)); t=t.replace(old,new)
rep('<p class="meta ng-risk reveal r4">Risk</p>\n<p class="body reveal r4">Doing nothing',
    '<div class="ng-riskblock reveal r4"><p class="meta ng-risk">Risk</p>\n<p class="body">Doing nothing')
rep('losing young adults a little more every year.</p>\n</div>\n<figure class="ng-fan','losing young adults a little more every year.</p></div>\n</div>\n<figure class="ng-fan')
rep('Weekly XFN<sup class="fn-mark" aria-hidden="true">*</sup> sync','Weekly XFN sync')
rep('<span class="fn"><sup class="fn-mark">*</sup>XFN: cross-functional partners outside design, such as engineering, product, research and data.</span>','')
css='''
/* 11/2 · four fixes (Julie) */
.ng-riskblock { display: grid; gap: var(--ck-space-2); }
.ng-riskblock .ng-risk { margin: 0; }
section[data-slide-id="directive"] .qt-note { font: 400 var(--meta)/1.4 var(--font-body); }
@media (min-width: 1024px) {
  .pillars-slide .split.venn-split { grid-template-columns: minmax(0, max-content) minmax(min-content, 1fr); column-gap: 0;
    margin-right: calc(var(--ck-pager-target) - var(--margin)); }
  .pillars-slide .split.venn-split > .dv-venn { justify-self: center; padding-inline: clamp(24px, 4vw, 72px); } }
.pillars-slide .dv-pb { line-height: 1.4; padding-block: var(--ck-space-1); }
.pillars-slide .dv-pick { gap: var(--ck-space-3); }
'''
k=t.find('<body');last=t.rfind('</style>',0,k);t=t[:last]+css+t[last:]
open(dst,'w').write(t);print('ok')
