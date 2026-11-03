# 11/3 batch: "First, ask if the moment needs a visual at all." + "Anyone can see what needs to change." (anyone-a)
import sys
src, dst = sys.argv[1], sys.argv[2]
h = open(src, encoding='utf-8').read()
def sect(sid):
    import re
    ms = list(re.finditer(r'<section[^>]*data-slide-id="%s"' % sid, h)); assert len(ms) == 1
    s = ms[0].start(); e = h.index('</section>', s) + 10
    return s, e
# 1+2 · pilot
s, e = sect('pilot'); p = h[s:e]
assert 'First, ask if the moment <span class="b">needs a visual</span>' in p
n = p.count('minimal traffic, out of scope'); assert n > 2
p = p.replace('minimal traffic, out of scope', 'minimal traffic')
assert p.count('minimal traffic and out of scope') == 1
p = p.replace('minimal traffic and out of scope', 'minimal traffic')
line = '<p class="body reveal r2">I measured the result against those exact variants, by surface and team.</p>\n'
assert p.count(line) == 1; p = p.replace(line, '')
assert 'out of scope' not in p.lower()
h = h[:s] + p + h[e:]
# 3 · anyone-a: keep text, swap the visual for the annotated phone from anyone-b
s, e = sect('anyone-b'); b = h[s:e]
bv0 = b.index('<div data-plx="1" class="cp cp-after reveal r2">'); bv1 = b.index('<p class="role">')
phone = b[bv0:bv1].rstrip()
assert phone.endswith('</div>\n</div>')
phone = phone[:-len('\n</div>')]  # drop the anyone-grid closer
s, e = sect('anyone-a'); a = h[s:e]
assert 'Anyone can see <span class="b">what needs to change.</span>' in a
v0 = a.index('<div class="anyone-vis">'); v1 = a.index('</figure></div>', v0) + len('</figure></div>')
assert a.count('<div class="anyone-vis">') == 1
a = a[:v0] + phone + a[v1:]
old_al = 'aria-label="Anyone can see what needs to change: asset containers at true scale."'
assert a.count(old_al) == 1
a = a.replace(old_al, 'aria-label="Anyone can see what needs to change: the account-restore screen after, with what changed called out."')
h = h[:s] + a + h[e:]
open(dst, 'w', encoding='utf-8').write(h)
print('pilot label instances:', n)
