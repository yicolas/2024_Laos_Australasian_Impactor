"""Supplementary Figs S1 (trace elements) and S4 (platinum-group elements), house style (7.09 in wide, bold panel
letters, legend strips at the bottom). Same data and calculations as summarize.fig16 / figs_data.fig17.
Usage: python make_figS_geochem.py <res_dir> <outdir>"""
import sys, os, pickle, numpy as np, pandas as pd
import matplotlib as mpl, matplotlib.pyplot as plt
from matplotlib.lines import Line2D
from load import epma, laicpms, OX
from summarize import summarise, source_traces, mixture_traces, eu_star, CI, REE
from figs_data import SCOL, TCOL, LAB, pge_stats, CI_PGE, UCC_PGE
RES, OUT = sys.argv[1], sys.argv[2]; os.makedirs(OUT, exist_ok=True)
mpl.rcParams.update({'font.family': 'DejaVu Sans', 'font.size': 6.5, 'axes.linewidth': 0.6, 'xtick.major.width': 0.5,
                     'ytick.major.width': 0.5, 'xtick.major.size': 2.5, 'ytick.major.size': 2.5, 'svg.fonttype': 'none',
                     'pdf.fonttype': 42, 'axes.labelpad': 2})
def letter(ax, s, title):
    ax.text(-0.02, 1.025, s, transform=ax.transAxes, fontsize=9, fontweight='bold', ha='right', va='bottom')
    ax.text(0.0, 1.025, title, transform=ax.transAxes, fontsize=6.3, ha='left', va='bottom')
def save(fig, name):
    for ext in ['svg', 'pdf', 'png']:
        fig.savefig(os.path.join(OUT, f'{name}.{ext}'), dpi=400 if ext == 'png' else None, bbox_inches='tight', pad_inches=0.03)
    plt.close(fig)
SRC = ['Khorat sandstone', 'Khorat mudstone', 'Unweathered shale (PAAS)', 'Bolaven tholeiite', 'Bolaven alkali basalt',
       'Lateritic saprolite', 'Sedimentary laterite', 'Diamicton / "catastro-loess"']
SHORTN = {'Unweathered shale (PAAS)': 'Unweathered shale (PAAS)', 'Diamicton / "catastro-loess"': 'Diamicton / loess'}

# ======================= S1: trace elements =======================
S = summarise(pickle.load(open(os.path.join(RES, 'res_main.pkl'), 'rb'))); tr = source_traces(); mixtr = mixture_traces(S, tr)
l, _ = laicpms(); e = epma()
from load import ROOT
lit = pd.read_csv(ROOT + "Tektite data/AAT_master_list.csv", low_memory=False)
lit = lit[lit.SheetName.isin(['Muong Nong', 'Indochinites', 'Indochinite', 'Hanoi', 'Vinh', 'Dalat', 'Saigon'])]
fig = plt.figure(figsize=(7.09, 3.25))
gs = fig.add_gridspec(1, 3, left=0.07, right=0.99, top=0.9, bottom=0.36, wspace=0.34, width_ratios=[1.25, 1, 1])
# (a) accuracy check
ax = fig.add_subplot(gs[0])
A1 = e[e.tektite == 'MNG24_A3_1'][OX].mean(); la1 = l[l.tektite == 'MNG24_A3_1']
chk = {'Al$_2$O$_3$': la1.Al2O3_LA.mean() / A1.Al2O3, 'MgO': la1.MgO_LA.mean() / A1.MgO, 'TiO$_2$': la1.TiO2_LA.mean() / A1.TiO2, 'MnO': la1.MnO_LA.mean() / A1.MnO}
lit_el = ['Sc', 'Cr', 'Co', 'Ni', 'Rb', 'Sr', 'Zr', 'Ba', 'La', 'Ce', 'Sm', 'Eu', 'Yb', 'Hf', 'Th', 'U']
lr = {el: la1[el].median() / pd.to_numeric(lit[el], errors='coerce').median() for el in lit_el}
xs = list(chk) + lit_el; vs = list(chk.values()) + list(lr.values())
ax.axhspan(0.8, 1.2, color='0.92', zorder=0, lw=0); ax.axhline(1, color='k', lw=0.6)
ax.bar(range(len(xs)), vs, color=['#b5523b'] * len(chk) + ['#1f5fbf'] * len(lit_el), edgecolor='k', lw=0.3, width=0.75)
ax.set_xticks(range(len(xs))); ax.set_xticklabels(xs, rotation=90, fontsize=5.6); ax.set_ylim(0, 2.2); ax.set_xlim(-0.7, len(xs) - 0.3)
ax.set_ylabel('LA-ICP-MS / reference')
ax.text(0.98, 0.97, 'LA / EPMA, same tektite', color='#b5523b', fontsize=5.6, transform=ax.transAxes, va='top', ha='right')
ax.text(0.98, 0.90, 'LA / Indochinite literature median', color='#1f5fbf', fontsize=5.6, transform=ax.transAxes, va='top', ha='right')
letter(ax, 'a', 'LA-ICP-MS accuracy check (MNG24_A3_1); band ±20 %')
# (b) REE
ax = fig.add_subplot(gs[1]); x = np.arange(len(REE))
litv = np.array([[pd.to_numeric(lit[el], errors='coerce').quantile(q) / CI[el] for el in REE] for q in (.1, .5, .9)])
ax.fill_between(x, litv[0], litv[2], color='0.86', lw=0); ax.plot(x, litv[1], color='0.55', lw=1.0)
for nm in SRC:
    if nm in tr and np.isfinite(tr[nm].get('La', np.nan)): ax.plot(x, [tr[nm][el] / CI[el] for el in REE], '--', color=SCOL[nm], lw=0.7)
