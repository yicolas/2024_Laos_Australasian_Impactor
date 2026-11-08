"""Figure 3 — (a) composite stratigraphy of the Bolaven target (redrawn from the LEAD_3 column)
and (b) composite sketch of the proximal-to-distal ejecta breccia (redrawn after Sieh et al.,
Fig. 2 of the proximal-ejecta manuscript). All vector; text stays editable in Illustrator/Inkscape
(SVG text as <text>, PDF Type-42 fonts). Every element carries a gid for easy selection.
Usage: python make_fig3.py <outdir>"""
import sys, os
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
import matplotlib.patheffects as pe
from matplotlib.patches import Polygon, Rectangle, Ellipse, FancyArrowPatch, PathPatch, Arc
from matplotlib.path import Path
from scipy.interpolate import interp1d

OUT = sys.argv[1] if len(sys.argv) > 1 else '.'; os.makedirs(OUT, exist_ok=True)
mpl.rcParams.update({'font.family': 'DejaVu Sans', 'font.size': 7, 'svg.fonttype': 'none',
                     'pdf.fonttype': 42, 'hatch.linewidth': 0.5, 'axes.linewidth': 0.6})
rng = np.random.default_rng(7)

# palette
SAPRO = '#c96a22'; BASALT = '#5b5c63'; SST = '#e8d18b'; MUD = '#c98a6a'
WB = '#e9973a'; WB_E = '#a8641e'; UB = '#d93a33'; SSC = '#8c7887'; VQ = '#f5e74a'
MZS = '#a69aa8'; MZM = '#c9a7b8'; SILT_DOT = '#555555'

PH_IN, PY0_IN = 1.38, 0.86                 # field-photo row (d-h): height and bottom (inches)
FIG_H = PY0_IN + PH_IN + 0.2365 + 3.03 + 0.2365
fig = plt.figure(figsize=(7.09, FIG_H))   # 180 mm wide
LEG_H = 0.80 / FIG_H                       # legend strip height (fraction)
TOP, BOT = 1 - 0.2365 / FIG_H, (PY0_IN + PH_IN + 0.2365) / FIG_H   # shared top/bottom edges for panels a-c
LAB_Y = 1 - 0.0215 / FIG_H               # common baseline for panel letters
def panel_letter(x, s): fig.text(x, LAB_Y, s, fontsize=10, fontweight='bold', va='top', ha='left')

# =============================== (a) magnetostratigraphy ===============================
M = fig.add_axes([0.058, BOT, 0.165, TOP - BOT])
AGE_MAX = 1440                     # base of record = WBE-A, the lowest basalt flow
M.set_ylim(AGE_MAX, 0); M.set_xlim(0, 10)
M.spines[['top', 'right', 'bottom']].set_visible(False); M.set_xticks([])
M.set_yticks(range(0, 1401, 200)); M.set_ylabel('Age (ka)', labelpad=1)
M.tick_params(axis='y', labelsize=6, length=2, pad=1)
# GPTS 2020 (Ogg, 2020): normal intervals
NORMAL = [(0, 773, 'Brunhes'), (990, 1071, 'Jaramillo'), (1180, 1215, 'Cobb Mtn')]
BAR = (0.0, 1.7)
M.add_patch(Rectangle((BAR[0], 0), BAR[1] - BAR[0], AGE_MAX, fc='white', ec='black', lw=0.6, gid='a_gpts_reversed'))
for t0, t1, nm in NORMAL:
    M.add_patch(Rectangle((BAR[0], t0), BAR[1] - BAR[0], t1 - t0, fc='black', ec='black', lw=0.6, gid='a_gpts_normal'))
