"""Tables 1 & 2 data from corrected pmagpy_fits (MAD_free <= 15), per-site GPS for VGPs. Usage: python make_tables_data.py <pmagpy_fits> <outdir>"""
import sys, os, json, numpy as np, pandas as pd, pmagpy.pmag as pmag
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'Fig8')); from pmag_sites import load, fisher, two_tier, NAME, MADCUT
P, OUT = sys.argv[1], sys.argv[2]
GPS = {'NWFA': (15.6446, 106.1427), 'NWFB': (15.6236, 105.9859), 'NWFC': (15.4148, 106.1433), 'PKQA': (15.1020, 105.8536),
       'PKSB': (15.1543, 106.1897), 'PKSF': (15.1131, 106.2282), 'PKSG': (15.1558, 106.1903), 'PKSH': (15.1557, 106.1918),
       'PKSI': (15.2328, 106.1908), 'PKSJ': (15.2431, 106.2581), 'PKSK': (15.2419, 106.2585), 'WBEA': (15.2700, 106.3472)}
GPTS = [(0, 773, 'C1n', 'N'), (773, 990, 'C1r.1r', 'R'), (990, 1071, 'C1r.1n (Jaramillo)', 'N'), (1071, 1180, 'C1r.2r', 'R'),
        (1180, 1215, 'C1r.2n (Cobb Mtn)', 'N'), (1215, 1775, 'C1r.3r', 'R')]
def chron(a):
    return next(c for t0, t1, c, p in GPTS if t0 <= a < t1), next(p for t0, t1, c, p in GPTS if t0 <= a < t1)
allspec = pd.read_csv(os.path.join(P, 'specimens.txt'), sep='\t', skiprows=1)
allspec = allspec[(allspec.dir_tilt_correction == 0) & (allspec.dir_comp == 'mt')]
s = load(P); ht = s[s.slot == 'HT']
def vgp(d, i, site):
    la, lo = GPS[site]; plon, plat, dp, dm = pmag.dia_vgp(d, i, 0, la, lo); return plat, plon
rows = []
UNITS = [('PKSK', 'PKSK'), ('NWFA', 'NWFA'), ('PKSI', 'PKSI'), ('PKSJ', 'PKSJ'), ('PKSH-HA', 'PKSH'), ('PKSH-HB', 'PKSH'),
         ('NWFB', 'NWFB'), ('PKSB', 'PKSB'), ('WBEA', 'WBEA')]
for u, site in UNITS:
    g = ht[ht.unit == u]
    pre = {'PKSH-HA': 'PKSH-[12]', 'PKSH-HB': 'PKSH-3'}.get(u, site)
    ntot = allspec.specimen.str.match(pre).sum()
    m, sm = two_tier(g); spec = fisher(g.dir_dec, g.dir_inc)
    plat, plon = vgp(m['dec'], m['inc'], site)
    r = dict(unit=u, name=NAME[u], ncores=m['n'], nspec=len(g), ntot=int(ntot), dec=m['dec'], inc=m['inc'], a95=m['a95'], k=m['k'],
             spec_a95=spec['a95'], spec_k=spec['k'], vgp_lat=plat, vgp_lon=plon,
             cores=[dict(core=c['sample'], n=c['n'], dec=c['dec'], inc=c['inc'], a95=c['a95'], k=c['k'],
                         vgp_lat=vgp(c['dec'], c['inc'], site)[0]) for c in sm])
    rows.append(r)
json.dump(dict(units=rows, gps=GPS, madcut=MADCUT), open(os.path.join(OUT, 'tables_data.json'), 'w'), indent=1, default=float)
for r in rows:
    print(f"{r['name']:7} N{r['ncores']} n{r['nspec']}/{r['ntot']} {r['dec']:6.1f} {r['inc']:+6.1f} a95 {r['a95']:6.1f} k {r['k']:7.1f} | spec a95 {r['spec_a95']:.1f} k {r['spec_k']:.1f} | VGP {r['vgp_lat']:+.1f}/{r['vgp_lon']:.1f}")
    if r['ncores'] <= 3:
        for c in r['cores']: print('     ', c['core'], c['n'], round(c['dec'],1), round(c['inc'],1), round(c['vgp_lat'],1))
for a in [407, 518, 553, 601, 770.5, 934, 1155, 1397]: print(a, chron(a))
