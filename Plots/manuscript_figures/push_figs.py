"""Push final Figs 1-8, S1-S2 and Tables 1-2 into manuscript_LEAD_4 (merged.docx -> LEAD_4_new.docx)."""
import re, copy
from docx import Document
from docx.oxml.ns import qn
from PIL import Image

import sys
GEO = len(sys.argv) > 1 and sys.argv[1] == "geo"   # geochem (Fig 5, S1, S2) only when the updated runs are done
O = '/mnt/user-data/outputs/'
doc = Document('merged.docx')
body = doc.element.body
W = lambda e: ''.join(t.text or '' for t in e.iter(qn('w:t')))
log = []

def para_starting(s):
    hits = [p for p in body.iterchildren(qn('w:p')) if W(p).startswith(s)]
    assert len(hits) == 1, (s, len(hits)); return hits[0]
def para_containing(s):
    hits = [p for p in body.iterchildren(qn('w:p')) if s in W(p)]
    assert len(hits) >= 1, s; return hits[0]
def prev_img(p):
    q = p.getprevious()
    while q is not None and not list(q.iter(qn('a:blip'))): q = q.getprevious()
    return q
def has_img(p): return bool(list(p.iter(qn('a:blip'))))

def caption_md(path, label):
    t = open(path).read()
    m = re.search(r'\*\*' + re.escape(label) + r'\*\*(.*?)(?:\n## |\Z)', t, re.S)
    s = m.group(1)
    s = re.sub(r'\n\s*\n', ' ', s).replace('\n', ' ')
    s = re.sub(r'\*\*(.*?)\*\*', r'\1', s)
    return re.sub(r'\s+', ' ', s).strip()

def set_image(p, png, width_in=6.5):
    rId, _ = doc.part.get_or_add_image(png)
    w, h = Image.open(png).size
    cx = int(width_in * 914400); cy = int(cx * h / w)
    if cy > int(8.6 * 914400):           # keep within page height
        cy = int(8.6 * 914400); cx = int(cy * w / h)
    blips = list(p.iter(qn('a:blip'))); blips[0].set(qn('r:embed'), rId)
    for e in p.iter(qn('wp:extent')): e.set('cx', str(cx)); e.set('cy', str(cy))
    for e in p.iter(qn('a:ext')):
        if e.get('cx') is not None: e.set('cx', str(cx)); e.set('cy', str(cy))

def set_caption(p, label, text):
    rpr = None
    for r in p.iter(qn('w:r')):
        rp = r.find(qn('w:rPr'))
        if rp is not None: rpr = copy.deepcopy(rp); break
    for ch in list(p):
        if ch.tag != qn('w:pPr'): p.remove(ch)
    for txt, bold in [(label, True), (' ' + text, False)]:
        r = p.makeelement(qn('w:r'), {}); rp = copy.deepcopy(rpr) if rpr is not None else r.makeelement(qn('w:rPr'), {})
        b = rp.find(qn('w:b'))
        if bold and b is None: rp.insert(1 if rp.find(qn('w:rFonts')) is not None else 0, rp.makeelement(qn('w:b'), {}))
        if not bold and b is not None: rp.remove(b)
        r.append(rp); t = r.makeelement(qn('w:t'), {}); t.text = txt; t.set('{http://www.w3.org/XML/1998/namespace}space', 'preserve'); r.append(t); p.append(r)

def drop(p): p.getparent().remove(p)

# ---------------- figures ----------------
cap = {
 1: caption_md(O + 'Fig1/Fig1_caption.md', 'Figure 1.'),
 2: caption_md('/mnt/user-data/uploads/2024_Laos_Australasian_Impactor/Plots/manuscript_figures/Fig2/Fig2_caption.md', 'Figure 2.'),
 3: caption_md(O + 'Fig3/Fig3_caption.md', 'Figure 3.'),
 4: caption_md(O + 'Fig4/Fig4_caption.md', 'Figure 4.'),
 6: caption_md(O + 'Fig6/Fig6_caption.md', 'Figure 6.'),
}
t5 = open(O + 'Fig5/Fig5_caption.md').read(); cap[5] = re.sub(r'\s+', ' ', re.sub(r'\*\*', '', t5.split('**Figure 5.**')[1].split('Script:')[0])).strip()
t8 = open(O + 'Fig8/Fig8_caption.md').read(); cap[8] = re.sub(r'\s+', ' ', re.sub(r'\*\*', '', t8.split('**Figure 8.**')[1].split('Script:')[0])).strip()