M.text(2.15, 386, 'Brunhes (C1n)', rotation=90, color='black', fontsize=5.8, ha='center', va='center', gid='a_chron_labels')
M.text(2.15, 1106, 'Matuyama (C1r)', rotation=90, color='black', fontsize=5.8, ha='center', va='center', gid='a_chron_labels')
M.text(2.75, 1030, 'Jaramillo', fontsize=5, va='center', ha='left', color='#333', gid='a_chron_labels')
M.text(2.75, 1197, 'Cobb Mtn', fontsize=5, va='center', ha='left', color='#333', gid='a_chron_labels')
# impact level
IMP = 790
M.axhline(IMP, xmin=0, xmax=1, color='#c1121f', lw=1.0, ls=(0, (4, 2)), gid='a_impact_level')
M.text(9.9, IMP + 18, 'impact ~790 ka', color='#c1121f', fontsize=5.6, ha='right', va='top', gid='a_impact_label')
# sites (LEAD_3 Table 1): name, age, 2s, measured polarity, result
SITES = [('PKS-K', 407, 18, 'R', 'fail'), ('NWF-A', 518, 6, 'N', 'pass'), ('PKS-J', 601, 44, 'R', 'fail'),
         ('PKS-H', 770, 9.3, 'R', 'disturbed'), ('PKS-B', 1155, 2, 'R', 'pass'), ('WBE-A', 1397, 13, 'R', 'pass')]
CLASTS = [('PKS-I', 553, 20), ('NWF-B', 934, 30)]
XS = 5.7
for nm, age, e, pol, res in SITES:
    M.errorbar(XS, age, yerr=e, fmt='none', ecolor='black', elinewidth=0.6, capsize=1.5, gid='a_site_errors')
    M.scatter(XS, age, s=22, marker='o', facecolor='black' if pol == 'N' else 'white', edgecolor='black', lw=0.7, zorder=5, gid='a_sites')
    ly = age + {'NWF-A': -22, 'PKS-J': 20}.get(nm, 0)
    M.text(XS + 0.75, ly, nm, fontsize=6, va='center', ha='left', gid='a_site_labels')
for nm, age, e in CLASTS:
    M.errorbar(XS, age, yerr=e, fmt='none', ecolor='#888', elinewidth=0.6, capsize=1.5)
    M.scatter(XS, age, s=18, marker='D', facecolor='#d9d9d9', edgecolor='#666', lw=0.6, zorder=5, gid='a_clast_sites')
    M.text(XS + 0.75, age, nm, fontsize=6, va='center', ha='left', color='#666', gid='a_site_labels')
panel_letter(0.005, 'a')

# =============================== (b) composite column ===============================
A = fig.add_axes([0.235, BOT, 0.255, TOP - BOT]); A.set_xlim(0, 10); A.set_ylim(0.3, 12.6); A.axis('off')
x0, x1 = 0.1, 2.3
def unit(y0, y1, gid, **kw):
    r = Rectangle((x0, y0), x1 - x0, y1 - y0, lw=0.8, ec='black', **kw); r.set_gid(gid); A.add_patch(r); return r
unit(0.3, 3.5, 'b_mudstone', fc=MUD, hatch='..')
unit(3.5, 6.6, 'b_sandstone', fc=SST)
for y in [3.9, 4.65, 5.4, 6.15]:
    A.plot([x0 + 0.3, x0 + 1.2], [y, y + 0.15], color='#6b5520', lw=0.6, gid='b_crossbeds')
unit(6.75, 11.6, 'b_basalt', fc=BASALT)
for y in [7.5, 8.25, 10.1, 10.85]:
    A.plot([x0, x1], [y, y], color='black', lw=0.5, ls=(0, (3, 2)), gid='b_flow_contacts')
v = rng.uniform([x0 + 0.15, 6.9], [x1 - 0.15, 11.45], (55, 2))
A.scatter(v[:, 0], v[:, 1], s=4, c='#d9d9d9', lw=0, gid='b_vesicles')
IMP_Y = 9.15
A.plot([x0, x1], [IMP_Y, IMP_Y], color='#ff4d5a', lw=1.4, ls=(0, (4, 2)), gid='b_impact_level')
unit(11.6, 12.6, 'b_saprolite', fc=SAPRO, hatch='xx')
xx = np.linspace(x0, x1, 200); A.plot(xx, 6.67 + 0.05 * np.sin(xx * 14), color='black', lw=1.3, gid='b_unconformity')
A.add_patch(Rectangle((x0, 6.6), x1 - x0, 0.15, fc='white', ec='none', zorder=0))
tx = x1 + 0.3
def T(y, s, **kw): A.text(tx, y, s, va='center', ha='left', fontsize=6, **kw)
T(12.1, 'Lateritic / bauxitic saprolite')
T(11.15, 'Bolaven basalt cap (≤300 m;\n~16 Ma–27 ka); buries crater')
T(10.0, 'post-impact flows:\nNWF-A, PKS-J, PKS-K', color='#1f4e8c')
T(IMP_Y, '~790 ka impact level', color='#c1121f', fontweight='bold')
T(8.3, 'pre-impact flows: PKS-B;\nWBE-A = basal flow', color='#1f4e8c')
T(6.68, 'erosional unconformity; off-\nplateau the ejecta breccia (c)\nrests on this surface', style='italic')
T(5.05, 'Khorat Gp. sandstone\n(200–250 m, cross-bedded\nfluvial quartz arenite)')
T(1.9, 'Khorat Gp. mudstone /\nsiltstone (~250 m, fluvial–\nfloodplain red beds)')
panel_letter(0.232, 'b')
# tie line: impact age in (a) -> impact level in (b)
from matplotlib.patches import ConnectionPatch
fig.add_artist(ConnectionPatch(xyA=(10, IMP), coordsA=M.transData, xyB=(x0, IMP_Y), coordsB=A.transData,
                               color='#c1121f', lw=0.8, ls=(0, (2, 2)), gid='ab_impact_tie'))

