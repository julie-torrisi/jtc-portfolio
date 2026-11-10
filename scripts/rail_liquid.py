"""Section rail: equal negative space + liquid bead (Julie, 11/10).
Usage: python3 rail_liquid.py in.html out.html   — exact string replaces, each asserted to match once."""
import sys
src = open(sys.argv[1], encoding='utf-8').read()
def rep(old, new, count=1):
    global src
    n = src.count(old); assert n == count, (n, old[:90]); src = src.replace(old, new)

# 1 · token: new kit motion token (SYSTEM GAP approved 11/10: motion.duration.flow 450ms)
rep("  --ck-motion-duration-standard: 300ms;\n",
    "  --ck-motion-duration-standard: 300ms;\n  --ck-motion-duration-flow: 450ms;   /* 11/10 (Julie): the rail bead's one-pull jump across several slides */\n")

# 2 · CSS: liquid layer fades only under reduced motion
rep(".ck-pager-live { position: absolute;",
    ".ck-pager .liq-fade { transition: opacity var(--pg-dur-reduced) var(--pg-ease); }\n.ck-pager-live { position: absolute;")

# 3 · Pager: helpers (px of a length token, cubic-bezier from the easing token)
rep("  function reduced() { return root.dataset.motion === 'reduce' || matchMedia('(prefers-reduced-motion: reduce)').matches; }\n",
    """  function reduced() { return root.dataset.motion === 'reduce' || matchMedia('(prefers-reduced-motion: reduce)').matches; }
  function px(name) { var p = document.createElement('div'); p.style.cssText = 'position:absolute;visibility:hidden;inline-size:var(' + name + ')';
    root.append(p); var w = p.getBoundingClientRect().width; p.remove(); return w; }
  function ease(name) {   // the token's cubic-bezier as a function of t
    var m = getComputedStyle(root).getPropertyValue(name).match(/cubic-bezier\\(([^)]+)\\)/); if (!m) return function (t) { return t; };
    var c = m[1].split(',').map(parseFloat), x1 = c[0], y1 = c[1], x2 = c[2], y2 = c[3];
    function b(a1, a2, s) { return 3 * a1 * s * (1 - s) * (1 - s) + 3 * a2 * s * s * (1 - s) + s * s * s; }
    return function (t) { if (t <= 0) return 0; if (t >= 1) return 1; var lo = 0, hi = 1, s = t;
      for (var i = 0; i < 24; i++) { s = (lo + hi) / 2; if (b(x1, x2, s) < t) lo = s; else hi = s; } return b(y1, y2, s); };
  }
""")

# 4 · Pager: rail pitch + dot from the board tokens (o.pitchToken / o.dotToken), bead at rest = one lit dot
rep("""      pitch = Math.max(tok('--ck-component-pager-pitchMin', 3),
        Math.min(tok('--ck-component-pager-pitchDense', 5), Math.floor(room / cells * 4) / 4));
      r = U * tok('--ck-component-pager-dotDense', .8) / 2;""",
    """      if (o.pitchToken) {   // 11/10 (Julie): the rail reads the dot board's pitch and dot, so every gap is a whole number of board cells
        pitch = tok(o.pitchToken, 8); r = U * (px(o.dotToken) / pitch) / 2;
      } else {
        pitch = Math.max(tok('--ck-component-pager-pitchMin', 3),
          Math.min(tok('--ck-component-pager-pitchDense', 5), Math.floor(room / cells * 4) / 4));
        r = U * tok('--ck-component-pager-dotDense', .8) / 2;
      }""")

rep("""      if (fade) {
        beads = pos.map(""",
    """      if (o.liquid) { liq = liquid(); bead = null; }
      else if (fade) {
        beads = pos.map(""")
