# -*- coding: utf-8 -*-
"""Push 5 into LEAD_4: MAPS-style citations + rebuilt reference list; sample counts (12 sites,
57 cores/blocks, 364 specimens); annotated field photos as Fig. S18. Usage: python push5.py in.docx out.docx"""
import sys, re, copy
from docx import Document
from docx.oxml.ns import qn
from PIL import Image
sys.path.insert(0, '/home/claude/r5')
from cite_style import convert, COMMA, AMP
from refs_maps import REFS
IN, OUTF = sys.argv[1], sys.argv[2]
doc = Document(IN); body = doc.element.body
W = lambda e: ''.join(t.text or '' for t in e.iter(qn('w:t')))
log = []
paras = lambda: list(body.iter(qn('w:p')))

# ---------- locate reference block ----------
P = doc.paragraphs
i_ref = next(k for k, p in enumerate(P) if p.text.strip() == 'References' and p.style.name.startswith('Heading'))
i_end = next(k for k in range(i_ref + 1, len(P)) if P[k].style.name.startswith('Heading'))
ref_ps = [P[k]._p for k in range(i_ref + 1, i_end)]
ref_set = set(id(x) for x in ref_ps)

# ---------- 1. in-text citations ----------
changed = []
for p in paras():
    if id(p) in ref_set: continue
    before = W(p)
    for t in p.iter(qn('w:t')):
        if t.text:
            nt = convert(t.text)
            if nt != t.text: t.text = nt
    after = W(p)
    if after != before: changed.append((before, after))
    # split-run leftovers
    left = [m.group(0) for m in COMMA.finditer(convert(after)) if convert(after) != after] + [m.group(0) for m in AMP.finditer(after)]
    if convert(after) != after: log.append('SPLIT-RUN leftover: ' + after[:160])
log.append(f'citations restyled in {len(changed)} paragraphs')

# ---------- 2. sample counts ----------
def para_containing(s):
    h = [p for p in paras() if s in W(p)]; assert len(h) >= 1, s; return h[0]
def set_text(p, txt):
    ts = [t for t in p.iter(qn('w:t'))]
    ts[0].text = txt; ts[0].set('{http://www.w3.org/XML/1998/namespace}space', 'preserve')
    for t in ts[1:]: t.text = ''
def replace_in(p, a, b):
    full = W(p); assert a in full, a
    set_text(p, full.replace(a, b))
p = para_containing('analyzing approximately 80 drill core and block samples from 16 localities')
replace_in(p, 'analyzing approximately 80 drill core and block samples from 16 localities across southern Laos',
           'analyzing 57 oriented drill cores and blocks (364 specimens) from 12 sites across the plateau')
p = para_containing('We collected approximately 80 oriented drill core and block samples')
old = W(p)
new = re.sub(r'We collected approximately 80 .*$',
    'We collected 57 oriented drill cores and block samples (364 specimens) at 12 sites across the Bolaven Plateau volcanic '
    'field (Table S1). Seven sites are in dated basalt flows, for magnetostratigraphy (NWF-A, PKS-B, PKS-H, PKS-I, PKS-J, '
    'PKS-K and WBE-A; PKS-I proved to be a displaced corestone), and five are boulder or block populations in the proposed '
    'proximal ejecta deposits, for conglomerate tests (NWF-B, NWF-C, PKQ-A, PKS-F and PKS-G); the three PKS-H cores were '
    'also tested as a conglomerate.', old)
set_text(p, new); log.append('Methods + abstract counts updated')

# ---------- 3. reference list ----------
tmpl = ref_ps[0]
anchor = ref_ps[-1]
new_ps = []
for a, t, j, v in REFS:
    np_ = copy.deepcopy(tmpl)
    rpr = None
    for r in np_.iter(qn('w:r')):
        rp = r.find(qn('w:rPr'))
        if rp is not None: rpr = copy.deepcopy(rp)
        break
    for ch in list(np_):
        if ch.tag != qn('w:pPr'): np_.remove(ch)
    for txt, ital in [(a + t, False), (j, True), (v, False)]:
        if not txt: continue
        r = np_.makeelement(qn('w:r'), {})
        rp = copy.deepcopy(rpr) if rpr is not None else r.makeelement(qn('w:rPr'), {})
        for tag in ('w:i', 'w:b'):
            e = rp.find(qn(tag))
            if e is not None: rp.remove(e)
        if ital: rp.append(rp.makeelement(qn('w:i'), {}))
        r.append(rp); te = r.makeelement(qn('w:t'), {}); te.text = txt
        te.set('{http://www.w3.org/XML/1998/namespace}space', 'preserve'); r.append(te); np_.append(r)
    new_ps.append(np_)
for np_ in new_ps: anchor.addnext(np_); anchor = np_
for op in ref_ps: op.getparent().remove(op)
log.append(f'reference list rebuilt: {len(ref_ps)} -> {len(REFS)} entries')

# ---------- 4. Fig. S18 annotated photos ----------
def para_starting(s):
    h = [p for p in paras() if W(p).replace('\xa0', ' ').startswith(s)]; assert len(h) == 1, (s, len(h)); return h[0]
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
    for e in p.iter(qn('wp:docPr')): e.set('id', str(abs(hash(png)) % 10 ** 8))
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
        if bold and b is None: rp.insert(0, rp.makeelement(qn('w:b'), {}))
        if not bold and b is not None: rp.remove(b)
        r.append(rp); t = r.makeelement(qn('w:t'), {}); t.text = txt
        t.set('{http://www.w3.org/XML/1998/namespace}space', 'preserve'); r.append(t); p.append(r)
S18 = ('Annotated field photographs of two diamicton exposures (re-drawn from the field annotations; site identifications '
       'to be confirmed). (a) Road cut through the boulder-bearing pebbly diamicton beneath the catastro-loess silt; the dashed '
       'line marks the irregular silt–diamicton contact, and P1–P8 are the eight basalt boulders sampled for the conglomerate '
       'test. People for scale. (b) Section showing sandy silt (AA1) over pebbly diamicton (AA2) with a brecciated quartz vein '
       'below.')
if 'Figure S18.' not in W(body):
    c17 = para_starting('Figure S17.'); im = copy.deepcopy(prev_img(c17))
    set_image(im, '/home/claude/r5/FigS18_field_photos.jpg')
    c18 = copy.deepcopy(c17); set_caption(c18, 'Figure S18.', S18)
    c17.addnext(im); im.addnext(c18); log.append('Figure S18 added')
    c3 = para_starting('Figure 3.')
    ts = [t for t in c3.iter(qn('w:t')) if t.text]
    ts[-1].text = ts[-1].text.rstrip() + ' Annotated outcrop views of two diamicton exposures are given in Fig. S18.'
    log.append('Fig 3 caption points to S18')

used = set(e.get(qn('r:embed')) for e in body.iter(qn('a:blip')))
for rId, rel in list(doc.part.rels.items()):
    if rel.reltype.endswith('/image') and rId not in used: doc.part.drop_rel(rId)
doc.save(OUTF)
print('\n'.join(log))
import json; json.dump(changed, open('/home/claude/r5/cite_changes.json', 'w'), ensure_ascii=False, indent=0)
