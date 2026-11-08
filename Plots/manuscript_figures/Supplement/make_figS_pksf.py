"""Supplementary figure: PKS-F conglomerate test, lines only vs lines + planes (McFadden & McElhinny, 1988).
Inputs: pmagpy_fits (via pmag_sites) and pksf_lnp.pkl written by mcfadden_gc_check.py.
Usage: python make_figS_pksf.py <pmagpy_fits> <pksf_lnp.pkl> <outdir>"""
import sys, os, pickle, numpy as np
import matplotlib as mpl, matplotlib.pyplot as plt
from matplotlib.lines import Line2D
import pmagpy.pmag as pmag
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from pmag_sites import load, fisher, resultant, watson_ro, SLOTC
from ea_helpers import xy, net, gad_stars, dot, circle, letter, statbox
P, PK, OUT = sys.argv[1:4]; os.makedirs(OUT, exist_ok=True)
mpl.rcParams.update({'font.family': 'DejaVu Sans', 'font.size': 6, 'svg.fonttype': 'none', 'pdf.fonttype': 42})
s = load(P); g = s[(s.slot == 'HT') & (s.site == 'PKSF')]
L = pickle.load(open(PK, 'rb')); recs, bdf = L['recs'], L['bdf']
HT = SLOTC['HT']; PL = '#d95f02'

def gc(ax, pd_, pi_, c, lw=0.6):
    """great circle with pole (pd_, pi_): solid lower, dashed upper hemisphere"""
    v = pmag.dir2cart([pd_, pi_, 1.0]); v = v / np.linalg.norm(v)
    u = np.cross(v, [0, 0, 1.0]); u = u / np.linalg.norm(u) if np.linalg.norm(u) > 1e-6 else np.array([1.0, 0, 0]); w = np.cross(v, u)
    t = np.linspace(0, 2 * np.pi, 361); P3 = np.cos(t)[:, None] * u + np.sin(t)[:, None] * w
    di = np.array([pmag.cart2dir(p)[:2] for p in P3]); x, y = xy(di[:, 0], di[:, 1]); lo = di[:, 1] >= 0
    for seg in (True, False):
        m = lo == seg; ax.plot(np.where(m, x, np.nan), np.where(m, y, np.nan), color=c, lw=lw, ls='-' if seg else (0, (2, 1.2)), zorder=3)

fig = plt.figure(figsize=(7.09, 3.3))
# (a) lines only (MAD <= 15), as in Fig. 7r
ax = fig.add_axes([0.03, 0.27, 0.30, 0.60]); net(ax); gad_stars(ax, 22)
dot(ax, g.dir_dec, g.dir_inc, '0.7', s=4, lw=0.3, z=2)
bm = {}
for b, x in g.groupby('boulder'):
    m = fisher(x.dir_dec, x.dir_inc); bm[b] = m
    circle(ax, m['dec'], m['inc'], m['a95'], HT, lw=0.6); dot(ax, m['dec'], m['inc'], HT, s=20, marker='s', ec='k', lw=0.45, z=6)
R = resultant([m['dec'] for m in bm.values()], [m['inc'] for m in bm.values()]); r95, r99 = watson_ro(len(bm))
letter(ax, 'a', 'Lines only', 'HT fits with MAD ≤ 15° (as in Fig. 7r)')
statbox(ax, [(f'N = {len(bm)} boulders · R = {R:.2f}', '0.15'), (f'Ro95 {r95:.2f} · Ro99 {r99:.2f}', '0.15'), ('CLUSTERED (fail)' if R >= r95 else 'RANDOM (pass)', '#b2182b' if R >= r95 else '#1b7837')])
# (b) lines + planes
ax = fig.add_axes([0.36, 0.27, 0.30, 0.60]); net(ax); gad_stars(ax, 22)
for unit, rl in recs.items():
    for r in rl:
        if r['method_codes'] == 'DE-BFP': gc(ax, r['dir_dec'], r['dir_inc'], PL, 0.45)
        else: dot(ax, r['dir_dec'], r['dir_inc'], '0.7', s=4, lw=0.3, z=2)