# =============================== (b) breccia sketch ===============================
B = fig.add_axes([0.50, BOT, 0.495, TOP - BOT]); B.set_xlim(0, 108); B.set_ylim(0, 63.5); B.axis('off')
panel_letter(0.495, 'c')
# --- key surfaces (x from proximal 0 to distal 100)
xs = np.linspace(0, 100, 400)
f_sub = interp1d([0, 20, 25, 40, 50, 52, 60, 72, 80, 88, 100], [8.5, 7.8, 8.2, 8.0, 8.8, 9.6, 9.8, 12.0, 16.0, 20.5, 21.5], kind='quadratic')
f_top = interp1d([0, 3, 6, 9, 12, 16, 22, 27, 35, 45, 55, 63, 70, 78, 88, 100], [53, 51.5, 48, 47, 48, 47.6, 47.3, 46, 43.5, 39.5, 35.5, 32.5, 29.6, 28.6, 28.2, 28.3], kind='quadratic')
silt_top = [(0, 60), (25, 59.5), (45, 57.5), (47, 63), (70, 62), (71, 50), (85, 49.5), (90, 45), (100, 45)]
sub = f_sub(xs); top = f_top(xs)

# substrate blocks
def band(xa, xb, gid, **kw):
    m = (xs >= xa) & (xs <= xb)
    p = Polygon(np.vstack([np.c_[xs[m], sub[m]], [[xb, 0], [xa, 0]]]), lw=0.6, ec='#333333', **kw); p.set_gid(gid); B.add_patch(p)
band(0, 24, 'b_Mz_sandstone', fc=MZS, hatch='....')
band(24, 51, 'b_basalt_flow', fc=WB)
band(51, 100, 'b_Mz_mudstone', fc=MZM, hatch='...')
for cx, cy, r in [(28, 4.3, 2.6), (33.5, 3.0, 2.2), (32.5, 7.0, 1.4), (38.5, 3.5, 3.3), (43.5, 6.3, 1.9), (44.5, 2.4, 1.8), (48.5, 4.6, 2.0), (36, 7.3, 1.2), (26.5, 7.2, 1.0)]:
    th = np.linspace(0, 2 * np.pi, 40); rr = r * (1 + 0.12 * np.sin(3 * th + cx))
    for k, (fc, sc) in enumerate([(WB, 1.18), (UB, 1.0)]):
        p = Polygon(np.c_[cx + sc * rr * np.cos(th), cy + 0.75 * sc * rr * np.sin(th)], fc=fc, ec=WB_E, lw=0.4, gid='b_corestones'); B.add_patch(p)

