"""Load and QC the Bolaven tektite + source-rock geochemistry (Paolo_Data)."""
import numpy as np, pandas as pd, re
import os
_HERE = os.path.dirname(os.path.abspath(__file__))
_ICLOUD = os.path.expanduser("~/Library/Mobile Documents/com~apple~CloudDocs/Caltech Projects/Australasian Impactor")
# raw data are not in the git repo: Paolo_Data/ sits beside Code/ locally; the regional compilation lives in iCloud
ROOT = os.environ.get("GEOCHEM_ROOT", os.path.join(_HERE, "..", "..", "Paolo_Data", "AAT Laos - Geochem data")) + "/"
S4 = os.environ.get("GEOCHEM_S4", os.path.join(_ICLOUD, "Dataset_S4_Basalt geochemical data.xlsx"))
SICAT = os.environ.get("GEOCHEM_SICAT", os.path.join(_ICLOUD, "geochem.csv"))   # Sieh et al. (2019) compilation
OX = ['SiO2','TiO2','Al2O3','FeOt','MnO','MgO','CaO','Na2O','K2O']
TOTAL_MIN = 97.0          # EPMA acceptance (Carter et al. 2025 PCA criterion)

def epma(all_spots=False):
    e = pd.read_excel(ROOT+"Tektite data/EPMA_tektite_data_full.xlsx").rename(columns={'  SAMPLE':'spot','FeO':'FeOt'})
    e['tektite'] = e.spot.str.replace(r'_s\d+$','',regex=True,case=False)
    e['total'] = e['Oxide Totals']
    if not all_spots: e = e[e.total >= TOTAL_MIN].copy()
    e[OX] = e[OX].clip(lower=0.005)
    e[OX] = e[OX].div(e[OX].sum(axis=1), axis=0)*100
    return e.reset_index(drop=True)

TR = ['Li','Be','Sc','V','Cr','Co','Ni','Cu','Zn','Rb','Sr','Y','Zr','Nb','Cs','Ba','La','Ce','Pr','Nd','Sm','Eu','Gd',
      'Tb','Dy','Ho','Er','Tm','Yb','Lu','Hf','Ta','Pb','Th','U','Ru','Pd','Ir191','Ir193']

def laicpms():
    """LA-ICP-MS rows. Internal standard = per-spot EPMA SiO2 as reduced in the master. Spots on MNG24_A3_2
    were standardised to SiO2 of 27-65 wt% from failed EPMA points (totals 33-86 %); their Al/Si (IS-independent)
    matches MNG24_A3_1, so they are re-standardised to the MNG24_A3_1 accepted-EPMA mean SiO2."""
    l = pd.read_excel(ROOT+"Tektite data/Tektite_LAICPMS_master.xlsx").dropna(subset=['Sample'])
    l = l.rename(columns={'191  Ir':'Ir191','193  Ir':'Ir193','208  Pb':'Pb','232  Th':'Th','238  U':'U'})
    l['tektite'] = l.Sample.str[:10]; l['spot'] = l.Sample
    l['SiO2_IS_orig'] = l.SiO2
    ref = epma(); si_ref = ref.loc[ref.tektite=='MNG24_A3_1','SiO2'].mean()
    l['SiO2_IS'] = np.where(l.tektite=='MNG24_A3_2', si_ref, l.SiO2)
    f = l.SiO2_IS/l.SiO2_IS_orig
    for c in TR+['Mg','Al','Ti','Mn']: l[c] = l[c]*f
    l['Al2O3_LA'] = l.Al*1.8895e-4; l['MgO_LA']=l.Mg*1.6583e-4; l['TiO2_LA']=l.Ti*1.6681e-4; l['MnO_LA']=l.Mn*1.2912e-4
    return l.reset_index(drop=True), si_ref

def _num(x):
    return pd.to_numeric(x, errors='coerce')

LITH = {  # field lithology -> dictionary type
 'Sandstone':'Khorat sandstone','Pebbly sandstone':'Khorat sandstone','Sandstone (fresh)':'Khorat sandstone',
 'Sandstone (weathered)':'Khorat sandstone','Mudstone':'Khorat mudstone','Basalt':'Bolaven basalt',
 'Saprolite':'Lateritic saprolite',"Catastroloess'":'Diamicton / "catastro-loess"',"Catasroloess'":'Diamicton / "catastro-loess"',
 'Diamicton':'Diamicton / "catastro-loess"',"Catastroloess' with quartz pebbles":'Diamicton / "catastro-loess"'}

