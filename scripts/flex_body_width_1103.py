# "No one agreed on what our assets should look like…": body copy runs the headline's longest line.
import sys
src, dst = sys.argv[1], sys.argv[2]
h = open(src, encoding='utf-8').read()
assert h.count('No one agreed on what our <span class="b">assets should look like</span>') == 1
old_css = '.flex-copy .stack > p.body { max-width: 86ch; }'
assert h.count(old_css) == 1
h = h.replace(old_css, old_css + '\nsection[data-pass] .flex-copy > .stack > p.body { max-width: var(--hw, 86ch); text-wrap: pretty; }')
anchor = '<script id="copy-width-js">'
assert h.count(anchor) == 1
js = '''<script id="flex-copy-width-js">
(() => {
  // Body copy on the FLEX direction beat runs the headline's longest rendered line (Julie, 11/3).
  function fit() {
    document.querySelectorAll('.flex-copy > .stack').forEach(st => {
      const hd = st.querySelector(':scope > h2'); if (!hd) return;
      const r = document.createRange(); r.selectNodeContents(hd);
      const left = hd.getBoundingClientRect().left; let w = 0;
      for (const b of r.getClientRects()) w = Math.max(w, b.right - left);
      if (w) st.style.setProperty('--hw', Math.min(st.clientWidth, Math.ceil(w)) + 'px');
    });
  }
  const run = () => requestAnimationFrame(fit);
  if (document.fonts && document.fonts.ready) document.fonts.ready.then(run); else run();
  addEventListener('load', run); addEventListener('resize', run);
})();
</script>
'''
h = h.replace(anchor, js + anchor)
open(dst, 'w', encoding='utf-8').write(h)
