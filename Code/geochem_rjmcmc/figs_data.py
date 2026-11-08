"""Figures that depend only on the data: Fig 14 (EPMA QC + Harker) and Fig 17 (PGE / Pd interference)."""
import os
import numpy as np, pandas as pd, matplotlib
matplotlib.use('Agg'); import matplotlib.pyplot as plt
from load import epma, laicpms, sources_all as sources, literature_aat, OX, PAAS, UCC

plt.rcParams.update({'font.size': 9, 'axes.linewidth': 0.8, 'savefig.dpi': 300, 'font.family': 'DejaVu Sans'})
TCOL = {'MNG24_A3_1':'#1f5fbf','MNG24_B1':'#2a9d8f','MG24_B1':'#7b4fb5','KK24_T1':'#e07a1f'}
TLAB = {'MNG24_A3_1':'MNG24_A3_1 (Laos)','MNG24_B1':'MNG24_B1 (Laos)','MG24_B1':'MG24_B1 (Laos)','KK24_T1':'KK24_T1 (Khon Kaen, Thailand)'}
SCOL = {'Khorat sandstone':'#d9a520','Khorat mudstone':'#8c6d1f','Bolaven tholeiite':'#8b0000','Bolaven alkali basalt':'#e0457b','Lateritic saprolite':'#6b3e26',
        'Diamicton / "catastro-loess"':'#9a9a9a','Unweathered shale (PAAS)':'#3c3c3c',
        'Metatuff':'#4f8f5a','Sedimentary laterite':'#c46b2d'}
OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'figures') + '/'
def LAB(n): return 'Felsic metatuff' if n == 'Metatuff' else n