# breccia body
brec = Polygon(np.vstack([np.c_[xs, top], np.c_[xs[::-1], sub[::-1]]]), fc='white', ec='black', lw=0.9, gid='b_breccia_outline'); B.add_patch(brec)
# sandy silt
sx = np.array([p[0] for p in silt_top]); sy = np.array([p[1] for p in silt_top])
silt = Polygon(np.vstack([np.c_[sx, sy], np.c_[xs[::-1], top[::-1]]]), fc='white', ec='black', lw=0.9, gid='b_sandy_silt'); B.add_patch(silt)
from matplotlib.path import Path as MPath
sp = MPath(np.vstack([np.c_[sx, sy], np.c_[xs[::-1], top[::-1]]]))
pts = rng.uniform([0, 25], [100, 63], (2200, 2)); pts = pts[sp.contains_points(pts)]
ang = rng.uniform(0, np.pi, len(pts)); L = 0.28
segs = np.stack([np.c_[pts[:, 0] - L * np.cos(ang), pts[:, 1] - L * np.sin(ang)], np.c_[pts[:, 0] + L * np.cos(ang), pts[:, 1] + L * np.sin(ang)]], 1)
from matplotlib.collections import LineCollection
B.add_collection(LineCollection(segs, colors=SILT_DOT, lw=0.3, gid='b_silt_texture'))
for gx, gy in [(40, 57.6), (86, 46.5)]:   # grass
    for d in [-1, 1]:
        t = np.linspace(0, 1, 20); B.plot(gx + d * 3 * t ** 2, gy + 6 * t, color='#5aad4e', lw=0.9, gid='b_grass')
# pebble lag at breccia top (proximal & distal)
for xa, xb in [(0, 38), (62, 100)]:
    px = rng.uniform(xa, xb, 140); py = f_top(px) + rng.uniform(0.2, 1.8, 140)
    B.scatter(px, py, s=1.6, c='black', lw=0, gid='b_pebble_lag')

# breccia clasts
brp = MPath(np.vstack([np.c_[xs, top - 0.8], np.c_[xs[::-1], sub[::-1] + 0.6]]))
occupied = []
def free(x, y, r):
    return all(np.hypot(x - a, y - b) > r + c for a, b, c in occupied)
def blob(cx, cy, r, n=9, irr=0.28):
    th = np.sort(rng.uniform(0, 2 * np.pi, n)); rr = r * (1 + rng.uniform(-irr, irr, n))
    return np.c_[cx + rr * np.cos(th), cy + 0.8 * rr * np.sin(th)]
# unweathered basalt boulders (proximal, upper)
for cx, cy, r in [(7.5, 42.5, 4.0), (19.5, 41.0, 5.6), (13.0, 33.5, 2.4)]:
    p = Polygon(blob(cx, cy, r, 22, 0.07), closed=True, fc=UB, ec='#7a1a15', lw=0.4, gid='b_unweathered_basalt'); B.add_patch(p)
    occupied.append((cx, cy, r * 1.1))
# sandstone clasts (mid-distal, upper)
for cx, cy, r in [(48, 30.5, 1.3), (54, 27.5, 1.1), (57.5, 25.0, 0.9), (60.5, 31.5, 1.6), (64.5, 24.0, 3.2)]:
    p = Polygon(blob(cx, cy, r, 10, 0.18), fc=SSC, ec='#4f3f4c', lw=0.4, gid='b_sandstone_clasts'); B.add_patch(p); occupied.append((cx, cy, r * 1.1))
p = Polygon([[58, 37.0], [64, 34.2], [66.5, 33.0], [60, 35.6]], fc=SSC, ec='#4f3f4c', lw=0.4, gid='b_sandstone_clasts'); B.add_patch(p)
# weathered-basalt corestones with rinds (proximal, low)
for cx, cy, r in [(10.5, 16.5, 3.0), (20.5, 14.5, 1.6)]:
    for sc in [1.0, 0.85, 0.7]:
        th = np.linspace(0, 2 * np.pi, 50)
        B.add_patch(Polygon(np.c_[cx + sc * r * np.cos(th), cy + 0.8 * sc * r * np.sin(th)], fc=WB if sc == 1 else 'none', ec=WB_E, lw=0.4, gid='b_weathered_corestones'))
    occupied.append((cx, cy, r * 1.1))
# vein quartz (distal, low)
for cx, cy, w, h in [(55, 12.5, 1.6, 2.2), (59.5, 14.5, 2.4, 1.6), (64, 13.0, 1.2, 1.3), (67.5, 16.0, 1.6, 1.2), (66, 19.8, 1.0, 1.0),
                     (70.0, 21.0, 1.4, 1.0), (72.5, 18.0, 1.2, 1.0), (51.5, 11.5, 1.2, 0.9), (61.5, 18.8, 1.0, 0.9)]:
    B.add_patch(Ellipse((cx, cy), w * 1.6, h * 1.2, fc=VQ, ec='#9a8a10', lw=0.4, gid='b_vein_quartz')); occupied.append((cx, cy, max(w, h)))