for n, old in [(1, 'Figure 1.'), (2, 'Figure 2.'), (3, 'Figure 3.'), (4, 'Figure 4.'), (6, 'Figure 9.'), (8, 'Figure 12.')] + ([(5, 'Figure 14.')] if GEO else []):
    c = para_starting(old); im = prev_img(c)
    set_image(im, f'Fig{n}.png'); set_caption(c, f'Figure {n}.', cap[n]); log.append(f'Fig {n}: replaced old "{old}"')
# old Fig 11 -> Fig 7 (kept image)
c = para_starting('Figure 11.'); t = W(c)[len('Figure 11.'):].strip(); set_caption(c, 'Figure 7.', t); log.append('Fig 7: old Fig 11 kept, renumbered')
# remove superseded figures (image + caption)
for old, key in [('Figure 5.', 'Day plot'), ('Figure 6.', 'Low-temperature magnetometry'), ('Figure 7.', 'First-order reversal'),
                 ('Figure 8.', 'SEM/EDS mineralogy'), ('Figure 10.', 'Site-mean characteristic remanent'),
                 ('Figure 13.', 'Equal-area projections of boulder')] + ([('Figure 15.', 'Reversible-jump MCMC')] if GEO else []):
    hits = [p for p in body.iterchildren(qn('w:p')) if W(p).startswith(old) and key in W(p)[:120]]
    assert len(hits) == 1, (old, len(hits)); c = hits[0]
    # images immediately above (old Fig 9 has 7 stacked images; old Fig 13 has 4 images + panel labels)
    q = c.getprevious(); drop(c)
    while q is not None and (has_img(q) or re.match(r'^\([a-d]\) ', W(q)) or (W(q).strip() == '' and has_img(q))):
        nxt = q.getprevious(); drop(q); q = nxt
    log.append(f'removed old {old}')
# remaining stacked images of old Fig 9 (above the new Fig 6 image)
c6 = para_starting('Figure 6.'); im6 = prev_img(c6); q = im6.getprevious()
while q is not None and has_img(q) and W(q).strip() == '':
    nxt = q.getprevious(); drop(q); q = nxt; log.append('removed extra old-Fig-9 image')
# empty image-less paragraphs left between the old Fig 9 images and caption
q = im6.getnext()
while q is not None and q is not c6:
    nxt = q.getnext()
    if has_img(q): drop(q); log.append('removed extra old-Fig-9 image (below)')
    q = nxt

# ---------------- supplementary figures S1, S2 ----------------
if GEO:
  h_sem = para_starting('Supplementary: SEM/EDS'); h_nb = para_starting('Notebook-generated figures')
  h_new = copy.deepcopy(h_sem)
  for bm in list(h_new.iter(qn('w:bookmarkStart'))) + list(h_new.iter(qn('w:bookmarkEnd'))): bm.getparent().remove(bm)
  for t in h_new.iter(qn('w:t')): t.text = ''
  list(h_new.iter(qn('w:t')))[0].text = 'Supplementary figures'
  h_nb.addprevious(h_new)
  for old, new, png in [('Figure 16.', 'Figure S1.', 'FigS1.png'), ('Figure 17.', 'Figure S2.', 'FigS2.png')]:
      c = para_starting(old); im = prev_img(c); set_image(im, png)
      set_caption(c, new, W(c)[len(old):].strip()); h_nb.addprevious(im); h_nb.addprevious(c); log.append(f'{old} -> {new} (moved to supplement)')

