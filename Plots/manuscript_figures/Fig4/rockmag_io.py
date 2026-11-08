"""Readers + processing for MicroMag VSM (.hys, .hcr, .frc) and QD MPMS (.rso.dat) files."""
import re, numpy as np, pandas as pd

NUM = re.compile(r'^\s*[+-]?\d')

def _blocks(path):
    """Numeric data after the header, split on blank lines -> list of (n,2) arrays."""
    txt = open(path, encoding='latin-1').read().replace('\r', '')
    lines = txt.split('\n')
    # data start: first numeric line after the segment table header
    start = 0
    for i, l in enumerate(lines):
        if l.strip().startswith('Number of data') or l.strip().startswith('Number of segments'):
            start = i
    blocks, cur = [], []
    for l in lines[start + 1:]:
        if NUM.match(l) and ',' in l:
            cur.append([float(v) for v in l.split(',')[:2]])
        elif not l.strip():
            if cur: blocks.append(np.array(cur)); cur = []
    if cur: blocks.append(np.array(cur))
    return blocks, txt

def header_value(txt, key):
    m = re.search(rf'^{re.escape(key)}\s+([+-]?[\d.]+E[+-]\d+)', txt, re.M)
    return float(m.group(1)) if m else np.nan

def read_hys(path):
    """Hysteresis loop: returns field (mT), moment (Am2), dict of header params."""
    blocks, txt = _blocks(path)
    d = np.vstack([b for b in blocks if len(b) > 20])
    p = {k: header_value(txt, k) for k in ['Saturation', 'Remanence', 'Coercivity', 'Slope correction']}
    return d[:, 0] * 1e3, d[:, 1], p

def read_frc(path):
    """FORC file: returns list of (Ha, Hb[], M[]) in mT / Am2, drift-corrected by calibration points."""
    blocks, txt = _blocks(path)
    curves, cals = [], []
    for b in blocks:
        if len(b) == 1:
            cals.append(b[0, 1])
        else:
            curves.append(b)
    if len(cals) >= len(curves):
        cals = np.array(cals[:len(curves)])
        scale = cals[0] / cals
    else:
        scale = np.ones(len(curves))
    out = [(c[0, 0] * 1e3, c[:, 0] * 1e3, c[:, 1] * s) for c, s in zip(curves, scale)]
    return out

def forc_distribution(curves, SF=5, dH=None):
    """Pike et al. (1999) local quadratic fit on a regular (Ha, Hb) grid, with the
    Hb < Ha region extended by M(Ha, Ha) (Pike, 2003). Returns Bc, Bu grids (mT) and rho (normalised)."""
    Ha = np.array([c[0] for c in curves])
    if dH is None:
        dH = np.median(np.concatenate([np.diff(c[1]) for c in curves if len(c[1]) > 3]))
    hb_grid = np.arange(Ha.min(), max(c[1].max() for c in curves) + dH / 2, dH)
    ha_grid = np.arange(Ha.min(), Ha.max() + dH / 2, dH)
    M = np.full((len(ha_grid), len(hb_grid)), np.nan)
    # place each curve on the grid row nearest to its Ha
    rows = np.clip(np.round((Ha - ha_grid[0]) / dH).astype(int), 0, len(ha_grid) - 1)
    for r, (ha, hb, m) in zip(rows, curves):
        M[r] = np.interp(hb_grid, hb, m, left=np.nan, right=np.nan)
    # fill missing rows by interpolation along Ha
    for j in range(M.shape[1]):
        col = M[:, j]; ok = ~np.isnan(col)
        if ok.sum() > 2:
            M[:, j] = np.interp(ha_grid, ha_grid[ok], col[ok], left=np.nan, right=np.nan)
    # extension: Hb < Ha -> M(Ha, Ha)
    HA, HB = np.meshgrid(ha_grid, hb_grid, indexing='ij')
    M[HB < HA - 1e-9] = np.nan          # no extension: only fully measured windows are used
    # mixed derivative of a quadratic fit in a (2SF+1)^2 window: a_xy = sum(xyM)/sum(x^2y^2)
    k = np.arange(-SF, SF + 1) * dH
    K = np.outer(k, k); K /= (K ** 2).sum()
    from scipy.signal import convolve2d
    Mf = np.nan_to_num(M, nan=0.0); valid = (~np.isnan(M)).astype(float)
    a6 = convolve2d(Mf, K[::-1, ::-1], mode='same')
    full = convolve2d(valid, np.ones_like(K), mode='same') >= K.size - 0.5
    rho = -0.5 * a6; rho[~full] = np.nan
    rho[HB < HA] = np.nan
    Bc = (HB - HA) / 2; Bu = (HB + HA) / 2
    rho = rho / np.nanmax(rho)
    return Bc, Bu, rho, dH

def read_rso(path):
    """QD MPMS3 .rso.dat -> DataFrame (T K, field Oe, moment emu)."""
    txt = open(path, encoding='latin-1').read()
    i = txt.index('[Data]')
    from io import StringIO
    df = pd.read_csv(StringIO(txt[i + 7:]))
    return df.rename(columns={'Temperature (K)': 'T', 'Field (Oe)': 'H', 'Long Moment (emu)': 'm'})
