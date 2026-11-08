"""Supplementary Figs S2 (rock magnetism from the 2G RAPID .rmg sequences) and S3 (AF demagnetization directions).
.rmg sequence per specimen: NRM + 21 AF steps (to 94 mT) | ARM acquisition (bias 0-1 mT, 100 mT AF) | AF of ARM |
100 mT IRM + AF | IRM acquisition (5.7 mT-1 T) | AF of SIRM. Levels are in 0.1 mT (G), moments in emu (x1e-3 -> A m2).
Directions rotated specimen -> geographic with the corrected pmagpy_fits samples table (pmag.dogeo).
Usage: python make_figS_rockmag.py <RockMag dir> <pmagpy_fits> <outdir>"""
import sys, os, glob, numpy as np, pandas as pd
import matplotlib as mpl, matplotlib.pyplot as plt
from matplotlib.lines import Line2D
import pmagpy.pmag as pmag
sys.path.insert(0, '/home/claude/fig8')
from rmg import read_rmg
from ea_helpers import xy, net, gad_stars, dot
from pmag_sites import load, fisher, SLOTC
RM, P, OUT = sys.argv[1:4]; os.makedirs(OUT, exist_ok=True)
mpl.rcParams.update({'font.family': 'DejaVu Sans', 'font.size': 6.5, 'axes.linewidth': 0.6, 'xtick.major.width': 0.5,
                     'ytick.major.width': 0.5, 'xtick.major.size': 2.5, 'ytick.major.size': 2.5, 'svg.fonttype': 'none', 'pdf.fonttype': 42})
sa = pd.read_csv(os.path.join(P, 'samples.txt'), sep='\t', skiprows=1).set_index('sample')
ht = load(P); ht = ht[ht.slot == 'HT']
SITEC = {'NWFA': '#2c6fb0', 'NWFB': '#8c6d1f', 'NWFC': '#1b9e77', 'PKQA': '#e7298a', 'PKSJ': '#c8372d', 'PKSF': '#7570b3', 'PKSG': '#e6ab02', 'WBEA': '#555555'}
def letter(ax, s, t):
    ax.text(-0.02, 1.03, s, transform=ax.transAxes, fontsize=9, fontweight='bold', ha='right', va='bottom')
    ax.text(0.0, 1.03, t, transform=ax.transAxes, fontsize=6.2, ha='left', va='bottom')
def save(fig, name):
    for ext in ['svg', 'pdf', 'png']:
        fig.savefig(os.path.join(OUT, f'{name}.{ext}'), dpi=400 if ext == 'png' else None, bbox_inches='tight', pad_inches=0.03)
    plt.close(fig)
def runs(segs):
    """split into measurement runs, each starting at a 22-step NRM/AF segment"""
    idx = [i for i, s in enumerate(segs) if s[0][0] == 'NRM' and len(s) == 22]
    out = []
    for j, i in enumerate(idx):
        end = idx[j + 1] if j + 1 < len(idx) else None
        out.append([s for s in segs[i:end] if s[0][0] in ('NRM', 'AF', 'ARM', 'AFz', 'IRMz')])
    return out
EXCLUDE = {'NWF-A-2E': 'moments after the NRM step are at holder-noise level (<1e-7 emu): specimen not measured correctly'}
D = {}
for f in sorted(glob.glob(os.path.join(RM, '*', '*.rmg'))):
    name = os.path.basename(f)[:-4]; R_ = runs(read_rmg(f))
    if not R_ or name in EXCLUDE: continue
    run = R_[0]                                         # NRM from the first run (later 'NRM' rows follow lab remanences)
    rock = [x for x in R_[-1] if len(x) > 1]           # ARM/IRM sequence from the last (repeated, complete) run
    site = name[:5].replace('-', ''); smp = site + '-' + name.split('-')[-1][:-1]
    r = dict(name=name, site=site, sample=smp, nrm=np.array([[x[1] / 10, x[3], x[4], x[5] * 1e-3] for x in run[0]]))
    full = [run[0]] + rock[1:] if len(rock) >= 5 else [s for s in run if len(s) > 1]
    if len(full) >= 5:
        arm_acq, arm_af, irm100_af, irm_acq, sirm_af = full[1], full[2], full[3], full[4], full[5] if len(full) > 5 else None
        r['arm_acq'] = np.array([[x[2] * 0.1, x[5] * 1e-3] for x in arm_acq])            # bias in mT, moment
        r['arm_af'] = np.array([[x[1] / 10, x[5] * 1e-3] for x in arm_af])
        r['irm_acq'] = np.array([[x[1] / 10, x[5] * 1e-3] for x in irm_acq])
        r['sirm_af'] = np.array([[x[1] / 10, x[5] * 1e-3] for x in full[5]]) if len(full) > 5 else None
    D[name] = r
