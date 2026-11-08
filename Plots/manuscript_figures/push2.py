"""Second push into LEAD_4 (input: current LEAD_4 with Figs 1-4, 6-8 and Tables 1-2 already in).
- drop Fig 7 (old Fig 11); Fig 8 -> Fig 7 (PKQ-A as 3 boulders)
- geochem: Fig 5 (rebuilt from the updated pipeline) replaces old Figs 14-15; old 16, 17 -> S1, S4;
  geochem results subsection moved before the thermal-demagnetization results so figures are cited in order
- Table 3 (conglomerate tests) after the conglomerate paragraphs; supplementary tables S1-S5
- notebook appendix A1-A62 replaced by Supplementary figures S1-S16
- text: Figs 1 and 2 cited in Introduction / Geological Context; reference renumbering
Usage: python push2.py in.docx out.docx"""
import sys, re, copy
from docx import Document
from docx.oxml.ns import qn
from PIL import Image

IN, OUTF = sys.argv[1], sys.argv[2]
doc = Document(IN); body = doc.element.body
W = lambda e: ''.join(t.text or '' for t in e.iter(qn('w:t')))
N = lambda s: s.replace('\xa0', ' ')
log, miss = [], []
def paras(): return list(body.iterchildren(qn('w:p')))
def para_starting(s, key=None):
    h = [p for p in paras() if N(W(p)).startswith(s) and (key is None or key in W(p))]
    assert len(h) == 1, (s, key, len(h)); return h[0]
def para_containing(s):
    h = [p for p in paras() if s in N(W(p))]; assert h, s; return h[0]
def has_img(p): return bool(list(p.iter(qn('a:blip'))))
def prev_img(p):
    q = p.getprevious()
    while q is not None and not has_img(q): q = q.getprevious()
    return q
def drop(e): e.getparent().remove(e)

def set_image(p, png, width_in=6.5, max_h=8.6):
    rId, _ = doc.part.get_or_add_image(png); w, h = Image.open(png).size
    cx = int(width_in * 914400); cy = int(cx * h / w)
    if cy > int(max_h * 914400): cy = int(max_h * 914400); cx = int(cy * w / h)
    list(p.iter(qn('a:blip')))[0].set(qn('r:embed'), rId)
    for e in p.iter(qn('wp:extent')): e.set('cx', str(cx)); e.set('cy', str(cy))
    for e in p.iter(qn('a:ext')):
        if e.get('cx') is not None: e.set('cx', str(cx)); e.set('cy', str(cy))
    for e in p.iter(qn('wp:docPr')): e.set('id', str(abs(hash(png + str(cx))) % 10 ** 8))

def set_runs(p, parts):
    """parts: list of (text, bold). Keeps pPr and the first run's rPr."""
    rpr = None
    for r in p.iter(qn('w:r')):
        rp = r.find(qn('w:rPr'))
        if rp is not None: rpr = copy.deepcopy(rp); break
    for ch in list(p):
        if ch.tag != qn('w:pPr'): p.remove(ch)
    for txt, bold in parts:
        r = p.makeelement(qn('w:r'), {}); rp = copy.deepcopy(rpr) if rpr is not None else r.makeelement(qn('w:rPr'), {})
        b = rp.find(qn('w:b'))
        if bold and b is None: rp.insert(1 if rp.find(qn('w:rFonts')) is not None else 0, rp.makeelement(qn('w:b'), {}))
        if not bold and b is not None: rp.remove(b)
        r.append(rp); t = r.makeelement(qn('w:t'), {}); t.text = txt
        t.set('{http://www.w3.org/XML/1998/namespace}space', 'preserve'); r.append(t); p.append(r)
def set_caption(p, label, text): set_runs(p, [(label, True), (' ' + text, False)])
def md_caption(path, label):
    t = open(path).read(); s = t.split('**' + label + '**')[1]
    s = re.split(r'\n## |\nScript:', s)[0]
    return re.sub(r'\s+', ' ', re.sub(r'\*\*', '', s)).strip()

