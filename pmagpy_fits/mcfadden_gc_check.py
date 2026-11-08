#!/usr/bin/env python3
"""McFadden & McElhinny (1988) combined lines-and-planes double-check of the
conglomerate tests, from the canonical fitquest/pmagpy fits + measurement data.

Problem: ~10% of specimens (mostly PKSF-3/-4) never isolate a stable endpoint by
the 450-510 C ceiling (high MAD and/or high dang). Treating their arcs as great
circles instead of discarding/trusting bad lines tests whether the Watson verdicts
are robust.

Pipeline per specimen:
  1. "Good line" (mt fit with MAD<=15 and dang<=15 or dang undefined): use the
     stored geographic direction as a DE-BFL line.
  2. "Unresolved" (MAD>15 or dang>15): fit a best-fit plane (DE-BFP) to the demag
     trajectory (steps >= 433 K = 160 C) in SPECIMEN coordinates, then rotate the
     pole to geographic with a per-specimen rotation solved by Kabsch from the
     specimen's own paired component fits (lt/MT/mt recomputed in specimen frame
     vs their stored geographic directions). Rotations are accepted only if
     signed inter-component angles are preserved (<4 deg) and Kabsch residual
     < 5 deg; validated by reproducing the stored mt direction.
  3. Per boulder: pmag.dolnp (McFadden & McElhinny 1988) on lines+planes.
  4. Per site: Watson (1956) randomness test on boulder means (MC Ro, 4e5 draws).
"""
import numpy as np
import pandas as pd
from pmagpy import pmag

RNG = np.random.default_rng(42)
CONG = ['NWFB', 'NWFC', 'PKQA', 'PKSF', 'PKSG', 'PKSH']

m = pd.read_csv('measurements.txt', sep='\t', skiprows=1, low_memory=False)
m = m[m.method_codes.str.contains('LT-T-Z|LT-NO|LT-LT-Z', na=False)]
sp = pd.read_csv('specimens.txt', sep='\t', skiprows=1)
geo = sp[sp.dir_tilt_correction == 0]
mt = geo[geo.dir_comp == 'mt'].set_index('specimen')

def cart(d, i):
    return np.array(pmag.dir2cart([[d, i, 1.]]))[0]

def dirr(v):
    d = pmag.cart2dir(v)
    return d[0], d[1]

def steps(spec, tmin, tmax):
    mm = m[(m.specimen == spec) & (m.treat_temp.between(tmin, tmax))].sort_values('treat_temp')
    return mm

def spec_fit(spec, tmin, tmax, calc):
    mm = steps(spec, tmin, tmax)
    if len(mm) < (4 if calc == 'DE-BFP' else 3):
        return None
    db = [[r.treat_temp, r.dir_dec, r.dir_inc, r.magn_moment, 0, 'g'] for r in mm.itertuples()]
    try:
        f = pmag.domean(db, 0, len(db) - 1, calc)
    except Exception:
        return None
    if 'specimen_dec' not in f or f.get('specimen_mad', 99) is None:
        return None
    return f['specimen_dec'], f['specimen_inc'], f.get('specimen_mad', np.nan), len(mm)

def kabsch(U, V):
    H = U.T @ V
    S, _, Vt = np.linalg.svd(H)
    d = np.sign(np.linalg.det(Vt.T @ S.T))
    R = Vt.T @ np.diag([1, 1, d]) @ S.T
    return R

