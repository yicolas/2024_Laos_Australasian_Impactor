"""Build Fig2_southern_Laos.gpkg (EPSG:4326): harmonised geology (1998 Lao map inside Laos,
USGS OFR 97-470-F geo3bl outside), faults, crater outlines, sites, towns, rivers, borders."""
import sys, os, numpy as np, pandas as pd, geopandas as gpd, shapely
from shapely.ops import unary_union
U = '/mnt/user-data/uploads/Australasian Impactor/QGIS/'
NE = os.path.expanduser('~/.local/share/cartopy/shapefiles/natural_earth/')
OUT = sys.argv[1]
if os.path.exists(OUT): os.remove(OUT)
def W(g, n): g.to_file(OUT, layer=n, driver='GPKG'); print(n, len(g))
WIN = shapely.box(104.6, 13.6, 108.4, 17.0)

UNITS = {  # code: (order, era, description)
    'Q':   (1, 'Quaternary', 'Alluvium (Mekong and Sekong rivers)'),
    'QB':  (2, 'Quaternary', 'Alkaline basalt'),
    'Mz3': (3, 'Mesozoic', 'Riverine sandstones, evaporites (salt, gypsum)'),
    'Mz2': (4, 'Mesozoic', 'Marine sandstones, coal'),
    'Mz1': (5, 'Mesozoic', 'Marine clastic sediments, rhyolite, dacite, tuff'),
    'Pz3': (6, 'Paleozoic', 'Upper Paleozoic sandstone, shale, limestone, volcanic rocks'),
    'Pz2': (7, 'Paleozoic', 'Middle Paleozoic mudrock, sandstone, limestone, volcanic rocks'),
    'Pz1': (8, 'Paleozoic', 'Lower Paleozoic mudrock, sandstone, wacke, volcanic rocks'),
    'Tgr': (9, 'Intrusive', 'Granitoids (granite, granodiorite)'),
    'PR':  (10, 'Proterozoic', 'Gneiss and schist'),
    'H2O': (11, '', 'Water'),
}
lao = gpd.read_file(U + 'data/polbnda_lao.shp').to_crs(4326)
lao_u = unary_union(lao.geometry).buffer(0)

# --- inside Laos: 1998 Lao geological map (N. Anderson digitisation)
g = gpd.read_file(U + 'geo_polygons.shp').to_crs(4326)
g['unit'] = g.Unit.str.strip().replace({'Qb': 'QB', 'Pr': 'PR', 'Pgr': 'Tgr'})
g['geometry'] = g.buffer(0).intersection(lao_u)
g = g[~g.is_empty][['unit', 'geometry']]; g['source'] = '1998 Geological Map of Lao PDR'

# --- outside Laos: USGS geo3bl reclassified to the same legend
b = gpd.read_file(U + 'Maps/geo3bl/geo3bl.shp').to_crs(4326)
b = b[b.intersects(WIN)].copy()
def rc(r):
    glg, typ = (r.GLG or ''), (r.TYPE or '')
    if glg == 'H2O': return 'H2O'
    if typ == 'i': return 'Tgr'
    if typ == 'v' and glg in ('NQ', 'TQ', 'Q'): return 'QB'
    if glg in ('Q', 'TQ'): return 'Q'
    if glg == 'NQ': return 'QB'
    if glg in ('K',): return 'Mz3'
    if glg in ('J', 'JK', 'TrJ'): return 'Mz2'
    if glg in ('Tr', 'PTr') : return 'Mz1'
    if glg in ('CmO', 'OS'): return 'Pz1'
    if glg in ('D', 'DC', 'PZ', 'PZMZ'): return 'Pz2'
    if glg in ('CP', 'P', 'PZu'): return 'Pz3'
    if glg.startswith('Pt'): return 'PR'
    return None
b['unit'] = b.apply(rc, axis=1); print('unmapped geo3bl:', b[b.unit.isna()].GLG.value_counts().to_dict())
b = b[b.unit.notna()].copy()
b['geometry'] = b.buffer(0).intersection(WIN).difference(lao_u)
b = b[~b.is_empty][['unit', 'GLG', 'TYPE', 'geometry']]; b['source'] = 'USGS OFR 97-470-F (geo3bl), generalised'
geo = pd.concat([g, b], ignore_index=True)
geo['order'] = geo.unit.map(lambda u: UNITS[u][0]); geo['era'] = geo.unit.map(lambda u: UNITS[u][1])
geo['description'] = geo.unit.map(lambda u: UNITS[u][2]); geo['in_laos'] = geo.source.str.startswith('1998')
W(gpd.GeoDataFrame(geo, crs=4326), 'geology')

W(gpd.read_file(U + 'fault_lines.shp').to_crs(4326), 'faults')
c = gpd.read_file(U + 'crater_diameters.shp').to_crs(4326)[['name', 'geometry']]
c['label'] = c.name.map({'gravity crater': 'Bouguer gravity anomaly (Sieh et al., 2020)', 'geology crater': 'Geologic crater outline (Sieh et al., 2020)'})
W(c, 'crater_outlines')

