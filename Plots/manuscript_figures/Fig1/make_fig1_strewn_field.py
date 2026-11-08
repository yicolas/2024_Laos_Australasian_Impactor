"""
Figure 1 — Australasian tektite / microtektite strewn field.
Redrawn after Folco et al. (2010, EPSL 293) Fig. 1 from compiled site data
(australasian_tektites.csv; Glass 1994; Chalmers et al. 1976; Folco et al. 2010;
Gattacceca et al. 2022) plus Laos tektite finds (Sieh et al., Dataset S1).

Usage: python make_fig1_strewn_field.py <data_dir> <out_dir>
  data_dir must contain australasian_tektites.csv, Dataset_S1_Tektites_information.csv,
  tektite_field_outline.shp/.shx/.dbf
"""
import sys, os
import numpy as np
import pandas as pd
import matplotlib as mpl
import matplotlib.pyplot as plt
from matplotlib.lines import Line2D
import cartopy.crs as ccrs
import cartopy.feature as cfeature
import shapefile
from scipy.optimize import least_squares

data_dir = sys.argv[1] if len(sys.argv) > 1 else "."
out_dir = sys.argv[2] if len(sys.argv) > 2 else "."
os.makedirs(out_dir, exist_ok=True)

mpl.rcParams.update({
    "font.family": "DejaVu Sans", "font.size": 7.5, "axes.linewidth": 0.6,
    "pdf.fonttype": 42, "ps.fonttype": 42, "svg.fonttype": "none",
})

# ---------------- colours (colour-blind safe) ----------------
LAND = "#e9e6df"; OCEAN = "#ffffff"; COAST = "#8a8578"
C_MICRO = "#2c6fb0"      # deep-sea microtektites
C_ANT = "#2a9d8f"        # Antarctic microtektites
C_LAND = "#1b1b1b"       # land tektites
C_LAOS = "#c2410c"       # Muong Nong-type (layered)
C_SPLASH = "#7b3294"     # splash-form, SE Asia
C_STUDY = "#ffd23f"
C_CRATER = "#d62728"
C_FIELD = "#3b3b3b"

# ---------------- data ----------------
t = pd.read_csv(os.path.join(data_dir, "australasian_tektites.csv"))
t["abundance_mt_per_cm2"] = pd.to_numeric(t["abundance_mt_per_cm2"], errors="coerce")
micro = t[t.category == "deep_sea_microtektite"]
ant = t[t.category == "antarctic_microtektite"]
landt = t[(t.category == "land_tektite") & (t.tektite_type == "australite")]
mn = t[(t.category == "land_tektite") & (t.tektite_type.str.contains("Muong", na=False))]

# ---- AAT master list (compiled geochem; Paolo_Data) ----
aat = pd.read_csv(os.path.join(data_dir, "AAT_master_list.csv"), low_memory=False)
aat["Lat"] = pd.to_numeric(aat.Lat, errors="coerce"); aat["Lon"] = pd.to_numeric(aat.Lon, errors="coerce")
aat = aat.dropna(subset=["Lat", "Lon"])
sh = aat.SheetName.str.lower()
is_micro = sh.str.contains("microtektite")
# Chernonozhkin 2021 lists some land tektites under "Microtektites": reclassify by sample id
land_ids = aat.Sample.str.contains(r"-(?:JAV|PMJ|FT-|TI8|MA-)", regex=True)
is_micro &= ~land_ids
def tclass(r):
    s, smp = r.SheetName.lower(), r.Sample
    if s == "new": return "study"
    if "muong" in s: return "mn"
    if s.startswith("australite") or "-AN" in smp or "-MA-" in smp: return "aus"
    return "splash"   # indochinites, philippinites, javanites, billitonites, S China, Dalat/Hanoi/Vinh/Saigon, splash-form
aat["cls"] = np.where(is_micro, "micro", aat.apply(tclass, axis=1))
def uniq(df, la="Lat", lo="Lon"):
    return df.assign(_a=df[la].round(2), _o=df[lo].round(2)).drop_duplicates(["_a", "_o"])
aat_u = uniq(aat.copy().assign(key=aat.cls))  # unique per class below
A = {c: uniq(aat[aat.cls == c]) for c in ["study", "mn", "aus", "splash", "micro"]}
A_micro_ant = A["micro"][A["micro"].Lat < -60]
A_micro_sea = A["micro"][A["micro"].Lat >= -60]
for k, v in A.items(): print(k, len(aat[aat.cls == k]), "analyses at", len(v), "locations")

s1 = pd.read_csv(os.path.join(data_dir, "Dataset_S1_Tektites_information.csv"), encoding="utf-8-sig")
s1.columns = [c.strip() for c in s1.columns]
for c in ["Latitude", "Longitude", "Distance from crater (km)"]:
    s1[c] = pd.to_numeric(s1[c], errors="coerce")