for _, r in bdf.iterrows():
    mixed = r.n_planes > 0
    dot(ax, r.dec, r.inc, PL if mixed else HT, s=22, marker='s', ec='k', lw=0.45, z=6)
    if mixed:
        old = bm.get(r.unit)
        if old is not None:
            (x0, y0), (x1, y1) = [np.ravel(xy(a, b)) for a, b in [(old['dec'], old['inc']), (r.dec, r.inc)]]
            ax.annotate('', xy=(x1, y1), xytext=(x0, y0), arrowprops=dict(arrowstyle='-|>', color='k', lw=0.6, mutation_scale=6, shrinkA=2, shrinkB=3), zorder=7)
            dot(ax, old['dec'], old['inc'], HT, s=12, marker='s', ec='k', lw=0.3, z=5, alpha=0.6)
        xb, yb = np.ravel(xy(r.dec, r.inc)); ax.annotate(r.unit.replace('PKSF-', ''), (xb, yb), xytext=(4, 3), textcoords='offset points', fontsize=5.2, fontweight='bold', zorder=8)
R2 = resultant(bdf.dec, bdf.inc); q95, q99 = watson_ro(len(bdf))
letter(ax, 'b', 'Lines + planes', 'unresolved specimens as remagnetization circles')
statbox(ax, [(f'N = {len(bdf)} boulders · R = {R2:.2f}', '0.15'), (f'Ro95 {q95:.2f} · Ro99 {q99:.2f}', '0.15'), ('CLUSTERED (fail)' if R2 >= q95 else 'RANDOM (pass)', '#b2182b' if R2 >= q95 else '#1b7837')])
# (c) table of boulder means
ax = fig.add_axes([0.70, 0.12, 0.29, 0.78]); ax.axis('off')
ax.text(0, 1.0, 'c  Boulder means (lines + planes)', fontsize=7, fontweight='bold', va='bottom', transform=ax.transAxes)
rows = ['Boulder   D/I (°)      lines planes']
for _, r in bdf.iterrows():
    rows.append(f"{r.unit.replace('PKSF-', ''):<8} {r.dec:5.1f}/{r.inc:+5.1f}  {int(r.n_lines):>4} {int(r.n_planes):>5}")
ax.text(0, 0.97, '\n'.join(rows), family='DejaVu Sans Mono', fontsize=5.6, va='top', transform=ax.transAxes)
ax.text(0, 0.30, 'Boulders 3 and 4 do not isolate a stable endpoint\nby 450–510 °C; their arcs are fitted as great circles\n(orange) and combined with the resolved lines\n(McFadden & McElhinny, 1988). Arrows: line-only\nmean → lines + planes mean. Both boulders move\ntoward the northerly, shallow cluster, so R rises\nfrom 5.31 to 6.09 and the fail is strengthened.',
        fontsize=5.4, va='top', transform=ax.transAxes, color='0.25')
lg = fig.add_axes([0.0, 0.0, 1.0, 0.09]); lg.axis('off')
h = [Line2D([], [], ls='', marker='o', ms=2.6, color='0.7', label='specimen line (filled lower / open upper)'),
     Line2D([], [], color=PL, lw=0.8, label='remagnetization circle (dashed: upper hem.)'),
     Line2D([], [], ls='', marker='s', ms=4, mfc=HT, mec='k', mew=0.4, label='boulder mean (lines)'),
     Line2D([], [], ls='', marker='s', ms=4, mfc=PL, mec='k', mew=0.4, label='boulder mean (lines + planes)'),
     Line2D([], [], ls='', marker='*', ms=5, mfc='k', mec='k', label='GAD normal / reversed (open)')]
lg.legend(handles=h, loc='center', ncol=5, fontsize=5.2, frameon=False, handletextpad=0.3, columnspacing=1.0)
for ext in ['svg', 'pdf', 'png']:
    fig.savefig(os.path.join(OUT, f'FigS_PKSF_lines_planes.{ext}'), dpi=400 if ext == 'png' else None, bbox_inches='tight', pad_inches=0.03)
print('R lines', round(R, 2), 'R L+P', round(R2, 2))
