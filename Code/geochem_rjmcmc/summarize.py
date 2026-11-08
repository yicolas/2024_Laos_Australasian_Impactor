"""Summarise rj-MCMC chains; Fig 15 (inversion) and Fig 16 (trace-element test)."""
import os
import numpy as np, pandas as pd, pickle, json, sys, matplotlib
matplotlib.use('Agg'); import matplotlib.pyplot as plt
from load import ROOT, epma, laicpms, sources_all as sources, literature_aat, OX, PAAS
from figs_data import SCOL, TCOL, OUT, LAB

SCOL = dict(SCOL, Random='#c9c9ff')
SHORT = {'Khorat sandstone':'Khorat sandstone','Khorat mudstone':'Khorat mudstone','Bolaven tholeiite':'Bolaven tholeiite','Bolaven alkali basalt':'Bolaven alkali basalt',
         'Lateritic saprolite':'Lateritic saprolite','Diamicton / "catastro-loess"':'Diamicton / loess',
         'Unweathered shale (PAAS)':'Unweathered shale','Random':'Random','Metatuff':'Felsic metatuff',
         'Sedimentary laterite':'Sedimentary laterite'}
ORDER = ['Khorat sandstone','Khorat mudstone','Unweathered shale (PAAS)','Bolaven tholeiite','Bolaven alkali basalt','Lateritic saprolite',
         'Diamicton / "catastro-loess"','Sedimentary laterite','Metatuff','Random']
# PAAS traces (Taylor & McLennan 1985)
PAAS_TR = dict(Sc=16, Th=14.6, La=38.2, Ce=79.6, Nd=33.9, Sm=5.55, Eu=1.08, Gd=4.66, Dy=4.68, Yb=2.82, Lu=0.433, Zr=210, Hf=5.0, Co=23, Ni=55, Cr=110)
CI = {'La':0.237,'Ce':0.613,'Pr':0.0928,'Nd':0.457,'Sm':0.148,'Eu':0.0563,'Gd':0.199,'Tb':0.0361,'Dy':0.246,'Ho':0.0546,
      'Er':0.16,'Tm':0.0247,'Yb':0.161,'Lu':0.0246}
REE = ['La','Ce','Nd','Sm','Eu','Gd','Dy','Yb','Lu']

def chain_table(res):
    rows = []
    for c, r in enumerate(res):
        names = r['names']
        for s in r['out']:
            w = np.zeros(len(names))
            for k, t in enumerate(s['types']): w[t] += s['W'][k].mean()
            rows.append(dict(chain=c, K=s['K'], ll=s['ll'], **{names[i]: w[i] for i in range(len(names))}))
    return pd.DataFrame(rows), res[0]['names']

