#!/usr/bin/env python3
"""Recompute all Laos site-level statistics from the canonical fitquest/pmagpy fits,
pmagpy-style: specimen -> sample (core/boulder) -> site Fisher averaging,
VGP-latitude polarity, and Watson (1956) randomness tests at boulder level
(Ro95/Ro99 by Monte Carlo, 1e6 draws, matching Watson's exact criterion).

ChRM = dir_comp 'mt' (the high-T window), geographic frame (dir_tilt_correction=0),
specimen acceptance MAD_free <= 15 deg (pmagpy default-style cutoff).
"""
import re
import numpy as np
import pandas as pd
from pmagpy import pmag

RNG = np.random.default_rng(42)
MADCUT = 15.0

sp = pd.read_csv('specimens.txt', sep='\t', skiprows=1)
chrm = sp[(sp.dir_tilt_correction == 0) & (sp.dir_comp == 'mt')].copy()
rej = chrm[chrm.dir_mad_free > MADCUT]
chrm = chrm[chrm.dir_mad_free <= MADCUT]

# core/boulder id = name prefix before the trailing specimen letter(s); keeps "PKSF-1."
chrm['unit'] = chrm.specimen.str.replace(r'[A-Z]+$', '', regex=True)

sites = pd.read_csv('sites.txt', sep='\t', skiprows=1)
coords = sites[sites.dir_tilt_correction == 0].set_index('site')[['lat', 'lon']].to_dict('index')


def fmean(decs, incs):
    data = [[d, i] for d, i in zip(decs, incs)]
    if len(data) == 1:
        return {'dec': decs.iloc[0] if hasattr(decs, 'iloc') else decs[0],
                'inc': incs.iloc[0] if hasattr(incs, 'iloc') else incs[0],
                'n': 1, 'r': 1.0, 'k': np.nan, 'alpha95': np.nan}
    return pmag.fisher_mean(data)


def ro_mc(n, sims=1_000_000):
    """Monte Carlo critical resultant lengths for Watson randomness test."""
    x = RNG.normal(size=(sims, n, 3))
    x /= np.linalg.norm(x, axis=2, keepdims=True)
    R = np.linalg.norm(x.sum(axis=1), axis=1)
    return np.quantile(R, 0.95), np.quantile(R, 0.99)


def vgp_lat(dec, inc, site):
    lat, lon = coords[site]['lat'], coords[site]['lon']
    plon, plat, dp, dm = pmag.dia_vgp(dec, inc, 1.0, lat, lon)
    return plat


# ---------- sample (core/boulder) means ----------
unit_rows = []
for (site, unit), g in chrm.groupby(['site', 'unit']):
    fm = fmean(g.dir_dec, g.dir_inc)
    unit_rows.append(dict(site=site, unit=unit, n_spec=len(g), dec=fm['dec'], inc=fm['inc'],
                          k=fm.get('k', np.nan), a95=fm.get('alpha95', np.nan)))
units = pd.DataFrame(unit_rows)
units['vgp_lat'] = [vgp_lat(r.dec, r.inc, r.site) for r in units.itertuples()]

# ---------- site means from unit means (in-situ scheme) ----------
site_rows = []
for site, g in units.groupby('site'):
    if len(g) == 1:
        u = g.iloc[0]
        gs = chrm[chrm.site == site]
        fm = fmean(gs.dir_dec, gs.dir_inc)  # specimen-level stats for single-core sites
        site_rows.append(dict(site=site, n_units=1, n_spec=int(u.n_spec), dec=u.dec, inc=u.inc,
                              k_spec=fm.get('k'), a95_spec=fm.get('alpha95'),
                              k=np.nan, a95=np.nan, vgp=vgp_lat(u.dec, u.inc, site)))
    else:
        fm = fmean(g.dec, g.inc)
        site_rows.append(dict(site=site, n_units=len(g), n_spec=int(g.n_spec.sum()),
                              dec=fm['dec'], inc=fm['inc'], k=fm.get('k'), a95=fm.get('alpha95'),
                              k_spec=np.nan, a95_spec=np.nan,
                              vgp=vgp_lat(fm['dec'], fm['inc'], site)))