# templates
cap_tpl = copy.deepcopy(para_starting('Figure 6.'))
img_tpl = copy.deepcopy(prev_img(para_starting('Figure 6.')))
body_tpl = copy.deepcopy(para_containing('Block samples were reoriented'))
h1_tpl = copy.deepcopy(para_starting('Notebook-generated figures'))
for bm in list(h1_tpl.iter(qn('w:bookmarkStart'))) + list(h1_tpl.iter(qn('w:bookmarkEnd'))): drop(bm)
def new_img(png, w=6.5, max_h=8.6): p = copy.deepcopy(img_tpl); set_image(p, png, w, max_h); return p
def new_cap(label, text): p = copy.deepcopy(cap_tpl); set_caption(p, label, text); return p
def new_h1(text): p = copy.deepcopy(h1_tpl); set_runs(p, [(text, False)]); return p

# ---------------- Fig 7 (old 11) out, Fig 8 -> Fig 7 ----------------
c = para_starting('Figure 7.', 'Magnetostratigraphic summary'); im = prev_img(c); drop(c); drop(im); log.append('dropped old Fig 7 (VGP vs age)')
c = para_starting('Figure 8.'); set_image(prev_img(c), 'Fig7.png')
set_caption(c, 'Figure 7.', md_caption('/home/claude/fig8/out7/Fig7_caption.md', 'Figure 7.')); log.append('Fig 8 -> Fig 7')

# ---------------- geochem figures ----------------
c = para_starting('Figure 14.'); set_image(prev_img(c), 'Fig5.png'); set_caption(c, 'Figure 5.', open('fig5_caption.txt').read().strip())
c = para_starting('Figure 15.'); drop(prev_img(c)); drop(c)
s1 = para_starting('Figure 16.'); s1i = prev_img(s1); s4 = para_starting('Figure 17.'); s4i = prev_img(s4)
set_image(s1i, 'FigS1.png'); set_caption(s1, 'Figure S1.', N(W(s1))[len('Figure 16.'):].strip())
set_image(s4i, 'FigS4.png'); set_caption(s4, 'Figure S4.', N(W(s4))[len('Figure 17.'):].strip())
for e in (s1i, s1, s4i, s4): drop(e)
log.append('Fig 5 in; old 15 out; old 16/17 -> S1/S4')

# move the geochemistry results subsection before the thermal-demagnetization results
hg = para_starting('Geochemistry: Testing the Bolaven Source Hypothesis'); hd = para_starting('Discussion')
ht = para_starting('Thermal Demagnetization Results')
blk = []; e = hg
while e is not None and e is not hd: blk.append(e); e = e.getnext()
for e in blk: ht.addprevious(e)
log.append(f'moved geochem results ({len(blk)} elements) before Thermal Demagnetization Results')

# ---------------- tables ----------------
tdoc = Document('/home/claude/tables/Tables_3_4_S.docx'); tb = list(tdoc.element.body)
TEXTW = 9360
def fit_table(tbl):
    tbl = copy.deepcopy(tbl); grid = tbl.find(qn('w:tblGrid')); cols = [int(g.get(qn('w:w'))) for g in grid]; s = TEXTW / sum(cols)
    for g in grid: g.set(qn('w:w'), str(int(int(g.get(qn('w:w'))) * s)))
    for tw in tbl.iter(qn('w:tcW')): tw.set(qn('w:w'), str(int(int(tw.get(qn('w:w'))) * s)))
    for tw in tbl.iter(qn('w:tblW')): tw.set(qn('w:w'), str(TEXTW))
    for rp in tbl.iter(qn('w:rPr')):
        for f in rp.findall(qn('w:rFonts')): rp.remove(f)
        rp.insert(0, rp.makeelement(qn('w:rFonts'), {qn('w:ascii'): 'Calibri', qn('w:hAnsi'): 'Calibri', qn('w:cs'): 'Calibri'}))
        for sz in rp.findall(qn('w:sz')): sz.set(qn('w:val'), '15')
    return tbl
def table_by(label):
    for i, e in enumerate(tb):
        if e.tag == qn('w:p') and W(e).startswith(label):
            j = i + 1
            while tb[j].tag != qn('w:tbl'): j += 1
            return W(e)[len(label):].strip(), fit_table(tb[j])
