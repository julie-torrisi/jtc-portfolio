# Delete "I hand off working code. All on spec, all on brand." (native-b) from the master.
# Finds the slide by headline, not index. Re-silks native-c so no neighbours share a silk.
import sys, re
src, dst = sys.argv[1], sys.argv[2]
h = open(src, encoding='utf-8').read()
head = 'I hand off working code. <span class="l">All on spec, all on brand.</span>'
assert h.count(head) == 1
i = h.index(head)
s = h.rfind('<section', 0, i)
e = h.index('</section>', i) + len('</section>')
assert h[s:i].count('<section') == 1 and 'native-b' in h[s:i]
block = h[s:e]
end = e + 1 if h[e:e+1] == '\n' else e
h = h[:s] + h[end:]
old = 'data-slide-id="native-c" data-dim=".35" data-silk="tide-turn"'
assert h.count(old) == 1
h = h.replace(old, 'data-slide-id="native-c" data-dim=".35" data-silk="iris"')
open(dst, 'w', encoding='utf-8').write(h)
open(dst + '.removed.html', 'w', encoding='utf-8').write(block)
print('removed', len(block), 'chars')