for cx, cy in [(57.5, 9.2), (52.5, 14.5)]:
    B.add_patch(Rectangle((cx, cy), 0.9, 2.6, fc=VQ, ec='#9a8a10', lw=0.4, gid='b_vein_quartz'))
# many small weathered-basalt clasts, fining distally
n_try = 0; placed = 0
while placed < 420 and n_try < 20000:
    n_try += 1
    x = rng.uniform(0.5, 99.5); y = rng.uniform(1, 55)
    if not brp.contains_point((x, y)): continue
    r = (0.68 - 0.0042 * x) * rng.uniform(0.7, 1.2)
    if not free(x, y, r * 2.2): continue
    shape = rng.choice(['chip', 'blob'], p=[0.65, 0.35])
    if shape == 'chip':
        a = rng.uniform(-0.6, 0.6); k = rng.uniform(1.0, 1.5)
        pts_ = np.array([[-k, 0], [0, 0.6], [k, 0.1], [0.2, -0.6]]) * r
        R = np.array([[np.cos(a), -np.sin(a)], [np.sin(a), np.cos(a)]]); poly = pts_ @ R.T + [x, y]
    else:
        poly = blob(x, y, r, 7, 0.35)
    B.add_patch(Polygon(poly, fc=WB, ec=WB_E, lw=0.3, gid='b_weathered_basalt_clasts')); occupied.append((x, y, r)); placed += 1
# onion-skin arcs (weathering-rind fragments)
for cx, cy in [(19, 25), (33, 24.5), (37, 19), (47, 20), (26, 21)]:
    for k in range(3):
        B.add_patch(Arc((cx + k * 0.6, cy), 3.0 - 0.6 * k, 2.4 - 0.5 * k, theta1=200, theta2=330, color=WB_E, lw=0.5, gid='b_rind_arcs'))
# distal fluvial-gravel lens (pre-impact substrate)
lens = Polygon([[84, 21.0], [86.5, 27.2], [100, 27.6], [100, 21.4]], fc='white', ec='black', lw=0.5, gid='b_fluvial_gravels'); B.add_patch(lens)
lp = MPath(lens.get_xy())
g = rng.uniform([84, 20.5], [100, 27.6], (500, 2)); g = g[lp.contains_points(g)][:110]
cols = rng.choice([UB, VQ, SSC, WB], len(g))
for (gx, gy), c in zip(g, cols): B.add_patch(Ellipse((gx, gy), 0.9, 0.55, fc=c, ec='#333333', lw=0.2, gid='b_fluvial_gravels'))
# tektites along the breccia top
for tx_ in [3.0, 15.5, 31.0, 44.0, 57.5, 76.0, 86.0, 93.0, 98.0]:
    ty = f_top(tx_) - (0.8 if tx_ < 40 else 0.3)
    B.text(tx_, ty, 'T', fontsize=6.5, fontweight='bold', ha='center', va='top', gid='b_tektites')
    B.add_patch(Ellipse((tx_ - 1.0, ty - 0.3), 0.9, 0.5, fc='black', ec='none', gid='b_tektites'))
B.text(1.5, 58.8, 'Proximal', fontsize=7.5, va='top', gid='b_label')
B.text(98.5, 44.0, 'Distal\n(>100 km)', fontsize=7.5, va='top', ha='right', gid='b_label')
B.annotate('', xy=(103, 63.3), xytext=(103, 0.3), xycoords='data', annotation_clip=False,
           arrowprops=dict(arrowstyle='<|-|>', lw=0.8, color='black', mutation_scale=7))
B.text(105.2, 31, '~0.5 to 10 m', rotation=90, va='center', ha='center', fontsize=7)

# field photographs (d-h): in-situ flows vs basalt boulders in the diamicton (2024 field season)
from PIL import Image, ImageOps
PHOTOS = [('Image 44.jpg', 'd', 'WBE-A: basal flow', (0.5, 0.55)), ('Image 79.jpg', 'e', 'NWF-A: flow in stream bed', (0.5, 0.6)),
          ('Image 91.jpg', 'f', 'NWF-C: boulders in diamicton', (0.45, 0.5)), ('Image 93.jpg', 'g', 'NWF-C: boulder being oriented', (0.5, 0.5)),
          ('Image 103.jpg', 'h', 'PKS-G: boulders, coffee farm', (0.5, 0.5))]
