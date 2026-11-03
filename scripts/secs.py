import re,html
def top_sections(t):
    # top-level sections only (skip nested)
    out=[];depth=0;start=None
    for m in re.finditer(r'<section\b[^>]*>|</section>',t):
        if m.group(0).startswith('</'):
            depth-=1
            if depth==0: out.append((start,m.end()))
        else:
            if depth==0: start=m.start()
            depth+=1
    return out
def text(s):
    s=re.sub(r'<(script|style)\b.*?</\1>','',s,flags=re.S)
    s=re.sub(r'<!--.*?-->','',s,flags=re.S)
    s=re.sub(r'<[^>]+>',' ',s)
    return ' '.join(html.unescape(s).split())
