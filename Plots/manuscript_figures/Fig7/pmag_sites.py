"""Shared site / sample / boulder statistics from the corrected pmagpy_fits MagIC tables (geographic frame).
Components (fitquest slots): lt -> LT, MT -> MT, mt -> HT (ChRM). No tilt correction (flows sub-horizontal; diamictons).
Used by Fig 6 (panel i) and Fig 8."""
import os, numpy as np, pandas as pd
import pmagpy.pmag as pmag

SLOT = {'lt': 'LT', 'LT': 'LT', 'MT': 'MT', 'mt': 'HT'}
SLOTC = {'LT': '#3a9d5d', 'MT': '#2a6f97', 'HT': '#9840D7'}
LAT, LON = 15.2, 106.2
GAD = np.degrees(np.arctan(2 * np.tan(np.radians(LAT))))
# PKQ-A: 10 cores from 3 field boulders, as in the manuscript / recompute_site_stats.py
# (B1 = cores 0-4, B2 = 5-6, B3 = 7-9; reproduces Laos_site_interpretations.md 272/74, 141/-1, 135/46).
# NB the SAM_Header README groups them differently (1,2 | 3,4 | 5,6 | 7,8,9,0) -- flagged to Nick.
PKQA_BOULDER = {'0': 'B1', '1': 'B1', '2': 'B1', '3': 'B1', '4': 'B1', '5': 'B2', '6': 'B2', '7': 'B3', '8': 'B3', '9': 'B3'}
MADCUT = 15.0     # specimen acceptance, MAD_free <= 15 deg (recompute_site_stats.py)
NAME = {'NWFA': 'NWF-A', 'NWFB': 'NWF-B', 'NWFC': 'NWF-C', 'PKQA': 'PKQ-A', 'PKSB': 'PKS-B', 'PKSF': 'PKS-F', 'PKSG': 'PKS-G',
        'PKSH': 'PKS-H', 'PKSI': 'PKS-I', 'PKSJ': 'PKS-J', 'PKSK': 'PKS-K', 'WBEA': 'WBE-A', 'PKSH-HA': 'PKS-HA', 'PKSH-HB': 'PKS-HB'}


def load(P):
    s = pd.read_csv(os.path.join(P, 'specimens.txt'), sep='\t', skiprows=1)
    s = s[(s.dir_tilt_correction == 0) & (s.dir_mad_free <= MADCUT)].copy()
    s['slot'] = s.dir_comp.map(SLOT)
    s['site'] = s.specimen.str[:4]
    s['sample'] = s.specimen.str[:-1]                       # core / block (PKSF-1. is its own core)
    s['core'] = s['sample'].str[5:]
    s['unit'] = s.site                                      # PKS-H split into its two horizons
    s.loc[s.specimen.str.match('PKSH-[12]'), 'unit'] = 'PKSH-HA'
    s.loc[s.specimen.str.match('PKSH-3'), 'unit'] = 'PKSH-HB'
    s['boulder'] = s['sample']
    q = s.site == 'PKQA'; s.loc[q, 'boulder'] = 'PKQA-' + s.loc[q, 'core'].str[0].map(PKQA_BOULDER)
    return s


def fisher(D, I):
    D, I = list(D), list(I)
    if len(D) == 0: return None
    if len(D) == 1: return dict(dec=D[0], inc=I[0], n=1, k=np.nan, a95=np.nan, r=1.0)
    f = pmag.fisher_mean([[d, i] for d, i in zip(D, I)])
    return dict(dec=f['dec'], inc=f['inc'], n=f['n'], k=f['k'], a95=f['alpha95'], r=f['r'])


def two_tier(g, by='sample'):
    """specimen -> sample (core) -> site Fisher mean; returns site mean and the sample means."""
    sm = [fisher(x.dir_dec, x.dir_inc) | {'sample': k} for k, x in g.groupby(by)]
    return fisher([m['dec'] for m in sm], [m['inc'] for m in sm]), sm


def vgp(dec, inc, a95=np.nan):
    plon, plat, dp, dm = pmag.dia_vgp(dec, inc, a95 if np.isfinite(a95) else 0, LAT, LON)
    return plat, plon, dp, dm


_RO = {}
def watson_ro(n, nsim=200000, seed=1):
    """Monte-Carlo 95 and 99 % critical R for N random unit vectors (Watson 1956)."""
    if n not in _RO:
        rng = np.random.default_rng(seed + n)
        v = rng.normal(size=(nsim, n, 3)); v /= np.linalg.norm(v, axis=2, keepdims=True)
        R = np.linalg.norm(v.sum(1), axis=1)
        _RO[n] = (np.percentile(R, 95), np.percentile(R, 99))
    return _RO[n]


def resultant(D, I):
    X = np.array([pmag.dir2cart([d, i, 1.0]) for d, i in zip(D, I)])
    return np.linalg.norm(X.sum(0))
