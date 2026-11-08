"""Figure 7 (was Fig 8) — paleomagnetic directions (consolidates LEAD_4 Figs 12 and 13), geographic coordinates, no tilt correction.
(a) in-situ site-mean ChRM (HT) directions, specimen -> core -> site; (b) site VGPs;
(c-n) every site: all specimen component fits (grey) with LT / MT / HT Fisher means (squares) and alpha95, fitquest colours;
(o-t) conglomerate tests (Watson 1956, Monte-Carlo Ro) on boulder-mean HT directions.
Equal-area, lower hemisphere filled / upper open.  Usage: python make_fig8.py <pmagpy_fits_dir> <outdir>"""
import sys, os, numpy as np
import matplotlib as mpl, matplotlib.pyplot as plt
from matplotlib.lines import Line2D
import cartopy.crs as ccrs, cartopy.feature as cfeature
import pmagpy.pmag as pmag
from pmag_sites import load, fisher, two_tier, vgp, watson_ro, resultant, SLOTC, GAD, NAME, LAT, LON

P, OUT = sys.argv[1], sys.argv[2]; os.makedirs(OUT, exist_ok=True)
mpl.rcParams.update({'font.family': 'DejaVu Sans', 'font.size': 6, 'axes.linewidth': 0.6, 'svg.fonttype': 'none',
                     'pdf.fonttype': 42})
s = load(P)
PCOL = {'N': '#2c6fb0', 'R': '#c8372d', 'disturbed': '#e08a1e', 'clast': '0.55'}
AGE = {'PKSK': '407 ± 18 ka', 'NWFA': '518 ± 6 ka', 'PKSI': '553 ± 20 ka', 'PKSJ': '601 ± 44 ka', 'PKSH': '~770–800 ka',
       'PKSB': '1155 ± 2 ka', 'WBEA': '1397 ± 13 ka', 'NWFB': '934 ± 30 ka', 'NWFC': 'diamicton', 'PKQA': 'diamicton',
       'PKSF': 'diamicton', 'PKSG': 'diamicton'}
KIND = {'PKSK': 'in-situ flow', 'NWFA': 'in-situ flow', 'PKSI': 'corestone', 'PKSJ': 'in-situ flow', 'PKSH': 'two horizons',
        'PKSB': 'in-situ flow', 'WBEA': 'basal flow', 'NWFB': 'blocks', 'NWFC': 'boulders', 'PKQA': 'boulders',
        'PKSF': 'boulders', 'PKSG': 'boulders'}

AMAX = 60     # alpha95 circles larger than this are listed in the stats box but not drawn
# ---------------- equal-area helpers ----------------
def xy(dec, inc):
    dec, inc = np.radians(np.atleast_1d(dec)), np.radians(np.abs(np.atleast_1d(inc)))
    r = np.sqrt(2) * np.sin((np.pi / 2 - inc) / 2)
    return r * np.sin(dec), r * np.cos(dec)

def net(ax, ticks=True):
    t = np.linspace(0, 2 * np.pi, 361); ax.plot(np.sin(t), np.cos(t), color='k', lw=0.6, zorder=1)
    if ticks:
        for a in range(0, 360, 10):
            L = 0.07 if a % 90 == 0 else 0.035; r = np.radians(a)
            ax.plot([np.sin(r) * (1 - L), np.sin(r)], [np.cos(r) * (1 - L), np.cos(r)], color='k', lw=0.4, zorder=1)
    ax.plot([-.04, .04], [0, 0], color='0.4', lw=0.4); ax.plot([0, 0], [-.04, .04], color='0.4', lw=0.4)
    ax.set_xlim(-1.04, 1.04); ax.set_ylim(-1.04, 1.04); ax.set_aspect('equal'); ax.axis('off')

def gad_stars(ax, s=22):
    for d, i in [(0, GAD), (180, -GAD)]:
        x, y = xy(d, i); ax.scatter(x, y, marker='*', s=s, c='k' if i > 0 else 'w', edgecolors='k', lw=0.5, zorder=6)

def dot(ax, dec, inc, c, s=6, marker='o', lw=0.4, ec=None, z=3, **kw):
    dec, inc = np.atleast_1d(dec), np.atleast_1d(inc); x, y = xy(dec, inc); lo = inc >= 0
    ec = c if ec is None else ec
    ax.scatter(x[lo], y[lo], s=s, marker=marker, c=c, edgecolors=ec, lw=lw, zorder=z, **kw)
    ax.scatter(x[~lo], y[~lo], s=s, marker=marker, facecolors='white', edgecolors=c, lw=max(lw * 1.8, 0.6), zorder=z, **kw)

