# Master batch 11/3 (d): phone labels one style; M3 left note; roadmap footnote; fires table desktop size;
# Any discipline eyebrow + What I did de-dup.
import sys
src, out = sys.argv[1], sys.argv[2]
s = open(src, encoding='utf-8').read()
def rep(old, new, n=1):
    global s
    c = s.count(old); assert c == n, (c, n, old[:90]); s = s.replace(old, new)
# M3: second left note
rep('<ul class="mco mco-l"><li class="good" style="--y:38.8%">replies pattern exploration</li></ul><ul class="mco mco-r"><li class="good" style="--y:27.3%">Explore Creator reaction</li>',
    '<ul class="mco mco-l"><li class="good" style="--y:38.8%">replies pattern exploration</li><li class="good" style="--y:60%">reduced to one dominant reaction with a number</li></ul><ul class="mco mco-r"><li class="good" style="--y:27.3%">Explore Creator reaction</li>')
# roadmap footnote
rep('<sup class="fn-mark">*</sup>PD: product design. M1–M4: milestones 1 to 4.', '<sup class="fn-mark">*</sup>M1–M4: milestones 1 to 4.')
rep('<b>PD<sup class="fn-mark" aria-hidden="true">*</sup> partner left</b>', '<b>Design partner left</b>', 2)
rep('scope set across 9 teams, PD partner left,', 'scope set across 9 teams, design partner left,')
# Any discipline: eyebrow + What I did
rep('<div class="split pv-split">\n<div class="stack">\n\n<h2 class="d-l reveal r2">Any discipline. Live data.',
    '<div class="split pv-split">\n<div class="stack">\n<p class="meta reveal">Proof of prototyping in native code · a precedent</p>\n<h2 class="d-l reveal r2">Any discipline. Live data.')
rep('<p class="role"><b>What I did</b><span>Designed every comment component and pattern in the library. Directed two designers: one built them into the final library, one owned documentation and guardrails.',
    '<p class="role"><b>What I did</b><span>Directed two designers: one built the comment components into the final library, one owned documentation and guardrails.')
anchor = '/* To get there: visual centered top to bottom'
css = ('/* labels under phones: one style everywhere, the "Failed patterns" caption (Julie, 11/3) */\n'
       'section :is(.dev-cap, .lcap, .lcap b, .baf-tag, .baf-tag b, .baf-tag > span), section.mi-slide .dev-cap, section .lineup .lcap b { font: 400 var(--meta)/1.3 var(--font-mono); letter-spacing: .08em; text-transform: uppercase; color: var(--dusk); }\n'
       '/* Four fires table: smaller cell copy on desktop (Julie, 11/3) */\n'
       '@media (min-width: 1025px) { section .fires .row:not(.head) :is(b, span:not(.n)) { font-size: var(--body-s); line-height: 1.35; } }\n')
rep(anchor, css + anchor)
open(out, 'w', encoding='utf-8').write(s)