rep("""      } else {
        bead = document.createElementNS(NS, 'g'); bead.setAttribute('class', 'bead'); pair(pos[0], bead); board.append(bead);
      }""",
    """      } else {
        bead = document.createElementNS(NS, 'g'); bead.setAttribute('class', 'bead'); pair(pos[0], bead); board.append(bead);
      }
      // liquid bead (11/10, Julie): at rest one lit-dot circle; while moving it stretches out of its dot, necks, and merges into the next.
      // A static goo filter (blur + alpha threshold) sits on this blue layer only; the circles move on transform only; the crisp
      // circles are merged back on top, so the rest state is exactly a lit dot and the lilac and dusk dots never pass through the filter.
      function liquid() {
        var K = 5, NECK = [1, .8, .68, .76, .9], gid = 'ck-goo-' + Math.random().toString(36).slice(2, 7);
        var defs = document.createElementNS(NS, 'defs');
        defs.innerHTML = '<filter id="' + gid + '" x="-100%" y="-100%" width="300%" height="300%" color-interpolation-filters="sRGB">' +
          '<feGaussianBlur in="SourceGraphic" stdDeviation="' + (r * .6) + '" result="b"/>' +
          '<feColorMatrix in="b" mode="matrix" values="1 0 0 0 0  0 1 0 0 0  0 0 1 0 0  0 0 0 24 -10" result="g"/>' +
          '<feMerge><feMergeNode in="g"/><feMergeNode in="SourceGraphic"/></feMerge></filter>';
        svg.prepend(defs);
        var g = document.createElementNS(NS, 'g'); g.setAttribute('class', 'bead liq'); g.setAttribute('filter', 'url(#' + gid + ')');
        var ghost = document.createElementNS(NS, 'g'); ghost.setAttribute('class', 'bead liq-fade'); ghost.style.opacity = 0;
        function circ(parent) { var p = at(pos[0], 0), e = document.createElementNS(NS, 'circle');
          e.setAttribute('cx', p[0]); e.setAttribute('cy', p[1]); e.setAttribute('r', r); e.style.transformBox = 'fill-box'; e.style.transformOrigin = 'center'; parent.append(e); return e; }
        var parts = []; for (var i = 0; i < K; i++) parts.push(circ(g));
        var drop = circ(g), old = circ(ghost);
        board.append(g, ghost);
        var head = 0, tw = null, hist = [], raf = 0, target = 0, maxSep = r * .95, cell = STEP * U, E = ease('--ck-motion-easing-enter'), LAG = tok('--ck-motion-stagger', 40);
        function ms(n) { return tok(n, 300); }
        function put(e, d, s) { e.style.transform = (vertical ? 'translateY(' : 'translateX(') + d + 'px) scale(' + s + ')'; }
        function rest() { cancelAnimationFrame(raf); raf = 0; tw = null; head = target; hist = [];
          parts.forEach(function (e) { put(e, target, 1); }); put(drop, target, 1); }
        function frame(now) {
          var e = E, lag = LAG;   // read once per move, never per frame (no style recalc in the loop)
          if (tw) { var k = Math.min(1, (now - tw.t0) / tw.dur); head = tw.from + (tw.to - tw.from) * e(k); }
          hist.push([now, head]); while (hist.length > 2 && hist[1][0] < now - K * lag) hist.shift();
          function at_(t) { for (var j = hist.length - 1; j >= 0; j--) if (hist[j][0] <= t) return hist[j][1]; return hist[0][1]; }
          var p = [head], dir = target >= head ? 1 : -1;
          for (var i = 1; i < K; i++) { var q = at_(now - i * lag), prev = p[i - 1];
            if (Math.abs(q - prev) > maxSep) q = prev + Math.sign(q - prev) * maxSep; p.push(q); }
          var len = Math.abs(p[K - 1] - p[0]), s = Math.min(1, len / ((K - 1) * maxSep));
          p.forEach(function (d, i) { put(parts[i], d, 1 - s * (1 - NECK[i])); });   // blob · neck · blob: the head leads, the middle thins, the tail still holds its dot
          put(drop, target, Math.max(0, Math.min(1, 1 - Math.abs(target - head) / cell)));   // the next dot swells to meet it: two drops merge
          var done = (!tw || now - tw.t0 >= tw.dur) && len < .01 && Math.abs(head - target) < .01;
          if (done) rest(); else raf = requestAnimationFrame(frame);
        }
        return {
          to: function (d, first) {
            if (first) { target = d; rest(); return; }
            if (reduced()) {   // law 10: no stretch. The bead fades out of the old dot and into the new one.
              put(old, target, 1); ghost.style.transition = 'none'; ghost.style.opacity = 1; g.removeAttribute('filter');
              g.classList.add('liq-fade'); g.style.transition = 'none'; g.style.opacity = 0; target = d; rest();
              requestAnimationFrame(function () { requestAnimationFrame(function () {
                ghost.style.transition = ''; g.style.transition = ''; ghost.style.opacity = 0; g.style.opacity = 1; }); });
              return;
            }
            g.setAttribute('filter', 'url(#' + gid + ')'); g.classList.remove('liq-fade'); g.style.opacity = '';
            E = ease('--ck-motion-easing-enter'); LAG = tok('--ck-motion-stagger', 40);
            var steps = Math.abs(d - head) / cell;
            target = d; tw = { from: head, to: d, t0: performance.now(),
              dur: steps > 1.01 ? ms('--ck-motion-duration-flow') : ms('--ck-motion-duration-standard') };
            if (!raf) raf = requestAnimationFrame(frame);
          },
          snap: function () { if (raf || tw) rest(); ghost.style.transition = 'none'; ghost.style.opacity = 0; g.style.transition = 'none'; g.style.opacity = '';
            requestAnimationFrame(function () { ghost.style.transition = ''; g.style.transition = ''; }); }
        };
      }""")
