"""Equal-area plotting helpers shared by Fig 7 and the supplementary figures."""
import numpy as np
import pmagpy.pmag as pmag
from pmag_sites import GAD
AMAX = 60
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