def sources():
    """Whole-rock majors (XRF, anhydrous-normalised block) + ICP-MS pellet traces for local lithologies,
    plus Sieh et al. (2019) Bolaven basalts (Dataset S4, Actlabs FUS-ICP / ICP-MS)."""
    w = pd.read_excel(ROOT+"Target rock data/Laos_analyses_master.xlsx", sheet_name="WR analyses", header=None).set_index(0)
    rows = list(w.index); i = rows.index('Normalized Majors')
    nm = w.iloc[i+1:i+11].T; nm.columns = ['SiO2','TiO2','Al2O3','Fe2O3','MgO','CaO','Na2O','K2O','P2O5','MnO']
    meta = w.loc[['Sample','Lithology']].T; meta.columns=['sample','lith']
    df = pd.concat([meta, nm.apply(_num)], axis=1).iloc[1:]
    df['lith'] = df.lith.astype(str).str.strip()
    df = df[df.lith.isin(LITH)].dropna(subset=['SiO2','Fe2O3'])
    df = df.drop_duplicates(subset=['sample'])                     # PKE24_B entered twice
    df['type'] = df.lith.map(LITH); df['FeOt'] = df.Fe2O3*0.8998
    # Khorat / laterite cut: XRF Cr, Ni
    xr = w.loc[['Sample','Cr','Ni','Cu','Zn','Rb','Sr','Zr','Ba']].T.iloc[1:]; xr.columns=['sample','Cr_x','Ni_x','Cu_x','Zn_x','Rb_x','Sr_x','Zr_x','Ba_x']
    xr = xr.drop_duplicates('sample')
    for c in xr.columns[1:]: xr[c] = _num(xr[c])
    df = df.merge(xr, on='sample', how='left')
    t = pd.read_excel(ROOT+"Target rock data/Laos_analyses_master.xlsx", sheet_name="Trace analyses", header=None)
    names = [re.sub(r'^\d+\s+','',str(x)).replace(' (total)','').strip() for x in t.iloc[3:,0]]
    tt = t.iloc[3:,4:].copy(); tt.index = names; tt.columns = [str(c).strip() for c in t.iloc[0,4:]]
    tt = tt.T.apply(_num); tt.index = tt.index.str.replace('PKQ24_AG1','PKQ24_A_G1')
    tt = tt.groupby(level=0).mean()
    df = df.merge(tt, left_on='sample', right_index=True, how='left')
    df['source'] = 'This study'
    # Sieh et al. 2019 basalts
    s = pd.read_excel(S4, header=None); cols = [str(c) for c in s.iloc[0]]
    sb = s.iloc[5:].copy(); sb.columns = ['sample','lat','lon','elev','lab']+cols[5:]
    sb = sb.dropna(subset=['SiO2'])
    for c in sb.columns[5:]: sb[c] = _num(sb[c])
    sb['FeOt'] = sb['Fe2O3(T)']*0.8998
    maj = ['SiO2','TiO2','Al2O3','FeOt','MnO','MgO','CaO','Na2O','K2O']
    sb[maj] = sb[maj].div(sb[maj].sum(axis=1),axis=0)*100
    sb['type']='Bolaven basalt'; sb['lith']='Basalt'; sb['source']='Sieh et al. 2019'
    sb = sb.rename(columns={'Cr':'Cr_x','Ni':'Ni_x'})
    keep = ['sample','lith','type','source']+maj+['Cr_x','Ni_x']+[c for c in TR if c in sb.columns and c not in ('Cr','Ni')]
    out = pd.concat([df, sb[keep]], ignore_index=True)
    out[maj] = out[maj].clip(lower=0.005); out[maj] = out[maj].div(out[maj].sum(axis=1),axis=0)*100
    out['Cr'] = out['Cr_x']; out['Ni'] = out['Ni_x']
    return out


SICAT_TYPE = {'KhoratCretaceous':'Khorat sandstone','sandstone':'Khorat sandstone','mudstone':'Khorat mudstone',
              'volcanic':'Bolaven basalt','basaltic\nlaterite':'Lateritic saprolite','saprolite':'Lateritic saprolite',
              'loess':'Diamicton / "catastro-loess"','pebbly laterite':'Sedimentary laterite',
              'sedimentary\nlaterite':'Sedimentary laterite','sedimentary\nbauxite':'Sedimentary laterite',
              'metatuff':'Metatuff'}
