"""Supplementary demagnetization plates: every thermally demagnetized specimen, one plate per site (split into
pages of <= 48). Zijderveld diagrams in geographic coordinates, x = N, y = E (filled) / Up (open), with the
LT / MT / HT fits as arrows (fitquest colours), as in Fig. 6. Usage: python make_figS_demag.py <pmagpy_fits> <outdir>"""
import sys, os, numpy as np, pandas as pd
import matplotlib as mpl, matplotlib.pyplot as plt
import pmagpy.pmag as pmag
P, OUT = sys.argv[1], sys.argv[2]; os.makedirs(OUT, exist_ok=True)
mpl.rcParams.update({'font.family': 'DejaVu Sans', 'font.size': 5, 'axes.linewidth': 0.4, 'xtick.major.width': 0.3,
                     'ytick.major.width': 0.3, 'xtick.major.size': 1.2, 'ytick.major.size': 1.2, 'svg.fonttype': 'none', 'pdf.fonttype': 42})
COMP = {'lt': '#3a9d5d', 'MT': '#2a6f97', 'mt': '#9840D7'}
NAME = {'NWFA': 'NWF-A', 'NWFB': 'NWF-B', 'NWFC': 'NWF-C', 'PKQA': 'PKQ-A', 'PKSB': 'PKS-B', 'PKSF': 'PKS-F', 'PKSG': 'PKS-G',
        'PKSH': 'PKS-H', 'PKSI': 'PKS-I', 'PKSJ': 'PKS-J', 'PKSK': 'PKS-K', 'WBEA': 'WBE-A'}
DESC = {'NWFA': 'in-situ flow, 518 ka', 'NWFB': 'transported blocks, 934 ka', 'NWFC': 'diamicton boulders', 'PKQA': 'diamicton, 3 field boulders',
        'PKSB': 'in-situ flow, 1155 ka', 'PKSF': 'diamicton boulders', 'PKSG': 'diamicton boulders', 'PKSH': 'two horizons, ~770 ka',
        'PKSI': 'corestone, 553 ka', 'PKSJ': 'in-situ flow, 601 ka', 'PKSK': 'in-situ flow, 407 ka', 'WBEA': 'basal flow, 1397 ka'}
m = pd.read_csv(os.path.join(P, 'measurements.txt'), sep='\t', skiprows=1)
s = pd.read_csv(os.path.join(P, 'specimens.txt'), sep='\t', skiprows=1); s = s[s.dir_tilt_correction == 0]
sa = pd.read_csv(os.path.join(P, 'samples.txt'), sep='\t', skiprows=1).set_index('sample')
redo = pd.read_csv(os.path.join(P, 'pmagpy_Laos_allsites.redo'), sep='\t', header=None, names=['spec', 'type', 'tmin', 'tmax', 'comp', 'color', 'f'])

def steps(sp):
    d = m[m.specimen == sp].sort_values('sequence').copy()
    smp = d['sample'].iloc[0]; az, dip = sa.loc[smp, 'azimuth'], sa.loc[smp, 'dip']
    g = [pmag.dogeo(D, I, az, dip) for D, I in zip(d.dir_dec, d.dir_inc)]
    xyz = np.array([pmag.dir2cart([a[0], a[1], J]) for a, J in zip(g, d.magn_moment)])
    d['N'], d['E'], d['D'] = xyz[:, 0], xyz[:, 1], xyz[:, 2]
    return d
def fit_line(d, tmin, tmax):
    g = d[(d.quality == 'g') & (d.treat_temp >= tmin) & (d.treat_temp <= tmax) & (d.method_codes == 'LT-T-Z')]
    X = g[['N', 'E', 'D']].values
    if len(X) < 2: return None
    c = X.mean(0); _, _, vt = np.linalg.svd(X - c); v = vt[0]; t = (X - c) @ v
    p0, p1 = c + t.min() * v, c + t.max() * v
    if np.dot(X[-1] - X[0], v) < 0: p0, p1 = p1, p0
    return p0, p1