t3cap, t3 = table_by('Table 3.')
anchor = para_containing('Specimens were averaged to their parent boulders')
c3 = new_cap('Table 3.', t3cap); anchor.addnext(c3); c3.addnext(t3); log.append('Table 3 (conglomerate tests) inserted')

# ---------------- supplement ----------------
hnb = para_starting('Notebook-generated figures'); hsem = para_starting('Supplementary: SEM/EDS')
e = hnb.getnext()
while e is not hsem: n = e.getnext(); drop(e); e = n
set_runs(hnb, [('Supplementary figures', False)])
SUPP = []
SUPP.append((['FigS1.png'], 'Figure S1.', N(W(s1))[len('Figure S1.'):].strip()))
SUPP.append((['FigS2.png'], 'Figure S2.', 'Additional rock magnetism of Bolaven basalts (MicroMag/2G AF and pulse-magnetizer measurements; plots from Code/AF_rockmag.ipynb). (a) Isothermal remanent magnetization (IRM) acquisition of eight specimens, normalised to the saturation IRM (SIRM); all reach 90 % of saturation by ~200–300 mT, as expected for magnetite-family carriers. (b) Alternating-field (AF) demagnetization of the NRM of three specimens, with median destructive fields (MDF) of ~9–20 mT. (c) AF demagnetization spectra of the NRM, an anhysteretic remanence (ARM) and the SIRM of WBE-A-1J. (d) ARM/SIRM, a magnetite grain-size proxy (higher values indicate finer, more single-domain-like grains), and ARM against SIRM.'))
SUPP.append((['FigS3.png'], 'Figure S3.', 'AF demagnetization of the NRM (geographic coordinates). (a) Specimen PKS-J-3A: equal-area path of the remanence with AF peak field (colour) and normalised intensity decay; AF cleaning isolates the same reversed ChRM (≈177°/−30°) as thermal demagnetization, and the remanence is AF-hard (MDF > 94 mT). (b) Equal-area projections of AF demagnetization paths to 94 mT for six specimens (filled = lower hemisphere, open = upper hemisphere).'))
SUPP.append((['FigS4.png'], 'Figure S4.', N(W(s4))[len('Figure S4.'):].strip()))
PL = [('NWFA', 'NWF-A (in-situ flow, 518 ka)'), ('PKSB', 'PKS-B (in-situ flow, 1155 ka)'), ('PKSH', 'PKS-H (upper horizon HA, cores 1–2; lower flow HB, core 3)'),
      ('PKSI', 'PKS-I (corestone, 553 ka)'), ('PKSJ', 'PKS-J (in-situ flow, 601 ka)'), ('PKSK', 'PKS-K (in-situ flow, 407 ka)'), ('WBEA', 'WBE-A (basal flow, 1397 ka)'),
      ('NWFB', 'NWF-B (transported blocks)'), ('NWFC', 'NWF-C (diamicton boulders)'), ('PKQA', 'PKQ-A (diamicton; field boulders B1 = cores 0–4, B2 = 5–6, B3 = 7–9)'),
      ('PKSF', 'PKS-F (diamicton boulders)'), ('PKSG', 'PKS-G (diamicton boulders)')]
import glob, os
for k, (site, desc) in enumerate(PL):
    files = sorted(glob.glob(f'/home/claude/figS/out/FigS_demag_{site}*.png'))
    SUPP.append((files, f'Figure S{5 + k}.', f'Orthogonal-vector (Zijderveld) diagrams of every thermally demagnetized specimen from {desc}, in geographic coordinates' +
                 (f' ({len(files)} parts)' if len(files) > 1 else '') + '. x = north; filled symbols = horizontal plane (east), open = vertical plane (up); scale in A m². Arrows are the LT (green), MT (blue) and HT (purple) least-squares fits from the fitquest re-fits, drawn in the direction of demagnetization. Each label gives the HT direction (declination/inclination) and MAD; red labels mark HT fits with MAD > 15°, which are excluded from all site, boulder and conglomerate statistics.'))