PW_IN = (0.99 * 7.09 - 4 * 0.06) / 5
for k, (fn, L, lab, (fx, fy)) in enumerate(PHOTOS):
    im = ImageOps.exif_transpose(Image.open(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'photos', fn))).convert('RGB')
    w, h = im.size; ar = PW_IN / PH_IN
    if w / h > ar: cw, ch = int(h * ar), h
    else: cw, ch = w, int(w / ar)
    x0 = int(min(max(fx * w - cw / 2, 0), w - cw)); y0 = int(min(max(fy * h - ch / 2, 0), h - ch))
    im = im.crop((x0, y0, x0 + cw, y0 + ch)); im.thumbnail((900, 900))
    ax = fig.add_axes([(0.005 * 7.09 + k * (PW_IN + 0.06)) / 7.09, PY0_IN / FIG_H, PW_IN / 7.09, PH_IN / FIG_H])
    ax.imshow(im, interpolation='lanczos'); ax.set_xticks([]); ax.set_yticks([])
    for sp in ax.spines.values(): sp.set_linewidth(0.5)
    ax.text(0.03, 0.97, L, transform=ax.transAxes, fontsize=10, fontweight='bold', color='white', va='top', ha='left',
            path_effects=[pe.withStroke(linewidth=1.6, foreground='black')])
    ax.text(0.0, 1.02, lab, transform=ax.transAxes, fontsize=6, va='bottom', ha='left')

# legend strip across the bottom (proxy artists; editable). 1 x-unit = 1 y-unit physically.
LG = fig.add_axes([0.005, 0.005, 0.99, LEG_H]); LGW = 0.99 * 7.09; LG.set_xlim(0, 220); LG.set_ylim(0, 220 * LEG_H * FIG_H / LGW); LG.axis('off')
def sw(x, y, kind):
    if kind in ('N', 'R'):
        LG.scatter(x + 2.2, y, s=18, facecolor='black' if kind == 'N' else 'white', edgecolor='black', lw=0.6)
    elif kind == 'clast':
        LG.scatter(x + 2.2, y, s=14, marker='D', facecolor='#d9d9d9', edgecolor='#666', lw=0.6)
    elif kind == 'err':
        LG.errorbar(x + 2.2, y, yerr=1.5, fmt='none', ecolor='black', elinewidth=0.6, capsize=1.5)
    elif kind == 'chk':
        LG.text(x + 0.3, y, '✓', color='#2a7d2e', fontsize=7, fontweight='bold', va='center'); LG.text(x + 2.6, y, '✗', color='#c1121f', fontsize=7, fontweight='bold', va='center')
    elif kind == 'imp':
        LG.plot([x, x + 4.5], [y, y], color='#c1121f', lw=1.0, ls=(0, (4, 2)))
    elif kind == 'silt':
        LG.add_patch(Rectangle((x, y - 1.1), 4.5, 2.2, fc='white', ec='#777', lw=0.4))
        for _ in range(14):
            a, b = rng.uniform(x + 0.3, x + 4.2), rng.uniform(y - 0.9, y + 0.9); t = rng.uniform(0, np.pi)
            LG.plot([a - 0.3 * np.cos(t), a + 0.3 * np.cos(t)], [b - 0.3 * np.sin(t), b + 0.3 * np.sin(t)], color=SILT_DOT, lw=0.35)
    elif kind == 'lag':
        LG.scatter(rng.uniform(x, x + 4.5, 14), rng.uniform(y - 0.8, y + 0.8, 14), s=1.6, c='k', lw=0)
    elif kind == 'tek':
        LG.text(x + 1.5, y + 0.9, 'T', fontsize=6.5, fontweight='bold', ha='center', va='top'); LG.add_patch(Ellipse((x + 0.5, y + 0.2), 0.9, 0.6, fc='k'))
    elif kind == 'vq':
        LG.add_patch(Rectangle((x, y - 0.7), 1.6, 1.4, fc=VQ, ec='#9a8a10', lw=0.4)); LG.add_patch(Ellipse((x + 3.3, y), 2.2, 1.6, fc=VQ, ec='#9a8a10', lw=0.4))
    elif kind == 'ss':
        LG.add_patch(Polygon(blob(x + 1.2, y, 1.0, 9, 0.2), fc=SSC, ec='#4f3f4c', lw=0.4)); LG.add_patch(Polygon(blob(x + 3.5, y, 0.8, 8, 0.2), fc=SSC, ec='#4f3f4c', lw=0.4))
    elif kind == 'wb':
        LG.add_patch(Polygon([[x, y - 0.4], [x + 1.4, y + 0.7], [x + 2.2, y - 0.1], [x + 0.9, y - 0.8]], fc=WB, ec=WB_E, lw=0.3))
        LG.add_patch(Arc((x + 3.6, y), 2.2, 1.9, theta1=200, theta2=330, color=WB_E, lw=0.6))
    elif kind == 'ub':
        LG.add_patch(Polygon(blob(x + 2.2, y, 1.6, 12, 0.1), fc=UB, ec='#7a1a15', lw=0.4))
    elif kind == 'flow':
        LG.add_patch(Rectangle((x, y - 1.1), 4.5, 2.2, fc=WB, ec='#333', lw=0.4)); LG.add_patch(Ellipse((x + 2.2, y), 2.4, 1.6, fc=UB, ec=WB_E, lw=0.4))
    elif kind == 'grav':
        LG.add_patch(Rectangle((x, y - 1.1), 4.5, 2.2, fc='white', ec='#333', lw=0.4))
        for k, c in enumerate([UB, VQ, SSC, WB, UB, VQ]):
            LG.add_patch(Ellipse((x + 0.6 + 0.65 * k, y + (0.45 if k % 2 else -0.45)), 0.8, 0.55, fc=c, ec='#333', lw=0.2))
    elif kind == 'mzs':
        LG.add_patch(Rectangle((x, y - 1.1), 4.5, 2.2, fc=MZS, ec='#333', lw=0.4, hatch='....'))
    elif kind == 'mzm':
        LG.add_patch(Rectangle((x, y - 1.1), 4.5, 2.2, fc=MZM, ec='#333', lw=0.4, hatch='...'))