def mdf(f, m):
    m = m / m[0]; i = np.where(m <= 0.5)[0]
    if not len(i): return np.nan
    i = i[0]; return np.interp(0.5, [m[i], m[i - 1]], [f[i], f[i - 1]])
print({k: (v['site'], 'full' if 'irm_acq' in v else 'NRM only') for k, v in D.items()})

# ======================= S2: rock magnetism =======================
fig = plt.figure(figsize=(7.09, 4.9))
gs = fig.add_gridspec(2, 3, left=0.075, right=0.99, top=0.94, bottom=0.17, wspace=0.36, hspace=0.5)
full = [k for k in D if 'irm_acq' in D[k]]
ax = fig.add_subplot(gs[0, 0])
for k, r in D.items():
    a = r['nrm']; ax.plot(a[:, 0], a[:, 3] / a[0, 3], '-o', ms=1.8, lw=0.7, color=SITEC[r['site']], alpha=0.9 if k in full else 0.45)
ax.axhline(0.5, color='0.5', ls=':', lw=0.6); ax.set_xlim(0, 95); ax.set_ylim(0, 1.15)
ax.set_xlabel('AF peak field (mT)'); ax.set_ylabel('NRM / NRM$_0$'); letter(ax, 'a', 'AF demagnetization of the NRM')
ax = fig.add_subplot(gs[0, 1])
for k in full:
    a = D[k]['irm_acq']; ax.plot(a[:, 0], a[:, 1] / a[:, 1].max(), '-', lw=0.9, color=SITEC[D[k]['site']])
ax.axhline(0.9, color='0.5', ls=':', lw=0.6); ax.set_xscale('log'); ax.set_xlim(5, 1100); ax.set_ylim(0, 1.05)
ax.set_xlabel('applied field (mT)'); ax.set_ylabel('IRM / SIRM'); letter(ax, 'b', 'IRM acquisition')
ax = fig.add_subplot(gs[0, 2])
for k in full:
    a = D[k]['arm_acq']; ax.plot(a[:, 0], a[:, 1] / D[k]['irm_acq'][:, 1].max(), '-o', ms=1.6, lw=0.8, color=SITEC[D[k]['site']])
ax.set_xlabel('DC bias field (mT)'); ax.set_ylabel('ARM / SIRM'); letter(ax, 'c', 'ARM acquisition (100 mT AF)')
ax = fig.add_subplot(gs[1, 0])
for k in full:
    c = SITEC[D[k]['site']]; a = D[k]['arm_af']; ax.plot(a[:, 0], a[:, 1] / a[0, 1], '--', lw=0.8, color=c)
    if D[k]['sirm_af'] is not None: s = D[k]['sirm_af']; ax.plot(s[:, 0], s[:, 1] / s[0, 1], '-', lw=0.9, color=c)
ax.axhline(0.5, color='0.5', ls=':', lw=0.6); ax.set_xlim(0, 200); ax.set_ylim(0, 1.05)
ax.set_xlabel('AF peak field (mT)'); ax.set_ylabel('M / M$_0$'); letter(ax, 'd', 'AF demagnetization of ARM (dashed) and SIRM')
ax = fig.add_subplot(gs[1, 1]); rows = []
for j, k in enumerate(full):
    r = D[k]; m_n = mdf(r['nrm'][:, 0], r['nrm'][:, 3]); m_a = mdf(r['arm_af'][:, 0], r['arm_af'][:, 1])
    m_s = mdf(r['sirm_af'][:, 0], r['sirm_af'][:, 1]) if r['sirm_af'] is not None else np.nan
    if not np.isfinite(m_n): ax.scatter(94, j, marker='>', s=18, facecolor='k', edgecolor='k', lw=0.5, zorder=3); ax.text(100, j, '> 94', fontsize=5, va='center')
    for v, mk, fc in [(m_n, 'o', 'k'), (m_a, 's', 'white'), (m_s, 'D', '0.6')]:
        ax.scatter(v, j, marker=mk, s=16, facecolor=fc, edgecolor='k', lw=0.5, zorder=3)
    ax.plot([np.nanmin([m_n, m_a, m_s]), np.nanmax([m_n, m_a, m_s])], [j, j], color=SITEC[r['site']], lw=1.4, zorder=1)
    rows.append((k, m_n, m_a, m_s, r['arm_acq'][-1, 1] / r['irm_acq'][:, 1].max(), r['irm_acq'][:, 1].max(), r['nrm'][0, 3]))
