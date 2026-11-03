# "What actually shipped.": add a sentiment row under the four outcomes (Julie, 11/3). Ledger rows verbatim numbers.
import sys
src, dst = sys.argv[1], sys.argv[2]
h = open(src, encoding='utf-8').read()
assert h.count('What actually <span class="l">shipped.</span>') == 1
anchor = '<span>daily views on Pinned Comments at launch</span></div></div>'
assert h.count(anchor) == 1
row = ('<div class="metrics four sent reveal r3">'
       '<div class="metric"><span class="dvn b" data-ledger="sentiment-positive">10.79%</span><span>increase in positive comments</span></div>'
       '<div class="metric"><span class="dvn l" data-ledger="toxicity">42%</span><span>drop in toxicity</span></div>'
       '<div class="metric"><span class="dvn b" data-ledger="sentiment-negative">24.18%</span><span>decrease in negative comments</span></div>'
       '</div>')
h = h.replace(anchor, anchor + row)
css_anchor = '</head>'
assert h.count(css_anchor) == 1
h = h.replace(css_anchor, '<style id="bp-sent">.bp-ship .metrics.sent { margin-top: var(--ck-space-2); } .bp-ship .metrics .metric > span:last-child { line-height: 1.3; } .bp-ship .metrics.sent .metric { padding-top: var(--ck-space-3); } .bp-ship .metrics .metric { gap: var(--ck-space-1); } .bp-ship .metrics.sent .dvn { font-size: var(--statement); } @media (min-width: 761px) and (max-width: 1365px) and (min-height: 501px) { section.slide.bp-ship.ck-fit { --bp-w: min(32vw, calc(94svh * 2167 / 2068)); } } @media (min-width: 761px) and (min-height: 501px) and (max-height: 880px) { section.slide.bp-ship.ck-fit { --bp-w: min(32vw, calc(94svh * 2167 / 2068)); } section.bp-ship .metrics .dvn { font-size: var(--statement); } section.slide.bp-ship.ck-fit .bp-split > .stack { gap: var(--ck-space-3); } } .bp-ship p.bp-feat { margin-top: var(--ck-space-4) !important; }</style>\n' + css_anchor)
open(dst, 'w', encoding='utf-8').write(h)