s1 = s1.dropna(subset=["Latitude", "Longitude"])

# Proposed crater centre: recovered by inverting the S1 "distance from crater" column
# (the centre Sieh et al. used). Median misfit ~1.4 km.
x = s1.dropna(subset=["Distance from crater (km)"])
def _res(p):
    a, b = np.radians(p); A, B = np.radians(x.Latitude.values), np.radians(x.Longitude.values)
    d = 2 * 6371 * np.arcsin(np.sqrt(np.sin((A - a) / 2) ** 2 + np.cos(a) * np.cos(A) * np.sin((B - b) / 2) ** 2))
    return d - x["Distance from crater (km)"].values
CR_LAT, CR_LON = least_squares(_res, [15.0, 106.0]).x
print(f"crater centre {CR_LAT:.3f} N {CR_LON:.3f} E")

sf = shapefile.Reader(os.path.join(data_dir, "tektite_field_outline.shp"))
outline = np.array(sf.shapes()[0].points)

def geodesic_circle(lat0, lon0, r_km, n=361):
    d = r_km / 6371.0; lat0, lon0 = np.radians(lat0), np.radians(lon0)
    az = np.linspace(0, 2 * np.pi, n)
    lat = np.arcsin(np.sin(lat0) * np.cos(d) + np.cos(lat0) * np.sin(d) * np.cos(az))
    lon = lon0 + np.arctan2(np.sin(az) * np.sin(d) * np.cos(lat0), np.cos(d) - np.sin(lat0) * np.sin(lat))
    return np.degrees(lon), np.degrees(lat)

def msize(a):  # marker area ∝ log abundance
    return 6 + 16 * np.log10(np.clip(a, 1, None))

# ---------------- figure ----------------
proj = ccrs.PlateCarree(central_longitude=103)
pc = ccrs.PlateCarree()
fig = plt.figure(figsize=(7.09, 5.6))  # 180 mm full-page width
ax = fig.add_axes([0.065, 0.20, 0.925, 0.79], projection=proj)
ax.set_extent([14, 192, -88, 40], crs=pc)
ax.set_facecolor(OCEAN)
ax.add_feature(cfeature.NaturalEarthFeature("physical", "land", "50m"),
               facecolor=LAND, edgecolor="none", zorder=1)
ax.add_feature(cfeature.NaturalEarthFeature("physical", "coastline", "50m"),
               facecolor="none", edgecolor=COAST, linewidth=0.35, zorder=2)

gl = ax.gridlines(crs=pc, draw_labels=True, linewidth=0.3, color="#bdbdbd", linestyle=":",
                  xlocs=np.arange(20, 200, 20), ylocs=np.arange(-80, 41, 20))
gl.top_labels = gl.right_labels = False
gl.xlabel_style = gl.ylabel_style = {"size": 6.5, "color": "#444"}

# distance rings from proposed crater
for r, lab, azi in [(2000, "2000 km", 292), (5000, "5000 km", 215), (10000, "10 000 km", 207)]:
    lo, la = geodesic_circle(CR_LAT, CR_LON, r)
    ax.plot(lo, la, transform=pc, color="#9a9a9a", lw=0.5, ls=(0, (1.5, 2)), zorder=3)
    k = int(round(azi)); 
    ax.text(lo[k], la[k], lab, transform=pc, fontsize=5.5, color="#7a7a7a", ha="center", va="bottom",
            zorder=3, clip_on=True, bbox=dict(fc="white", ec="none", pad=0.3, alpha=0.8))

# strewn-field outline
ax.plot(outline[:, 0], outline[:, 1], transform=pc, color=C_FIELD, lw=1.0,
        ls=(0, (5, 2.5)), zorder=4)

# deep-sea microtektites: abundance-sized from Glass (1994)/Folco (2010) table
ax.scatter(micro.longitude, micro.latitude, s=msize(micro.abundance_mt_per_cm2.fillna(30)),
           transform=pc, facecolor=C_MICRO, edgecolor="white", lw=0.4, alpha=0.9, zorder=6)
# extra microtektite-bearing cores in the AAT geochem compilation not in the abundance table
have = set(zip(micro.latitude.round(0), micro.longitude.round(0)))
extra = A_micro_sea[[ (round(a), round(o)) not in have for a, o in zip(A_micro_sea.Lat, A_micro_sea.Lon)]]
print("extra micro cores:", len(extra), extra[["Sample","Lat","Lon"]].to_string())
ax.scatter(extra.Lon, extra.Lat, s=14, transform=pc, facecolor="none", edgecolor=C_MICRO, lw=0.7, zorder=6)
# Antarctic microtektites (Folco et al. 2010 table + AAT compilation)
ax.scatter(pd.concat([ant.longitude, A_micro_ant.Lon]), pd.concat([ant.latitude, A_micro_ant.Lat]),
           s=20, marker="D", transform=pc, facecolor=C_ANT, edgecolor="white", lw=0.4, zorder=6)