def circle(ax, dec, inc, a95, c, lw=0.7, z=4):
    if not np.isfinite(a95) or a95 <= 0 or a95 > AMAX: return
    v = pmag.dir2cart([dec, inc, 1.0]); v = v / np.linalg.norm(v)
    u = np.cross(v, [0, 0, 1.0]) if abs(v[2]) < 0.99 else np.array([1.0, 0, 0]); u /= np.linalg.norm(u); w = np.cross(v, u)
    t = np.linspace(0, 2 * np.pi, 241); a = np.radians(a95)
    P3 = np.cos(a) * v[None] + np.sin(a) * (np.cos(t)[:, None] * u + np.sin(t)[:, None] * w)
    di = np.array([pmag.cart2dir(p)[:2] for p in P3]); x, y = xy(di[:, 0], di[:, 1]); lo = di[:, 1] >= 0
    for seg_lo in (True, False):            # solid lower / dashed upper hemisphere
        m = lo == seg_lo; xs, ys = np.where(m, x, np.nan), np.where(m, y, np.nan)
        ax.plot(xs, ys, color=c, lw=lw, ls='-' if seg_lo else (0, (2, 1.2)), zorder=z)

def letter(ax, L, title, sub=''):
    kw = dict(xycoords='axes fraction', textcoords='offset points', ha='left', va='bottom')
    ax.annotate(L, (0, 1), xytext=(-2, 11), fontsize=8.5, fontweight='bold', **kw)
    ax.annotate(title, (0, 1), xytext=(11, 11), fontsize=6.2, fontweight='bold', **kw)
    if sub: ax.annotate(sub, (0, 1), xytext=(11, 4), fontsize=4.8, color='0.35', **kw)

FS = 4.5
def statbox(ax, lines, y=-0.03):
    """lines: list of (text, colour); drawn in a light box under the net (inside the panel)."""
    t = ax.text(0.5, y, '\n'.join(l for l, _ in lines), transform=ax.transAxes, fontsize=FS, ha='center', va='top', color='none',
                family='DejaVu Sans Mono', bbox=dict(boxstyle='round,pad=0.25', fc='#f6f6f6', ec='0.8', lw=0.4), zorder=0)
    n = len(lines)
    for j, (l, c) in enumerate(lines):     # recolour line by line on top of the box
        ax.text(0.5, y, '\n' * j + l + '\n' * (n - 1 - j), transform=ax.transAxes, fontsize=FS, ha='center', va='top',
                color=c, family='DejaVu Sans Mono', zorder=7)

def fmt(m, lab):
    k = '—' if not np.isfinite(m['k']) else (f"{m['k']:.0f}" if m['k'] < 1000 else '>999')
    a = '—' if not np.isfinite(m['a95']) or m['a95'] >= 90 else f"{m['a95']:.0f}"
    return f"{lab} {m['dec']:3.0f}/{m['inc']:+3.0f} α95 {a:>2} k {k:>3} n{m['n']:<2}"

# ---------------- layout (inches) ----------------
W, H = 7.09, 7.65
fig = plt.figure(figsize=(W, H))
def axin(x, y, w, h, **kw): return fig.add_axes([x / W, y / H, w / W, h / H], **kw)
D = 0.98                           # small-net diameter (in)
CW = 1.13                          # cell width
RIGHT0 = 2.53                      # x of first site column
ROWS = [6.27, 4.63, 2.99]          # bottom of each site-net row (stats box hangs below)
CONG_Y = 1.12

# ---------------- (a) in-situ site means ----------------
ht = s[s.slot == 'HT']
INSITU = ['PKSK', 'NWFA', 'PKSI', 'PKSJ', 'PKSH-HA', 'PKSH-HB', 'PKSB', 'WBEA']
SM = {u: two_tier(ht[ht.unit == u]) for u in INSITU}
def pol(u, m):
    if u == 'PKSI': return 'clast'
    if u == 'PKSH-HA': return 'disturbed'
    return 'N' if vgp(m['dec'], m['inc'])[0] > 0 else 'R'
ax = axin(0.22, 5.38, 1.85, 1.85); net(ax); letter(ax, 'a', 'In-situ site means (HT/ChRM)', 'core-level means → site Fisher mean, α95')
gad_stars(ax, 60)
OFF = {'PKSK': (-30, 12), 'NWFA': (9, 4), 'PKSI': (7, 3), 'PKSJ': (-16, 15), 'PKSH-HA': (20, -4), 'PKSH-HB': (-34, 4), 'PKSB': (-14, -12), 'WBEA': (13, 9)}