def fig14():
    eall = epma(all_spots=True); eok = epma(); s = sources(); lit = literature_aat()
    fig = plt.figure(figsize=(11, 6.2)); gs = fig.add_gridspec(2, 4, hspace=0.38, wspace=0.34)
    ax = fig.add_subplot(gs[0, 0])
    tek = ['MNG24_A3_1','MNG24_A3_2','MNG24_A3_3','MNG24_B1','MNG24_C2','MG24_B1','KK24_T1']
    for i, t in enumerate(tek):
        v = eall.loc[eall.tektite == t, 'total']; ok = v >= 97
        ax.scatter(v[ok], np.full(ok.sum(), i)+np.random.default_rng(i).uniform(-.18,.18,ok.sum()), s=9, c=TCOL.get(t,'k'), zorder=3)
        ax.scatter(v[~ok], np.full((~ok).sum(), i)+np.random.default_rng(i).uniform(-.18,.18,(~ok).sum()), s=9, facecolors='none', edgecolors='0.45', lw=.6)
    ax.axvline(97, color='r', ls='--', lw=.9); ax.set_yticks(range(len(tek))); ax.set_yticklabels([t.replace('MNG24_','') for t in tek], fontsize=7.5)
    ax.set_xlabel('EPMA oxide total (wt%)'); ax.set_title('(a) Analytical totals', fontsize=9, loc='left')
    ax.text(95.5, 3.4, 'accept ≥ 97 %', color='r', fontsize=7, ha='right', rotation=90, va='center')
    panels = [('Al2O3','Al$_2$O$_3$'),('FeOt','FeO$_t$'),('MgO','MgO'),('CaO','CaO'),('Na2O','Na$_2$O'),('K2O','K$_2$O'),('TiO2','TiO$_2$')]
    srcm = s.groupby('type')[OX].median()
    srcm.loc['Unweathered shale (PAAS)'] = pd.Series(PAAS)
    for n, (ox, lab) in enumerate(panels):
        ax = fig.add_subplot(gs[(n+1)//4, (n+1) % 4])
        ax.scatter(lit.SiO2, lit[ox], s=5, c='0.82', lw=0, label='Indochinite / Muong Nong literature', zorder=1)
        for t, g in eok.groupby('tektite'):
            ax.scatter(g.SiO2, g[ox], s=10, c=TCOL[t], lw=0, label=TLAB[t], zorder=3)
        for t, row in srcm.iterrows():
            ax.scatter(row.SiO2, row[ox], marker='*', s=130, c=SCOL[t], edgecolors='k', lw=.5, zorder=4, label=LAB(t))
        ax.set_xlim(30, 100); ax.set_xlabel('SiO$_2$ (wt%, anhydrous)'); ax.set_ylabel(lab+' (wt%)')
        ax.set_title(f'({"bcdefgh"[n]})', fontsize=9, loc='left')
        if ox in ('CaO','Na2O','MgO','K2O'): ax.set_yscale('log'); ax.set_ylim(0.005, 15)
    h, l = ax.get_legend_handles_labels()
    fig.legend(h, l, loc='lower center', ncol=6, fontsize=7, frameon=False, bbox_to_anchor=(0.5, -0.07), markerscale=0.8)
    fig.suptitle('Tektite major elements: accepted EPMA analyses, regional literature and candidate source lithologies', fontsize=10.5, fontweight='bold', y=0.99)
    fig.savefig(OUT+'Fig14_EPMA_QC_Harker.png', bbox_inches='tight'); plt.close(fig)

CI_PGE = {'Ru':710,'Pd':550,'Ir':455}          # ppb, McDonough & Sun (1995)
UCC_PGE = {'Ru':0.34,'Pd':0.52,'Ir':0.022}     # ppb, Rudnick & Gao (2003)

def pge_stats():
    l, _ = laicpms()
    sp = l.groupby('spot').agg(tektite=('tektite','first'), Pd=('Pd','mean'), Y=('Y','mean'), Cu=('Cu','mean'),
                               Ru=('Ru','mean'), Ir191=('Ir191','mean'), Ir193=('Ir193','mean'), Zr=('Zr','mean'))
    sp['Pd/Y'] = sp.Pd/sp.Y
    return l, sp

def fig17():
    l, sp = pge_stats()
    fig, axs = plt.subplots(1, 3, figsize=(12, 3.7)); plt.subplots_adjust(wspace=0.32)
    ax = axs[0]
    for t, g in l.groupby('tektite'):
        c = TCOL.get(t, '#5aa0e0'); ax.scatter(g.Y, g.Pd*1000, s=10, c=c, alpha=.35, lw=0)
    for t, g in sp.groupby('tektite'):
        c = TCOL.get(t, '#5aa0e0'); ax.scatter(g.Y, g.Pd*1000, s=40, c=c, edgecolors='k', lw=.5, label=f'{t} (spot means)')
    yy = np.linspace(1, 40, 60)
    for ox, ls in [(0.001,':'),(0.002,'--'),(0.004,'-.')]:
        ax.plot(yy, yy*ox/0.2233*1000, 'k', ls=ls, lw=.8, label=f'apparent $^{{105}}$Pd from $^{{89}}$Y$^{{16}}$O$^+$, YO/Y = {ox*100:.1f}%')
    ax.axhline(UCC_PGE['Pd'], color='g', lw=1); ax.text(1, UCC_PGE['Pd']*1.3, 'upper crust 0.5 ppb', color='g', fontsize=7)
    ax.set_yscale('log'); ax.set_ylim(0.3, 1000); ax.set_xlim(0, 38)
    ax.set_xlabel('Y (µg/g)'); ax.set_ylabel('reported "Pd" (ppb)'); ax.legend(fontsize=6, loc='lower right')
    ax.set_title('(a) "Pd" tracks Y, not the glass budget', fontsize=9, loc='left')
    ax = axs[1]
    ax.scatter(l.Ir191*1000, l.Ir193*1000, s=14, c=[TCOL.get(t, '#5aa0e0') for t in l.tektite], edgecolors='k', lw=.3)
    ax.plot([0, 5], [0, 5], 'k--', lw=.8); ax.set_xlim(-0.2, 5); ax.set_ylim(-0.2, 5)
    n0 = ((l.Ir191 == 0) & (l.Ir193 == 0)).sum()
    ax.set_xlabel('$^{191}$Ir (ppb)'); ax.set_ylabel('$^{193}$Ir (ppb)')
    ax.text(0.3, 4.5, f'{n0} of {len(l)} analyses: both isotopes = 0\nnon-zero values do not agree\nbetween isotopes → below detection', fontsize=7, va='top')
    ax.set_title('(b) Ir is below detection', fontsize=9, loc='left')
    ax = axs[2]; el = ['Ru','Pd','Ir']; x = np.arange(3)
    ax.plot(x, [1]*3, 'k-', marker='*', ms=10, label='CI chondrite')
    ax.plot(x, [UCC_PGE[e]/CI_PGE[e] for e in el], 'g-o', ms=5, label='upper continental crust')
    ax.plot(x, [0.0005*CI_PGE[e]/CI_PGE[e] + UCC_PGE[e]/CI_PGE[e] for e in el], 'g:', label='crust + 0.05 % CI')
    ru = l.Ru.mean()*1000; pd_ = l.Pd.median()*1000; irmax = max(l.Ir191.max(), l.Ir193.max())*1000
    ax.plot([0], [ru/CI_PGE['Ru']], 'o', c='#1f5fbf', ms=7, label='tektites, LA-ICP-MS (Ru mean)')
    ax.plot([1], [pd_/CI_PGE['Pd']], 'X', c='r', ms=9, label='reported "Pd" (interference)')
    ax.errorbar([2], [irmax/CI_PGE['Ir']], yerr=[[irmax/CI_PGE['Ir']*0.6], [0]], uplims=True, fmt='v', c='#1f5fbf', ms=7, label='Ir upper limit (max non-zero)')
    ax.set_xticks(x); ax.set_xticklabels(el); ax.set_yscale('log'); ax.set_ylim(1e-5, 3)
    ax.set_ylabel('concentration / CI chondrite'); ax.legend(fontsize=6.3, loc='lower left')
    ax.set_title('(c) No PGE signal resolvable by LA-ICP-MS', fontsize=9, loc='left')
    fig.suptitle('Platinum-group elements: Ir below detection; the reported Pd is an analytical artefact', fontsize=10.5, fontweight='bold', y=1.03)
    fig.savefig(OUT+'Fig17_PGE_Pd_Ir.png', bbox_inches='tight'); plt.close(fig)
    return sp

if __name__ == '__main__':
    import os; os.makedirs(OUT, exist_ok=True)
    fig14(); sp = fig17()
    print(sp.round(4).to_string())
    print('YO/Y equivalent (%) per spot:', (sp['Pd/Y']*0.2233*100).round(3).tolist())
