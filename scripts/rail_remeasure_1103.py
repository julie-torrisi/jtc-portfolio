# Section rail: re-measure slide tops when the layout changes, so the last slide lights the last dot.
import sys
src, dst = sys.argv[1], sys.argv[2]
h = open(src, encoding='utf-8').read()
old = "  addEventListener('resize', measure);\n  if (document.fonts) document.fonts.ready.then(measure);\n  window.SectionRail"
assert h.count(old) == 1
new = ("  addEventListener('resize', measure);\n  if (document.fonts) document.fonts.ready.then(measure);\n"
       "  addEventListener('load', measure);\n"
       "  if ('ResizeObserver' in window) new ResizeObserver(() => { measure(); pager.go(where()); }).observe(box);\n"
       "  window.SectionRail")
h = h.replace(old, new)
open(dst, 'w', encoding='utf-8').write(h)
