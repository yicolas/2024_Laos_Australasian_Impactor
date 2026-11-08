"""Figure 4 — rock magnetism of Bolaven basalts (consolidates LEAD_3 Figs 4–7).
(a,b) hysteresis loops, fresh interior vs weathered rind; (c) Day plot of 7 fresh→weathered pairs;
(d) low-temperature MPMS of NWF-C; (e–j) FORC diagrams, fresh (top row) vs weathered (bottom row).
Usage: python make_fig4.py <repo_root> <outdir>"""
import sys, os, numpy as np, pandas as pd
import matplotlib as mpl, matplotlib.pyplot as plt
from matplotlib.colors import LinearSegmentedColormap, TwoSlopeNorm
from rockmag_io import read_hys, read_frc, forc_distribution, read_rso

R = sys.argv[1]; OUT = sys.argv[2]; os.makedirs(OUT, exist_ok=True)
VSM = os.path.join(R, 'VSM data'); LB = os.path.join(VSM, 'LaosBasalts'); MP = os.path.join(R, 'MPMS(Nick)')
mpl.rcParams.update({'font.family': 'DejaVu Sans', 'font.size': 6.5, 'axes.linewidth': 0.6, 'xtick.major.width': 0.5,
                     'ytick.major.width': 0.5, 'xtick.major.size': 2.5, 'ytick.major.size': 2.5, 'svg.fonttype': 'none',
                     'pdf.fonttype': 42, 'axes.labelpad': 2})
FRESH, WEATH = '#1f5fa8', '#c8372d'

fig = plt.figure(figsize=(7.09, 7.95))
L, Rt = 0.065, 0.905                       # common left / right edges
def letter(ax, s, dx=-0.0, dy=0.0):
    ax.text(-0.02 + dx, 1.02 + dy, s, transform=ax.transAxes, fontsize=9, fontweight='bold', ha='right', va='bottom')

# ---------------- row 1 ----------------
gs1 = fig.add_gridspec(1, 4, left=L, right=0.995, top=0.9686, bottom=0.7801, wspace=0.42, width_ratios=[1, 1, 1.05, 1.05])

def loop(path):
    """High-field (|B| > 700 mT) para/diamagnetic slope removed (fit separately on each side), normalised by Ms."""
    H, M, p = read_hys(path)
    pos, neg = H > 700, H < -700
    k = 0.5 * (np.polyfit(H[pos], M[pos], 1)[0] + np.polyfit(H[neg], M[neg], 1)[0])
    Mc = M - k * H
    Ms = 0.5 * (Mc[pos].mean() - Mc[neg].mean())
    return H, Mc / Ms
for i, (title, fr, we) in enumerate([('NWF-C clast', 'NWF24-C-P8 bottom.hys', 'NWF24-C-P8 weathered top.hys'),
                                     ('PKS-B flow (1155 ka)', 'PKS24-BA-P1 bottom.hys', 'PKS24-BA-P1 top small chip.hys')]):
    ax = fig.add_subplot(gs1[0, i])
    for f, c, lab in [(fr, FRESH, 'fresh interior'), (we, WEATH, 'weathered rind')]:
        H, m = loop(os.path.join(LB, f)); ax.plot(H, m, color=c, lw=0.8, label=lab)
    ax.axhline(0, color='0.6', lw=0.4); ax.axvline(0, color='0.6', lw=0.4)
    ax.set_xlim(-400, 400); ax.set_ylim(-1.1, 1.1); ax.set_xticks([-400, -200, 0, 200, 400])
    ax.set_xlabel('B (mT)'); ax.set_ylabel('M / Ms' if i == 0 else '')
    if i: ax.set_yticklabels([])
    ax.set_title(title, fontsize=6.3, pad=3)
    if i == 0: ax.legend(loc='lower right', fontsize=5.6, frameon=False, handlelength=1.4, borderaxespad=0.2)
    letter(ax, 'ab'[i])

