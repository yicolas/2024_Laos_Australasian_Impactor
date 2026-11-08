"""Figure 6 — representative thermal demagnetization (geographic coordinates), from the pmagpy_fits
MagIC tables + .redo fits (fitquest / fitgame_v15). Zijderveld: x = N, y = E (solid, horizontal plane)
and Up (open, vertical plane), as in fitquest; component fits (LT, MT, HT = ChRM) drawn as arrows in the
demagnetization direction (toward the origin). Intensity: J/J0 vs temperature with fit intervals shaded.
Orientation: standard MagIC (pmag.dogeo(dec, inc, azimuth, dip)) on the corrected pmagpy_fits tables (2026-11-07 fix).
Usage: python make_fig6.py <pmagpy_fits_dir> <outdir>"""
import sys, os, numpy as np, pandas as pd
import matplotlib as mpl, matplotlib.pyplot as plt
from matplotlib.lines import Line2D
import pmagpy.pmag as pmag

P = sys.argv[1]; OUT = sys.argv[2]; os.makedirs(OUT, exist_ok=True)
mpl.rcParams.update({'font.family': 'DejaVu Sans', 'font.size': 6.3, 'axes.linewidth': 0.6, 'xtick.major.width': 0.5,
                     'ytick.major.width': 0.5, 'xtick.major.size': 2, 'ytick.major.size': 2, 'svg.fonttype': 'none',
                     'pdf.fonttype': 42, 'axes.labelpad': 1.5})
COMP = {'lt': ('LT', '#3a9d5d'), 'MT': ('MT', '#2a6f97'), 'mt': ('HT (ChRM)', '#9840D7')}
EMU2AM2 = 1.0    # magn_moment already in A m^2 after the 2026-11-07 fix

m = pd.read_csv(os.path.join(P, 'measurements.txt'), sep='\t', skiprows=1)
s = pd.read_csv(os.path.join(P, 'specimens.txt'), sep='\t', skiprows=1); s = s[s.dir_tilt_correction == 0]
sa = pd.read_csv(os.path.join(P, 'samples.txt'), sep='\t', skiprows=1).set_index('sample')
redo = pd.read_csv(os.path.join(P, 'pmagpy_Laos_allsites.redo'), sep='\t', header=None, names=['spec', 'type', 'tmin', 'tmax', 'comp', 'color', 'f'])

PANELS = [  # specimen, title, note
    ('NWFA-4C', 'NWF-A', 'in situ flow, 518 ka · normal'),
    ('PKSJ-2E', 'PKS-J', 'in situ flow, 601 ka · reversed'),
    ('PKSB-1F', 'PKS-B', 'in situ flow, 1155 ka · reversed'),
    ('WBEA-2B', 'WBE-A', 'basal flow, 1397 ka · reversed'),
    ('PKSH-1I', 'PKS-H, core HA1', 'upper horizon · reversed VGP'),
    ('PKSH-2H', 'PKS-H, core HA2', 'upper horizon · 64° from HA1'),
    ('PKSH-3B', 'PKS-H, core HB1', 'lower flow · reversed VGP'),
    ('NWFC-1C', 'NWF-C', 'diamicton clast (conglomerate test)')]

def steps(sp):
    d = m[m.specimen == sp].sort_values('sequence').copy()
    smp = d['sample'].iloc[0]; az, dip = sa.loc[smp, 'azimuth'], sa.loc[smp, 'dip']
    g = [pmag.dogeo(D, I, az, dip) for D, I in zip(d.dir_dec, d.dir_inc)]
    d['dg'] = [x[0] for x in g]; d['ig'] = [x[1] for x in g]
    d['J'] = d.magn_moment * EMU2AM2
    xyz = np.array([pmag.dir2cart([a, b, c]) for a, b, c in zip(d.dg, d.ig, d.J)])
    d['N'], d['E'], d['D'] = xyz[:, 0], xyz[:, 1], xyz[:, 2]
    d['T'] = d.treat_temp - 273.0
    d['lab'] = np.where(d.method_codes == 'LT-NO', 'NRM', np.where(d.method_codes == 'LT-LT-Z', 'LN$_2$', d['T'].round().astype(int).astype(str) + '°'))
    return d