for t, g in l.groupby('tektite'): ax.plot(x, [g[el].median() / CI[el] for el in REE], '-o', ms=2.6, color=TCOL.get(t, '#5aa0e0'), lw=1.2)
ax.set_yscale('log'); ax.set_xticks(x); ax.set_xticklabels(REE, fontsize=5.8); ax.set_ylabel('sample / CI chondrite'); ax.set_ylim(3, 800)
letter(ax, 'b', 'Chondrite-normalised REE')
# (c) Th/Sc vs Eu/Eu*
ax = fig.add_subplot(gs[2])
th = pd.to_numeric(lit.Th, errors='coerce'); sc = pd.to_numeric(lit.Sc, errors='coerce')
sm = pd.to_numeric(lit.Sm, errors='coerce'); eu = pd.to_numeric(lit.Eu, errors='coerce'); tb = pd.to_numeric(lit.Tb, errors='coerce')
leu = (eu / CI['Eu']) / ((sm / CI['Sm']) ** (2 / 3) * (tb / CI['Tb']) ** (1 / 3))
ax.scatter(th / sc, leu, s=5, c='0.8', lw=0, zorder=1)
if len(mixtr): ax.scatter(mixtr['Th/Sc'], mixtr['Eu/Eu*'], s=3, c='#2ca02c', alpha=0.25, lw=0, zorder=2)
for nm in SRC:
    d = tr.get(nm)
    if d is not None and np.isfinite(d.get('Th', np.nan)): ax.scatter(d['Th'] / d['Sc'], eu_star(d), marker='*', s=55, c=SCOL[nm], edgecolors='k', lw=0.4, zorder=4)
for t, g in l.groupby('tektite'): ax.scatter(g.Th / g.Sc, eu_star(g), s=8, c=TCOL.get(t, '#5aa0e0'), edgecolors='k', lw=0.25, zorder=3)
ax.axhline(1, color='k', ls=':', lw=0.6); ax.set_xscale('log'); ax.set_xlim(0.05, 3); ax.set_ylim(0.4, 1.25)
ax.set_xlabel('Th / Sc'); ax.set_ylabel('Eu / Eu*'); letter(ax, 'c', 'Calibration-insensitive ratios')
lg = fig.add_axes([0.0, 0.0, 1.0, 0.2]); lg.axis('off')
h1 = [Line2D([], [], color=TCOL.get(t, '#5aa0e0'), marker='o', ms=3, lw=1.2, label=f'{t} (LA-ICP-MS)') for t in sorted(l.tektite.unique())]
h1 += [Line2D([], [], color='0.6', lw=4, alpha=0.5, label='Indochinite / Muong Nong literature (10–90 %, median)'),
       Line2D([], [], ls='', marker='o', ms=3, color='#2ca02c', alpha=0.5, label='posterior bulk mixtures (Fig. 5), c')]
l1 = lg.legend(handles=h1, loc='upper left', bbox_to_anchor=(0.005, 1.0), ncol=1, fontsize=5.4, frameon=False, title='Tektites and reference', title_fontsize=5.8)
l1._legend_box.align = 'left'; lg.add_artist(l1)
h2 = [Line2D([], [], color=SCOL[n], ls='--', marker='*', ms=5, mec='k', mew=0.3, lw=0.8, label=SHORTN.get(n, LAB(n))) for n in SRC if n in tr and np.isfinite(tr[n].get('Th', np.nan))]
l2 = lg.legend(handles=h2, loc='upper left', bbox_to_anchor=(0.42, 1.0), ncol=3, fontsize=5.4, frameon=False,
               title='Source lithology medians (dashed in b, stars in c)', title_fontsize=5.8)
l2._legend_box.align = 'left'
save(fig, 'FigS1_trace_elements')