def sicat():
    g = pd.read_csv(SICAT, low_memory=False)
    g = g[g['Sample type'].isin(SICAT_TYPE)].copy()
    g = g[~g.Sample.astype(str).str.strip().isin(['NASC','Avg','Max','Min','UCC','PAAS'])]
    g['type'] = g['Sample type'].map(SICAT_TYPE); g['lith'] = g['Sample type'].str.replace('\n',' ')
    g['source'] = 'Sieh et al. 2019 compilation (' + g['Project/Reference'].astype(str) + ')'
    g['FeOt'] = _num(g['FeO total (calc)']).fillna(_num(g['Fe2O3 total'])*0.8998)
    def _dl(x):   # '<0.10' -> half the detection limit
        x = x.astype(str).str.strip()
        lt = x.str.startswith('<')
        v = pd.to_numeric(x.str.lstrip('<').str.strip(), errors='coerce')
        return v.where(~lt, v/2)
    for c in OX+[e for e in TR if e in g.columns]+['Gd','Tb']:
        if c in g.columns: g[c] = _dl(g[c])
    for c in ['TiO2','MnO']: g[c] = g[c].fillna(g.groupby('type')[c].transform('median'))
    g = g.dropna(subset=['SiO2','Al2O3','FeOt','MgO','CaO','Na2O','K2O'])
    # screen volcanic analyses for alteration / poor totals (LOI > 3 wt% or reported total outside 98.5-101.5 wt%)
    loi = _num(g['LOI']); tot = _num(g['Total']); volc = g['Sample type'] == 'volcanic'
    bad = volc & ((loi > 3) | (tot.notna() & ((tot < 98.5) | (tot > 101.5))))
    g = g[~bad]
    g['sample'] = g.Sample.astype(str).str.strip()
    # metatuff: keep the felsic tuffs only (drop two altered mafic rocks and one Na-leached sample)
    g = g[~g['sample'].isin(['H18-16-A-1', 'H1818-A-1', 'DKI18-A-1'])]
    keep = ['sample','lith','type','source']+OX+[c for c in TR if c in g.columns]
    g = g[keep].copy(); g[OX] = g[OX].clip(lower=0.005); g[OX] = g[OX].div(g[OX].sum(axis=1),axis=0)*100
    return g

def sources_all():
    """This study + Sieh et al. (2019) regional compilation (replaces Dataset S4, which it contains)."""
    a = sources(); a = a[a.source == 'This study']
    out = pd.concat([a, sicat()], ignore_index=True)
    # split basalts at the Macdonald & Katsura (1964) alkaline/subalkaline divide: Na2O+K2O = 0.37 (SiO2 - 39)
    b = out.type == 'Bolaven basalt'
    alk = (out.Na2O + out.K2O) > 0.37*(out.SiO2 - 39)
    out.loc[b & alk, 'type'] = 'Bolaven alkali basalt'
    out.loc[b & ~alk, 'type'] = 'Bolaven tholeiite'
    return out

# literature reference compositions (anhydrous, FeOt)
PAAS = dict(SiO2=62.8,TiO2=1.0,Al2O3=18.9,FeOt=6.5,MnO=0.11,MgO=2.2,CaO=1.3,Na2O=1.2,K2O=3.7)       # Taylor & McLennan 1985
UCC  = dict(SiO2=66.6,TiO2=0.64,Al2O3=15.4,FeOt=5.04,MnO=0.10,MgO=2.48,CaO=3.59,Na2O=3.27,K2O=2.80) # Rudnick & Gao 2003

def literature_aat():
    a = pd.read_csv(ROOT+"Tektite data/AAT_master_list.csv", low_memory=False)
    a = a[a.SheetName.isin(['Muong Nong','Indochinites','Indochinite','Hanoi','Vinh','Dalat','Saigon'])].copy()
    fe = _num(a['FeO']).fillna(_num(a['FeO*'])).fillna(_num(a['FeOt']))
    fe = fe.fillna(_num(a['Fe2O3'])*0.8998) + (_num(a['Fe2O3']).fillna(0)*0.8998).where(_num(a['FeO']).notna(),0)
    a['FeOt'] = fe
    for c in OX: a[c] = _num(a[c])
    a = a.dropna(subset=['SiO2','Al2O3','FeOt','MgO','CaO','Na2O','K2O'])
    a['TiO2']=a.TiO2.fillna(0.7); a['MnO']=a.MnO.fillna(0.08)
    a[OX] = a[OX].div(a[OX].sum(axis=1),axis=0)*100
    return a

if __name__ == '__main__':
    e = epma(); print('EPMA accepted', len(e), e.tektite.value_counts().to_dict())
    l, si = laicpms(); print('LA rows', len(l), 'SiO2 ref', round(si,2))
    s = sources(); print(s.groupby('type').size()); print(s.groupby('type')[OX].mean().round(2))
    print(s.groupby('type')[['La','Th','Sc','Eu','Zr']].count())
    a = literature_aat(); print('lit', len(a)); print(a[OX].median().round(2))