for u in INSITU:
    m, sm = SM[u]; c = PCOL[pol(u, m)]
    if u == 'PKSH-HA':     # two cores 64° apart: plot both cores, joined
        for q in sm: dot(ax, q['dec'], q['inc'], c, s=26, marker='o', ec='k', lw=0.5, z=5)
        (x0, y0), (x1, y1) = [np.ravel(xy(q['dec'], q['inc'])) for q in sm]; ax.plot([x0, x1], [y0, y1], color=c, lw=0.7, zorder=4)
        xa, ya = x1, y1
    else:
        circle(ax, m['dec'], m['inc'], m['a95'], c, lw=0.8)
        dot(ax, m['dec'], m['inc'], c, s=30, marker='D' if u == 'PKSI' else 'o', ec='k', lw=0.5, z=5)
        xa, ya = np.ravel(xy(m['dec'], m['inc']))
    ax.annotate(NAME[u], (xa, ya), xytext=OFF[u], textcoords='offset points', fontsize=5.4, color=c, fontweight='bold',
                ha='left', va='center', arrowprops=dict(arrowstyle='-', color='0.5', lw=0.4, shrinkA=0, shrinkB=2))
lines = [(f'site    D/I      α95 N  VGP λ/φ', '0.2')]
for u in INSITU:
    m, sm = SM[u]; a = '—' if not np.isfinite(m['a95']) or m['a95'] >= 90 else f"{m['a95']:.0f}"
    pl, po, _, _ = vgp(m['dec'], m['inc'])
    lines.append((f"{NAME[u]:<6} {m['dec']:3.0f}/{m['inc']:+3.0f}  {a:>2} {m['n']}  {pl:+3.0f}/{po:3.0f}", PCOL[pol(u, m)]))
lines.append((f'GAD I = ±{GAD:.1f}° (★ N, ☆ R)', '0.2'))
statbox(ax, lines, y=-0.03)

# ---------------- (b) VGPs ----------------
import matplotlib.path as mpath
axv = axin(0.30, 2.62, 1.62, 1.62, projection=ccrs.LambertAzimuthalEqualArea(LON, 90))
RR = 6371007.0 * 2 * np.sin(np.radians(90 - 8) / 2)          # map edge at latitude 8°N
axv.set_xlim(-RR, RR); axv.set_ylim(-RR, RR)
th = np.linspace(0, 2 * np.pi, 200); axv.set_boundary(mpath.Path(np.c_[np.sin(th), np.cos(th)] * 0.5 + 0.5), transform=axv.transAxes)
axv.add_feature(cfeature.LAND.with_scale('110m'), fc='#ececec', ec='none'); axv.coastlines('110m', lw=0.3, color='0.55')
axv.gridlines(lw=0.3, color='0.78', xlocs=range(-180, 181, 30), ylocs=[30, 60])
axv.spines['geo'].set_linewidth(0.6)
lat45 = np.linspace(-180, 180, 361)
axv.plot(lat45, np.full_like(lat45, 45), color='k', lw=0.5, ls=(0, (3, 2)), transform=ccrs.PlateCarree())
axv.text(LON - 180 + 8, 43, '45°', fontsize=4.6, transform=ccrs.PlateCarree(), color='0.3', va='top')
axv.scatter(LON, LAT, marker='^', s=18, c='k', transform=ccrs.PlateCarree(), zorder=6)
VOFF = {'PKSK': (8, -6), 'NWFA': (8, 1), 'PKSI': (6, -3), 'PKSJ': (-26, -6), 'PKSH-HA': (-30, 4), 'PKSH-HB': (7, 7),
        'PKSB': (-14, 11), 'WBEA': (-4, -11)}
