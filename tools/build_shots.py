"""Build the guide's pictures from the original Xero screenshots, and work out where the marks go.

    python3 tools/build_shots.py <folder with the original screenshots> [output folder, default: img]
    python3 tools/apply_marks.py          # then copy the new mark positions into index.html

For each step this makes:
  img/<step>.jpg  (or .webp)  the full screenshot: wide screens, and the enlarged view on every screen
  img/<step>n.webp            a close-up for phones, made of one or more pieces cut from the same screenshot
  img/<step>f.webp            the whole screenshot(s), for the enlarged view
and writes tools/shots.json with the mark positions, in % of each picture.

The original screenshots are NOT in this repository: they show names, pay rates and hours.
Every redaction below is applied to the original before anything is cut from it.
Coordinates are pixels in the original screenshot. To find them, open the original in any image viewer.

Not built here (kept by hand in img/ and in index.html): A1, A2.
Needs: Python 3 and Pillow with WebP support.
"""
import sys, os
from PIL import Image, ImageDraw
import json
if len(sys.argv) < 2: sys.exit(__doc__)
S = os.path.join(sys.argv[1], ''); OUT = os.path.join(sys.argv[2] if len(sys.argv) > 2 else 'img', '')
HERE = os.path.dirname(os.path.abspath(__file__))
src={}
def load(n):
    if n not in src: src[n]=Image.open(S+n).convert('RGB')
    return src[n]
# ---- redactions on the sources, before any crop ----
d=ImageDraw.Draw(load('C2.jpeg'))
for y in (470,575,678,782): d.rectangle([534,y-30,1010,y+30],fill='#C9CED6')      # other earnings rates: keep the first word (same width as "Manual:"), hide the rest
# The full screenshots are shown too (the enlarged view), so everything private on the whole screen is covered here.
GREY=(85,85,85)
def cover(f, *boxes, fill=GREY):
    d=ImageDraw.Draw(load(f))
    for b in boxes: d.rectangle(b, fill=fill)
