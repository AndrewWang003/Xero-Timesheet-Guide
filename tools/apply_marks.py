"""Copy the mark positions from tools/shots.json into index.html, and the pixel size of every picture in img/.

    python3 tools/apply_marks.py

Run it after tools/build_shots.py, and after adding or replacing any picture in img/ (also the ones kept by hand).
Mark positions: it only touches the `shot:{...}` part of the steps that build_shots.py builds, and keeps `what:`.
Sizes: it rewrites the SIZES block, so each picture's space is kept on the page before the picture downloads.
It changes nothing if index.html is already up to date.
"""
import json, re, os, sys
HERE = os.path.dirname(os.path.abspath(__file__)); PAGE = os.path.join(HERE, '..', 'index.html')
s = open(PAGE, encoding='utf-8').read(); before = s
R = json.load(open(os.path.join(HERE, 'shots.json')))
js = lambda ms: '[' + ','.join('{' + ','.join(f"{k}:{json.dumps(v)}" for k, v in m.items()) + '}' for m in ms) + ']'
for code, r in R.items():
    pat = re.compile(r"shot:\{src:'img/" + code + r"\.\w+', (what:\"[^\"]*\"), marks:\[.*?\](?:,\n      nsrc:'img/" + code + r"n\.\w+', nmarks:\[.*?\])?\},\n", re.S)
    found = pat.findall(s)
    if len(found) != 1: sys.exit(f"step {code}: expected exactly one shot:{{...}} block in index.html, found {len(found)}")
    m = pat.search(s)
    new = f"shot:{{src:'{r['src']}', {m.group(1)}, marks:{js(r['marks'])}"
    if 'nsrc' in r: new += f",\n      nsrc:'{r['nsrc']}', nmarks:{js(r['nmarks'])}"
    s = s[:m.start()] + new + '},\n' + s[m.end():]
# picture sizes
from PIL import Image
IMG = os.path.join(HERE, '..', 'img'); sizes = {}
for f in sorted(os.listdir(IMG)):
    path = os.path.join(IMG, f)
    if f.endswith('.svg'):
        vb = re.search(r'viewBox="\s*[-\d.]+\s+[-\d.]+\s+([\d.]+)\s+([\d.]+)"', open(path).read())
        if vb: sizes['img/' + f] = [round(float(vb.group(1))), round(float(vb.group(2)))]
    elif f.lower().endswith(('.jpg', '.jpeg', '.png', '.webp')):
        sizes['img/' + f] = list(Image.open(path).size)
block = re.compile(r'/\* SIZES:start \*/.*?/\* SIZES:end \*/', re.S)
if len(block.findall(s)) != 1: sys.exit('index.html: SIZES block not found')
s = block.sub(lambda m: '/* SIZES:start */const SIZES = ' + json.dumps(sizes, separators=(',', ':')) + ';/* SIZES:end */', s)
missing = sorted(set(re.findall(r"src:'(img/[^']+)'", s)) - set(sizes))
if missing: sys.exit('pictures named in index.html but missing from img/: ' + ', '.join(missing))

if s == before: print('index.html already up to date')
else: open(PAGE, 'w', encoding='utf-8').write(s); print('index.html updated: marks for', ', '.join(R), '| sizes for', len(sizes), 'pictures')
