# Add Julie's copy to the body on "How does this impact craft?" (native-c). Finds slide by headline.
import sys
src, dst = sys.argv[1], sys.argv[2]
h = open(src, encoding='utf-8').read()
head = '<h2 class="d-l reveal r2">How does this impact <span class="l">craft?</span></h2>'
assert h.count(head) == 1
old = head + '\n<p class="body reveal r2">I block a day on the engineering team’s calendar'
assert h.count(old) == 1
new = (head + '\n<p class="body reveal r2">I use AI to prototype in the code it ships in. '
       'Drift isn’t an engineering problem. It’s a design gap. When design hands over one generic version, '
       'engineers have to make those calls themselves. Every call they make up is a place the design drifts. '
       'So I design for each OS, and I prototype in production code, with the real components.</p>\n'
       '<p class="body reveal r2">I block a day on the engineering team’s calendar')
h = h.replace(old, new)
open(dst, 'w', encoding='utf-8').write(h)