ax.set_yticks(range(len(full))); ax.set_yticklabels(full, fontsize=5.6); ax.invert_yaxis(); ax.set_xscale('log'); ax.set_xlim(3, 300)
ax.set_xlabel('median destructive field (mT)'); letter(ax, 'e', 'MDF: NRM (●; ▶ not reached by 94 mT), ARM (□), SIRM (◆)')
ax = fig.add_subplot(gs[1, 2])
for k, mn, ma, ms, ar, sirm, nrm in rows:
    ax.scatter(ar, nrm / sirm, s=22, color=SITEC[D[k]['site']], edgecolor='k', lw=0.4, zorder=3)
    ax.annotate(k, (ar, nrm / sirm), xytext=(3, 2), textcoords='offset points', fontsize=5)
ax.set_xlabel('ARM / SIRM (finer →)'); ax.set_ylabel('NRM / SIRM'); ax.set_yscale('log')
letter(ax, 'f', 'Grain-size and NRM-efficiency proxies')
lg = fig.add_axes([0.0, 0.0, 1.0, 0.08]); lg.axis('off')
NM = {'NWFA': 'NWF-A', 'NWFB': 'NWF-B', 'NWFC': 'NWF-C', 'PKQA': 'PKQ-A (NRM only)', 'PKSJ': 'PKS-J', 'PKSF': 'PKS-F', 'PKSG': 'PKS-G', 'WBEA': 'WBE-A'}
lg.legend(handles=[Line2D([], [], color=c, lw=1.4, label=NM[s]) for s, c in SITEC.items() if any(r['site'] == s for r in D.values())], loc='center', ncol=8, fontsize=5.6, frameon=False)
save(fig, 'FigS2_rockmag_extra')
pd.DataFrame(rows, columns=['specimen', 'MDF_NRM_mT', 'MDF_ARM_mT', 'MDF_SIRM_mT', 'ARM_SIRM', 'SIRM_Am2', 'NRM_Am2']).round(4).to_csv(os.path.join(OUT, 'FigS2_rockmag_parameters.csv'), index=False)

# ======================= S3: AF directions (geographic) =======================
# Specimens measured on the sample changer in 2025-26 wander along small circles from step to step
# (rotational/holder artefact, not a demagnetization path): shown in no panel, listed in the caption.
S3_EXCL = {'NWF-B-3I', 'NWF-C-7A', 'PKS-G-8E', 'WBE-A-1J'}
names = [n for n in D if n not in S3_EXCL]
nc = 4; nr = int(np.ceil(len(names) / nc))
fig = plt.figure(figsize=(5.8, 1.62 * nr + 0.8))
cm = plt.get_cmap('viridis')
for k, nmk in enumerate(names):
    r = D[nmk]; a = r['nrm']
    cand = [i for i in sa.index if str(i).startswith(r['sample']) and str(i)[len(r['sample']):].isalpha()]
    if not cand: print('no orientation for', nmk); continue
    az, dip = sa.loc[cand[0], 'azimuth'], sa.loc[cand[0], 'dip']        # same core -> same orientation
    g = np.array([pmag.dogeo(dd, ii, az, dip) for dd, ii in zip(a[:, 1], a[:, 2])])
    ax = fig.add_axes([(0.02 + (k % nc) * 0.25), 1 - (0.38 + (k // nc + 1) * 1.62) / (1.62 * nr + 0.8), 0.21, 1.2 / (1.62 * nr + 0.8)])
    net(ax); gad_stars(ax, 12)
    x, y = xy(g[:, 0], g[:, 1]); ax.plot(x, y, color='0.75', lw=0.4, zorder=2)
    for j in range(len(g)):
        dot(ax, g[j, 0], g[j, 1], mpl.colors.to_hex(cm(a[j, 0] / 94)), s=7, lw=0.3, z=4)
    hs = ht[ht['sample'] == r['sample']]   # thermal HT fits from the same core
    if len(hs):
        m = fisher(hs.dir_dec, hs.dir_inc); dot(ax, m['dec'], m['inc'], SLOTC['HT'], s=26, marker='s', ec='k', lw=0.5, z=6)
    ax.set_title(nmk, fontsize=6, pad=1)
cax = fig.add_axes([0.05, 0.04, 0.32, 0.014]); cb = mpl.colorbar.ColorbarBase(cax, cmap=cm, norm=mpl.colors.Normalize(0, 94), orientation='horizontal')
cb.set_label('AF peak field (mT)', fontsize=5.6); cb.ax.tick_params(labelsize=5)
fig.text(0.45, 0.045, '■ thermal HT mean of the same core (Fig. 7)\n★ GAD normal / ☆ reversed\nfilled lower / open upper hemisphere',
         fontsize=5.4, va='center')
save(fig, 'FigS3_AF_directions')
print(pd.DataFrame(rows, columns=['spec', 'mdfN', 'mdfA', 'mdfS', 'ARM/SIRM', 'SIRM', 'NRM']).round(3).to_string())