# ======================= S4: platinum-group elements =======================
l, sp = pge_stats()
fig = plt.figure(figsize=(7.09, 2.85))
gs = fig.add_gridspec(1, 3, left=0.075, right=0.99, top=0.9, bottom=0.3, wspace=0.36)
ax = fig.add_subplot(gs[0])
for t, g in l.groupby('tektite'): ax.scatter(g.Y, g.Pd * 1000, s=5, c=TCOL.get(t, '#5aa0e0'), alpha=0.35, lw=0)
for t, g in sp.groupby('tektite'): ax.scatter(g.Y, g.Pd * 1000, s=18, c=TCOL.get(t, '#5aa0e0'), edgecolors='k', lw=0.4)
yy = np.linspace(1, 40, 60)
for ox, ls in [(0.001, ':'), (0.002, '--'), (0.004, '-.')]:
    ax.plot(yy, yy * ox / 0.2233 * 1000, 'k', ls=ls, lw=0.7); ax.text(37.5, 37.5 * ox / 0.2233 * 1000, f'{ox * 100:.1f} %', fontsize=5.2, ha='right', va='bottom')
ax.axhline(UCC_PGE['Pd'], color='g', lw=0.8); ax.text(1, UCC_PGE['Pd'] * 1.4, 'upper crust 0.5 ppb', color='g', fontsize=5.4)
ax.set_yscale('log'); ax.set_ylim(0.3, 1000); ax.set_xlim(0, 38); ax.set_xlabel('Y (µg/g)'); ax.set_ylabel('reported "Pd" (ppb)')
letter(ax, 'a', '"Pd" tracks Y (lines: $^{89}$Y$^{16}$O$^+$ on $^{105}$Pd)')
ax = fig.add_subplot(gs[1])
ax.scatter(l.Ir191 * 1000, l.Ir193 * 1000, s=9, c=[TCOL.get(t, '#5aa0e0') for t in l.tektite], edgecolors='k', lw=0.25)
ax.plot([0, 5], [0, 5], 'k--', lw=0.6); ax.set_xlim(-0.2, 5); ax.set_ylim(-0.2, 5)
n0 = ((l.Ir191 == 0) & (l.Ir193 == 0)).sum()
ax.set_xlabel('$^{191}$Ir (ppb)'); ax.set_ylabel('$^{193}$Ir (ppb)')
ax.text(0.97, 0.55, f'{n0} of {len(l)} analyses have both\nisotopes = 0; non-zero values\ndisagree → Ir below detection', fontsize=5.4, ha='right', va='bottom', transform=ax.transAxes)
letter(ax, 'b', 'Ir is below detection')
ax = fig.add_subplot(gs[2]); el = ['Ru', 'Pd', 'Ir']; x = np.arange(3)
ax.plot(x, [1] * 3, 'k-', marker='*', ms=6, lw=0.8)
ax.plot(x, [UCC_PGE[q] / CI_PGE[q] for q in el], 'g-o', ms=3, lw=0.8)
ax.plot(x, [0.0005 + UCC_PGE[q] / CI_PGE[q] for q in el], 'g:', lw=0.9)
ru = l.Ru.mean() * 1000; pd_ = l.Pd.median() * 1000; irmax = max(l.Ir191.max(), l.Ir193.max()) * 1000
ax.plot([0], [ru / CI_PGE['Ru']], 'o', c='#1f5fbf', ms=4.5)
ax.plot([1], [pd_ / CI_PGE['Pd']], 'X', c='#c1121f', ms=5.5)
ax.errorbar([2], [irmax / CI_PGE['Ir']], yerr=[[irmax / CI_PGE['Ir'] * 0.6], [0]], uplims=True, fmt='v', c='#1f5fbf', ms=4.5, lw=0.8)
ax.set_xticks(x); ax.set_xticklabels(el); ax.set_yscale('log'); ax.set_ylim(1e-5, 3); ax.set_xlim(-0.4, 2.4)
ax.set_ylabel('concentration / CI chondrite'); letter(ax, 'c', 'No PGE signal resolvable by LA-ICP-MS')
lg = fig.add_axes([0.0, 0.0, 1.0, 0.13]); lg.axis('off')
h = [Line2D([], [], ls='', marker='o', ms=3.5, mfc=TCOL.get(t, '#5aa0e0'), mec='k', mew=0.3, label=f'{t} (large: ablation-site means)') for t in sorted(l.tektite.unique())]
h += [Line2D([], [], color='k', marker='*', ms=5, lw=0.8, label='CI chondrite'), Line2D([], [], color='g', marker='o', ms=3, lw=0.8, label='upper crust (Rudnick & Gao, 2003)'),
      Line2D([], [], color='g', ls=':', lw=0.9, label='crust + 0.05 % CI'), Line2D([], [], ls='', marker='o', ms=4, color='#1f5fbf', label='tektite Ru (mean)'),
      Line2D([], [], ls='', marker='X', ms=4.5, color='#c1121f', label='reported "Pd" (interference)'), Line2D([], [], ls='', marker='v', ms=4, color='#1f5fbf', label='Ir upper limit')]
lg.legend(handles=h, loc='center', ncol=4, fontsize=5.3, frameon=False, columnspacing=1.0, handletextpad=0.4)
save(fig, 'FigS4_PGE_Pd_Ir')
print('ok')