for u in INSITU:
    m, sm = SM[u]; c = PCOL[pol(u, m)]
    plat, plon, dp, dm = vgp(m['dec'], m['inc'], m['a95'])
    rev = plat < 0; la, lo = (-plat, (plon + 180) % 360) if rev else (plat, plon)   # reversed VGPs as antipodes
    if np.isfinite(m['a95']) and m['a95'] <= AMAX:   # A95 drawn as circle of radius sqrt(dp*dm)
        r = np.sqrt(dp * dm); t = np.linspace(0, 360, 121)
        cx = [pmag.dodirot(tt, 90 - r, lo, la) for tt in t]
        axv.plot([p[0] for p in cx], [p[1] for p in cx], color=c, lw=0.6, transform=ccrs.Geodetic(), zorder=4)
    axv.scatter(lo, la, s=24, marker='D' if u == 'PKSI' else 'o', c='white' if rev else c, edgecolors=c if rev else 'k',
                lw=0.9 if rev else 0.5, transform=ccrs.PlateCarree(), zorder=5)
    X, Y = axv.projection.transform_point(lo, la, ccrs.PlateCarree())
    axv.annotate(NAME[u], (X, Y), xytext=VOFF[u], textcoords='offset points', fontsize=4.8, color=c, fontweight='bold', va='center',
                 zorder=6, arrowprops=dict(arrowstyle='-', color='0.5', lw=0.3, shrinkA=0, shrinkB=2))
letter(axv, 'b', 'Site VGPs (in-situ)', 'reversed VGPs as antipodes (open); ▲ sites; λ/φ in (a)')

# ---------------- (c–n) every site, all components ----------------
SITES = ['PKSK', 'NWFA', 'PKSI', 'PKSJ', 'PKSH', 'PKSB', 'WBEA', 'NWFB', 'NWFC', 'PKQA', 'PKSF', 'PKSG']
for n, st in enumerate(SITES):
    r, c = divmod(n, 4); x0 = RIGHT0 + c * CW + (CW - D) / 2
    ax = axin(x0, ROWS[r], D, D); net(ax); gad_stars(ax, 16)
    g = s[s.site == st]
    dot(ax, g.dir_dec, g.dir_inc, '0.62', s=3.5, lw=0.35, z=2)
    lines = []
    if st == 'PKQA':   # three field boulders (cores 0-4, 5-6, 7-9): boulder means, no site mean
        for b, gb in g.groupby('boulder'):
            for k in ['LT', 'MT', 'HT']:
                gk = gb[gb.slot == k]; m = fisher(gk.dir_dec, gk.dir_inc)
                if m is None: continue
                circle(ax, m['dec'], m['inc'], m['a95'], SLOTC[k], lw=0.6)
                dot(ax, m['dec'], m['inc'], SLOTC[k], s=18, marker='s', ec='k', lw=0.45, z=6)
                if k == 'HT':
                    xb, yb = np.ravel(xy(m['dec'], m['inc']))
                    ax.annotate(b[-2:], (xb, yb), xytext=(4, 3), textcoords='offset points', fontsize=4.8, fontweight='bold', zorder=8)
                    lines.append((fmt(m, b[-2:]), SLOTC['HT']))
    else:
        for k in ['LT', 'MT', 'HT']:
            gk = g[g.slot == k]; m = fisher(gk.dir_dec, gk.dir_inc)
            if m is None: continue
            circle(ax, m['dec'], m['inc'], m['a95'], SLOTC[k], lw=0.75)
            dot(ax, m['dec'], m['inc'], SLOTC[k], s=22, marker='s', ec='k', lw=0.5, z=6)
            lines.append((fmt(m, k), SLOTC[k]))
    letter(ax, 'cdefghijklmn'[n], NAME[st], {'PKQA': '3 boulders · diamicton'}.get(st, f'{KIND[st]} · {AGE[st]}'))
    statbox(ax, lines)

# ---------------- (o–t) conglomerate tests ----------------
CONG = ['NWFB', 'NWFC', 'PKQA', 'PKSF', 'PKSG', 'PKSH']
CW6 = (W - 0.10) / 6
fig.text(0.012, (CONG_Y + D + 0.33) / H, 'Conglomerate tests — boulder-mean HT (ChRM) directions, Watson (1956) randomness test',
         fontsize=6.4, fontweight='bold', ha='left', va='bottom')