def avatar(f, x0, y0, y1):      # the account initials, top right: painted over in the colour of the bar around them
    im=load(f); cover(f, (x0, y0, im.size[0], y1), fill=im.getpixel((x0-130, (y0+y1)//2)))
for f in ('B1&B2.png','B3.png','D2.png','E1.png'): avatar(f, 2462, 0, 121)
for f in ('B4-1.png','B4-2.png'): avatar(f, 2455, 0, 113)
avatar('C2.jpeg', 2648, 0, 108); avatar('D3.JPG', 1476, 74, 127)
cover('E1.png', (2105, 978, 2215, 1025))               # this fortnight's hours
cover('B3.png', (2105, 978, 2215, 1025))               # the same, behind the window
cover('D2.png', (1990, 705, 2170, 775), (1895, 1035, 2060, 1230))   # totals and hours behind the window
cover('D2.png', (957, 1247, 1192, 1279))               # approver list: one bar lengthened so only two letters show
SEP=30   # gap between the pieces of one picture, in output pixels. It is left transparent: the page colours it.
def build(name, strips, marks, outw):
    parts=[]; offs=[]; y=0
    for f,(x0,y0,x1,y1) in strips:
        im=load(f).crop((x0,y0,x1,y1)); sc=outw/im.size[0]; im=im.resize((outw,round(im.size[1]*sc)),Image.LANCZOS)
        parts.append(im); offs.append((y,sc)); y+=im.size[1]+SEP
    H=y-SEP
    if len(parts)>1:   # the band between pieces is transparent: the page colours it (same as the number gutter), in day and night mode
        cv=Image.new('RGBA',(outw,H),(0,0,0,0))
        for im,(oy,_) in zip(parts,offs): cv.paste(im.convert('RGBA'),(0,oy))
        cv.save(OUT+name,quality=88,method=6)
    else:
        parts[0].save(OUT+name,quality=88)
    out=[]
    for m in marks:
        i,(mx0,my0,mx1,my1)=m['s'],m['b']; (bx0,by0,bx1,by1)=strips[i][1]; oy,sc=offs[i]
        mx0,mx1=max(mx0,bx0+3),min(mx1,bx1-3); my0,my1=max(my0,by0+3),min(my1,by1-3)
        o=dict(x=round((mx0-bx0)*sc/outw*100,1),y=round((oy+(my0-by0)*sc)/H*100,1),w=round((mx1-mx0)*sc/outw*100,1),h=round((my1-my0)*sc/H*100,1))
        if m.get('n'): o['n']=m['n']
        if m.get('g'): o['g']=m['g']
        if m.get('act'): o['act']=m['act']
        if m.get('side'): o['side']=m['side']
        out.append(o)
    return out
# A mark: M(piece index, (x0,y0,x1,y1) in the original, number, side of the number badge ('r' = right gutter),
#            g = belongs to mark number g but has no badge, act = 'click' | 'edit' | None (None = only check this))
M=lambda s,b,n=None,side=None,g=None,act=None: dict(s=s,b=b,n=n,side=side,g=g,act=act)
R={}
# step(code, pieces of the full picture, its marks, pieces of the phone close-up, its marks, width of the full picture)
# A piece is (original file name, (x0,y0,x1,y1)).
def step(code, wide, wmarks, narrow=None, nmarks=None, ww=1600):
    wn=f"{code}.{'webp' if len(wide)>1 else 'jpg'}"
    R[code]={'src':'img/'+wn,'marks':build(wn,wide,wmarks,ww)}
    if narrow: R[code].update(nsrc=f'img/{code}n.webp', nmarks=build(f'{code}n.webp',narrow,nmarks,920))
    # full screen (enlarged view): every original screenshot this step uses, whole, with the same marks
    files=[]
    for f,_ in wide:
        if f not in files: files.append(f)
    full=[(f,(0,0)+load(f).size) for f in files]
    fm=[dict(m, s=files.index(wide[m['s']][0])) for m in wmarks]
    R[code].update(fsrc=f'img/{code}f.webp', fmarks=build(f'{code}f.webp', full, fm, min(2048, max(load(f).size[0] for f in files))))
org=(180,15,770,100); add=(2005,708,2235,780)
step('B1',[('B1&B2.png',(0,0,2290,1080))],[M(0,org,1),M(0,add,2,act='click')],
     [('B1&B2.png',(0,0,920,215)),('B1&B2.png',(1330,690,2250,800)),('B1&B2.png',(340,690,1260,1062))],[M(0,org,1),M(1,add,2,act='click')])
step('B2',[('B3.png',(820,495,1768,1052))],[M(0,(888,698,1550,750),1,act='click'),M(0,(888,836,1170,884),2,act='click'),M(0,(1400,950,1560,1032),3,act='click')],ww=948)
# B3 is animated: the page shows week 1 (B4-1); the demo clicks the arrow and the same cut of week 2 (B4-2) fades in
# on top. Both originals line up exactly, so only Week ending and the dates change. The enlarged view shows both weeks.
arrow=(1780,690,1836,746); we=(1490,700,1774,762); dates=(1180,900,1850,995)
B3W=(340,540,2240,1010); B3N=(1000,610,1920,1010)
B3M=[M(0,arrow,1,act='click'),M(0,we,2),M(0,dates,g=2)]
step('B3',[('B4-1.png',B3W)],B3M,[('B4-1.png',B3N)],B3M)
build('B3-2.jpg',[('B4-2.png',B3W)],[],1600); build('B3n-2.webp',[('B4-2.png',B3N)],[],920)
R['B3'].update(fmarks=build('B3f.webp',[('B4-1.png',(0,0)+load('B4-1.png').size),('B4-2.png',(0,0)+load('B4-2.png').size)],
     [M(0,arrow,1,act='click'),M(1,we,2),M(1,dates,g=2)],2048))
rate=(430,838,1262,935); cells=(1278,1036,2034,1108)
step('C1',[('C2.jpeg',(370,400,2420,1290))],[M(0,rate,1,act='click'),M(0,cells,2,act='edit')],
     [('C2.jpeg',(400,405,1320,1110)),('C2.jpeg',(1250,905,2170,1200))],[M(0,rate,1,act='click'),M(1,cells,2,act='edit')])
# C2: the kilometre line, then the check and Submit (the old D1 step), on the same screenshot
al=(215,1205,520,1290); kr=(215,1110,1132,1190); kc=(1138,1110,1948,1190); sub=(1893,1430,2142,1522)
step('C2',[('D1.png',(150,480,2350,1536))],[M(0,al,1,act='click'),M(0,kr,2,act='click'),M(0,kc,3,'r',act='edit'),M(0,sub,4,act='click')],
     [('D1.png',(190,880,1150,1310)),('D1.png',(1110,880,2070,1310)),('D1.png',(1390,1410,2350,1536))],
     [M(0,al,1,act='click'),M(0,kr,2,act='click'),M(1,kc,3,act='edit'),M(2,sub,4,act='click')])
step('D1',[('D2.png',(880,555,1712,1415))],[M(0,(915,758,1674,810),1,act='click')],ww=832)   # the owner's redaction, plus the one bar above
# D2: green message, status, and (for a mistake) Revert to Draft. Mark 3 is only shown (eye): the demo must not press it.
gm=(172,408,1392,476); stt=(178,568,362,642); rv=(1150,1004,1294,1064)
step('D2',[('D3.JPG',(160,395,1400,665)),('D3.JPG',(160,985,1400,1075))],[M(0,gm,1),M(0,stt,2),M(1,rv,3)],
     [('D3.JPG',(160,400,860,482)),('D3.JPG',(160,490,860,660)),('D3.JPG',(700,985,1400,1075))],[M(0,gm,1),M(1,stt,2),M(2,rv,3)],ww=1240)
ov=(348,452,470,520); pe=(876,972,1092,1032)
step('D3',[('E1.png',(340,440,1480,1070))],[M(0,ov,1,act='click'),M(0,pe,2)],
     [('E1.png',(340,445,1260,525)),('E1.png',(340,790,1260,1065))],[M(0,ov,1,act='click'),M(1,pe,2)],ww=1140)
json.dump(R,open(os.path.join(HERE,'shots.json'),'w'),indent=1)
print('wrote', len(R), 'steps to', OUT, 'and tools/shots.json')