# ---------------- tables ----------------
tdoc = Document('/mnt/user-data/outputs/Tables/Tables_1_2_updated.docx')
tb = tdoc.element.body; tps = [e for e in tb if e.tag in (qn('w:p'), qn('w:tbl'))]
TEXTW = 9360   # 6.5 in
def fit_table(tbl):
    grid = tbl.find(qn('w:tblGrid')); cols = [int(g.get(qn('w:w'))) for g in grid]; s = TEXTW / sum(cols)
    for g in grid: g.set(qn('w:w'), str(int(int(g.get(qn('w:w'))) * s)))
    for tw in tbl.iter(qn('w:tcW')): tw.set(qn('w:w'), str(int(int(tw.get(qn('w:w'))) * s)))
    for tw in tbl.iter(qn('w:tblW')): tw.set(qn('w:w'), str(TEXTW))
    for rp in tbl.iter(qn('w:rPr')):
        for f in rp.findall(qn('w:rFonts')): rp.remove(f)
        rf = rp.makeelement(qn('w:rFonts'), {qn('w:ascii'): 'Calibri', qn('w:hAnsi'): 'Calibri', qn('w:cs'): 'Calibri'}); rp.insert(0, rf)
        for sz in rp.findall(qn('w:sz')): sz.set(qn('w:val'), '15')
    return tbl
def note_para(src_p, like):
    p = copy.deepcopy(like)
    for ch in list(p):
        if ch.tag != qn('w:pPr'): p.remove(ch)
    r = p.makeelement(qn('w:r'), {}); rp = r.makeelement(qn('w:rPr'), {})
    rp.append(rp.makeelement(qn('w:rFonts'), {qn('w:ascii'): 'Calibri', qn('w:hAnsi'): 'Calibri', qn('w:cs'): 'Calibri'}))
    sz = rp.makeelement(qn('w:sz'), {qn('w:val'): '18'}); rp.append(sz); r.append(rp)
    t = r.makeelement(qn('w:t'), {}); t.text = W(src_p); t.set('{http://www.w3.org/XML/1998/namespace}space', 'preserve'); r.append(t); p.append(r)
    return p
# new doc order: cap1, tbl1, notes(5), [sectbreak], cap2, tbl2, note
caps = [e for e in tps if e.tag == qn('w:p') and W(e).startswith('Table')]
tbls = [e for e in tps if e.tag == qn('w:tbl')]
notes1 = [e for e in tps if e.tag == qn('w:p') and W(e)[:1] in 'ᵃᵇᶜᵈᵉ' and W(e).strip()]
note2 = [e for e in tps if e.tag == qn('w:p') and W(e).startswith('Sites in order of age')]
old_tbls = [e for e in body.iterchildren(qn('w:tbl'))]
for k, (lab, oldcap) in enumerate([('Table 1.', 'Table 1.'), ('Table 2.', 'Table 2.')]):
    c = para_starting(oldcap); set_caption(c, lab, W(caps[k])[len(lab):].strip())
    old = [t for t in old_tbls if t.getprevious() is not None and c in [t.getprevious(), t.getprevious().getprevious()]][0]
    new = fit_table(copy.deepcopy(tbls[k])); old.addprevious(new); drop(old)
    anchor = new
    for n in (notes1 if k == 0 else note2):
        np_ = note_para(n, c); anchor.addnext(np_); anchor = np_
    log.append(f'{lab} replaced')

