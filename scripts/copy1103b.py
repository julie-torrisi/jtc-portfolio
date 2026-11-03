# Master batch 11/3: Anyone can see (drop 60% line x3, "in the UI*", footnote), Bringing the brand (drop line),
# A system not a style guide (add line, grey sans in Before/After cards), No one agreed (grey card body).
import sys
src, out = sys.argv[1], sys.argv[2]
s = open(src, encoding='utf-8').read()
def rep(old, new, n=1):
    global s
    c = s.count(old); assert c == n, (c, n, old[:80]); s = s.replace(old, new)
WD = 'When design works, you almost don’t notice it. People’s content should shine, and everything around it should get out of the way.'
rep('<p class="body reveal r3" data-ledger="complexity">60% fewer aspect ratios.</p>\n', '', 2)
rep('<figcaption class="dv-cap">60% fewer aspect ratios.</figcaption>', '')
rep('immersive 9:16. 60% fewer aspect ratios."', 'immersive 9:16."')
rep('End-to-end flow · the rules, in the UI<sup class="fn-mark" aria-hidden="true">*</sup>', 'End-to-end flow · the rules', 2)
rep('<span class="fn fn-inline"><sup class="fn-mark">*</sup>UI: user interface. Hi-fi: high-fidelity art.</span>', '')
rep('<h2 class="d-l reveal r2">Bringing the brand <span class="b">into the app.</span></h2>\n<p class="body reveal r2">' + WD + '</p>\n',
    '<h2 class="d-l reveal r2">Bringing the brand <span class="b">into the app.</span></h2>\n')
rep('<p class="body reveal r2">Visual debt is findable for the first time.</p>\n',
    '<p class="body reveal r2">Visual debt is findable for the first time. ' + WD + '</p>\n')
anchor = '.flex-copy .stack :is(.body, .subtitle, .lg > span:last-child) { color: var(--neutral-50); }'
css = ('\n/* card body = grey sans, the deck-wide .lg pattern (Julie, 11/3) */\n'
       'section.flex-beat .flex-copy .bento.prob > .lg > span:last-child { color: var(--dusk); }\n'
       'section[data-slide-id="system"] .bento.ba-cards > .lg > span:last-child { font: 400 var(--body-s)/1.45 var(--font-body); color: var(--dusk); }\n'
       'section[data-slide-id="system"] .sys-copy > .body { max-width: none; }\n'
       '@media (min-width: 1025px) { section[data-slide-id="system"] .bento.ba-cards { grid-template-columns: repeat(2, minmax(0, 1fr)); } section[data-slide-id="system"] .bento.ba-cards > .lg { grid-column: auto; } }')
rep(anchor, anchor + css)
open(out, 'w', encoding='utf-8').write(s)