def summarise(res, tol=50.0):
    df, names = chain_table(res)
    lp = pd.Series({c: np.median(r['trace'][len(r['trace'])//2:, 3]) for c, r in enumerate(res)})
    med = lp; best = med.max()
    good = med.index[med >= best - tol].tolist()
    g = df[df.chain.isin(good)]
    summ = {}
    bas = [n for n in names if n.startswith('Bolaven')]
    if bas: df['All basalt'] = df[bas].sum(axis=1); g = df[df.chain.isin(good)]
    for nm in names + (['All basalt'] if bas else []):
        within = g.groupby('chain')[nm].var().mean(); between = g.groupby('chain')[nm].mean().var() if len(good) > 1 else 0
        summ[nm] = dict(mean=100*g[nm].mean(), sd=100*np.sqrt(np.nan_to_num(within)+np.nan_to_num(between)),
                        p_present=float((g[nm] > 0.01).mean()), mean_all=100*df[nm].mean())
    Kd = g.K.value_counts(normalize=True).sort_index()
    comp = {}
    for nm_i, nm in enumerate(names):
        acc = []; wts = []
        for c in good:
            for smp in res[c]['out']:
                for k, t in enumerate(smp['types']):
                    if t == nm_i:
                        v = smp['V'][k]; acc.append(v/v.sum()*100); wts.append(smp['W'][k].mean())
        if acc and sum(wts) > 0: comp[nm] = np.average(np.array(acc), axis=0, weights=np.array(wts))
    # posterior predictive
    Y = np.mean([s['Y'] for c in good for s in res[c]['out']], axis=0)   # D x N
    e = epma(); obs = e[res[0]['oxides']].values.T
    resid = (Y-obs)/obs*100
    pred_mean = Y.mean(1); obs_mean = obs.mean(1)
    return dict(comp=comp, df=df, good=good, chain_ll=med.to_dict(), summ=summ, K=Kd.to_dict(), resid=resid,
                pred_mean=pred_mean, obs_mean=obs_mean, oxides=res[0]['oxides'], names=names)

def source_traces():
    s = sources(); t = {}
    for typ, g in s.groupby('type'):
        t[typ] = {e: float(pd.to_numeric(g[e], errors='coerce').median()) for e in ['Sc','Th','La','Ce','Nd','Sm','Eu','Gd','Dy','Yb','Lu','Zr','Hf','Co','Ni','Cr']}
    t['Unweathered shale (PAAS)'] = PAAS_TR
    return t

def eu_star(d):
    return (d['Eu']/CI['Eu'])/np.sqrt((d['Sm']/CI['Sm'])*(d['Gd']/CI['Gd']))

def mixture_traces(S, tr):
    """Bulk (mass-weighted) trace mixture for each posterior sample, excluding the Random component."""
    out = []
    for _, r in S['df'][S['df'].chain.isin(S['good'])].iterrows():
        f = {nm: r[nm] for nm in S['names'] if nm != 'Random' and r[nm] > 0 and np.isfinite(tr.get(nm, {}).get('Th', np.nan))}
        tot = sum(f.values()); d = {}
        for el in ['Sc','Th','La','Sm','Eu','Gd','Yb','Zr','Hf','Co','Ni','Cr']:
            d[el] = sum(f[nm]*tr[nm][el] for nm in f)/tot
        d['Th/Sc'] = d['Th']/d['Sc']; d['Eu/Eu*'] = eu_star(d); d['basalt'] = (f.get('Bolaven tholeiite', 0)+f.get('Bolaven alkali basalt', 0))/tot
        out.append(d)
    return pd.DataFrame(out)

def fig15(S, sens):
    fig = plt.figure(figsize=(12, 7.2)); gs = fig.add_gridspec(2, 3, hspace=0.42, wspace=0.3)
    ax = fig.add_subplot(gs[0, 0])
    for c, r in enumerate(S['res']):
        tr = r['trace']; ax.plot(tr[:, 0]/1000, tr[:, 3], lw=.6, alpha=.9 if c in S['good'] else .35,
                                 color=('C0' if c in S['good'] else '0.6'))
    n = S['res'][0]['trace'][-1, 0]
    ax.axvline(n/2000, color='k', ls=':', lw=.8); ax.set_xlabel('iteration (×10³)'); ax.set_ylabel('log-likelihood')
    lo = min(np.percentile(r['trace'][len(r['trace'])//2:, 3], 1) for r in S['res'])
    ax.set_ylim(lo-150, max(r['trace'][:, 3].max() for r in S['res'])+40)
    ax.set_title('(a) Log-likelihood, 12 chains\n(dotted line = end of burn-in)', fontsize=8.5, loc='left')
    ax = fig.add_subplot(gs[0, 1])
    for c, r in enumerate(S['res']):
        tr = r['trace']; ax.plot(tr[:, 0]/1000, tr[:, 1]+np.random.default_rng(c).uniform(-.15, .15), lw=.7,
                                 color=('C0' if c in S['good'] else '0.6'), alpha=.8)
    ax.set_xlabel('iteration (×10³)'); ax.set_ylabel('number of components K')
    ax.set_title('(b) Trans-dimensional sampling of K', fontsize=8.5, loc='left')
    ax = fig.add_subplot(gs[0, 2])
    names = [n for n in ORDER if n in S['names']]; x = np.arange(len(names))
    m = [S['summ'][n]['mean'] for n in names]; sd = [S['summ'][n]['sd'] for n in names]
    ax.bar(x, m, yerr=sd, color=[SCOL[n] for n in names], edgecolor='k', lw=.5, capsize=3)
    for c in S['good']:
        cm = S['df'][S['df'].chain == c][names].mean()*100
        ax.scatter(x+np.random.default_rng(c).uniform(-.25, .25, len(x)), cm, s=8, c='k', zorder=3)
    ax.set_xticks(x); ax.set_xticklabels([SHORT[n] for n in names], fontsize=7, rotation=40, ha='right', rotation_mode='anchor')
    ax.set_ylabel('mixing weight (wt%, mean of analyses)')
    ax.set_title('(c) Posterior source contributions\n(bars: mean ± 1σ within+between chains; dots: chain means)', fontsize=8.5, loc='left')
    ax = fig.add_subplot(gs[1, 0:2])
    labs = ['SiO$_2$','TiO$_2$','Al$_2$O$_3$','FeO$_t$','MnO','MgO','CaO','Na$_2$O','K$_2$O']
    ox = S['oxides']; idx = [OX.index(o) for o in ox]
    ax.boxplot([S['resid'][i] for i in range(len(ox))], positions=np.arange(len(ox)), widths=.5, showfliers=False)
    ax.axhline(0, color='k', lw=.6); ax.set_xticks(np.arange(len(ox))); ax.set_xticklabels([labs[i] for i in idx])
    ax.set_ylabel('posterior-mean model − observed\n(% of observed, per analysis)')
    ax.set_title('(d) Posterior predictive fit to the 82 accepted EPMA analyses', fontsize=8.5, loc='left')
    ax = fig.add_subplot(gs[1, 2])
    runs = [('main','Full dictionary'), ('no_random','No random\ncomponent'), ('no_alkali','Na$_2$O, K$_2$O\nexcluded'), ('local_only','Regional\nlithologies only')]
    runs = [r for r in runs if r[0] in sens]
    width = 0.8/len(names)
    for j, nm in enumerate(names):
        vals = [sens[k]['summ'].get(nm, {'mean': 0})['mean'] if nm in sens[k]['names'] else 0 for k, _ in runs]
        ax.bar(np.arange(len(runs))+j*width-0.4+width/2, vals, width, color=SCOL[nm], edgecolor='k', lw=.3, label=LAB(nm))
    ax.set_xticks(np.arange(len(runs))); ax.set_xticklabels([l for _, l in runs], fontsize=7)
    ax.set_ylabel('mixing weight (wt%)'); ax.legend(fontsize=6, loc='upper right', frameon=False)
    ax.set_title('(e) Sensitivity to the dictionary and data', fontsize=8.5, loc='left')
    fig.suptitle('Reversible-jump MCMC source unmixing of tektite major elements (formulation of Carter et al., 2025)', fontsize=10.5, fontweight='bold', y=1.0)
    fig.savefig(OUT+'Fig15_rjMCMC.png', bbox_inches='tight'); plt.close(fig)

def fig16(S, mixtr):
    l, _ = laicpms(); e = epma(); tr = source_traces(); lit = pd.read_csv(
        ROOT + "Tektite data/AAT_master_list.csv", low_memory=False)
    lit = lit[lit.SheetName.isin(['Muong Nong','Indochinites','Indochinite','Hanoi','Vinh','Dalat','Saigon'])]
    fig, axs = plt.subplots(1, 3, figsize=(13, 4.1)); plt.subplots_adjust(wspace=0.3)
    ax = axs[0]
    A1 = e[e.tektite == 'MNG24_A3_1'][OX].mean(); la1 = l[l.tektite == 'MNG24_A3_1']
    chk = {'Al$_2$O$_3$': la1.Al2O3_LA.mean()/A1.Al2O3, 'MgO': la1.MgO_LA.mean()/A1.MgO, 'TiO$_2$': la1.TiO2_LA.mean()/A1.TiO2, 'MnO': la1.MnO_LA.mean()/A1.MnO}
    lit_el = ['Sc','Cr','Co','Ni','Rb','Sr','Zr','Ba','La','Ce','Sm','Eu','Yb','Hf','Th','U']
    lr = {el: la1[el].median()/pd.to_numeric(lit[el], errors='coerce').median() for el in lit_el}
    xs = list(chk)+lit_el; vs = list(chk.values())+list(lr.values())
    cols = ['#b5523b']*len(chk)+['#1f5fbf']*len(lit_el)
    ax.bar(range(len(xs)), vs, color=cols, edgecolor='k', lw=.4)
    ax.axhline(1, color='k', lw=.7); ax.axhspan(0.8, 1.2, color='0.9', zorder=0)
    ax.set_xticks(range(len(xs))); ax.set_xticklabels(xs, rotation=90, fontsize=7.5); ax.set_ylim(0, 2.2)
    ax.set_ylabel('ratio'); ax.text(0.02, 0.97, 'LA / EPMA, same tektite', color='#b5523b', fontsize=7.5, transform=ax.transAxes, va='top')
    ax.text(0.02, 0.91, 'LA / Indochinite literature median', color='#1f5fbf', fontsize=7.5, transform=ax.transAxes, va='top')
    ax.set_title('(a) LA-ICP-MS accuracy check (MNG24_A3_1)', fontsize=8.5, loc='left')
    ax = axs[1]; x = np.arange(len(REE))
    litv = np.array([[pd.to_numeric(lit[el], errors='coerce').quantile(q)/CI[el] for el in REE] for q in (.1, .5, .9)])
    ax.fill_between(x, litv[0], litv[2], color='0.85', label='Indochinite literature (10–90 %)')
    ax.plot(x, litv[1], color='0.5', lw=1.2)
    for t, g in l.groupby('tektite'):
        ax.plot(x, [g[el].median()/CI[el] for el in REE], '-o', ms=3.5, color=TCOL.get(t, '#5aa0e0'), lw=1.6, label=f'{t} (LA-ICP-MS)')
    for nm in ['Khorat sandstone','Khorat mudstone','Bolaven tholeiite','Bolaven alkali basalt','Lateritic saprolite','Diamicton / "catastro-loess"','Sedimentary laterite','Metatuff','Unweathered shale (PAAS)']:
        ax.plot(x, [tr[nm][el]/CI[el] for el in REE], '--', color=SCOL[nm], lw=.9, label=LAB(nm))
    ax.set_yscale('log'); ax.set_xticks(x); ax.set_xticklabels(REE); ax.set_ylabel('sample / CI chondrite')
    ax.legend(fontsize=5.8, loc='lower left', ncol=2, frameon=False); ax.set_ylim(3, 800)
    ax.set_title('(b) Rare-earth patterns', fontsize=8.5, loc='left')
    ax = axs[2]
    th = pd.to_numeric(lit.Th, errors='coerce'); sc = pd.to_numeric(lit.Sc, errors='coerce')
    sm = pd.to_numeric(lit.Sm, errors='coerce'); eu = pd.to_numeric(lit.Eu, errors='coerce'); tb = pd.to_numeric(lit.Tb, errors='coerce')
    leu = (eu/CI['Eu'])/((sm/CI['Sm'])**(2/3)*(tb/CI['Tb'])**(1/3))
    ax.scatter(th/sc, leu, s=8, c='0.78', lw=0, label='Indochinite literature (Eu* from Sm, Tb)')
    if len(mixtr):
        ax.scatter(mixtr['Th/Sc'], mixtr['Eu/Eu*'], s=4, c='#2ca02c', alpha=.25, lw=0, label='posterior mixtures (bulk)')
    for t, g in l.groupby('tektite'):
        ax.scatter(g.Th/g.Sc, eu_star(g), s=14, c=TCOL.get(t, '#5aa0e0'), edgecolors='k', lw=.3, label=t)
    for nm in ['Khorat sandstone','Khorat mudstone','Bolaven tholeiite','Bolaven alkali basalt','Lateritic saprolite','Diamicton / "catastro-loess"','Sedimentary laterite','Metatuff','Unweathered shale (PAAS)']:
        d = tr[nm]; ax.scatter(d['Th']/d['Sc'], eu_star(d), marker='*', s=150, c=SCOL[nm], edgecolors='k', lw=.5)
    ax.axhline(1, color='k', ls=':', lw=.7); ax.set_xscale('log'); ax.set_xlim(0.05, 3); ax.set_ylim(0.4, 1.25)
    ax.set_xlabel('Th / Sc'); ax.set_ylabel('Eu / Eu*'); ax.legend(fontsize=6, loc='lower left', frameon=False)
    ax.set_title('(c) Provenance ratios (insensitive to calibration\nand dilution); stars = source lithologies', fontsize=8.5, loc='left')
    fig.suptitle('Trace elements: LA-ICP-MS data quality and provenance (two tektites, MNG24_A3_1 and _A3_2)', fontsize=10.5, fontweight='bold', y=1.03)
    fig.savefig(OUT+'Fig16_trace.png', bbox_inches='tight'); plt.close(fig)
    return chk, lr

if __name__ == '__main__':
    main = sys.argv[1] if len(sys.argv) > 1 else 'main'
    sens = {}
    for nm in ['main','no_random','no_alkali','local_only']:
        fn = os.path.join(os.path.dirname(os.path.abspath(__file__)), f'res_{nm if nm != "main" else main}.pkl')
        try: res = pickle.load(open(fn, 'rb'))
        except FileNotFoundError: continue
        S = summarise(res); S['res'] = res; sens[nm] = S
    S = sens['main']; tr = source_traces(); mixtr = mixture_traces(S, tr)
    fig15(S, sens); chk, lr = fig16(S, mixtr)
    rep = {k: dict(good=v['good'], chain_ll={int(a): round(b, 1) for a, b in v['chain_ll'].items()},
                   K={int(a): round(b, 3) for a, b in v['K'].items()},
                   summ={n: {kk: round(vv, 3) for kk, vv in d.items()} for n, d in v['summ'].items()},
                   resid_median={o: round(float(np.median(v['resid'][i])), 1) for i, o in enumerate(v['oxides'])},
                   resid_iqr={o: [round(float(np.percentile(v['resid'][i], 25)), 1), round(float(np.percentile(v['resid'][i], 75)), 1)] for i, o in enumerate(v['oxides'])},
                   comp={n: [round(float(x), 2) for x in c] for n, c in v['comp'].items()},
                   bulk_misfit={o: round(float((v['pred_mean'][i]-v['obs_mean'][i])/v['obs_mean'][i]*100), 1) for i, o in enumerate(v['oxides'])})
           for k, v in sens.items()}
    rep['mix_traces'] = {c: [round(float(mixtr[c].quantile(q)), 3) for q in (.05, .5, .95)] for c in ['Th/Sc', 'Eu/Eu*', 'basalt', 'La', 'Th', 'Sc', 'Zr', 'Co', 'Ni', 'Cr']} if len(mixtr) else {}
    rep['LA_vs_EPMA'] = {k: round(v, 3) for k, v in chk.items()}; rep['LA_vs_lit'] = {k: round(float(v), 3) for k, v in lr.items()}
    json.dump(rep, open(OUT+'summary.json', 'w'), indent=1)
    print(json.dumps({k: rep[k] for k in rep if k not in ('LA_vs_lit',)}, indent=1)[:6000])