def rotation_for(spec):
    """Solve specimen->geographic rotation from this specimen's own paired fits."""
    rows = geo[geo.specimen == spec]
    pairs = []
    for _, r in rows.iterrows():
        f = spec_fit(spec, r.meas_step_min, r.meas_step_max, 'DE-BFL')
        if f and f[2] <= 12:
            pairs.append((cart(f[0], f[1]), cart(r.dir_dec, r.dir_inc)))
    if len(pairs) < 2:
        return None, 'too few pairs'
    # keep pairs whose signed mutual angles are preserved
    keep = list(range(len(pairs)))
    def angs(vecs, idx):
        return {(a, b): np.degrees(np.arccos(np.clip(np.dot(vecs[a], vecs[b]), -1, 1)))
                for a in idx for b in idx if a < b}
    while len(keep) >= 2:
        au = angs([p[0] for p in pairs], keep)
        av = angs([p[1] for p in pairs], keep)
        bad = {k: abs(au[k] - av[k]) for k in au if abs(au[k] - av[k]) > 4}
        if not bad:
            break
        # drop the index appearing most in bad pairs
        cnt = {}
        for (a, b) in bad:
            cnt[a] = cnt.get(a, 0) + 1
            cnt[b] = cnt.get(b, 0) + 1
        keep.remove(max(cnt, key=cnt.get))
    if len(keep) < 2:
        return None, 'angles not preserved'
    U = np.array([pairs[k][0] for k in keep])
    V = np.array([pairs[k][1] for k in keep])
    R = kabsch(U, V)
    resid = np.degrees(np.arccos(np.clip((U @ R.T * V).sum(1), -1, 1))).max()
    if resid > 5:
        return None, f'kabsch residual {resid:.1f}'
    return R, f'{len(keep)} pairs, resid {resid:.1f} deg'

def plane_pole_geo(spec):
    """Great-circle pole in geographic coords for an unresolved specimen."""
    R, info = rotation_for(spec)
    if R is None:
        return None, info
    row = mt.loc[spec]
    tmin = min(433, row.meas_step_min)
    f = spec_fit(spec, tmin, 790, 'DE-BFP')
    if f is None:
        return None, 'plane fit failed'
    if f[2] > 15:
        return None, f'plane MAD {f[2]:.1f} > 15'
    pole_s = cart(f[0], f[1])
    pole_g = R @ pole_s
    d, i = dirr(pole_g)
    return (d, i, f[2], f[3]), info

def validate_rotation(spec):
    """Rotate my own specimen-frame mt fit; compare to stored geographic mt."""
    R, info = rotation_for(spec)
    if R is None:
        return None
    row = mt.loc[spec]
    f = spec_fit(spec, row.meas_step_min, row.meas_step_max, 'DE-BFL')
    if not f:
        return None
    v = R @ cart(f[0], f[1])
    tgt = cart(row.dir_dec, row.dir_inc)
    return np.degrees(np.arccos(np.clip(np.dot(v, tgt), -1, 1)))

# ---------------- classify specimens ----------------
recs = {}   # site -> unit -> list of dicts for dolnp
notes = []
val_errs = []
for spec, row in mt.iterrows():
    site = row.site
    if site not in CONG:
        continue
    unit = spec[:len(spec) - 1] if not spec.endswith('.') else spec
    unit = pd.Series([spec]).str.replace(r'[A-Z]+$', '', regex=True)[0]
    good = (row.dir_mad_free <= 15) and (pd.isna(row.dir_dang) or row.dir_dang <= 15)
    if good:
        rec = {'dir_dec': row.dir_dec, 'dir_inc': row.dir_inc,
               'method_codes': 'DE-BFL', 'specimen': spec}
    else:
        pol, info = plane_pole_geo(spec)
        if pol is None:
            notes.append(f'{spec}: EXCLUDED ({info})')
            continue
        ve = validate_rotation(spec)
        if ve is not None:
            val_errs.append(ve)
        rec = {'dir_dec': pol[0], 'dir_inc': pol[1],
               'method_codes': 'DE-BFP', 'specimen': spec}
        notes.append(f'{spec}: plane (MAD {pol[2]:.1f}, {pol[3]} steps; rot {info}; mt-reproduction {"%.1f deg" % ve if ve is not None else "n/a"})')
    recs.setdefault(site, {}).setdefault(unit, []).append(rec)

# validation stats on a sample of good-line specimens too
import random
random.seed(1)
sample_goods = [s for s in mt.index if mt.loc[s, 'site'] in CONG][::12]
good_val = [validate_rotation(s) for s in sample_goods]
good_val = [v for v in good_val if v is not None]