specs = sorted(s.specimen.unique())
order = ['NWFA', 'PKSB', 'PKSH', 'PKSI', 'PKSJ', 'PKSK', 'WBEA', 'NWFB', 'NWFC', 'PKQA', 'PKSF', 'PKSG']
NC, NR = 8, 6
made = []
for site in order:
    sp_site = [x for x in specs if x.startswith(site)]
    pages = [sp_site[i:i + NC * NR] for i in range(0, len(sp_site), NC * NR)]
    for pi, chunk in enumerate(pages):
        nr = int(np.ceil(len(chunk) / NC))
        fig = plt.figure(figsize=(7.09, 0.42 + 0.98 * nr))
        gs = fig.add_gridspec(nr, NC, left=0.03, right=0.995, top=1 - 0.36 / (0.42 + 0.98 * nr), bottom=0.02, wspace=0.35, hspace=0.45)
        for k, sp in enumerate(chunk):
            ax = fig.add_subplot(gs[k // NC, k % NC]); d = steps(sp); good = d[d.quality == 'g']
            if not len(good): ax.axis('off'); continue
            sc = np.abs(good[['N', 'E', 'D']].values).max(); ex = int(np.floor(np.log10(sc))); f = 10.0 ** ex
            ax.plot(good.N / f, good.E / f, '-', color='0.6', lw=0.35); ax.plot(good.N / f, -good.D / f, color='0.6', lw=0.35, ls=(0, (2, 1.5)))
            ax.scatter(good.N / f, good.E / f, s=3, c='k', lw=0, zorder=3)
            ax.scatter(good.N / f, -good.D / f, s=3, facecolor='white', edgecolor='k', lw=0.35, zorder=3)
            hd = ''
            for comp in ['lt', 'MT', 'mt']:
                fr = redo[(redo.spec == sp) & (redo.comp == comp)]
                if not len(fr): continue
                res = fit_line(d, fr.tmin.iloc[0], fr.tmax.iloc[0])
                if res is None: continue
                p0, p1 = res
                for y0, y1, ls in [(p0[1], p1[1], '-'), (-p0[2], -p1[2], (0, (3, 1.5)))]:
                    ax.annotate('', xy=(p1[0] / f, y1 / f), xytext=(p0[0] / f, y0 / f), arrowprops=dict(arrowstyle='-|>', color=COMP[comp], lw=0.8, ls=ls, mutation_scale=4, shrinkA=0, shrinkB=0), zorder=4)
            ch = s[(s.specimen == sp) & (s.dir_comp == 'mt')]
            if len(ch):
                c = ch.iloc[0]; hd = f'HT {c.dir_dec:.0f}/{c.dir_inc:+.0f} MAD {c.dir_mad_free:.0f}' + ('' if c.dir_mad_free <= 15 else ' ✗')
            xs = np.r_[good.N / f, 0]; ys = np.r_[good.E / f, -good.D / f, 0]
            span = max(xs.max() - xs.min(), ys.max() - ys.min()) * 1.1; cx, cy = (xs.min() + xs.max()) / 2, (ys.min() + ys.max()) / 2
            ax.set_xlim(cx - span / 2, cx + span / 2); ax.set_ylim(cy - span / 2, cy + span / 2); ax.set_aspect('equal', adjustable='box')
            ax.spines[['left', 'bottom']].set_position('zero'); ax.spines[['top', 'right']].set_visible(False)
            ax.set_xticks([]); ax.set_yticks([])
            ax.set_title(f'{sp}\n{hd}', fontsize=4.6, pad=1.5, color='#b2182b' if '✗' in hd else 'k')
            ax.text(1.0, 0.0, f'10$^{{{ex}}}$', transform=ax.transAxes, fontsize=3.8, color='0.45', ha='right', va='bottom')
        part = f' ({pi + 1}/{len(pages)})' if len(pages) > 1 else ''
        fig.text(0.01, 1 - 0.06 / (0.42 + 0.98 * nr), f'{NAME[site]} — {DESC[site]}{part}: {len(sp_site)} specimens', fontsize=7, fontweight='bold', va='top')
        fig.text(0.99, 1 - 0.06 / (0.42 + 0.98 * nr), 'x = N; filled = E (horizontal), open = Up (vertical); arrows: LT green, MT blue, HT purple; scale in A m²',
                 fontsize=4.8, va='top', ha='right', color='0.3')
        fn = f'FigS_demag_{site}' + (f'_{pi + 1}' if len(pages) > 1 else '')
        fig.savefig(os.path.join(OUT, fn + '.png'), dpi=250); fig.savefig(os.path.join(OUT, fn + '.pdf')); plt.close(fig); made.append(fn)
print(made)
