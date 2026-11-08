"""Build Fig1_strewn_field.gpkg with every layer used in Figure 1 (EPSG:4326)."""
import numpy as np, pandas as pd, geopandas as gpd, shapefile, os, sys
import shapely.geometry as sg
from scipy.optimize import least_squares
D = sys.argv[1]; OUT = sys.argv[2]
NE = os.path.expanduser('~/.local/share/cartopy/shapefiles/natural_earth')
if os.path.exists(OUT): os.remove(OUT)
def W(gdf, name): gdf.to_file(OUT, layer=name, driver='GPKG'); print(name, len(gdf))

t = pd.read_csv(f'{D}/australasian_tektites.csv')
t['abundance_mt_per_cm2'] = pd.to_numeric(t.abundance_mt_per_cm2, errors='coerce')
pt = lambda df, x, y: gpd.GeoDataFrame(df, geometry=gpd.points_from_xy(df[x], df[y]), crs=4326)

# microtektites (deep sea, abundance-sized) and Antarctic
W(pt(t[t.category == 'deep_sea_microtektite'].copy(), 'longitude', 'latitude'), 'microtektites_deepsea')
aat = pd.read_csv(f'{D}/AAT_master_list.csv', low_memory=False)
aat['Lat'] = pd.to_numeric(aat.Lat, errors='coerce'); aat['Lon'] = pd.to_numeric(aat.Lon, errors='coerce')
aat = aat.dropna(subset=['Lat', 'Lon'])
sh = aat.SheetName.str.lower()
land_ids = aat.Sample.str.contains(r'-(?:JAV|PMJ|FT-|TI8|MA-)', regex=True)
micro = sh.str.contains('microtektite') & ~land_ids
def tclass(r):
    s, smp = r.SheetName.lower(), r.Sample
    if s == 'new': return 'This study (EPMA)'
    if 'muong' in s: return 'Muong Nong-type (layered)'
    if s.startswith('australite') or '-AN' in smp or '-MA-' in smp: return 'Australites'
    return 'Splash-form, SE Asia'
aat['tektite_class'] = np.where(micro, 'microtektite', aat.apply(tclass, axis=1))
keep = ['Sample', 'SheetName', 'SourceFile', 'coords approx', 'Lat', 'Lon', 'tektite_class']
u = aat[keep].assign(_a=aat.Lat.round(2), _o=aat.Lon.round(2)).drop_duplicates(['tektite_class', '_a', '_o']).drop(columns=['_a', '_o'])
ant = pd.concat([t[t.category == 'antarctic_microtektite'][['site_name', 'latitude', 'longitude', 'source']].rename(columns={'latitude': 'Lat', 'longitude': 'Lon'}),
                 u[(u.tektite_class == 'microtektite') & (u.Lat < -60)][['Sample', 'Lat', 'Lon', 'SourceFile']].rename(columns={'Sample': 'site_name', 'SourceFile': 'source'})])
W(pt(ant, 'Lon', 'Lat'), 'microtektites_antarctic')

tek = u[u.tektite_class != 'microtektite'].copy()
# add australites from australasian_tektites.csv and Muong Nong (Gattacceca) + Sieh S1 Laos finds
x = t[t.category == 'land_tektite'].copy()
x['tektite_class'] = np.where(x.tektite_type.str.contains('Muong', na=False), 'Muong Nong-type (layered)', 'Australites')
x = x.rename(columns={'site_name': 'Sample', 'latitude': 'Lat', 'longitude': 'Lon', 'source': 'SourceFile'})
s1 = pd.read_csv(f'{D}/Dataset_S1_Tektites_information.csv', encoding='utf-8-sig'); s1.columns = [c.strip() for c in s1.columns]
for c in ['Latitude', 'Longitude', 'Distance from crater (km)']: s1[c] = pd.to_numeric(s1[c], errors='coerce')
s1 = s1.dropna(subset=['Latitude', 'Longitude'])
s1b = pd.DataFrame({'Sample': s1['Sample(s) name'], 'Lat': s1.Latitude, 'Lon': s1.Longitude, 'SourceFile': 'Sieh et al. Dataset S1',
                    'tektite_class': 'Muong Nong-type (layered)'})
tek = pd.concat([tek, x[['Sample', 'Lat', 'Lon', 'SourceFile', 'tektite_class']], s1b], ignore_index=True)
W(pt(tek, 'Lon', 'Lat'), 'tektites')

# crater centre (inverted from S1 distance column)
z = s1.dropna(subset=['Distance from crater (km)'])
def res(p):
    a, b = np.radians(p); A, B = np.radians(z.Latitude.values), np.radians(z.Longitude.values)
    return 2 * 6371 * np.arcsin(np.sqrt(np.sin((A - a) / 2) ** 2 + np.cos(a) * np.cos(A) * np.sin((B - b) / 2) ** 2)) - z['Distance from crater (km)'].values
la, lo = least_squares(res, [15, 106]).x
W(gpd.GeoDataFrame({'name': ['Proposed source crater (Bolaven Plateau)'], 'lat': [la], 'lon': [lo]}, geometry=[sg.Point(lo, la)], crs=4326), 'source_crater')

def circ(lat0, lon0, r, n=721):
    d = r / 6371; lat0, lon0 = np.radians(lat0), np.radians(lon0); az = np.linspace(0, 2 * np.pi, n)
    lat = np.arcsin(np.sin(lat0) * np.cos(d) + np.cos(lat0) * np.sin(d) * np.cos(az))
    lon = lon0 + np.arctan2(np.sin(az) * np.sin(d) * np.cos(lat0), np.cos(d) - np.sin(lat0) * np.sin(lat))
    return np.degrees(lon), np.degrees(lat)
rings = []
for r in [100, 200, 300, 400, 500, 2000, 5000, 10000]:
    x_, y_ = circ(la, lo, r); rings.append((r, sg.LineString(np.column_stack([x_, y_]))))
W(gpd.GeoDataFrame({'radius_km': [r for r, _ in rings], 'label': [f'{r:,} km'.replace(',', ' ') for r, _ in rings]}, geometry=[g for _, g in rings], crs=4326), 'distance_rings')

o = np.array(shapefile.Reader(f'{D}/tektite_field_outline.shp').shapes()[0].points)
W(gpd.GeoDataFrame({'name': ['Australasian strewn field']}, geometry=[sg.LineString(o)], crs=4326), 'strewn_field_outline')
W(gpd.GeoDataFrame({'name': ['inset extent']}, geometry=[sg.box(100.5, 12.8, 108.8, 18.6)], crs=4326), 'inset_extent')
W(gpd.read_file(f'{NE}/physical/ne_50m_land.shp')[['geometry']], 'ne_land')
W(gpd.read_file(f'{NE}/cultural/ne_50m_admin_0_boundary_lines_land.shp')[['geometry']], 'ne_borders')
lab = pd.DataFrame({'label': ['ODP 1144A', 'ODP 1143A', 'ODP 769A', 'ODP 758B', 'V28-239', 'V20-138', 'RC14-46', 'DSDP 213', 'RC8-52', 'E45-71']})
W(pt(lab.merge(t.rename(columns={'site_name': 'label'})[['label', 'latitude', 'longitude']], on='label'), 'longitude', 'latitude'), 'core_labels')