# Day plot
ax = fig.add_subplot(gs1[0, 2])
d = pd.read_csv(os.path.join(VSM, 'Volcanics_VSM_Data.csv'), encoding='utf-8-sig').dropna(subset=['Mr/Ms'])
PAIRS = [  # label, sample, fresh row selector, weathered row selector, marker, color
    ('PKS-B (flow)', 'PKS24-BA-P1', 'bottom 1', 'top', 'o', '#6a3d9a'),
    ('PKS-H (flow)', 'PKS24-HB-P1', 'top', 'bottom', 'o', '#1b9e77'),
    ('PKS-I (corestone)', 'PKS24-I-P1', 'bottom', 'top', 'D', '#e7298a'),
    ('NWF-C (clast)', 'NWF24-C-P8', 'bottom', 'top 1', '^', '#1f78b4'),
    ('PKQ-A 2A (clast)', 'PKQ24-A-P2A', 'bottom', 'top', '^', '#ff7f00'),
    ('PKQ-A 5A (clast)', 'PKQ24-A-P5A', 'bottom', 'top', '^', '#b15928'),
    ('PKQ-A 5C (clast)', 'PKQ24-A-P5C', 'bottom', 'top', '^', '#e31a1c')]
ax.axhspan(0.5, 0.6, color='0.93', lw=0); ax.axhline(0.5, color='0.4', lw=0.5, ls='--'); ax.axhline(0.05, color='0.4', lw=0.5, ls='--')
ax.axvline(1.5, color='0.4', lw=0.5, ls=':'); ax.axvline(4.0, color='0.4', lw=0.5, ls=':')
fr_all, we_all = [], []
for lab, smp, fsel, wsel, mk, col in PAIRS:
    f = d[(d['Sample #'] == smp) & (d['Weathered t/b'] == fsel)].iloc[0]; w = d[(d['Sample #'] == smp) & (d['Weathered t/b'] == wsel)].iloc[0]
    fr_all.append(f['Mr/Ms']); we_all.append(w['Mr/Ms'])
    ax.annotate('', xy=(w['Hcr/Hc'], w['Mr/Ms']), xytext=(f['Hcr/Hc'], f['Mr/Ms']), arrowprops=dict(arrowstyle='-|>', color=col, lw=0.7, mutation_scale=6, shrinkA=3, shrinkB=3))
    ax.scatter(f['Hcr/Hc'], f['Mr/Ms'], marker=mk, s=18, color=col, edgecolor='k', lw=0.3, zorder=4, label=lab)
    ax.scatter(w['Hcr/Hc'], w['Mr/Ms'], marker=mk, s=18, facecolor='white', edgecolor=col, lw=0.8, zorder=4)
ax.set_xlim(1.2, 4.3); ax.set_ylim(0.1, 0.55); ax.set_xticks([1.5, 2, 3, 4]); ax.set_xlabel('Hcr / Hc'); ax.set_ylabel('Mr / Ms')
ax.text(1.24, 0.525, 'SD', fontsize=5.8, color='0.35', va='center'); ax.text(1.6, 0.47, 'PSD', fontsize=6.5, color='0.35')
ax.text(4.27, 0.405, 'MD →\n(Mr/Ms < 0.05)', fontsize=4.8, color='0.35', ha='right', va='top')
ax.legend(loc='lower right', fontsize=4.9, frameon=False, handletextpad=0.2, borderaxespad=0.1, labelspacing=0.3, scatterpoints=1, bbox_to_anchor=(1.02, 0.0))
ax.text(4.27, 0.475, 'filled = fresh\nopen = weathered', fontsize=4.9, ha='right', va='top', color='0.25')
letter(ax, 'c')
print('mean Mr/Ms fresh %.3f weathered %.3f' % (np.mean(fr_all), np.mean(we_all)))

