"""Third push into LEAD_4: Fig 3 with field photos (d-h), Fig 2 legend fix, Fig 1 caption citations,
restyled S1-S4, new S17 (PKS-F lines-and-planes). Usage: python push3.py in.docx out.docx"""
import sys, re, copy
from docx import Document
from docx.oxml.ns import qn
from PIL import Image
IN, OUTF = sys.argv[1], sys.argv[2]
doc = Document(IN); body = doc.element.body
W = lambda e: ''.join(t.text or '' for t in e.iter(qn('w:t')))
N = lambda s: s.replace('\xa0', ' ')
log = []
def paras(): return list(body.iterchildren(qn('w:p')))
def para_starting(s):
    h = [p for p in paras() if N(W(p)).startswith(s)]; assert len(h) == 1, (s, len(h)); return h[0]
def para_containing(s):
    h = [p for p in paras() if s in N(W(p))]; assert h, s; return h[0]
def has_img(p): return bool(list(p.iter(qn('a:blip'))))
def prev_img(p):
    q = p.getprevious()
    while q is not None and not has_img(q): q = q.getprevious()
    return q
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
def md(path, label):
    t = open(path).read(); s = t.split('**' + label + '**')[1]; s = re.split(r'\n## |\nScript:', s)[0]
    return re.sub(r'\s+', ' ', re.sub(r'\*\*', '', s)).strip()
O = '/mnt/user-data/outputs/'
for lab, png, cap in [('Figure 1.', None, md(O + 'Fig1/Fig1_caption.md', 'Figure 1.')),
                      ('Figure 2.', 'Fig2.png', None), ('Figure 3.', 'Fig3.png', md(O + 'Fig3/Fig3_caption.md', 'Figure 3.'))]:
    c = para_starting(lab)
    if png: set_image(prev_img(c), png)
    if cap: set_caption(c, lab, cap)
    log.append(f'{lab} updated')
S2 = ("Additional rock magnetism from the 2G RAPID sequences (Code/figS: make_figS_rockmag.py). Colours are sites. (a) AF demagnetization of the NRM to 94 mT "
      "(PKQ-A specimens, pale, were measured for the NRM only). (b) IRM acquisition to 1 T, normalised to the SIRM; most of the IRM is acquired by ~100–200 mT, "
      "as expected for (titano)magnetite-family carriers. (c) ARM acquisition in a 100 mT AF with a 0–1 mT DC bias, normalised to the SIRM. (d) AF demagnetization "
      "of the ARM (dashed) and the SIRM (solid). (e) Median destructive fields (MDF) of NRM, ARM and SIRM; arrows mark NRMs that retain more than half their "
      "intensity at 94 mT (AF-hard). (f) ARM/SIRM (a grain-size proxy; higher = finer) against NRM/SIRM. NWF-A-2E is omitted: its moments after the NRM step "
      "are at holder-noise level. Where a specimen was run more than once, the NRM is taken from the first run and the laboratory remanences from the last, complete run.")
S3 = ("AF demagnetization paths of the NRM in geographic coordinates (rotated with the corrected sample orientations), coloured by AF peak field (0–94 mT); "
      "filled = lower, open = upper hemisphere. Purple squares are thermal HT (ChRM) means of the same core (Fig. 7) where available; stars are the GAD "
      "directions. The PKQ-A specimens (measured in 2024) and PKS-J-3A, PKS-F-4A and PKS-F-8H decay along coherent paths, and PKQ-A-0H, -2M, -3H and -9I "
      "converge on the thermal HT direction. The NWF-B, NWF-C, PKS-G and WBE-A specimens (measured on the sample changer in 2025–26) give declinations that "
      "wander along small circles at near-constant inclination from step to step, as expected if the specimen rotated in its holder between measurements; "
      "their AF directions are not interpreted.")
S17 = ("PKS-F conglomerate test with lines only and with lines plus planes (McFadden & McElhinny, 1988; mcfadden_gc_check.py). (a) Boulder-mean HT directions "
       "from HT fits with MAD ≤ 15° (as in Fig. 7r): R = 5.31 against Ro95 = 5.28. (b) Specimens that do not isolate a stable endpoint by 450–510 °C, mostly "
       "in boulders 3 and 4, are re-expressed as remagnetization circles (orange; poles rotated to geographic with each specimen's own component fits) and "
       "combined with the resolved lines. Arrows run from the line-only to the lines-plus-planes boulder means; both move toward the northerly, shallow "
       "cluster, R rises to 6.09 and the population is clustered under either treatment. (c) Lines-plus-planes boulder means.")
for lab, png, cap in [('Figure S1.', 'S1.png', None), ('Figure S2.', 'S2.png', S2), ('Figure S3.', 'S3.png', S3), ('Figure S4.', 'S4.png', None)]:
    c = para_starting(lab); set_image(prev_img(c), png)
    if cap: set_caption(c, lab, cap)
    log.append(f'{lab} replaced')
c16 = para_starting('Figure S16.'); im = copy.deepcopy(prev_img(c16)); set_image(im, 'S17.png')
c17 = copy.deepcopy(c16); set_caption(c17, 'Figure S17.', S17); c16.addnext(im); im.addnext(c17); log.append('Figure S17 added')
p = para_containing('Specimens were averaged to their parent boulders')
ts = [t for t in p.iter(qn('w:t')) if t.text]; ts[-1].text = ts[-1].text.rstrip() + ' The PKS-F comparison is shown in Fig. S17.'
log.append('S17 cited')
used = set(e.get(qn('r:embed')) for e in body.iter(qn('a:blip')))
for rId, rel in list(doc.part.rels.items()):
    if rel.reltype.endswith('/image') and rId not in used: doc.part.drop_rel(rId)
doc.save(OUTF); print('\n'.join(log))