site_means = pd.DataFrame(site_rows)

# ---------- Watson randomness tests on unit (boulder) means ----------
def watson(site, groups):
    """groups: DataFrame of unit means (dec, inc)."""
    X = np.array(pmag.dir2cart([[d, i, 1.0] for d, i in zip(groups.dec, groups.inc)]))
    R = np.linalg.norm(X.sum(axis=0))
    n = len(groups)
    ro95, ro99 = ro_mc(n)
    return dict(site=site, n=n, R=R, Ro95=ro95, Ro99=ro99,
                result='RANDOM (pass)' if R < ro95 else 'CLUSTERED (fail)')

cong_sites = ['NWFB', 'NWFC', 'PKQA', 'PKSF', 'PKSG', 'PKSH']
wrows = [watson(s, units[units.site == s]) for s in cong_sites]

# PKQA field regrouping into 3 boulders: test both mappings of "cores 1-4, 5-6, 7-10"
pkqa = units[units.site == 'PKQA'].copy()
pkqa['num'] = pkqa.unit.str.extract(r'PKQA-(\d+)').astype(int)
maps = {
    'A: field1-10 = blocks 0-9 (B1=0-3, B2=4-5, B3=6-9)': {tuple(range(0, 4)): 'B1', (4, 5): 'B2', tuple(range(6, 10)): 'B3'},
    'B: field1-10 = blocks 1-9&0 (B1=1-4, B2=5-6, B3=7-9+0)': {tuple(range(1, 5)): 'B1', (5, 6): 'B2', (7, 8, 9, 0): 'B3'},
}
pkqa_variants = {}
for name, mp in maps.items():
    rows = []
    for nums, b in mp.items():
        qn = chrm.unit.str.extract(r'PKQA-(\d+)')[0]
        sel = chrm[(chrm.site == 'PKQA') & (qn.notna()) & (qn.fillna('-1').astype(int).isin(nums))]
        fm = fmean(sel.dir_dec, sel.dir_inc)
        rows.append(dict(boulder=b, n_spec=len(sel), dec=fm['dec'], inc=fm['inc'],
                         k=fm.get('k'), a95=fm.get('alpha95')))
    bdf = pd.DataFrame(rows)
    w = watson('PKQA(3B)', bdf)
    pkqa_variants[name] = (bdf, w)

# PKSF 10-boulder variant: merge PKSF-1. into PKSF-1
pf = chrm[chrm.site == 'PKSF'].copy()
pf['unit10'] = pf.unit.str.replace('PKSF-1.', 'PKSF-1', regex=False)
rows = []
for u, g in pf.groupby('unit10'):
    fm = fmean(g.dir_dec, g.dir_inc)
    rows.append(dict(unit=u, dec=fm['dec'], inc=fm['inc']))
pf10 = pd.DataFrame(rows)
w_pf10 = watson('PKSF(10)', pf10)

# ---------- output ----------
pd.set_option('display.width', 220)
print("REJECTED specimens (MAD_free > %.0f):" % MADCUT)
print(rej[['specimen', 'site', 'dir_dec', 'dir_inc', 'dir_mad_free', 'dir_dang']].to_string(index=False))

print("\n================ UNIT (core/boulder) MEANS ================")
print(units.round(1).to_string(index=False))

print("\n================ SITE MEANS (specimen->sample->site) ================")
print(site_means.round(1).to_string(index=False))

print("\n================ WATSON RANDOMNESS TESTS (boulder means, MC Ro) ================")
print(pd.DataFrame(wrows).round(2).to_string(index=False))
print("\nPKSF 10-boulder variant (PKSF-1. merged into PKSF-1):")
print(pd.DataFrame([w_pf10]).round(2).to_string(index=False))
for name, (bdf, w) in pkqa_variants.items():
    print(f"\nPKQA 3-boulder regrouping, mapping {name}:")
    print(bdf.round(1).to_string(index=False))
    print(pd.DataFrame([w]).round(2).to_string(index=False))

units.to_csv('recomputed_unit_means.csv', index=False)
site_means.to_csv('recomputed_site_means.csv', index=False)