# MPMS
ax = fig.add_subplot(gs1[0, 3])
z = read_rso(os.path.join(MP, 'NWF24-C-P8_ZFCFC0.rso.dat')).dropna(subset=['m'])
brk = np.where(np.diff(z['T'].values) < -50)[0]
zfc, fc = (z.iloc[:brk[0] + 1], z.iloc[brk[0] + 1:]) if len(brk) else (z, None)
s = read_rso(os.path.join(MP, 'NWF24-C-P8_SIRMcycle.rso.dat')).dropna(subset=['m'])
imin = s['T'].values.argmin(); cool, warm = s.iloc[:imin + 1], s.iloc[imin:]
ax.axvspan(110, 125, color='#f2d16b', alpha=0.35, lw=0)
ax.text(117.5, 1.245, 'Verwey (~120 K)', fontsize=5.2, ha='center', va='top', color='#8a6d00')
nz = max(zfc['m'].max(), fc['m'].max() if fc is not None else 0)
ax.plot(zfc['T'], zfc['m'] / nz, '-', color='#1f5fa8', lw=0.9, label='ZFC LT-SIRM')
if fc is not None: ax.plot(fc['T'], fc['m'] / nz, '--', color='#1f5fa8', lw=0.9, label='FC LT-SIRM')
ns = s['m'].max()
ax.plot(cool['T'], cool['m'] / ns, '-', color='#d95f02', lw=0.9, label='RT-SIRM cooling')
ax.plot(warm['T'], warm['m'] / ns, '--', color='#d95f02', lw=0.9, label='RT-SIRM warming')
ax.set_xlim(0, 300); ax.set_ylim(0, 1.25); ax.set_xlabel('T (K)'); ax.set_ylabel('M / M$_{max}$')
ax.legend(loc='lower left', fontsize=5.0, frameon=False, handlelength=1.6, borderaxespad=0.1, labelspacing=0.25)
ax.set_title('NWF-C, low temperature', fontsize=6.3, pad=3)
letter(ax, 'd')

# ---------------- FORC grid ----------------
cmap = LinearSegmentedColormap.from_list('forc', [(0, '#2b59a8'), (0.12, '#9ec3e6'), (0.16, '#ffffff'), (0.2, '#ffffff'), (0.3, '#fde3b8'), (0.5, '#f5a54a'), (0.7, '#d4661c'), (0.88, '#8c2d04'), (1, '#3d1300')])
gs2 = fig.add_gridspec(2, 3, left=L, right=Rt, top=0.7033, bottom=0.3542, wspace=0.12, hspace=0.12)
FORC = [  # column title, fresh file, weathered file, SF per file
    ('PKS-H (in situ flow)', ('PKQ24-HB-P1 top unweathered.frc', 5), ('PKS24-HB-P1 bottom weathered.frc', 5)),
    ('PKS-I (corestone)', ('PKQ24-I-P1 bottom.frc', 5), ('PKQ24-I-P1 top FORC.frc', 5)),
    ('PKS-B (in situ flow) / NWF-C (clast)', ('PKS24-BA-P1 bottom for FORC.frc', 10), ('NWF24-C-P8 weathered top for FORC.frc', 5))]
levels = np.linspace(-0.2, 1.0, 25); norm = mpl.colors.Normalize(vmin=-0.2, vmax=1.0)
peaks = {}
for j, (title, fr, we) in enumerate(FORC):
    for i, (fname, SF) in enumerate([fr, we]):
        ax = fig.add_subplot(gs2[i, j])
        Bc, Bu, rho, dH = forc_distribution(read_frc(os.path.join(LB, fname)), SF=SF)
        cs = ax.contourf(Bc, Bu, rho, levels=levels, cmap=cmap, norm=norm, extend='both')
        ax.contour(Bc, Bu, rho, levels=[0.2, 0.4, 0.6, 0.8], colors='k', linewidths=0.25, alpha=0.5)
        ax.axhline(0, color='k', lw=0.3, ls=':')
        k = np.nanargmax(rho); peaks[fname] = (Bc.ravel()[k], Bu.ravel()[k])
        pk = Bc.ravel()[k]; lim = np.nanmin(np.where(np.isnan(rho), np.nan, Bc))
        ax.text(0.97, 0.94, (f'peak Bc ≈ {pk:.0f} mT' if pk > lim + 1 else f'peak Bc ≤ {lim:.0f} mT'), transform=ax.transAxes, ha='right', va='top', fontsize=5.4)
        sub = 'PKS-B, fresh interior' if (j == 2 and i == 0) else ('NWF-C, weathered rind' if (j == 2 and i == 1) else None)
        if sub: ax.text(0.97, 0.06, sub, transform=ax.transAxes, ha='right', va='bottom', fontsize=5.4, color='0.2')
        ax.set_xlim(0, 60); ax.set_ylim(-25, 25); ax.set_xticks([0, 20, 40, 60]); ax.set_yticks([-20, 0, 20])
        if i == 1: ax.set_xlabel('B$_c$ (mT)')
        else: ax.set_xticklabels([])
        if j == 0: ax.set_ylabel(('Fresh interior\n' if i == 0 else 'Weathered rind\n') + 'B$_u$ (mT)')
        else: ax.set_yticklabels([])
        if i == 0: ax.set_title(title.split(' / ')[0] if j < 2 else 'PKS-B flow / NWF-C clast', fontsize=6.3, pad=3)
        letter(ax, 'efghij'[j * 2 + i] if False else 'efghij'[i * 3 + j])
