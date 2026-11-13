# -*- coding: utf-8 -*-
"""Assemble a MagIC (data model 3.0) contribution for the Bolaven paper from the fitted pmagpy tables.
- hierarchy fixed: specimen = e.g. NWFA-1B, sample = oriented core/block (NWFA-1), site = NWFA, location = Bolaven Plateau
- one sample row per core (57), with the corrected orientation (fix_orientation_units.py) and orientation method
- site rows carry coordinates (Table S1), setting, 40Ar/39Ar ages (Table 1) and the HT site means of Table 2/3
- writes magic_upload/*.txt and runs ipmag.upload_magic (validation + single upload file)
Usage: python build_magic_upload.py"""
import os, re, numpy as np, pandas as pd
from pmagpy import ipmag
HERE = os.path.dirname(os.path.abspath(__file__)); OUT = os.path.join(HERE, 'magic_upload'); os.makedirs(OUT, exist_ok=True)
rd = lambda f: pd.read_csv(os.path.join(HERE, f), sep='\t', skiprows=1, low_memory=False)
def wr(df, name):
    with open(os.path.join(OUT, name + '.txt'), 'w') as fh:
        fh.write(f'tab\t{name}\n'); df.to_csv(fh, sep='\t', index=False)
CIT = 'This study'; LOC = 'Bolaven Plateau'
core = lambda s: re.sub(r'[A-Z]$', '', s)

SITES = {  # lat, lon, setting, geologic_types, sun-oriented?, age_ka, age_sigma_ka(2s), description
 'NWFA': (15.6446, 106.1427, 'In-situ flow', 'Lava Flow', True, 518, 6, ''),
 'NWFB': (15.6236, 105.9859, 'Transported blocks (conglomerate test)', 'Lava Flow', False, 934, 30, 'Blocks; age of parent flow'),
 'NWFC': (15.4148, 106.1433, 'Diamicton boulders (conglomerate test)', 'Lava Flow', True, None, None, ''),
 'PKQA': (15.1020, 105.8536, 'Diamicton boulders (conglomerate test); field boulders = cores 0-4, 5-6, 7-9', 'Lava Flow', True, None, None, 'Cores 0 and 3 magnetic-compass oriented'),
 'PKSB': (15.1543, 106.1897, 'In-situ flow', 'Lava Flow', True, 1155, 2, ''),
 'PKSF': (15.1131, 106.2282, 'Diamicton boulders (conglomerate test)', 'Lava Flow', True, None, None, ''),
 'PKSG': (15.1558, 106.1903, 'Diamicton boulders / corestones (conglomerate test)', 'Lava Flow', False, None, None, ''),
 'PKSH': (15.1557, 106.1918, 'Two horizons: HA (cores 1-2) above HB (core 3)', 'Lava Flow', True, 770.5, 9.3, 'Age is of the upper horizon'),
 'PKSI': (15.2328, 106.1908, 'Displaced corestone', 'Lava Flow', True, 553, 20, 'Ex situ'),
 'PKSJ': (15.2431, 106.2581, 'In-situ flow', 'Lava Flow', False, 601, 44, ''),
 'PKSK': (15.2419, 106.2585, 'In-situ flow', 'Lava Flow', False, 407, 18, ''),
 'WBEA': (15.2700, 106.3472, 'Basal flow', 'Lava Flow', False, 1397, 13, ''),
}
MAG_CORES = {'PKQA-0', 'PKQA-3'}

# ---------------- measurements / specimens ----------------
m = rd('measurements.txt').drop(columns=['meas_n_orient']); m['sample'] = m['specimen'].map(core); m['location'] = LOC
wr(m, 'measurements')
sp = rd('specimens.txt'); sp['sample'] = sp['specimen'].map(core); sp['location'] = LOC
sp['citations'] = CIT
wr(sp, 'specimens')

# ---------------- samples (one per core) ----------------
s0 = rd('samples.txt'); s0['core'] = s0['sample'].map(core)
rows = []
for c, g in s0.groupby('core'):
    site = g.site.iloc[0]; lat, lon, setting, gtype, sun, *_ = SITES[site]
    so = 'SO-SUN' if (sun and c not in MAG_CORES) else 'SO-MAG'
    rows.append(dict(sample=c, site=site, specimens=':'.join(sorted(g['sample'])), azimuth=g.azimuth.iloc[0], dip=g.dip.iloc[0],
                     bed_dip=0, bed_dip_direction=0, lat=lat, lon=lon, geologic_classes='Igneous:Extrusive',
                     geologic_types=gtype, lithologies='Basalt', method_codes=so + ':SO-CMD-NORTH', citations=CIT,
                     software_packages='pmagpy', location=LOC))
samples = pd.DataFrame(rows); wr(samples, 'samples')

# ---------------- sites ----------------
mean = pd.read_csv(os.path.join(HERE, 'recomputed_site_means.csv')).set_index('site')
rows = []
for site, (lat, lon, setting, gtype, sun, age, asig, desc) in SITES.items():
    r = mean.loc[site]
    k = r.k if pd.notna(r.k) else r.k_spec; a95 = r.a95 if pd.notna(r.a95) else r.a95_spec
    d = dict(site=site, location=LOC, samples=':'.join(samples[samples.site == site]['sample']), lat=lat, lon=lon,
             geologic_classes='Igneous:Extrusive', geologic_types=gtype, lithologies='Basalt', description='; '.join(x for x in [setting, desc] if x),
             dir_comp_name='HT', dir_dec=round(r.dec, 1), dir_inc=round(r.inc, 1), dir_k=round(k, 1), dir_alpha95=round(a95, 1),
             dir_n_samples=int(r.n_units), dir_n_specimens=int(r.n_spec), dir_tilt_correction=0, vgp_lat=round(r.vgp, 1),
             method_codes='LP-DIR-T:DE-BFL:DA-DIR-GEO:SM-FISHER', criteria='MAD<=15', citations=CIT, software_packages='pmagpy',
             result_type='i', result_quality='g')
    if age is not None:
        d.update(age=age, age_sigma=round(asig / 2, 1), age_unit='Ka', method_codes=d['method_codes'] + ':GM-ARAR')
    rows.append(d)
wr(pd.DataFrame(rows), 'sites')

# ---------------- location ----------------
lats = [v[0] for v in SITES.values()]; lons = [v[1] for v in SITES.values()]
loc = pd.DataFrame([dict(location=LOC, location_type='Outcrop', lat_s=min(lats), lat_n=max(lats), lon_w=min(lons), lon_e=max(lons),
                         geologic_classes='Igneous:Extrusive', lithologies='Basalt', sites=':'.join(SITES), age_low=400, age_high=1400,
                         age_unit='Ka', citations=CIT, description='Bolaven Plateau volcanic field, southern Laos; in-situ flows and '
                         'diamicton boulders sampled March 2024')])
wr(loc, 'locations')
os.chdir(OUT)
res = ipmag.upload_magic(dir_path=OUT, concat=False)
print(res)