YT = LG.get_ylim()[1]; ROW = (YT - 1.0) / 5
COLS = [(1, [('h', 'a  Paleomagnetic sites'), ('N', 'Flow, normal polarity'), ('R', 'Flow, reversed polarity'),
             ('clast', 'Clast / conglomerate site'), ('err', 'Ar/Ar age ±2σ (Table 1)')]),
        (52, [('h', 'c  Cover and breccia'), ('silt', 'Sandy silt'), ('lag', 'Pebble lag'), ('tek', 'Tektites'), ('vq', 'Vein quartz')]),
        (96, [('h', ''), ('ss', 'Sandstone clasts'), ('wb', 'Weathered basalt clasts, rinds'), ('ub', 'Unweathered basalt'), ('imp', 'Impact level (~790 ka; a, b)')]),
        (145, [('h', 'c  Pre-impact substrate'), ('flow', 'Weathered basalt flow'), ('grav', 'Fluvial gravels'), ('mzs', 'Mesozoic sandstone'), ('mzm', 'Mesozoic mudstone')])]
for cx, items in COLS:
    y = YT - 0.5 - ROW / 2
    for kind, label in items:
        if kind == 'h':
            LG.text(cx, y, label, fontsize=6.5, fontweight='bold', va='center')
        else:
            sw(cx + 0.5, y, kind); LG.text(cx + 6.5, y, label, fontsize=6, va='center')
        y -= ROW
LG.text(219, 0.4, 'Panel c redrawn and\nmodified after\nSieh et al. (2023)', fontsize=5.6, style='italic', ha='right', va='bottom')
LG.plot([0.5, 219.5], [YT - 0.15, YT - 0.15], color='#999', lw=0.4)

for ext in ['svg', 'pdf', 'png']:
    fig.savefig(os.path.join(OUT, f'Fig3_stratigraphy.{ext}'), dpi=400 if ext == 'png' else None, bbox_inches='tight', pad_inches=0.03)
print('done')