anchor = hnb
for files, lab, text in SUPP:
    for f in files:
        ip = new_img(f, 6.5, 8.4); anchor.addnext(ip); anchor = ip
    cp = new_cap(lab, text); anchor.addnext(cp); anchor = cp
log.append(f'supplementary figures: {len(SUPP)}')
# supplementary tables
set_runs(hsem, [('Supplementary tables', False)])
intro = para_containing('lists the complete set of ten quantitative')
for t in intro.iter(qn('w:t')):
    if t.text and 'Table 3' in N(t.text): t.text = N(t.text).replace('Table 3', 'Table S4'); break
for t in intro.iter(qn('w:t')):
    if t.text and '(Fig. 8)' in N(t.text): t.text = N(t.text).replace('(Fig. 8)', '(Fig. 4k,l)')
eds_cap = para_starting('Table 3.', 'Complete EDS'); set_caption(eds_cap, 'Table S4.', N(W(eds_cap))[len('Table 3.'):].strip().replace('summarized in Fig. 8', 'shown in Fig. 4k,l'))
anchor = hsem
for lab in ['Table S1.', 'Table S2.', 'Table S3.']:
    ctext, tt = table_by(lab); cp = new_cap(lab, ctext); anchor.addnext(cp); cp.addnext(tt)
    sp = copy.deepcopy(body_tpl); set_runs(sp, [('', False)]); tt.addnext(sp); anchor = sp
eds_tbl = [e for e in body.iterchildren(qn('w:tbl')) if 'Titanomagnetite' in W(e)][0]
ctext, tt = table_by('Table S5.'); cp = new_cap('Table S5.', ctext); eds_tbl.addnext(cp); cp.addnext(tt)
log.append('supplementary tables S1-S5')

# ---------------- text ----------------
def rep(key, a, b, required=True):
    p = para_containing(key)
    for t in p.iter(qn('w:t')):
        if t.text and a in N(t.text): t.text = N(t.text).replace(a, b, 1); log.append(f'ref: {a} -> {b}'); return
    (miss if required else log).append(f'MISSED: {a} [{key[:30]}]')
def append_sentence(key, text):
    p = para_containing(key); ts = [t for t in p.iter(qn('w:t')) if t.text]; ts[-1].text = ts[-1].text.rstrip() + ' ' + text; log.append(f'+ sentence [{key[:30]}]')
def insert_after(key, text):
    p = para_containing(key); q = copy.deepcopy(body_tpl); set_runs(q, [(text, False)]); p.addnext(q); log.append(f'+ paragraph after [{key[:30]}]')

# Figs 1, 2 in background / regional geology
rep('covering approximately 20% of', '(Glass & Pizzuto, 1994)', '(Glass & Pizzuto, 1994; Fig. 1)')
rep('points to an impact site in eastern central', 'Indochina (Glass &', 'Indochina (Fig. 1; Glass &')
rep('Bolaven Plateau rises approximately 1 km', 'east of the Mekong River (Sieh et al., 2019)', 'east of the Mekong River (Fig. 2; Sieh et al., 2019)')
insert_after('A unique outcrop 10-20 km southeast',
 'Figure 2 places these observations, and our sampling, on the regional geology. The negative Bouguer anomaly and the crater outline proposed by Sieh et al. (2019) lie beneath the summit of the plateau, where every dated flow is younger than the impact, whereas the brecciated ejecta crop out off the plateau margin to the southeast, and the tektite-bearing diamicton (“catastro-loess”) blankets the plateau and its flanks. In their composite section (Fig. 3c), the proximal breccia carries unweathered boulders of basalt and sandstone near its top. If these basalt boulders are ejecta, they were excavated from pre-impact flows, were cold when they landed, and should retain the remanence of their parent flows in random orientations; if they are corestones weathered in place, or rock remagnetized after deposition, their directions should cluster. We therefore sampled two kinds of site (Fig. 2): dated flows on and around the plateau (NWF-A, NWF-B, PKS-B, PKS-H, PKS-J, PKS-K and WBE-A, together with the PKS-I corestone), which test the ⁴⁰Ar/³⁹Ar chronology magnetostratigraphically, and basalt boulders in the diamicton at four localities (NWF-C, PKQ-A, PKS-F and PKS-G), on which conglomerate tests distinguish transported clasts from rock that was weathered or remagnetized in place.')
