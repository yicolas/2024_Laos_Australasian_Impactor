"""Figure 5 — tektite major-element geochemistry and rj-MCMC source unmixing (consolidates LEAD_4 Figs 14–15).
(a–g) anhydrous Harker diagrams of the 82 accepted EPMA analyses vs literature tektites and source-lithology medians;
(h) log-likelihood and (i) K traces of the 12 chains; (j) posterior mixing weights by lithology type;
(k) sensitivity runs; (l) posterior-predictive residuals. One colour per lithology throughout.
Run after run.py (main, no_random, no_alkali, local_only). Usage: python make_fig5.py <res_dir> <outdir>"""
import sys, os, pickle, numpy as np, pandas as pd
import matplotlib as mpl, matplotlib.pyplot as plt
from matplotlib.lines import Line2D
from matplotlib.patches import Patch
from load import epma, sources_all as sources, literature_aat, OX, PAAS
from summarize import summarise, ORDER, SHORT
from figs_data import SCOL, TCOL, TLAB

RES = sys.argv[1]; OUT = sys.argv[2]; os.makedirs(OUT, exist_ok=True)
SCOL = dict(SCOL, Random='#c9c9ff')
mpl.rcParams.update({'font.family': 'DejaVu Sans', 'font.size': 6.5, 'axes.linewidth': 0.6, 'xtick.major.width': 0.5,
                     'ytick.major.width': 0.5, 'xtick.major.size': 2.5, 'ytick.major.size': 2.5, 'svg.fonttype': 'none',
                     'pdf.fonttype': 42, 'axes.labelpad': 2})
def letter(ax, s): ax.text(-0.02, 1.02, s, transform=ax.transAxes, fontsize=9, fontweight='bold', ha='right', va='bottom')

load = lambda n: pickle.load(open(os.path.join(RES, f'res_{n}.pkl'), 'rb'))
S = summarise(load('main')); S['res'] = load('main')
sens = {'main': S}
for n in ['no_random', 'no_alkali', 'local_only']:
    try: sens[n] = summarise(load(n))
    except FileNotFoundError: pass

fig = plt.figure(figsize=(7.09, 6.6))
L, R = 0.075, 0.995

# ---------------- Harker diagrams (a–g) + legend slot ----------------
gsH = fig.add_gridspec(2, 4, left=L, right=R, top=0.968, bottom=0.515, wspace=0.42, hspace=0.36)
eok = epma(); s = sources(); lit = literature_aat()
srcm = s.groupby('type')[OX].median(); srcm.loc['Unweathered shale (PAAS)'] = pd.Series(PAAS)
PANELS = [('Al2O3', 'Al$_2$O$_3$', False), ('FeOt', 'FeO$_t$', False), ('TiO2', 'TiO$_2$', False), ('MgO', 'MgO', True),
          ('CaO', 'CaO', True), ('Na2O', 'Na$_2$O', True), ('K2O', 'K$_2$O', True)]
# (a) analytical totals
eall = epma(all_spots=True)
ax = fig.add_subplot(gsH[0, 0])
tek = ['MNG24_A3_1', 'MNG24_A3_2', 'MNG24_A3_3', 'MNG24_B1', 'MNG24_C2', 'MG24_B1', 'KK24_T1']
for i, t in enumerate(tek):
    v = eall.loc[eall.tektite == t, 'total']; ok = (v >= 97).values; j = np.random.default_rng(i).uniform(-.2, .2, len(v))
    ax.scatter(v.values[ok], (i + j)[ok], s=5, c=TCOL.get(t, 'k'), lw=0, zorder=3)
    ax.scatter(v.values[~ok], (i + j)[~ok], s=5, facecolors='none', edgecolors='0.5', lw=0.4)
