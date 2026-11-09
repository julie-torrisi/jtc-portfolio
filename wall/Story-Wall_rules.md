# Story Wall rules (Julie's bento motion wall)

Every edit Julie asks for becomes a rule here. One file: this replaces Story-Wall_rules.md (v9) and Story-Wall_rules_1.md (Rovo analysis, 11/9).
Source build: jtc-portfolio, branch `story-wall`, folder `/wall`. Current build: `v10.html` (dark, 11/9), assets in `v9/` + `v10/`, faces in `img/face-*.png`, clips in `clips/`. Previous: `v9.html`. Older template: `src.html`.
References: Eduardo Sonnino's Story Factory wall, and his Rovo story wall (Team '26 Europe; Julie's capture `~/Downloads/_Video/rovo_story_wall.mov`, 8.1 s, 4096×2284, analyzed 11/9 at 8 fps). Julie's Rovo observations are marked J1–J11.
Consolidated 11/9 (Julie's calls: Rovo grid, one tile per app, Rovo glow in brand colors, no metric cards). v10 edits 11/9: rules 5, 6, 6g, 6h, 6i, 6k, 9b, 10.2, 10.3.

## Content
1. Only real pieces: Blueprint library components exported as-is (Figma file zsAGUQCLwwGQzlD2gvzSTt), Julie's own prototype captures (Xcode / Messenger recordings), official Facebook brand assets and her brand refresh animations. Never invent or redraw a pattern.
2. Components only. No screens, no phone frames, no captions or labels, no metric cards or data cards (metrics go in the deck), no presentation-deck visuals (no 3D silver art, no flower, no swirl/fingerprint deck art inside attachments). (Confirmed 11/9: the Rovo data cards stay off the wall.)
3. Show as many comment-related components as possible, isolated, outside a phone screen.
4. Never the same asset twice on screen, including photos inside components (the camera roll tray and the media comment must not share an image). Brand video shows as different micro clips, each used once.
4a. ONE COMPONENT, ONCE ON SCREEN (hard rule, never break it). A component counts as the same visual no matter its variant, color, theme, surface (Default, On Color, On Media), data or copy. Two Progress Bar Charts (Primary and Star Rating), two Bar charts (vertical and horizontal), two Comment Threads, a comment plus a comment stack, a light and a dark copy: all repeats. Before showing any frame, list the Blueprint component set behind every tile and confirm each set appears once. Variants of one component may only appear as states of that one tile over time (cycling in place). One thread or one two-bubble chat counts as one tile.
4b. Show a skeleton state: one tile loads with a Blueprint Glimmer (skeleton) component first, then resolves to its real content.
5. App icons: one small tile each, icon small and centered (11/9, replaces the 2x2 cluster). Two sets of 4: Claude, Figma, Cursor, Xcode, then TestFlight, Simulator, Terminal, Slack (Slack icon still needed; its slot stays an empty tile). Icons are @2x exports shown at 80 px in a one-unit tile. Small tiles hold still once built (rule 13b); they pop in per rule 10.
6. The keyboard card is Julie's north star: the Messenger composer with the keyboard already up from the first frame, the + menu (Files, Payment, Location, Games, AI media) opening and closing, cut from her Messenger composer recording at native 444 px, everything above the composer except the menu painted out to the chat white (11/9). The talk-to-text card uses the real Messenger pattern: tap the mic, the voice pill replaces the input field. The keyboard card is the real keyboard rising under the composer. Julie's Quiet, Speech and Loud waveform lives only inside the blue voice pill and moves low to high like a voice. No separate waveform card.
6a. No placeholder copy anywhere ("Label", "Headline", "Body type input"). All copy is fake but relevant. Labels fit their column with no wrapping.
6b. Bottom nav is the pill nav from the current Facebook app: Home, Groups, Reels, Marketplace, Feeds, and Julie's photo as Profile; no text labels; selected tab sits in a soft blue pill. In dark mode it is the dark pill.
6c. No expressive-icon size ladder.
6d. Every count is unique and arbitrary (no 99.9K anywhere). The same comment keeps its count across its own states.
6e. Every chart number is arbitrary and every bar or segment is sized to the number it shows, on one shared scale per chart. Bars sit centered on their labels; tracks are equal length.
6f. The full facebook wordmark sits static on a white panel inside a grey tile.
6g. Camera roll tray photos are Julie's own photos only, each one different (decided 11/9). Pending: the photos and the tray export.
6h. Include the brand refresh motion as micro clips from the two GIFs on her brand refresh page (brand_Video.gif, fb_brand refresh.gif): the tapering, facebook and fa tiles, each its own 2×2 tile at native 190 px, plus the icon grid and sticker burst from the brand video. The f logo construction in the tapering / facebook tiles is the wall's logo trace (rule 10.3); never redraw the f.
6i. People and comments: real faces with names, in a casual, believable fake conversation (her light-mode comments reference: "keep keep keep 🔥🔥🔥", "need a full-length pic of the fit 📸"). Each name always has the same photo. Faces come from her own prototype screens and the reference she supplied, never invented. No testimonials anywhere on the wall (decided 11/9).
6j. Include one bento-within-a-bento brand card: small brand tiles nested inside one grey tile, with no asset that also appears elsewhere on screen.
6k. Comment rows match her light-mode reference, in dark mode: avatar, Name · time, text, optional rounded photo attachment, then Reply, one reaction + count, and the like icon on the right. No Author / Admin / Follow badge strip, no truncated text, no repeated name on every comment. Different people reply to each other. Thread lines are 1.5 px, and the thread line connects up to the first comment's avatar (11/9).
6l. No logos of companies Julie is applying to (deck rule). Facebook brand assets from her own work (6f, 6h, 6j) are allowed.

## Scale
7. Nothing scales. Components render at native pixel size. The page never zooms to fit the window.
7a. Videos stay as small as their tile allows so they read sharp. Trim any clip whose first frames show stray content.

## Grid and look
8. The whole wall drifts right to left as one sheet at 0.06 screen heights a second: 64.8 px/s at 1080 (checked against Story Factory at about 65 px/s and Rovo at about 140 px/s at 2284 tall).
9. Colors measured from Eduardo's video: wall #1F1E21, tiles #24232A, a soft shadow. Components sit inside the grey tile as their own card.
9a. No hairlines anywhere: tiles have no borders, never scale, and move on whole device pixels.
9b. One shared grid: 7 rows, 128 px units, 20 px gaps (11/9, replaces 6 × 152). Every tile is a whole multiple of the unit in both directions, with an equal gap on every side of every tile (J1). Inside a tile, the component sits with the same padding on all four sides (at least 24 px); the tile size snaps up to the next unit. How: the component's own card fills the tile with 24 px on every side and the component centers on it; a clip that can't grow sets its own equal pad (190 px brand tiles: 43; keyboard: 64). Small items sit in square one-unit tiles. Empty tiles are one unit each.
9c. The first frame is already full. Empty tiles in the tile color fill the grid between content tiles.
9d. The loop is wider than the screen, so a column never meets its own copy on screen.

## A tile entering, in order
10. Tiles ride the wall in: each tile already sits in its grid slot off the right edge and reaches the screen because the wall moves (J1). Nothing populates until the tile is fully in frame. Then:
   1. An empty shell at full size.
   2. A glow outline, once (J2, J3): a thin gradient traces the edge, lit on two or three sides with gaps, like one light source. Fade in about 150 ms, hold about 450 ms, fade out about 650 ms, drifting about 40° around the tile. Never loops. Colors: kit blue → lilac → mist with an amber warm stop (11/9, Julie: blue and amber); amber is the proposed --ck-glow-warm until the kit has it (see Gaps).
   3. The component builds in, each piece with its own entrance (J4):
      - Header first, then rows wipe in about 160 ms apart (thread rows and chat bubbles 160–200 ms).
      - App icons pop in, scaling up (J7); several in view enter about 250 ms apart.
      - Inputs type out letter by letter.
      - A logo traces itself as a stroke, then resolves to the filled mark.
      - Chart components (Blueprint bar and progress charts, J8): bars fill left to right and a donut sweeps clockwise from 12 o'clock; their numbers count up with the bar or sweep, in the number's own format (count-up-rule.md, rules 2–3; the final value is the arbitrary chart number from 6e, not a ledger number). Use /count-up wherever a number sits on a chart. On exported PNGs: an empty-bar copy sits under the export, the real bars reveal on top, a live number counts over the digits and lifts at the end so the last frame is the exported pixels.
   4. Then it holds still or keeps one slow loop (rule 13).

## Motion
12. Enter on out.bold, leave on in.practical, move on inout.bold. Spring only for people (cursors), reactions and the hanging card. Trays 300 ms ease-out. Count-ups ease-out quart (proposed, count-up-rule.md).
13. Micro moments stay short: one looping element per tile, under 6 s a loop (the voice hold is about 4.5 s), so the eye can wander (J6, J9). Examples: the voice waveform, a drifting dot grid, a wordmark marquee, a spinner.
13a. Some cards stay still after they build.
13b. Small single-icon tiles always hold still once built (J10). That stillness makes the moving tiles readable.
13c. Hanging card (J5): a card with a handle bar hangs from a hook and swings once on entry. Spring, pivot top center, about ±3°, settling in about 1.6 s (unchecked at 8 fps).
14. Figma cursors (Julie, Adam, Eduardo, Jeremy, Josh): ONE at a time, never two on screen. Large pointers with a colored name pill (22 px semibold label, 34 px pointer). Each enters from the nearest edge, presses one real control (switch, pill tab, mic, pinned message button, a reaction on a comment; the component steps to its next variant, or a tile builds in), holds a beat and leaves the way it came. A cursor never crosses the whole screen. The next starts only after the last is gone.

## Process
15. Export each component from Figma at native size in DEFAULT / DARK mode (Blueprint - Color collection). For copy, numbers and faces, use a temporary page of instances: swap fonts to SF Pro, set text, set Actor image fills, export. Detach only when a bar must be resized. Delete the temp page "_Story Wall export v8 (temp, delete me)" when the wall is final.
16. Check before showing: static frame first, then a 30 s preview. Run the 4a component check (the page logs window.__components), confirm nothing scaled, no placeholder copy, no wrapped labels, no hairlines, equal padding, every tile on the 128 px grid, one glow per tile entry, one cursor at a time, thread lines 1.5 px.
16a. Never merge to main or push to the live page without Julie's go. Commit on the `story-wall` branch.

## Facebook comment components (UFI bento and anything else with comments)
17. Thumbs down never has the cuff. Only the Like thumbs up has the cuff (Facebook brand).
18. The blue Like reaction icon is the thumbs up.
19. Like resolves to the reaction you picked, with the real reaction icon. The count only rises for the like or reaction. Dislike only fills in and turns blue; it has no count and feeds comment ranking.
20. Every component is at least 375 px wide.
21. Show components as a card inside a grey tile. Never a plain white tile.
22. People in the UFI bento: Julie Torrisi-Coffey (her photo) is the creator. The main comment is by Nancy Ahn (her photo). Spread other avatars equally across Adam, Josh, Jeremy, Julie, Eduardo and Charlie Sutton, using their LinkedIn photos. On the Story Wall, rule 6i applies instead.
23. Name badges next to the name (UFI bento only): Author (person icon), Author (pencil), Admin (shield), and "[like] by Author".
24. Creator reaction: the creator's avatar with their reaction sits on the reaction row. Facepile: avatars + reaction + count, with the count on either side.
25. UFI bento: the original laugh-burst phone stays in the center as is. One animation per recording.

## Gaps
- [SYSTEM GAP] Missing: a warm glow stop · Needed for: the tile glow (rule 10.2) · Proposed: --ck-glow-warm · Fallback: blue → lilac → mist (in use) · Proceed with proposed or fallback?
- [SYSTEM GAP] Missing: --ck-motion-duration-glow and the count-up tokens · Needed for: rule 10 · Proposed: values in count-up-rule.md · Fallback: duration.cinematic + easing.enter · Proceed with proposed or fallback?
- v10 is on 7 × 128 (done 11/9).
- Open: the keyboard and talk-to-text cards are both the Messenger composer. With a 3,256 px loop they can share a 1920 screen near the loop seam, and so can the static wordmark and the facebook brand tile. Keep, or merge talk-to-text into the keyboard tile as a state?
- Missing: a Blueprint card with a handle bar for the hanging card (13c); the Slack icon (5); Julie's photos + camera roll tray export (6g).