def fit_line(d, tmin, tmax):
    g = d[(d.quality == 'g') & (d.treat_temp >= tmin) & (d.treat_temp <= tmax) & (d.method_codes == 'LT-T-Z')]
    X = g[['N', 'E', 'D']].values
    if len(X) < 2: return None
    c = X.mean(0); u, sv, vt = np.linalg.svd(X - c); v = vt[0]
    t = (X - c) @ v
    p0, p1 = c + t.min() * v, c + t.max() * v
    # orient: arrow from the first (lowest-T) step toward the last (demag direction)
    if np.dot(X[-1] - X[0], v) < 0: p0, p1 = c + t.max() * v, c + t.min() * v
    if np.linalg.norm(X[0] - p1) < np.linalg.norm(X[0] - p0): p0, p1 = p1, p0
    return p0, p1, g

W, H = 7.09, 8.6
fig = plt.figure(figsize=(W, H))
outer = fig.add_gridspec(4, 2, left=0.045, right=0.745, top=0.955, bottom=0.07, hspace=0.50, wspace=0.16)
for k, (sp, site, note) in enumerate(PANELS):
    d = steps(sp); good = d[d.quality == 'g']; bad = d[d.quality != 'g']
    inner = outer[k // 2, k % 2].subgridspec(1, 2, width_ratios=[1.5, 1], wspace=0.34)
    # ---- Zijderveld (x = N, y = E / Up), axes through the origin
    ax = fig.add_subplot(inner[0, 0])
    sc = np.abs(good[['N', 'E', 'D']].values).max(); ex = int(np.floor(np.log10(sc))); f = 10.0 ** ex
    ax.plot(good.N / f, good.E / f, '-', color='0.55', lw=0.5, zorder=1)
    ax.plot(good.N / f, -good.D / f, '-', color='0.55', lw=0.5, ls=(0, (2, 1.5)), zorder=1)
    ax.scatter(good.N / f, good.E / f, s=9, c='k', lw=0, zorder=3)
    ax.scatter(good.N / f, -good.D / f, s=9, facecolor='white', edgecolor='k', lw=0.6, zorder=3)
    nrm0 = d[d.method_codes == 'LT-NO'].iloc[0]
    if nrm0.quality != 'g':
        ax.scatter([nrm0.N / f], [nrm0.E / f], s=10, marker='s', facecolor='0.7', edgecolor='0.4', lw=0.4, zorder=3)
        ax.scatter([nrm0.N / f], [-nrm0.D / f], s=10, marker='s', facecolor='white', edgecolor='0.4', lw=0.4, zorder=3)
    bad = bad[bad.method_codes != 'LT-NO']
    if len(bad): ax.scatter(bad.N / f, bad.E / f, s=6, marker='x', c='0.6', lw=0.4, zorder=2)
    for comp in ['lt', 'MT', 'mt']:
        fr = redo[(redo.spec == sp) & (redo.comp == comp)]
        if not len(fr): continue
        res = fit_line(d, fr.tmin.iloc[0], fr.tmax.iloc[0])
        if res is None: continue
        p0, p1, _ = res; col = COMP[comp][1]
        for y0, y1, ls in [(p0[1], p1[1], '-'), (-p0[2], -p1[2], (0, (3, 1.5)))]:
            ax.annotate('', xy=(p1[0] / f, y1 / f), xytext=(p0[0] / f, y0 / f),
                        arrowprops=dict(arrowstyle='-|>', color=col, lw=1.3, ls=ls, mutation_scale=7, shrinkA=0, shrinkB=0), zorder=4)
    # labels: NRM and the last good step
    for _, r in pd.concat([d[d.method_codes == 'LT-NO'].iloc[[0]], good.iloc[[-1]]]).iterrows():
        ax.annotate(r.lab, (r.N / f, r.E / f), xytext=(2, 2), textcoords='offset points', fontsize=4.8, color='0.25')
    allp = pd.concat([good, d[d.method_codes == 'LT-NO']])
    xs = np.r_[allp.N / f, 0]; ys = np.r_[allp.E / f, -allp.D / f, 0]
    x0, x1, y0, y1 = xs.min(), xs.max(), ys.min(), ys.max(); span = max(x1 - x0, y1 - y0) * 1.12
    cx, cy = (x0 + x1) / 2, (y0 + y1) / 2
    ax.set_xlim(cx - span / 2, cx + span / 2); ax.set_ylim(cy - span / 2, cy + span / 2); ax.set_aspect('equal', adjustable='box')
    ax.spines[['left', 'bottom']].set_position('zero'); ax.spines[['top', 'right']].set_visible(False)
    ax.tick_params(labelsize=4.6, pad=1)
    ax.text(ax.get_xlim()[1], 0, ' N', ha='left', va='center', fontsize=5.6, fontweight='bold', clip_on=False)
    ax.text(0, ax.get_ylim()[1], 'E, Up', ha='center', va='bottom', fontsize=5.6, fontweight='bold', clip_on=False)
    ax.text(0.02, 0.02, f'×10$^{{{ex}}}$ A m$^2$', transform=ax.transAxes, fontsize=4.8, color='0.3')
    ax.text(-0.18, 1.20, f'{"abcdefgh"[k]}', transform=ax.transAxes, fontsize=9, fontweight='bold', va='bottom', ha='left')
    ax.text(-0.02, 1.215, f'{site} · {sp}', transform=ax.transAxes, fontsize=6.6, fontweight='bold', va='bottom', ha='left')
    ch = s[(s.specimen == sp) & (s.dir_comp == 'mt')].iloc[0]
    ax.text(-0.02, 1.04, f'{note}\nChRM D = {ch.dir_dec:.0f}°, I = {ch.dir_inc:.0f}°, MAD = {ch.dir_mad_free:.1f}°',
            transform=ax.transAxes, fontsize=5.0, va='bottom', ha='left', color='0.25')
    # ---- intensity decay
    ax2 = fig.add_subplot(inner[0, 1])
    J0 = d[d.method_codes == 'LT-NO'].J.iloc[0]; th = good[good.method_codes == 'LT-T-Z']
    for comp in ['lt', 'MT', 'mt']:
        fr = redo[(redo.spec == sp) & (redo.comp == comp)]
        if len(fr): ax2.axvspan(fr.tmin.iloc[0] - 273, fr.tmax.iloc[0] - 273, color=COMP[comp][1], alpha=0.16, lw=0)
    ax2.plot(th['T'], th.J / J0, '-o', color='k', ms=2.2, lw=0.6, mfc='k')
    nrm = d[d.method_codes == 'LT-NO']; ln2 = good[good.method_codes == 'LT-LT-Z']
    ax2.plot([20] * len(nrm), nrm.J / J0, 's', color='k', ms=2.6, mfc='white', mew=0.6)
    if len(ln2): ax2.plot([20] * len(ln2), ln2.J / J0, 'D', color='#3b6db0', ms=2.4, mfc='white', mew=0.6)
    ax2.set_xlim(0, 560); ax2.set_xticks([0, 200, 400]); ax2.set_ylim(0, max(1.1, (good.J / J0).max() * 1.05))
    ax2.set_xlabel('T (°C)', fontsize=5.6); ax2.set_ylabel('J / J$_0$', fontsize=5.6); ax2.tick_params(labelsize=4.8, pad=1)
    ax2.text(0.97, 0.97, f'J$_0$ = {J0:.1e} A m$^2$'.replace('e-0', 'e−'), transform=ax2.transAxes, fontsize=4.6, ha='right', va='top', color='0.3')
    ax2.spines[['top', 'right']].set_visible(False)


# ---------------- (i) ChRM inclination vs age (replaces LEAD_4 Fig 10) ----------------
AGES = {'PKSK': (407, 18), 'NWFA': (518, 6), 'PKSI': (553, 20), 'PKSJ': (601, 44), 'PKSH-HA': (770, 9.3),
        'PKSH-HB': (800, 0), 'NWFB': (934, 30), 'PKSB': (1155, 2), 'WBEA': (1397, 13)}       # Table 1; HB plotted below the HA datum
SITE = {'PKSK': ('PKS-K', 'R', 'mismatch'), 'NWFA': ('NWF-A', 'N', 'a'), 'PKSI': ('PKS-I', 'clast', ''), 'PKSJ': ('PKS-J', 'R', 'b'),
        'PKSH-HA': ('PKS-HA', 'disturbed', 'e, f'), 'PKSH-HB': ('PKS-HB', 'R', 'g'), 'NWFB': ('NWF-B', 'clast', ''),
        'PKSB': ('PKS-B', 'R', 'c'), 'WBEA': ('WBE-A', 'R', 'd')}
TAB2 = {'NWFA': 23.7, 'PKSB': -10.6, 'PKSI': -35.6, 'PKSJ': -31.9, 'PKSK': -33.2, 'WBEA': -34.5, 'PKSH-HB': 7.9, 'NWFB': -60.2}   # core-level site means (Table 2)
PCOL = {'N': '#2c6fb0', 'R': '#c8372d', 'disturbed': '#e08a1e', 'clast': '0.55'}
ax = fig.add_axes([0.80, 0.07, 0.185, 0.885])
GAD = np.degrees(np.arctan(2 * np.tan(np.radians(15.2))))
ax.axvspan(-90, 90, ymin=0, ymax=1, color='none')
ax.axhspan(0, 773, color='#2c6fb0', alpha=0.06, lw=0); ax.axhspan(773, 1450, color='#c8372d', alpha=0.06, lw=0)
for t0, t1 in [(990, 1071), (1180, 1215)]: ax.axhspan(t0, t1, color='white', lw=0); ax.axhspan(t0, t1, color='#2c6fb0', alpha=0.10, lw=0)
ax.text(-88, 1030, 'Jaramillo', fontsize=4.6, color='#2c6fb0', va='center'); ax.text(-88, 1197, 'Cobb Mtn', fontsize=4.6, color='#2c6fb0', va='center')
ax.axhline(773, color='0.3', lw=0.6, ls=':'); ax.text(88, 768, 'B–M 773 ka', fontsize=4.8, ha='right', va='bottom', color='0.3')
ax.axhline(790, color='#c1121f', lw=0.7, ls=(0, (4, 2))); ax.text(-88, 795, 'impact ~790 ka', fontsize=4.8, ha='left', va='top', color='#c1121f')
for g in (-GAD, GAD): ax.axvline(g, color='0.45', lw=0.6, ls='--')
ax.axvline(0, color='0.75', lw=0.4)
sp_ch = s[s.dir_comp == 'mt']
for key, (age, e) in AGES.items():
    lab, pol, panels = SITE[key]
    if key.startswith('PKSH'):
        pre = 'PKSH-1|PKSH-2' if key == 'PKSH-HA' else 'PKSH-3'
        incs = sp_ch[sp_ch.specimen.str.match(pre)].dir_inc.values
    else:
        incs = sp_ch[sp_ch.site == key].dir_inc.values
    jit = np.random.default_rng(len(key)).uniform(-12, 12, len(incs))
    ax.scatter(incs, age + jit, s=4, c='0.75', lw=0, zorder=2)
    col = PCOL[pol]
    if key == 'PKSH-HA':
        for inc in (-28.0, 9.8):   # the two HA cores, 64° apart
            ax.scatter(inc, age, s=26, marker='o', c=col, edgecolor='k', lw=0.5, zorder=4)
        ax.plot([-28.0, 9.8], [age, age], color=col, lw=0.8, zorder=3)
        xm = 9.8
    else:
        inc = TAB2[key]; ax.errorbar(inc, age, xerr=np.std(incs) if len(incs) > 1 else 0, yerr=e if e else None, fmt='none', ecolor=col, elinewidth=0.8, capsize=1.5, zorder=3)
        ax.scatter(inc, age, s=26, marker='o' if pol != 'clast' else 'D', c=col, edgecolor='k', lw=0.5, zorder=4)
        xm = inc
    txt = lab + (f' ({panels})' if panels and panels != 'mismatch' else '')
    ax.annotate(txt, (xm, age), xytext=(4, -1), textcoords='offset points', fontsize=5.0, va='center', zorder=5,
                bbox=dict(boxstyle='round,pad=0.15', fc='white', ec='none', alpha=0.8))
ax.set_xlim(-90, 90); ax.set_xticks([-90, -GAD, 0, GAD, 90]); ax.set_xticklabels(['−90', f'−{GAD:.0f}', '0', f'{GAD:.0f}', '90'], fontsize=5)
ax.set_ylim(1450, 350); ax.set_ylabel('⁴⁰Ar/³⁹Ar age (ka)', fontsize=6); ax.set_xlabel('ChRM inclination (°, geographic)', fontsize=6)
ax.tick_params(labelsize=5)
ax.text(-88, 380, 'Brunhes (N)', fontsize=5, color='#2c6fb0', va='top'); ax.text(-88, 1440, 'Matuyama (R)', fontsize=5, color='#c8372d', va='bottom')
ax.text(-0.05, 1.012, 'i', transform=ax.transAxes, fontsize=9, fontweight='bold', va='bottom', ha='right')
ax.text(0.0, 1.012, 'ChRM inclination vs age', transform=ax.transAxes, fontsize=6.4, fontweight='bold', va='bottom', ha='left')

# legend strip
lg = fig.add_axes([0.0, 0.0, 1.0, 0.05]); lg.axis('off')
h = [Line2D([], [], ls='', marker='o', ms=3.2, color='k', label='horizontal (N–E)'),
     Line2D([], [], ls='', marker='o', ms=3.2, mfc='white', mec='k', label='vertical (N–Up)'),
     Line2D([], [], ls='', marker='x', ms=3, color='0.6', label='step rejected in fitting')]
h += [Line2D([], [], color=c, lw=1.4, marker='>', ms=3.5, label=f'{n} fit (arrow = demagnetization direction)') for k_, (n, c) in COMP.items()]
h += [Line2D([], [], ls='', marker='o', ms=4, mfc=PCOL['N'], mec='k', label='site mean, normal (i)'), Line2D([], [], ls='', marker='o', ms=4, mfc=PCOL['R'], mec='k', label='reversed (i)'),
      Line2D([], [], ls='', marker='o', ms=4, mfc=PCOL['disturbed'], mec='k', label='disturbed PKS-HA cores (i)'), Line2D([], [], ls='', marker='D', ms=3.5, mfc=PCOL['clast'], mec='k', label='clast locality (i)'),
      Line2D([], [], color='0.45', ls='--', lw=0.7, label=f'GAD inclination (±{GAD:.0f}°)')]
h += [Line2D([], [], ls='', marker='s', ms=3, mfc='0.7', mec='0.4', label='NRM (not used in fits)'), Line2D([], [], ls='', marker='D', ms=3, mfc='white', mec='#3b6db0', label='after LN$_2$ (low-T demag.)')]
lg.legend(handles=h, loc='center', ncol=5, fontsize=5.2, frameon=False, columnspacing=1.0, handlelength=1.8)
for ext in ['svg', 'pdf', 'png']:
    fig.savefig(os.path.join(OUT, f'Fig6_demagnetization.{ext}'), dpi=400 if ext == 'png' else None, bbox_inches='tight', pad_inches=0.03)
print('done')