# ---------------- in-text figure references ----------------
REFS = [  # (paragraph key, old, new)
 ('96.3–96.9 wt%', 'Fig. 14a', 'Fig. 5a'), ('96.3–96.9 wt%', 'Fig. 16a', 'Fig. S1a'),
 ('nal constraints on magnetic mineralogy', 'Fig.\xa06', 'Fig.\xa04d'),
 ('Representative hysteresis loops', 'Fig.\xa04)', 'Fig.\xa04a,b)'), ('Representative hysteresis loops', 'Fig.\xa05)', 'Fig.\xa04c)'),
 ('Mineral identification (SEM/EDS)', 'Fig.\xa08)', 'Fig.\xa04k,l)'),
 ('Representative demagnetization behavior', 'Figure\xa09', 'Figure\xa06'), ('Representative demagnetization behavior', 'Fig.\xa09a,b', 'Fig.\xa06a,d'),
 ('Representative demagnetization behavior', 'Fig.\xa09d,e', 'Fig.\xa06e,f'), ('Representative demagnetization behavior', 'Fig.\xa09f', 'Fig.\xa06g'),
 ('Representative demagnetization behavior', 'Fig.\xa09g', 'Fig.\xa06h'),
 ('NWF-A/NWF24-A (518', 'Fig. 9a', 'Fig. 6a'), ('WBE-A/WBE24-A (1397', 'Fig. 9b', 'Fig. 6d'), ('PKS-J/PKS24-J (601', 'Fig. 9c', 'Fig. 6b'),
 ('PKS-H/PKS24-HA+HB', 'Fig. 9f', 'Fig. 6g'), ('These polarity determinations provide', 'Figs. 10, 11', 'Figs. 6i, 7'),
 ('summarised on a single equal-area projection', 'Figure\xa012', 'Figure\xa08a'),
 ('test outcomes are shown in', 'Figure 13', 'Figure 8o–t'),
 ('have oxide totals of at least 97', 'Fig. 14a', 'Fig. 5a'), ('have oxide totals of at least 97', 'Fig. 14b–h', 'Fig. 5b–h'),
 ('have oxide totals of at least 97', 'Fig. 16a', 'Fig. S1a'),
 ('except MnO', 'Fig. 15d', 'Fig. 5l'), ('except MnO', 'Fig. 15a,b', 'Fig. 5i,j'), ('except MnO', 'Fig. 15c', 'Fig. 5k'),
 ('except MnO', 'Fig. 14e,f', 'Fig. 5f,g'), ('except MnO', 'Fig. 15e', 'Fig. 5m'),
 ('calibration-insensitive ratios', 'Fig. 16b', 'Fig. S1b'), ('calibration-insensitive ratios', 'Fig. 16c', 'Fig. S1c'),
 ('Th/Sc versus Eu/Eu*', 'Fig. 15', 'Fig. 5'),
 ('Ir is therefore', 'Fig. 17b', 'Fig. S2b'), ('Ir is therefore', 'Fig. 17a', 'Fig. S2a'),
 ('extending the three oxide analyses', '(Fig.\xa08)', '(Fig.\xa04k,l)'),
]
GEOKEYS = ('96.3–96.9', 'have oxide totals', 'except MnO', 'calibration-insensitive', 'Th/Sc versus', 'Ir is therefore')
miss = []
for key, a, b in REFS:
    if not GEO and key.startswith(GEOKEYS): continue
    p = para_containing(key); done = False
    for t in p.iter(qn('w:t')):
        if t.text and a in t.text: t.text = t.text.replace(a, b, 1); done = True; break
    (log if done else miss).append(f'{"ref" if done else "MISSED"}: {a} -> {b}  [{key[:30]}]')
# drop relationships to images no longer referenced anywhere in the document body
used = set(e.get(qn('r:embed')) for e in body.iter(qn('a:blip')))
for rId, rel in list(doc.part.rels.items()):
    if rel.reltype.endswith('/image') and rId not in used: doc.part.drop_rel(rId) if hasattr(doc.part, 'drop_rel') else None
doc.save('LEAD_4_new.docx')
print('\n'.join(log)); print('\n'.join(miss) or 'all refs replaced')
# leftover old-number references in the main text
main = []
for p in body.iterchildren(qn('w:p')):
    s = W(p)
    if s.startswith('Notebook-generated'): break
    main.append(s)
for s in main:
    for m in re.finditer(r'Fig(?:ure|s?\.)[\s\xa0]*(9|1[0-7])\b', s):
        print('LEFTOVER:', s[max(0, m.start() - 50):m.end() + 20])