ax.axvline(97, color='#c1121f', ls='--', lw=0.7); ax.set_yticks(range(len(tek))); ax.set_yticklabels([t.replace('MNG24_', '') for t in tek], fontsize=5.4)
ax.set_xlabel('EPMA total (wt%)'); ax.text(95.5, 6.6, '≥ 97 %', color='#c1121f', fontsize=5.4, ha='right', va='center')
ax.set_ylim(-0.6, 7.0); letter(ax, 'a')
for n, (ox, lab, logy) in enumerate(PANELS):
    ax = fig.add_subplot(gsH[(n + 1) // 4, (n + 1) % 4])
    ax.scatter(lit.SiO2, lit[ox], s=3, c='0.8', lw=0, zorder=1, rasterized=True)
    for t, g in eok.groupby('tektite'):
        ax.scatter(g.SiO2, g[ox], s=5, c=TCOL[t], lw=0, zorder=3)
    for t, row in srcm.iterrows():
        ax.scatter(row.SiO2, row[ox], marker='*', s=55, c=SCOL[t], edgecolors='k', lw=0.4, zorder=4)
    ax.set_xlim(30, 100); ax.set_xticks([40, 60, 80, 100])
    if logy: ax.set_yscale('log'); ax.set_ylim(0.005, 20)
    ax.set_ylabel(lab + ' (wt%)')
    if (n + 1) // 4 == 1: ax.set_xlabel('SiO$_2$ (wt%)')
    letter(ax, 'bcdefgh'[n])

# ---------------- rj-MCMC (h–l) ----------------
gsM = fig.add_gridspec(2, 4, left=L, right=R, top=0.405, bottom=0.215, wspace=0.42, hspace=0.32,
                       width_ratios=[0.8, 1.3, 0.85, 1.3])
names = [n for n in ORDER if n in S['names']]
# (h) log-likelihood, (i) K
ax = fig.add_subplot(gsM[0, 0])
for c, r in enumerate(S['res']):
    tr = r['trace']; ax.plot(tr[:, 0] / 1000, tr[:, 3], lw=0.4, color='#2c6fb0' if c in S['good'] else '0.6', alpha=0.8)
nmax = S['res'][0]['trace'][-1, 0]; ax.axvline(nmax / 2000, color='k', ls=':', lw=0.6)
lo = min(np.percentile(r['trace'][len(r['trace']) // 2:, 3], 1) for r in S['res'])
ax.set_ylim(lo - 120, max(r['trace'][:, 3].max() for r in S['res']) + 30); ax.set_ylabel('log-likelihood'); ax.set_xticklabels([])
letter(ax, 'i')
ax = fig.add_subplot(gsM[1, 0])
for c, r in enumerate(S['res']):
    tr = r['trace']; ax.plot(tr[:, 0] / 1000, tr[:, 1] + np.random.default_rng(c).uniform(-.15, .15), lw=0.5,
                             color='#2c6fb0' if c in S['good'] else '0.6', alpha=0.85)
ax.axvline(nmax / 2000, color='k', ls=':', lw=0.6); ax.set_xlabel('iteration (×10³)'); ax.set_ylabel('components K')
letter(ax, 'j')
# (j) posterior weights
ax = fig.add_subplot(gsM[:, 1]); x = np.arange(len(names))
m = [S['summ'][n]['mean'] for n in names]; sd = [S['summ'][n]['sd'] for n in names]
ax.bar(x, m, yerr=sd, color=[SCOL[n] for n in names], edgecolor='k', lw=0.4, capsize=1.8, error_kw=dict(lw=0.6), width=0.75)
for c in S['good']:
    cm = S['df'][S['df'].chain == c][names].mean() * 100
    ax.scatter(x + np.random.default_rng(c).uniform(-.22, .22, len(x)), cm, s=3, c='k', zorder=3, lw=0)
ax.set_xticks(x); ax.set_xticklabels([SHORT[n].replace('Unweathered shale', 'Shale (PAAS)') for n in names], rotation=55, ha='right', rotation_mode='anchor', fontsize=4.9)
ax.set_ylabel('posterior mixing weight (wt%)'); ax.set_ylim(0, 100)
ax.text(0.98, 0.98, f'{len(S["good"])} chains · mean ± 1σ · dots = chains',
        transform=ax.transAxes, ha='right', va='top', fontsize=5.2)
letter(ax, 'k')
# (k) sensitivity
ax = fig.add_subplot(gsM[:, 3])
runs = [r for r in [('main', 'Full'), ('no_random', 'No\nrandom'), ('no_alkali', 'No Na$_2$O,\nK$_2$O'),
                    ('local_only', 'Regional\nonly')] if r[0] in sens]
w = 0.8 / len(names)
for j, nm in enumerate(names):
    vals = [sens[k]['summ'][nm]['mean'] if nm in sens[k]['names'] else 0 for k, _ in runs]
    ax.bar(np.arange(len(runs)) + j * w - 0.4 + w / 2, vals, w, color=SCOL[nm], edgecolor='k', lw=0.25)
ax.set_xticks(np.arange(len(runs))); ax.set_xticklabels([l for _, l in runs], fontsize=5.0); ax.tick_params(axis='x', length=0)
ax.set_ylabel('mixing weight (wt%)'); letter(ax, 'm')
# (l) residuals
ax = fig.add_subplot(gsM[:, 2])
labs = {'SiO2': 'SiO$_2$', 'TiO2': 'TiO$_2$', 'Al2O3': 'Al$_2$O$_3$', 'FeOt': 'FeO$_t$', 'MnO': 'MnO', 'MgO': 'MgO', 'CaO': 'CaO', 'Na2O': 'Na$_2$O', 'K2O': 'K$_2$O'}
ox = S['oxides']
bp = ax.boxplot([S['resid'][i] for i in range(len(ox))], positions=np.arange(len(ox)), widths=0.55, showfliers=False, vert=False,
                medianprops=dict(color='#d95f02', lw=0.8), boxprops=dict(lw=0.5), whiskerprops=dict(lw=0.5), capprops=dict(lw=0.5))
ax.axvline(0, color='k', lw=0.5); ax.set_yticks(np.arange(len(ox))); ax.set_yticklabels([labs[o] for o in ox], fontsize=5.6)
ax.invert_yaxis(); ax.set_xlabel('model − observed (% of obs.)'); letter(ax, 'l')

# ---------------- legend strip: tektites (a–h) and lithologies (stars b–h, bars k, m) ----------------
lg = fig.add_axes([0.0, 0.0, 1.0, 0.105]); lg.axis('off')
ht = [Line2D([], [], ls='', marker='o', ms=3.2, color=TCOL[t], label=TLAB[t].replace(' (Khon Kaen, Thailand)', ' (Thailand)')) for t in ['MNG24_A3_1', 'MNG24_B1', 'MG24_B1', 'KK24_T1']]
ht += [Line2D([], [], ls='', marker='o', ms=3.2, color='0.8', label='Indochinite / Muong Nong (lit.)'),
       Line2D([], [], ls='', marker='o', ms=3.2, mfc='none', mec='0.5', label='Rejected (total < 97 %)')]
l1 = lg.legend(handles=ht, loc='upper left', bbox_to_anchor=(0.005, 1.0), ncol=2, fontsize=5.6, frameon=False, handletextpad=0.3,
               columnspacing=1.0, labelspacing=0.35, title='Tektites (EPMA, this study)', title_fontsize=6)
l1._legend_box.align = 'left'; lg.add_artist(l1)
hs = [Line2D([], [], ls='', marker='s', ms=5.5, mfc=SCOL[n], mec='k', mew=0.4, label=SHORT[n] if n != 'Random' else 'Random (unconstrained)') for n in names]
l2 = lg.legend(handles=hs, loc='upper left', bbox_to_anchor=(0.41, 1.0), ncol=3, fontsize=5.6, frameon=False, handletextpad=0.3,
               columnspacing=1.0, labelspacing=0.35, title='Source lithologies: medians (★, b–h; this study + Sieh et al. 2020; PAAS) and mixing components (k, m)', title_fontsize=6)
l2._legend_box.align = 'left'
for ext in ['svg', 'pdf', 'png']:
    fig.savefig(os.path.join(OUT, f'Fig5_tektite_geochem_rjMCMC.{ext}'), dpi=400 if ext == 'png' else None, bbox_inches='tight', pad_inches=0.03)
print({n: (round(S['summ'][n]['mean'], 1), round(S['summ'][n]['sd'], 1)) for n in names}, 'good chains', len(S['good']))
