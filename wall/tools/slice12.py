# usage: python3 slice12.py sheet.png layout.json outdir [review.png]
import sys,json,os
from PIL import Image
im=Image.open(sys.argv[1]).convert('RGB');L=json.load(open(sys.argv[2]));d=sys.argv[3];os.makedirs(d,exist_ok=True)
for n,x,y,w,h in L: im.crop((x,y,x+w,y+h)).save(os.path.join(d,n.replace('dk4-','')+'.png'))
if len(sys.argv)>4:
  full=sorted([l for l in L if not l[0].endswith('-e')]);cols=4;rows=(len(full)+3)//4
  cs=Image.new('RGB',(cols*395,rows*270));
  for i,(n,x,y,w,h) in enumerate(full): cs.paste(im.crop((x,y,x+w,y+h)),((i%cols)*395,(i//cols)*270))
  cs.save(sys.argv[4])
print(im.size,len(L))
