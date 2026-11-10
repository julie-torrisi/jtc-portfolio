import sys
p=sys.argv[1]; h=open(p,encoding='utf-8').read()
def rep(a,b,n=1):
    global h
    c=h.count(a); assert c==n,(c,a[:80]); h=h.replace(a,b)
# M1 slide 2 background line (verbatim) + M2 Meta line
rep('<p class="intro-lead reveal r2">20 years in design, 11+ in product, building high-impact brand systems and scaling creative orgs, including almost five years at Meta leading design systems, end-to-end experiences and AI.</p>',
 '<p class="intro-lead reveal r2">I started in graphic design and brand, in New York and London, and I’ve spent the last 11+ years in product. Most recently, I spent almost five years at Meta as a Principal Product Designer.</p>\n<p class="body reveal r3">At Meta I was on the Creators team, helping people become full-time Facebook creators, and in 2025 I worked on Messenger’s rebrand and strategy.</p>')
# M3 slide 3 Brand line
rep('<span>I trained formally in graphic design and grew up in brand and advertising. For the last 11+ years I’ve been in product design, delivering end to end.</span>',
 '<span>I worked at R/GA in digital advertising, in New York and London. Since then I’ve been in product design, delivering end to end.</span>')
# M4 slide 3 Systems + Tin Can watch
rep('<span>I build design systems for desktop, native apps and watches.</span>',
 '<span>I build design systems for desktop, native apps and watches, including a kids’ smartwatch that shipped at Tin Can.</span>')
# M5 slide 3 Native
rep('<span>And I build in native code, and I design the logic AI models use to keep improving the experience.</span>',
 '<span>I design straight to native, in SwiftUI and Compose, so what ships is what we designed. And I design the logic AI models use to keep improving the experience.</span>')
# M6 slide 3 talk track
rep('Graphic design degree, then nine years in brand and advertising at R/GA and agencies in New York and London.',
 'Graphic design degree, then R/GA in digital advertising, in New York and London.')
# M7 superpower 01
rep('<b>I get called when it’s on fire</b><span>When something’s stuck and no one’s sure how to fix it, I get the call. I join the team, learn how it works, fix what’s broken and hand it back stronger.</span>',
 '<b>Tapped when it’s on fire</b><span>When something’s stuck and no one’s sure how to fix it, I get the call. I join the team, fix what’s broken and move on, and it runs without me.</span>')
# M8 superpower 06
rep('<span>Designers come to me to get better at presenting, and directors send theirs to me before they ship. I help them build the confidence that drives alignment fast. I post videos from design exhibitions I visit in New York to the design org channel, and invite everyone to share how design shows up in their life.</span>',
 '<span>Directors sent their designers to me for review before they shipped. I coach presenting, so the team’s work gets aligned and decided faster. I share the design shows I visit and invite everyone to share theirs.</span>')
# M9 How I lead 01
rep('<b>Low ego, outcome driven.</b><span>Engineers trust my work as much as designers do.',
 '<b>No ego, serious about craft,</b><span>and committed to making the work fun. Engineers trust my work as much as designers do.')
# M10 How I lead 05
rep('<b>I grow the bench.</b><span>I grow designers who want to get better through hands-on mentorship. I show them, I don’t just tell them, and I share what I know often so others share too.</span>',
 '<b>I grow the bench.</b><span>I build curious teams that ask whether we’re solving the right problem. I mentor hands on: I show, I don’t just tell, and I share what I know so others share too.</span>')
# M11 composer exit line
rep('Recommended parity with Messenger to the head of Facebook, it was approved but I left the company before it was implemented.',
 'I recommended parity with Messenger to the Head of Facebook. It was approved and handed off for build.')
# D2·A: keep slide 2 on one screen
rep(' Both come down to hierarchy, density and attention: deciding what earns space on a busy screen.</p>','</p>')
open(p,'w',encoding='utf-8').write(h); print('ok')