# land tektites
aus_lo = pd.concat([landt.longitude, A["aus"].Lon]); aus_la = pd.concat([landt.latitude, A["aus"].Lat])
ax.scatter(aus_lo, aus_la, s=20, marker="*", transform=pc, color=C_LAND, lw=0, zorder=6)
ax.scatter(A["splash"].Lon, A["splash"].Lat, s=20, marker="*", transform=pc, color=C_SPLASH, lw=0, zorder=6)
mn_lo = pd.concat([s1.Longitude, mn.longitude, A["mn"].Lon]); mn_la = pd.concat([s1.Latitude, mn.latitude, A["mn"].Lat])
ax.scatter(mn_lo, mn_la, s=12, marker="s", transform=pc, color=C_LAOS, lw=0, zorder=7)
# crater
ax.scatter([CR_LON], [CR_LAT], s=110, marker="*", transform=pc, facecolor=C_CRATER,
           edgecolor="black", lw=0.6, zorder=9)

# labels (Folco-style key cores)
labs = {"ODP 1144A": (4, 3), "ODP 1143A": (-3, -7), "ODP 769A": (5, -2), "ODP 758B": (-5, 3),
        "V28-239": (3, 3), "V20-138": (3, 2), "RC14-46": (3, -3), "DSDP 213": (3, -3),
        "RC8-52": (-6, -5), "E45-71": (3, -4)}
for n, (dx, dy) in labs.items():
    r = t[t.site_name == n]
    if len(r):
        lo, la = r.longitude.iloc[0], r.latitude.iloc[0]
        ax.annotate(n, (lo, la), xytext=(lo + dx, la + dy), xycoords=pc._as_mpl_transform(ax),
                    textcoords=pc._as_mpl_transform(ax), fontsize=5.5, color="#333",
                    ha="left" if dx > 0 else "right", va="center",
                    arrowprops=dict(arrowstyle="-", lw=0.35, color="#777", shrinkA=0, shrinkB=2),
                    zorder=8)
ax.annotate("Proposed source crater\n(Bolaven Plateau, S Laos)", (CR_LON, CR_LAT), xytext=(84, 31),
            xycoords=pc._as_mpl_transform(ax), textcoords=pc._as_mpl_transform(ax), fontsize=6.3,
            fontweight="bold", ha="center", va="bottom", color="#222", zorder=11,
            arrowprops=dict(arrowstyle="-", lw=0.5, color="#333", shrinkA=0, shrinkB=5))
ax.text(132, -60, "Australasian tektite/\nmicrotektite strewn field", transform=pc, fontsize=7,
        style="italic", ha="center", va="center", color="#333", zorder=5)
ax.text(156, -78, "Transantarctic\nMountains", transform=pc, fontsize=5.8, ha="right",
        va="center", color="#1f6f66", zorder=8)

ax.text(27, -66, "Dronning Maud\nLand", transform=pc, fontsize=5.8, ha="center", va="bottom", color="#1f6f66", zorder=8)
# ---------------- legend ----------------
h = [
    Line2D([], [], marker="*", ls="", color=C_CRATER, mec="black", mew=0.5, ms=10, label="Proposed source crater"),
    Line2D([], [], marker="s", ls="", color=C_LAOS, ms=4, label="Tektites: Muong Nong-type (layered)"),
    Line2D([], [], marker="*", ls="", color=C_SPLASH, ms=7, label="Tektites: splash-form, SE Asia"),
    Line2D([], [], marker="*", ls="", color=C_LAND, ms=7, label="Tektites: australites"),
    Line2D([], [], marker="o", ls="", mfc=C_MICRO, mec="white", ms=5, label="Microtektites, deep-sea cores (sized by abundance)"),
    Line2D([], [], marker="D", ls="", mfc=C_ANT, mec="white", ms=4, label="Microtektites, Antarctica"),
    Line2D([], [], color=C_FIELD, lw=1.0, ls=(0, (5, 2.5)), label="Strewn-field limit"),
    Line2D([], [], color="#9a9a9a", lw=0.6, ls=(0, (1.5, 2)), label="Great-circle distance from crater"),
    Line2D([], [], marker="o", ls="", mfc=C_STUDY, mec="black", mew=0.5, ms=5, label="Tektites analysed, this study (inset)"),
]
leg = fig.legend(handles=h, loc="lower left", bbox_to_anchor=(0.06, 0.005), ncol=2, fontsize=6, columnspacing=1.2,
                frameon=True, framealpha=0.95, edgecolor="#999", borderpad=0.6, handletextpad=0.4)