cax = fig.add_axes([Rt + 0.015, 0.3542, 0.012, 0.3491])
cb = fig.colorbar(cs, cax=cax, ticks=[-0.2, 0, 0.2, 0.4, 0.6, 0.8, 1.0]); cb.set_label('ρ (normalised)', fontsize=6); cb.ax.tick_params(labelsize=5.5)
print({k: tuple(round(v, 1) for v in p) for k, p in peaks.items()})

# ---------------- row 3: SEM/EDS of fresh basalt LS-H18 ----------------
from PIL import Image
EDS_OX = ['FeO', 'TiO2', 'Cr2O3', 'V2O5', 'MnO', 'MgO', 'Al2O3', 'SiO2', 'CaO', 'Na2O', 'K2O']
# LS-H18 Area 1, Oxford Instruments EDS, wt% normalised to 100 (LEAD_3 Table 2 / LEAD_4 Table 3);
# spot labels matched to analyses by acquisition order in the instrument report
EDS = [  # n, BSE label, phase, oxides (FeO TiO2 Cr2O3 V2O5 MnO MgO Al2O3 SiO2 CaO Na2O K2O)
    (1, 'Oxide_1', 'Titanomagnetite', [73.80, 21.74, 0, 0.89, 0.82, 1.15, 1.18, 0.42, 0, 0, 0]),
    (4, 'Oxide_2', 'Cr-titanomagnetite', [62.55, 16.03, 10.83, 1.16, 0.61, 2.72, 3.80, 2.30, 0, 0, 0]),
    (5, 'Oxide_3', 'Titanomagnetite', [68.48, 22.41, 1.07, 0.91, 0.60, 1.68, 2.56, 2.02, 0.26, 0, 0]),
    (10, 'Oxide_5', 'Titanomagnetite', [65.33, 20.15, 0, 0.73, 0, 2.28, 3.37, 7.00, 0.39, 0.28, 0.48]),
    (8, 'Oxide_4', 'Fe–Mn oxide (secondary)', [80.66, 0, 0, 0, 4.05, 9.31, 0, 3.02, 2.97, 0, 0]),
    (3, 'Pyx_1', 'Olivine (Fo53)', [40.26, 0, 0, 0, 0, 25.30, 0.77, 32.99, 0.68, 0, 0]),
    (7, 'Pyx_2', 'Olivine (Fo78)', [19.37, 0, 0, 0, 0, 38.88, 1.32, 39.73, 0.70, 0, 0]),
    (9, 'Ukn_1', 'Augite', [14.92, 2.37, 0, 0, 0, 9.55, 3.87, 49.93, 19.11, 0, 0.26]),
    (2, 'Plag_1', 'Plagioclase (An59)', [1.07, 0, 0, 0, 0, 0.45, 29.13, 53.60, 11.27, 4.14, 0.34]),
    (6, 'Plag_2', 'Plagioclase (An62)', [0.90, 0, 0, 0, 0, 0, 29.22, 52.53, 12.95, 4.12, 0.28])]