# ---------------- boulder means via dolnp ----------------
def boulder_mean(rlist):
    lines = [r for r in rlist if r['method_codes'] == 'DE-BFL']
    planes = [r for r in rlist if r['method_codes'] == 'DE-BFP']
    if len(planes) == 0:
        fm = pmag.fisher_mean([[r['dir_dec'], r['dir_inc']] for r in lines])
        return fm['dec'], fm['inc'], len(lines), 0
    if len(lines) + len(planes) < 2:
        return None
    fp = pmag.dolnp(rlist, 'DE-BFP')
    return float(fp['dec']), float(fp['inc']), len(lines), len(planes)

def ro_mc(n, sims=400000):
    x = RNG.normal(size=(sims, n, 3))
    x /= np.linalg.norm(x, axis=2, keepdims=True)
    Rr = np.linalg.norm(x.sum(axis=1), axis=1)
    return np.quantile(Rr, 0.95), np.quantile(Rr, 0.99)

def watson(bdf):
    X = np.array(pmag.dir2cart([[d, i, 1.] for d, i in zip(bdf.dec, bdf.inc)]))
    R = np.linalg.norm(X.sum(axis=0))
    n = len(bdf)
    ro95, ro99 = ro_mc(n)
    return R, ro95, ro99, ('RANDOM (pass)' if R < ro95 else 'CLUSTERED (fail)')

print('=' * 70)
print('SPECIMEN NOTES (planes and exclusions)')
for n_ in notes:
    print(' ', n_)
print(f'\nrotation validation on good-line specimens (n={len(good_val)}): '
      f'median {np.median(good_val):.1f} deg, max {np.max(good_val):.1f} deg'
      if good_val else 'no validation sample')

print('\n' + '=' * 70)
all_bd = {}
for site in CONG:
    rows = []
    for unit, rl in sorted(recs[site].items()):
        bm = boulder_mean(rl)
        if bm is None:
            continue
        rows.append(dict(unit=unit, dec=bm[0], inc=bm[1], n_lines=bm[2], n_planes=bm[3]))
    bdf = pd.DataFrame(rows)
    all_bd[site] = bdf
    R, ro95, ro99, verdict = watson(bdf)
    print(f'\n{site}: {len(bdf)} boulders  R={R:.2f}  Ro95={ro95:.2f}  Ro99={ro99:.2f}  -> {verdict}')
    print(bdf.round(1).to_string(index=False))

# PKSF 10-boulder variant
pf = all_bd['PKSF'].copy()
pf['u10'] = pf.unit.str.replace('PKSF-1.', 'PKSF-1', regex=False)
rows = []
for u, g in pf.groupby('u10'):
    rl = sum((recs['PKSF'][uu] for uu in pf[pf.u10 == u].unit), [])
    bm = boulder_mean(rl)
    rows.append(dict(unit=u, dec=bm[0], inc=bm[1]))
b10 = pd.DataFrame(rows)
R, ro95, ro99, verdict = watson(b10)
print(f'\nPKSF 10-boulder variant: R={R:.2f} Ro95={ro95:.2f} -> {verdict}')

# PKQA 3-field-boulder variant
qa = all_bd['PKQA'].copy()
qa['num'] = qa.unit.str.extract(r'PKQA-(\d+)').astype(int)
groups = {'B1': [0, 1, 2, 3, 4], 'B2': [5, 6], 'B3': [7, 8, 9]}
rows = []
for b, nums in groups.items():
    units = qa[qa.num.isin(nums)].unit
    rl = sum((recs['PKQA'][u] for u in units), [])
    bm = boulder_mean(rl)
    rows.append(dict(unit=b, dec=bm[0], inc=bm[1]))
b3 = pd.DataFrame(rows)
R, ro95, ro99, verdict = watson(b3)
print(f'PKQA 3-field-boulder variant: R={R:.2f} Ro95={ro95:.2f} -> {verdict}')
print(b3.round(1).to_string(index=False))

# ---- export PKS-F records for the supplementary figure (Fig S) ----
import pickle
pickle.dump(dict(recs=recs['PKSF'], bdf=all_bd['PKSF']), open('pksf_lnp.pkl', 'wb'))
