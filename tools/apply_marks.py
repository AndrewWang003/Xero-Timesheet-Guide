"""Copy the mark positions from tools/shots.json into index.html.

    python3 tools/apply_marks.py

Run it after tools/build_shots.py. It only touches the `shot:{...}` part of the steps that build_shots.py builds,
and it keeps each step's `what:` text. It changes nothing if the positions are already up to date.
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
if s == before: print('index.html already up to date')
else: open(PAGE, 'w', encoding='utf-8').write(s); print('index.html updated for', ', '.join(R))