OXCOL = {'FeO': '#7f0000', 'TiO2': '#e6550d', 'Cr2O3': '#31a354', 'V2O5': '#756bb1', 'MnO': '#636363', 'MgO': '#9ecae1',
         'Al2O3': '#c6dbef', 'SiO2': '#e0e0e0', 'CaO': '#fdd0a2', 'Na2O': '#fff2ae', 'K2O': '#bcbddc'}
gs3 = fig.add_gridspec(1, 2, left=L, right=0.995, top=0.268, bottom=0.04, wspace=0.10, width_ratios=[0.92, 1])
ax = fig.add_subplot(gs3[0, 0])
img = Image.open(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'LS-H18_Area1_BSE.png')).convert('L').crop((99, 10, 1862, 1223))
ax.imshow(img, cmap='gray', interpolation='none'); ax.set_xticks([]); ax.set_yticks([])
# ring the Fe-Ti oxide spots (positions of the instrument '+' markers, crop pixel coords)
SPOTS = {'Oxide_1': (707, 442), 'Oxide_2': (795, 672), 'Oxide_3': (523, 826), 'Oxide_5': (321, 298), 'Oxide_4': (1333, 148)}
for k, (x, y) in SPOTS.items():
    ax.add_patch(plt.Circle((x, y), 34, fill=False, ec='#ff7f0e' if k != 'Oxide_4' else '#9ecae1', lw=1.0))
px500 = 462.5; x0b, y0b = 60, img.size[1] - 55
ax.add_patch(plt.Rectangle((x0b - 15, y0b - 60), px500 + 30, 95, fc='black', alpha=0.55, lw=0))
ax.plot([x0b, x0b + px500], [y0b, y0b], color='white', lw=2)
ax.text(x0b + px500 / 2, y0b - 12, '500 µm', color='white', ha='center', va='bottom', fontsize=6)
ax.text(0.99, 0.02, 'BSE, fresh basalt LS-H18', transform=ax.transAxes, color='white', ha='right', va='bottom', fontsize=5.8)
t_ = ax.text(0.99, 0.09, 'titanomagnetite spots', transform=ax.transAxes, color='white', ha='right', va='bottom', fontsize=5.6)
ax.scatter([0.640], [0.112], s=22, transform=ax.transAxes, facecolor='none', edgecolor='#ff7f0e', lw=1.0, clip_on=False)
letter(ax, 'k')
ax = fig.add_subplot(gs3[0, 1])
ylab = []
for i, (n, lab, phase, v) in enumerate(EDS):
    left = 0
    for ox, val in zip(EDS_OX, v):
        if val > 0:
            ax.barh(i, val, left=left, color=OXCOL[ox], edgecolor='white', lw=0.3, height=0.78)
            left += val
    ylab.append(f'{phase} ({lab.replace("_", " ")})')
ax.set_yticks(range(len(EDS))); ax.set_yticklabels(ylab, fontsize=5.4); ax.invert_yaxis()
ax.set_xlim(0, 100); ax.set_xlabel('Oxide (wt%, EDS, normalised)')
ax.axhspan(-0.5, 3.5, color='#ffe8cc', zorder=-1, lw=0)
from matplotlib.patches import Patch
ax.legend(handles=[Patch(color=OXCOL[o], label=o.replace('2', '$_2$').replace('3', '$_3$').replace('5', '$_5$')) for o in EDS_OX],
          loc='upper center', bbox_to_anchor=(0.5, 1.13), ncol=11, fontsize=4.8, frameon=False, handlelength=0.9,
          handletextpad=0.25, columnspacing=0.55)
ax.yaxis.tick_right(); ax.tick_params(axis='y', length=0)
letter(ax, 'l')

for ext in ['svg', 'pdf', 'png']:
    fig.savefig(os.path.join(OUT, f'Fig4_rock_magnetism.{ext}'), dpi=400 if ext == 'png' else None, bbox_inches='tight', pad_inches=0.03)
print('done')
