# -*- coding: utf-8 -*-
"""Clean re-annotation of the two field photographs (boulder-wall site and
diamicton section) using the geometry of Nick's hand annotations: smooth dashed
contact line, neat ellipses around the sampled boulders, typeset labels."""
import numpy as np
from PIL import Image, ImageDraw, ImageFont
from scipy import ndimage
from numpy.lib.stride_tricks import sliding_window_view

A = '/mnt/user-data/attachments/427a30ae-35a3-58d0-9a17-7b191c6f0d00/'
clean1 = Image.open(A + '897e6c7f-image.jpg').convert('RGB')
clean2 = Image.open(A + '7b04f76f-image.jpg').convert('RGB')
ann1 = np.array(Image.open(A + '17f068ac-image.jpg'))

FB = ImageFont.truetype('/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf', 58)
FBig = ImageFont.truetype('/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf', 72)
FP = ImageFont.truetype('/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf', 64)

def ymask(img):
    r, g, b = img[..., 0].astype(int), img[..., 1].astype(int), img[..., 2].astype(int)
    return (r > 180) & (g > 160) & (b < 120) & (abs(r - g) < 70)

def otext(dr, xy, s, font, fill='white', anchor='la'):
    x, y = xy
    for dx in (-3, 0, 3):
        for dy in (-3, 0, 3):
            dr.text((x + dx, y + dy), s, font=font, fill='black', anchor=anchor)
    dr.text((x, y), s, font=font, fill=fill, anchor=anchor)

def dashed(dr, pts, dash=46, gap=30, width=9, color='white', outline=True):
    # pts: list of (x,y); draw dashes along polyline
    segs = []
    acc = 0.0; on = True; start = pts[0]
    import math
    def seg(p, q, c, w): dr.line([p, q], fill=c, width=w)
    i = 0
    cur = pts[0]
    for nxt in pts[1:]:
        d = math.hypot(nxt[0] - cur[0], nxt[1] - cur[1])
        if d == 0: continue
        t = 0.0
        while t < d:
            step = min((dash if on else gap) - acc, d - t)
            p = (cur[0] + (nxt[0] - cur[0]) * t / d, cur[1] + (nxt[1] - cur[1]) * t / d)
            q = (cur[0] + (nxt[0] - cur[0]) * (t + step) / d, cur[1] + (nxt[1] - cur[1]) * (t + step) / d)
            if on:
                if outline: seg(p, q, 'black', width + 6)
                segs.append((p, q))
            t += step; acc += step
            if acc >= (dash if on else gap) - 1e-6:
                acc = 0.0; on = not on
        cur = nxt
    for p, q in segs:
        seg(p, q, color, width)

def ellipse(dr, cx, cy, rx, ry, width=8):
    dr.ellipse([cx - rx - 3, cy - ry - 3, cx + rx + 3, cy + ry + 3], outline='black', width=width + 6)
    dr.ellipse([cx - rx, cy - ry, cx + rx, cy + ry], outline='white', width=width)

# ---------------- Panel (a): boulder wall ----------------
m1 = ndimage.binary_dilation(ymask(ann1), iterations=4)
H, W = m1.shape
band = m1[900:1350, :]
line = np.full(W, np.nan)
for x in range(W):
    ys = np.where(band[:, x])[0]
    if len(ys): line[x] = 900 + np.median(ys)
idx = np.arange(W); good = ~np.isnan(line)
line = np.interp(idx, idx[good], line[good])
k = 161; pad = np.pad(line, (k // 2, k // 2), mode='edge')
line = np.median(sliding_window_view(pad, k), axis=1)

img1 = clean1.copy(); dr = ImageDraw.Draw(img1)
pts = [(x, float(line[x])) for x in range(0, W, 12)]
dashed(dr, pts)

# boulders: (label, cx, rx, ry, dy offset from line)
boulders = [('P4', 238, 62, 55, 35), ('P1', 342, 58, 52, 30), ('P5', 508, 88, 75, 45),
            ('P3', 1075, 85, 72, 40), ('P7', 1236, 78, 66, 32), ('P8', 1372, 85, 72, 42),
            ('P6', 1533, 90, 78, 50), ('P2', 1906, 68, 58, 25)]
for lab, cx, rx, ry, dy in boulders:
    cy = float(line[int(cx)]) + dy
    ellipse(dr, cx, cy, rx, ry)
    otext(dr, (cx, cy - ry - 18), lab, FP, anchor='ms')

otext(dr, (2540, float(line[2500]) - 150), 'Catastro-loess silt', FB, anchor='rs')
otext(dr, (2540, float(line[2500]) + 185), 'Pebbly diamicton', FB, anchor='rs')
otext(dr, (40, 95), '(a)', FBig)

# ---------------- Panel (b): diamicton section ----------------
img2 = clean2.copy(); dr2 = ImageDraw.Draw(img2)
rings = [((52, 274, 787, 1015), ['AA1 \u2013 sandy silt'], 1),
         ((9, 183, 1343, 1554), ['AA2 \u2013 pebbly', 'diamicton'], 1),
         ((918, 1150, 1660, 1986), ['AA2 \u2013 brecciated', 'quartz vein'], 1)]
for (x0, x1, y0, y1), labs, _ in rings:
    cx, cy = (x0 + x1) / 2, (y0 + y1) / 2
    rx, ry = (x1 - x0) / 2 + 8, (y1 - y0) / 2 + 8
    ellipse(dr2, cx, cy, rx, ry)
    dr2.line([(cx + rx, cy), (cx + rx + 70, cy)], fill='black', width=14)
    dr2.line([(cx + rx, cy), (cx + rx + 70, cy)], fill='white', width=8)
    ty = cy - 34 * (len(labs) - 1) - 20
    for s in labs:
        otext(dr2, (cx + rx + 86, ty), s, FB)
        ty += 68
otext(dr2, (40, 110), '(b)', FBig)

img1.save('FigPhoto_a_boulder_wall.png')
img2.save('FigPhoto_b_diamicton_section.png')

# composite: (a) left, (b) right scaled to same height
h = img1.height
b = img2.resize((int(img2.width * h / img2.height), h), Image.LANCZOS)
comp = Image.new('RGB', (img1.width + b.width + 24, h), 'white')
comp.paste(img1, (0, 0)); comp.paste(b, (img1.width + 24, 0))
comp.save('Fig_field_photos.png')
print('saved', comp.size)