leg.get_frame().set_linewidth(0.5); leg.set_zorder(20)

# size key for microtektite abundance
kx = fig.add_axes([0.80, 0.03, 0.18, 0.115]); kx.set_xlim(0, 1); kx.set_ylim(0, 1); kx.axis("off")
kx.add_patch(plt.Rectangle((0, 0), 1, 1, transform=kx.transAxes, fc="white", ec="#999", lw=0.5, alpha=0.95))
kx.text(0.5, 0.86, "Microtektites cm$^{-2}$ (>125 µm)", ha="center", fontsize=5.8)
for xx, v in zip([0.16, 0.39, 0.62, 0.86], [1, 10, 100, 1000]):
    kx.scatter(xx, 0.45, s=msize(v), facecolor=C_MICRO, edgecolor="white", lw=0.4)
    kx.text(xx, 0.12, f"{v:g}", ha="center", fontsize=5.6)

# ---------------- inset: Indochina ----------------
fig.canvas.draw(); P = ax.get_position()
ix = fig.add_axes([P.x0 + 0.006, P.y1 - 0.262, 0.235, 0.256], projection=pc)
ix.set_extent([100.5, 108.8, 12.8, 18.6], crs=pc)
ix.add_feature(cfeature.NaturalEarthFeature("physical", "land", "50m"), facecolor=LAND, edgecolor="none")
ix.add_feature(cfeature.NaturalEarthFeature("physical", "coastline", "50m"), facecolor="none", edgecolor=COAST, lw=0.4)
ix.add_feature(cfeature.NaturalEarthFeature("cultural", "admin_0_boundary_lines_land", "50m"),
               facecolor="none", edgecolor="#9b9b9b", lw=0.4, ls="--")
for r in [100, 200, 300, 400, 500]:
    lo, la = geodesic_circle(CR_LAT, CR_LON, r)
    ix.plot(lo, la, color="#9a9a9a", lw=0.45, ls=(0, (1.5, 2)))
    if CR_LAT + r / 111.2 > 18.3: continue
    ix.text(CR_LON - 0.15, CR_LAT + r / 111.2 + 0.03, f"{r} km" if r == 100 else f"{r}", fontsize=4.8, color="#7a7a7a", ha="right", clip_on=True)
ix.scatter(mn_lo, mn_la, s=7, marker="s", color=C_LAOS, lw=0, alpha=0.85, zorder=5)
ix.scatter(A["splash"].Lon, A["splash"].Lat, s=16, marker="*", color=C_SPLASH, lw=0, zorder=5)
ix.scatter(A["study"].Lon, A["study"].Lat, s=30, marker="o", facecolor=C_STUDY, edgecolor="black", lw=0.5, zorder=7)
ix.scatter([CR_LON], [CR_LAT], s=70, marker="*", facecolor=C_CRATER, edgecolor="black", lw=0.5, zorder=6)
for nm, lo, la in [("LAOS", 104.6, 17.9), ("THAILAND", 101.6, 15.2), ("CAMBODIA", 104.4, 13.75),
                   ("VIETNAM", 107.85, 15.0)]:
    ix.text(lo, la, nm, fontsize=5, color="#8a8578", ha="center", va="center", style="italic")
ix.text(CR_LON + 0.2, CR_LAT - 0.35, "Bolaven\nPlateau", fontsize=5.3, ha="left", va="top", color="#222")
for s in ix.spines.values(): s.set_linewidth(0.6)
for xv in [102, 104, 106, 108]:
    ix.plot([xv, xv], [12.8, 13.0], color="k", lw=0.5, transform=pc)
    ix.text(xv, 13.05, f"{xv}°E", fontsize=4.8, ha="center", va="bottom", color="#555", transform=pc)
for yv in [14, 16, 18]:
    ix.plot([108.62, 108.8], [yv, yv], color="k", lw=0.5, transform=pc)
    ix.text(108.58, yv, f"{yv}°N", fontsize=4.8, ha="right", va="center", color="#555", transform=pc)
# locator box on main map
ax.add_patch(plt.Rectangle((100.5, 12.8), 8.3, 5.8, transform=pc, fc="none", ec="black", lw=0.6, zorder=10))

for ext in ["pdf", "png", "svg"]:
    fig.savefig(os.path.join(out_dir, f"Fig1_Australasian_strewn_field.{ext}"),
                dpi=600 if ext == "png" else None, bbox_inches="tight", pad_inches=0.02)
print("done")
