# Fix proposed phone (4th) in img/asset-map.webp: un-clip first Reply row, add thumbs-down on Tsz Kei Ho row.
import sys
from PIL import Image
src, out = sys.argv[1], sys.argv[2]
im = Image.open(src).convert('RGB')
o = im.copy()
X0, X1 = 1440, 1805
clean_row = im.crop((X0, 509, X1, 532))          # Reply ♡67 👍 👎, full height (23px)
replies   = im.crop((X0, 388, 1600, 404))        # "390 replies ⌄"
# 1. clear the clipped Reply row + 390 replies band
o.paste((255,255,255), (X0, 368, X1, 426))
# 2. full Reply row, same top as before (372) -> icons/text land where they were
o.paste(clean_row, (X0, 370))
# 3. 390 replies below it (same gap as other rows' Reply -> next line)
o.paste(replies, (X0, 397))
# 4. Tsz Kei Ho row: swap lone thumbs-up for thumbs-up + thumbs-down pair
icons = im.crop((1715, 511, 1800, 532))          # 👍 👎 from a clean row (icon top 513)
o.paste((255,255,255), (1715, 702, 1800, 726))
o.paste(icons, (1715, 704))                      # icon top 706, matches original
o.save(out, 'WEBP', quality=92, method=6)