rep("var svg, board, bead, beads = [],", "var liq = null, svg, board, bead, beads = [],")
rep("      else { var d = (pos[cur] - pos[0]) * U; bead.style.transform = vertical ? 'translateY(' + d + 'px)' : 'translateX(' + d + 'px)'; }",
    "      else if (liq) liq.to((pos[cur] - pos[0]) * U, first);\n      else { var d = (pos[cur] - pos[0]) * U; bead.style.transform = vertical ? 'translateY(' + d + 'px)' : 'translateX(' + d + 'px)'; }")
# law 6: any key or press anywhere finishes a running bead move
rep("    function finish() { el.classList.add('fin');",
    "    if (o.liquid) { addEventListener('keydown', function () { if (liq) liq.snap(); }, true); addEventListener('pointerdown', function () { if (liq) liq.snap(); }, true); }\n    function finish() { if (liq) liq.snap(); el.classList.add('fin');")

# 5 · Section rail: board pitch, one-dot bead, liquid; a pick on the rail flows straight to it (no hop back through the slides it scrolls past)
rep("const pager = window.CadencePager(nav, { mode: 'rail', items: secs.length, start: where(), acts, noun: 'Slide', onGo: i => go(i) });",
    "let jump = null, jumpT = 0;\n  const pager = window.CadencePager(nav, { mode: 'rail', items: secs.length, start: where(), acts, noun: 'Slide', lineCells: 1, liquid: true,\n    pitchToken: '--ck-board-pitch', dotToken: '--ck-board-dot', onGo: i => { jump = i; clearTimeout(jumpT); jumpT = setTimeout(() => { jump = null; }, 2000); go(i); } });")
rep("if (!raf) raf = requestAnimationFrame(() => { raf = 0; pager.go(where()); nav.dataset.act = actOf(where()).name; });",
    "if (!raf) raf = requestAnimationFrame(() => { raf = 0; const w = where(); if (jump !== null) { if (w !== jump) return; jump = null; } pager.go(w); nav.dataset.act = actOf(w).name; });")
open(sys.argv[2], 'w', encoding='utf-8').write(src)
print('ok')