# geochem refs (old 14-17)
rep('96.3–96.9 wt%) of MNG24_B1 and MG24_B1', ' (Fig. 14a)', '')
rep('96.3–96.9 wt%) of MNG24_B1 and MG24_B1', '(Fig. 16a)', '(Fig. S1a)')
rep('96.3–96.9 wt%) of MNG24_B1 and MG24_B1', 'Accepted analyses were recomputed anhydrous with total Fe as FeO.', 'Accepted analyses were recomputed anhydrous with total Fe as FeO; the analysed tektites and screening results are listed in Table S2.')
rep('have oxide totals of at least 97', 'Fig. 14a', 'Fig. 5a'); rep('have oxide totals of at least 97', 'Fig. 14b–h', 'Fig. 5b–h'); rep('have oxide totals of at least 97', 'Fig. 16a', 'Fig. S1a')
rep('except MnO', 'Fig. 15d', 'Fig. 5l'); rep('except MnO', 'Fig. 15a,b', 'Fig. 5i,j'); rep('except MnO', 'Fig. 15c', 'Fig. 5k')
rep('except MnO', 'Fig. 14e,f', 'Fig. 5f,g'); rep('except MnO', 'Fig. 15e', 'Fig. 5m; Table S5')
rep('calibration-insensitive ratios', 'Fig. 16b', 'Fig. S1b'); rep('calibration-insensitive ratios', 'Fig. 16c', 'Fig. S1c')
rep('Th/Sc versus Eu/Eu*', 'Fig. 15', 'Fig. 5')
rep('Ir is therefore', 'Fig. 17b', 'Fig. S4b'); rep('Ir is therefore', 'Fig. 17a', 'Fig. S4a')
# paleomag refs
rep('These polarity determinations provide', 'Figs. 6i, 7', 'Fig. 6i')
rep('summarised on a single equal-area projection', 'Figure 8a', 'Figure 7a')
rep('test outcomes are shown in', 'Figure 8o–t', 'Figure 7o–t; Table 3')
rep('CLAST', '(“CLAST” in Table 1)', '(“Displaced clast” in Table 1)', required=False)
append_sentence('All site means reported in this section follow', 'Site ages, polarities and statistics are listed in Tables 1 and 2.')
append_sentence('Representative demagnetization behavior is summarized', 'Orthogonal-vector diagrams of all 364 specimens are given in Figs S5–S16.')
rep('Representative hysteresis loops', 'Fig. 4c)', 'Fig. 4c; Table S3)')
rep('Mineral identification (SEM/EDS)', 'Fig. 4k,l)', 'Fig. 4k,l; Table S4)')
append_sentence('Summary: Comprehensive rock magnetic analyses', 'IRM acquisition, AF demagnetization of the NRM, ARM/SIRM ratios and AF coercivity spectra are shown in Figs S2 and S3.')
append_sentence('Block samples were reoriented to their original', 'Sites, sample types, orientation methods and specimen numbers are listed in Table S1.')
# leftovers in table cells / captions
for t in body.iter(qn('w:t')):
    if t.text and 'Fig. 8o' in N(t.text): t.text = N(t.text).replace('Fig. 8o', 'Fig. 7o'); log.append('cell: Fig. 8o -> 7o')

# drop now-unused image relationships
used = set(e.get(qn('r:embed')) for e in body.iter(qn('a:blip')))
for rId, rel in list(doc.part.rels.items()):
    if rel.reltype.endswith('/image') and rId not in used: doc.part.drop_rel(rId)
doc.save(OUTF)
print('\n'.join(log)); print('\n'.join(miss) or 'no misses')
txt = [N(W(p)) for p in paras()]
for s in txt:
    for m in re.finditer(r'Fig(?:ure|s?\.)\s*(8|9|1[0-7])\b', s): print('LEFTOVER:', s[max(0, m.start() - 40):m.end() + 15])