# --- paleomag sites (GPS from all_samples_laos.shp)
S = [  # site, gps names, type, note
 ('NWF-A', 'NWF24-A-P', 'In situ basalt flow', '518 ka'),
 ('NWF-B', 'NWF24-B-P', 'Basalt clasts in diamicton (conglomerate test)', 'passes'),
 ('NWF-C', 'NWF24-C', 'Basalt clasts in diamicton (conglomerate test)', 'passes'),
 ('PKQ-A', 'PKQ24-A', 'Basalt clasts in diamicton (conglomerate test)', 'scale-dependent'),
 ('PKS-B', 'PKS24-B', 'In situ basalt flow', '1155 ka'),
 ('PKS-F', 'PKS24-F', 'Basalt clasts in diamicton (conglomerate test)', 'fails'),
 ('PKS-G', 'PKS24-HF', 'Basalt clasts in diamicton (conglomerate test)', 'fails'),
 ('PKS-H', 'PKS24-HA-P', 'Basalt clasts in diamicton (conglomerate test)', 'n=3'),
 ('PKS-I', 'PKS24-I-P', 'Anomalous corestone (ex situ)', ''),
 ('PKS-J', 'PKS24-J-P', 'In situ basalt flow', '601 ka'),
 ('PKS-K', 'PKS24-K-P', 'In situ basalt flow', '553 ka'),
 ('WBE-A', 'WBE24-A-P', 'In situ basalt flow', '1395 ka'),
]
a = gpd.read_file(U + 'all_samples_laos.shp')
rows = []
for site, key, typ, note in S:
    m = a[a.Name.str.startswith(key) & ~a.Name.str.startswith('PKS24-BF')]
    p = m.geometry.union_all().centroid
    rows.append(dict(site=site, site_type=typ, note=note, n_gps=len(m), lat=round(p.y, 5), lon=round(p.x, 5), geometry=p))
sites = gpd.GeoDataFrame(rows, crs=4326)
# label text for the regional map (sites < 0.5 km apart grouped); offsets (mm) for the zoom inset
grp = {'PKS-B': 'PKS-B, -G, -H', 'PKS-G': '', 'PKS-H': '', 'PKS-J': 'PKS-J, -K', 'PKS-K': ''}
sites['label_main'] = sites.site.map(lambda s: grp.get(s, s))
off = {'PKS-B': (-6.0, 2.0), 'PKS-G': (-6.0, -2.0), 'PKS-H': (5.0, 2.0), 'PKS-J': (-1.5, 2.5), 'PKS-K': (3.5, -1.0),
       'PKS-I': (0, 2.5), 'PKS-F': (0, -2.5), 'WBE-A': (0, 2.5)}
sites['lab_dx'] = sites.site.map(lambda s: off.get(s, (0, 2.5))[0]); sites['lab_dy'] = sites.site.map(lambda s: off.get(s, (0, 2.5))[1]); print(sites[['site', 'n_gps', 'lat', 'lon']].to_string())
W(sites, 'paleomag_sites')

# --- towns (GCPs used for the 1998 map + Paksong)
gcp = pd.read_csv('/mnt/user-data/uploads/Australasian Impactor/laos_geology_ref_modified.tif.points', comment='#')
T = pd.DataFrame([('Pakse', 15.11, 105.80), ('Salavan', 15.716, 106.416), ('Attapeu', 14.804, 106.839), ('Champasak', 14.894, 105.873),
                  ('Khong Sedone', 15.58, 105.804), ('Paksong', 15.183, 106.233)], columns=['name', 'lat', 'lon'])
W(gpd.GeoDataFrame(T, geometry=gpd.points_from_xy(T.lon, T.lat), crs=4326), 'towns')

r = gpd.read_file(NE + 'physical/ne_10m_rivers_lake_centerlines.shp')
r = r[r.intersects(WIN)][['name', 'geometry']].clip(WIN); r['name'] = r.name.replace({'Kong': 'Xe Kong'}); W(r, 'rivers')
W(lao[['geometry']].dissolve().boundary.to_frame('geometry').set_crs(4326) if False else gpd.GeoDataFrame(geometry=[lao_u.boundary], crs=4326), 'laos_border')
bl = gpd.read_file(NE + 'cultural/ne_50m_admin_0_boundary_lines_land.shp'); W(bl[bl.intersects(WIN)][['geometry']], 'borders_ne')
W(gpd.read_file(NE + 'physical/ne_50m_land.shp').clip(shapely.box(90, -12, 125, 30))[['geometry']], 'land_regional')
W(gpd.GeoDataFrame({'name': ['Figure 2 extent']}, geometry=[shapely.box(105.35, 14.45, 107.65, 16.3)], crs=4326), 'fig2_extent')
W(gpd.GeoDataFrame({'name': ['Bolaven zoom']}, geometry=[shapely.box(106.07, 15.085, 106.39, 15.30)], crs=4326), 'zoom_extent')
cl = pd.DataFrame([('THAILAND', 105.43, 15.68), ('CAMBODIA', 106.75, 14.5), ('VIETNAM', 107.55, 15.9), ('LAOS', 106.95, 16.18)], columns=['name', 'lon', 'lat'])
W(gpd.GeoDataFrame(cl, geometry=gpd.points_from_xy(cl.lon, cl.lat), crs=4326), 'country_labels')
