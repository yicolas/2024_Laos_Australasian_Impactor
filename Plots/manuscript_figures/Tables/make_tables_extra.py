"""Data for Table 3 (conglomerate tests), Table 4 (rj-MCMC weights), Tables S2 (rock-mag pairs), S3 (paleomag inventory), S4 (tektites).
Usage: python make_tables_extra.py <pmagpy_fits> <summary.json> <VSM csv> <outdir>"""
import sys, os, json, numpy as np, pandas as pd
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'Fig8'))
sys.path.insert(0, '/home/claude/fig8')
from pmag_sites import load, fisher, resultant, watson_ro, NAME
P, SUMM, VSM, OUT = sys.argv[1:5]
s = load(P); ht = s[s.slot == 'HT']
allsp = pd.read_csv(os.path.join(P, 'specimens.txt'), sep='\t', skiprows=1); allsp = allsp[allsp.dir_tilt_correction == 0]
allsp['site'] = allsp.specimen.str[:4]
LP = {'NWFB': 2.38, 'NWFC': 3.26, 'PKQA': 2.25, 'PKSF': 6.09, 'PKSG': 6.58, 'PKSH': 2.50}   # mcfadden_gc_check.py
MAT = {'NWFB': 'Blocks (3)', 'NWFC': 'Boulders (8)', 'PKQA': 'Field boulders (3; 10 cores)', 'PKSF': 'Boulders (11)', 'PKSG': 'Boulders (8)', 'PKSH': 'Cores HA1, HA2, HB1'}
t3 = []
for st in ['NWFB', 'NWFC', 'PKQA', 'PKSF', 'PKSG', 'PKSH']:
    g = ht[ht.site == st]; bm = [fisher(x.dir_dec, x.dir_inc) for _, x in g.groupby('boulder')]
    R = resultant([b['dec'] for b in bm], [b['inc'] for b in bm]); r95, r99 = watson_ro(len(bm))
    gm = fisher([b['dec'] for b in bm], [b['inc'] for b in bm])
    t3.append(dict(site=NAME[st], mat=MAT[st], N=len(bm), nspec=len(g), R=R, r95=r95, r99=r99, dec=gm['dec'], inc=gm['inc'], k=gm['k'], a95=gm['a95'],
                   lp=LP[st], verdict='Random' if (R < r95 and LP[st] < r95) else 'Clustered'))
S = json.load(open(SUMM)); t4 = {k: S[k]['summ'] for k in ['main', 'no_random', 'no_alkali', 'local_only']}
t4n = {k: len(S[k]['good']) for k in t4}
v = pd.read_csv(VSM, encoding='utf-8-sig').dropna(subset=['Mr/Ms'])
PAIRS = [('PKS-B', 'In-situ flow', 'PKS24-BA-P1', 'bottom 1', 'top'), ('PKS-H (HB)', 'In-situ flow', 'PKS24-HB-P1', 'top', 'bottom'),
         ('PKS-I', 'Corestone', 'PKS24-I-P1', 'bottom', 'top'), ('NWF-C', 'Diamicton clast', 'NWF24-C-P8', 'bottom', 'top 1'),
         ('PKQ-A (2A)', 'Diamicton clast', 'PKQ24-A-P2A', 'bottom', 'top'), ('PKQ-A (5A)', 'Diamicton clast', 'PKQ24-A-P5A', 'bottom', 'top'),
         ('PKQ-A (5C)', 'Diamicton clast', 'PKQ24-A-P5C', 'bottom', 'top')]
ts2 = []
for lab, kind, smp, f, w in PAIRS:
    for state, sel in [('fresh', f), ('weathered', w)]:
        r = v[(v['Sample #'] == smp) & (v['Weathered t/b'] == sel)].iloc[0]
        ts2.append(dict(site=lab, kind=kind, sample=smp.replace('PKQ24-I', 'PKS24-I'), state=state, mass=r['Mass (g)'], Hc=r['Hc(mT)'], Hcr=r['Hcr(mT)'],
                        Mr=r['Mr(µAm^2)'], Ms=r['Ms(µAm^2)'], MrMs=r['Mr/Ms'], HcrHc=r['Hcr/Hc']))
GPS = json.load(open('tables_data.json'))['gps']
INV = {  # sample type, orientation (SAM headers), setting
 'NWFA': ('Block', 'Sun', 'In-situ flow'), 'NWFB': ('Block', 'Magnetic (IGRF-corr.)', 'Blocks (transported)'),
 'NWFC': ('Block', 'Sun', 'Diamicton boulders'), 'PKQA': ('Core', 'Sun (cores 0, 3 magnetic)', 'Diamicton boulders'),
 'PKSB': ('Block', 'Sun', 'In-situ flow'), 'PKSF': ('Core', 'Sun', 'Diamicton boulders'), 'PKSG': ('Block', 'Magnetic (IGRF-corr.)', 'Diamicton boulders'),
 'PKSH': ('Core', 'Sun', 'Two horizons (HA, HB)'), 'PKSI': ('Core', 'Sun', 'Corestone'), 'PKSJ': ('Core', 'Magnetic (IGRF-corr.)', 'In-situ flow'),
 'PKSK': ('Core', 'Magnetic (IGRF-corr.)', 'In-situ flow'), 'WBEA': ('Block', 'Magnetic (IGRF-corr.)', 'Basal flow')}
ts3 = []
for st in ['NWFA', 'NWFB', 'NWFC', 'PKQA', 'PKSB', 'PKSF', 'PKSG', 'PKSH', 'PKSI', 'PKSJ', 'PKSK', 'WBEA']:
    a = allsp[(allsp.site == st) & (allsp.dir_comp == 'mt')]
    ts3.append(dict(site=NAME[st], lat=GPS[st][0], lon=GPS[st][1], setting=INV[st][2], stype=INV[st][0], orient=INV[st][1],
                    nsamp=a.specimen.str[:-1].nunique(), nspec=a.specimen.nunique(), nacc=int((a.dir_mad_free <= 15).sum()),
                    nfits=int((allsp.site == st).sum())))
sys.path.insert(0, '/home/claude/geochem2/code'); os.chdir('/home/claude/geochem2/code')
from load import epma
e = epma(all_spots=True); ts4 = []
LOC = {'KK24_T1': 'Khon Kaen, NE Thailand', 'MG24_B1': 'Muong Nong area, Savannakhet, Laos'}
for t, g in e.groupby('tektite'):
    ts4.append(dict(tek=t, loc=LOC.get(t, 'Muong Nong area, Savannakhet, Laos'), n=len(g), nacc=int((g.total >= 97).sum()), tmin=g.total.min(), tmax=g.total.max(),
                    la='yes (5 sites × 5)' if t in ('MNG24_A3_1', 'MNG24_A3_2') else '—'))
os.chdir(OUT)
json.dump(dict(t3=t3, t4=t4, t4n=t4n, ts2=ts2, ts3=ts3, ts4=ts4), open('extra_data.json', 'w'), indent=1, default=float)
print(pd.DataFrame(t3).round(2).to_string()); print(pd.DataFrame(ts3).to_string()); print(pd.DataFrame(ts4).round(2).to_string())
