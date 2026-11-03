# Julie Torrisi-Coffey · Design leader · Portfolio deck

A 44-slide, scroll-and-step presentation of my work as a principal product designer: how I build with AI, Facebook's brand refresh in product (the Visual Asset Framework), and the Facebook Comments modernization.

**View it:** https://julie-torrisi.github.io/jtc-portfolio/

## How to present
- **Arrow keys / Space / Page Down** step through every slide and every step inside a slide.
- **N** shows the talk track for the current slide.
- **P** pauses background motion. Reduced-motion settings are respected.
- Works on phones, tablets and desktop. On phones it reads as a vertical page.

## What's here
| Path | What it is |
|---|---|
| `index.html` | The whole deck: markup, styles (design tokens in `:root`) and script in one file |
| `bg/` | Background silks, one per slide, never the same twice in a row |
| `img/`, `vid/` | Product screens, prototypes and supporting visuals |
| `scripts/` | Edit scripts from the final pass (Nov 2, 2026): they find slides by headline and assert a single match |
| `archive/ending-removed-2026-11-02.html` | Slides cut from the final ending, kept so any of them can be restored |

## Run it locally
```
python3 -m http.server 8765
```
Then open http://127.0.0.1:8765. (Opening `index.html` straight from disk breaks the phone screen masks.)

## Built with
Cadence design tokens ([cadence-kit](https://github.com/julie-torrisi/cadence-kit)), Instrument Serif, Inter, Geist Mono and Redaction 50. Designed in Figma and built with Claude.

Product screens show fictional people. Third-party app screens and press quotes are shown for commentary.

© 2026 Julie Torrisi-Coffey