fig.add_artist(Line2D([0.01, 0.99], [(CONG_Y + D + 0.31) / H] * 2, color='0.6', lw=0.5))
CONG_ROWS = []
for n, st in enumerate(CONG):
    x0 = 0.05 + n * CW6 + (CW6 - D) / 2
    ax = axin(x0, CONG_Y, D, D); net(ax); gad_stars(ax, 16)
    g = ht[ht.site == st]
    dot(ax, g.dir_dec, g.dir_inc, '0.72', s=3, lw=0.3, z=2)
    bm = []
    for b, x in g.groupby('boulder'):
        m = fisher(x.dir_dec, x.dir_inc); bm.append(m)
        circle(ax, m['dec'], m['inc'], m['a95'], SLOTC['HT'], lw=0.6)
        dot(ax, m['dec'], m['inc'], SLOTC['HT'], s=16, marker='s', ec='k', lw=0.45, z=6)
    R = resultant([b['dec'] for b in bm], [b['inc'] for b in bm]); r95, r99 = watson_ro(len(bm))
    gm = fisher([b['dec'] for b in bm], [b['inc'] for b in bm])
    circle(ax, gm['dec'], gm['inc'], gm['a95'], 'k', lw=0.7)
    dot(ax, gm['dec'], gm['inc'], 'k', s=26, marker='s', ec='k', lw=0.5, z=7)
    verdict = 'RANDOM (pass)' if R < r95 else 'CLUSTERED (fail)'
    vc = '#1b7837' if R < r95 else '#b2182b'
    unit = 'boulders' if st == 'PKQA' else ('cores' if st == 'PKSH' else 'boulders')
    lines = [(f"N = {len(bm)} {unit} · R = {R:.2f}", '0.15'), (f"Ro95 {r95:.2f} · Ro99 {r99:.2f}", '0.15'), (verdict, vc)]
    if st == 'PKSF':   # McFadden & McElhinny (1988) lines-and-planes double-check (mcfadden_gc_check.py)
        lines.append(("lines+planes R 6.09 > 5.28", '#b2182b'))
    a = '—' if not np.isfinite(gm['a95']) or gm['a95'] >= 90 else f"{gm['a95']:.0f}"
    lines.append((f"mean {gm['dec']:.0f}/{gm['inc']:+.0f} k {gm['k']:.1f} α95 {a}", '0.15'))
    letter(ax, 'opqrst'[n], NAME[st], {'PKSH': 'cores HA1, HA2, HB1'}.get(st, ''))
    statbox(ax, lines)
    CONG_ROWS.append(dict(site=NAME[st], N=len(bm), R=round(R, 2), Ro95=round(r95, 2), Ro99=round(r99, 2), verdict=verdict))

# ---------------- legend strip ----------------
lg = axin(0, 0.22, W, 0.30); lg.axis('off')
h = [Line2D([], [], ls='', marker='o', ms=2.6, color='0.6', label='specimen fit (lower / upper hemisphere: filled / open)'),
     Line2D([], [], ls='', marker='s', ms=4, mfc=SLOTC['LT'], mec='k', mew=0.4, label='LT mean'),
     Line2D([], [], ls='', marker='s', ms=4, mfc=SLOTC['MT'], mec='k', mew=0.4, label='MT mean'),
     Line2D([], [], ls='', marker='s', ms=4, mfc=SLOTC['HT'], mec='k', mew=0.4, label='HT (ChRM) mean / boulder mean'),
     Line2D([], [], ls='', marker='s', ms=4, mfc='k', mec='k', label='clast-population mean'),
     Line2D([], [], color='0.3', lw=0.7, label=f'α95 ≤ {AMAX}° (dashed: upper hem.)'),
     Line2D([], [], ls='', marker='*', ms=5, mfc='k', mec='k', label='GAD normal'),
     Line2D([], [], ls='', marker='*', ms=5, mfc='w', mec='k', label='GAD reversed'),
     Line2D([], [], ls='', marker='o', ms=4, mfc=PCOL['N'], mec='k', mew=0.4, label='normal'),
     Line2D([], [], ls='', marker='o', ms=4, mfc=PCOL['R'], mec='k', mew=0.4, label='reversed'),
     Line2D([], [], ls='', marker='o', ms=4, mfc=PCOL['disturbed'], mec='k', mew=0.4, label='PKS-HA (discordant)'),
     Line2D([], [], ls='', marker='D', ms=3.5, mfc=PCOL['clast'], mec='k', mew=0.4, label='PKS-I (corestone)')]
lg.legend(handles=h, loc='center', ncol=6, fontsize=5.1, frameon=False, handletextpad=0.3, columnspacing=0.9, labelspacing=0.4)

for ext in ['svg', 'pdf', 'png']:
    fig.savefig(os.path.join(OUT, f'Fig7_paleomag_directions.{ext}'), dpi=400 if ext == 'png' else None, bbox_inches='tight', pad_inches=0.03)
import json; json.dump(CONG_ROWS, open(os.path.join(OUT, 'Fig7_conglomerate_tests.json'), 'w'), indent=1)
print(CONG_ROWS)
