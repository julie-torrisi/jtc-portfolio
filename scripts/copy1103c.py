# Master batch 11/3 (c): No one agreed period lilac; one-room sticker off the type + visual centered;
# data-layer: Audit results -> What I did, bottom role removed; THE BET text centered in its pill.
import sys
src, out = sys.argv[1], sys.argv[2]
s = open(src, encoding='utf-8').read()
def rep(old, new, n=1):
    global s
    c = s.count(old); assert c == n, (c, n, old[:90]); s = s.replace(old, new)
rep('or <span class="l">where they should live</span>.</h2>', 'or <span class="l">where they should live.</span></h2>')
rep('<p class="dl-results reveal r3"><p class="meta">Audit results</p>', 'x', 0)  # guard: structure is a div
rep('<div class="dl-results reveal r3"><p class="meta">Audit results</p><p class="dl-cap">Every user-facing visual across Facebook, sorted into 11 categories.</p></div>\n</div>\n<p class="role"><b>What I did</b><span>Audited every visual by hand and turned an image dump into 11 categories.</span></p>\n',
    '<div class="dl-results reveal r3"><p class="meta">What I did</p><p class="dl-cap">Audited every visual by hand and turned an image dump into 11 categories.</p></div>\n</div>\n')
FB = '<div class="fbset"><picture data-plx="2" class="fb m-hide" style="--x:81%;--y:68%;--s:clamp(70px,7vw,130px)" aria-hidden="true"><img src="img/fb/ava-buns.webp" alt="" loading="lazy" decoding="async"></picture></div>\n'
rep(FB, '')
FB2 = '<div class="fbset room-fb"><picture data-plx="2" class="fb m-hide" style="--x:calc(100% - var(--s) * .5);--y:calc(var(--s) * -.5);--s:clamp(70px,7vw,130px)" aria-hidden="true"><img src="img/fb/ava-buns.webp" alt="" loading="lazy" decoding="async"></picture></div>'
rep('<source src="vid/workshop.mp4" type="video/mp4"></video></figure>', '<source src="vid/workshop.mp4" type="video/mp4"></video>' + FB2 + '</figure>')
rep('<text class="dv-k dv-t-blue" x="264.0" y="274.4" text-anchor="middle" dominant-baseline="central" font-size="13.2">THE BET</text>',
    '<text class="dv-k dv-t-blue" x="264.0" y="271.9" text-anchor="middle" dominant-baseline="central" font-size="13.2">THE BET</text>')
anchor = '/* card body = grey sans, the deck-wide .lg pattern (Julie, 11/3) */'
css = ('/* To get there: visual centered top to bottom across from the type; sticker pinned to the video top-right corner, off the type (Julie, 11/3) */\n'
       '.room-v2 { align-items: center; }\n.room-v2 > .room-proof { align-content: center; }\n'
       )
rep(anchor, css + anchor)
open(out, 'w', encoding='utf-8').write(s)
