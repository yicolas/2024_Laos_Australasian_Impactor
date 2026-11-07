# -*- coding: utf-8 -*-
"""Build manuscript_LEAD_5.docx (MAPS main) + Supporting_Information_LEAD_5.docx
from the fresh manuscript_LEAD_4.docx (Nick's 8-figure scheme). Anchored on caption
and heading text, tolerant to missing pieces (warns instead of dying)."""
import copy, os, re, zipfile
import docx
from docx.shared import Inches
from lead5_content import MAIN, ABSTRACT

SRC = '/mnt/user-data/uploads/Australasian Impactor/manuscript_LEAD_4.docx'
NEWFIG = '/mnt/user-data/uploads/Plots/manuscript_figures'
WARN = []

src = docx.Document(SRC)
SP = src.paragraphs
os.makedirs('media4', exist_ok=True)
z = zipfile.ZipFile(SRC)
for nm in z.namelist():
    if nm.startswith('word/media/'):
        open('media4/' + nm.split('/')[-1], 'wb').write(z.read(nm))

def par_media(p):
    rids = p._p.xpath('.//a:blip/@*[local-name()="embed"]')
    return ['media4/' + src.part.related_parts[r].partname.split('/')[-1] for r in rids]

def find_par(prefix, start=0):
    for i in range(start, len(SP)):
        if SP[i].text.strip().startswith(prefix):
            return i
    return None

def heading_range(name):
    i = None
    for j, p in enumerate(SP):
        if p.text.strip() == name and p.style.name.startswith('Heading'):
            i = j; lvl = int(p.style.name.split()[-1]); break
    if i is None:
        return None
    for j in range(i + 1, len(SP)):
        st = SP[j].style.name
        if st.startswith('Heading') and int(st.split()[-1]) <= lvl:
            return i, j
    return i, len(SP)

def images_before(idx, lookback=9):
    out, j = [], idx - 1
    while j >= 0 and idx - j <= lookback:
        m = par_media(SP[j]); t = SP[j].text.strip()
        if m: out = m + out
        elif t: break
        j -= 1
    return out

def cap(idx):
    return re.sub(r'\s+', ' ', SP[idx].text).strip()

CAPI = {n: find_par(f'Figure {n}.') for n in range(1, 9)}
SCAPI = {k: find_par(f'Figure {k}.') for k in ('S1', 'S2')}

# ---------------- MAIN ----------------
doc = docx.Document(SRC)
body = doc.element.body
for el in list(body):
    if not el.tag.endswith('}sectPr'):
        body.remove(el)

def add(style, segments, d=doc):
    p = d.add_paragraph()
    try: p.style = style
    except Exception: pass
    for t, f in segments:
        r = p.add_run(t)
        if f and 'b' in f: r.bold = True
        if f and 'i' in f: r.italic = True
    return p

def add_pics(files, width=6.3, d=doc):
    for f in files:
        if not os.path.exists(f):
            WARN.append('missing image ' + f); continue
        p = d.add_paragraph()
        p.add_run().add_picture(f, width=Inches(width))

add('Title', [('Paleomagnetic and Geochemical Investigation of the Bolaven Plateau Volcanic '
    'Field: Testing the Australasian Impact Crater Hypothesis, Southern Laos', None)])
add('Author', [('Nicolas Anderson¹·*, Paolo Sanchez¹, Kerry Sieh², and Joseph '
    'L. Kirschvink¹  ¹Division of Geological and Planetary Sciences, California Institute '
    'of Technology, Pasadena, CA 91125, USA  ²Earth Observatory of Singapore, Nanyang '
    'Technological University, Singapore 639798  *Corresponding author: nanderson@caltech.edu', None)])
add('Abstract', [(ABSTRACT, None)])

def place_src_fig(n):
    i = CAPI.get(n)
    if i is None:
        WARN.append(f'Figure {n} caption not found in LEAD_4'); return
    add_pics(images_before(i))
    add('Body Text', [(f'Figure {n}.', 'b'), (' ' + cap(i).split('.', 1)[1].strip(), None)])

def place_table(n):
    i = find_par(f'Table {n}.')
    if i is None:
        WARN.append(f'Table {n} caption missing'); return
    add('Body Text', [(f'Table {n}.', 'b'), (' ' + cap(i).split('.', 1)[1].strip(), None)])
    body.append(copy.deepcopy(src.tables[n - 1]._tbl))
    add('Body Text', [('', None)])

# content stream: FIG keys map to source figure numbers in Nick's scheme
FIGMAP = {'fig1': 1, 'fig2': 2, 'fig3': 3, 'fig4': 4, 'fig5': None, 'fig6': 6,
          'fig7': 7, 'fig8': 8, 'fig9': None, 'fig10': 5, 'fig5g': 5}

# Reorder: Results order in content = rockmag, [geochem], magnetostrat, conglomerate.
# lead5_content MAIN still has geochem last; reorder blocks here.
H = [(i, st, seg) for i, (st, seg) in enumerate(MAIN)]
def find_h2(title):
    for i, (st, seg) in enumerate(MAIN):
        if st == 'Heading 2' and seg[0][0] == title:
            return i
    return None
i_rock = find_h2('Rock magnetism and magnetic mineralogy')
i_pol = find_h2('Polarity of dated flows and magnetostratigraphy')
i_cong = find_h2('Conglomerate tests of the diamicton boulders')
i_geo = find_h2('Tektite geochemistry')
i_disc = next(i for i, (st, seg) in enumerate(MAIN) if st == 'Heading 1' and seg[0][0] == 'Discussion')
order = (list(range(0, i_pol)) + list(range(i_geo, i_disc)) +
         list(range(i_pol, i_geo)) + list(range(i_disc, len(MAIN))))
STREAM = [MAIN[i] for i in order]

for style, payload in STREAM:
    if style == 'FIG':
        n = FIGMAP.get(payload)
        if payload in ('fig1', 'fig2', 'fig3', 'fig4'):
            k = int(payload[-1])
            png = {1: 'Fig1/Fig1_Australasian_strewn_field.png', 2: 'Fig2/Fig2_southern_Laos.png',
                   3: 'Fig3/Fig3_stratigraphy.png', 4: 'Fig4/Fig4_rock_magnetism.png'}[k]
            add_pics([f'{NEWFIG}/{png}'])
            i = CAPI.get(k)
            if i is not None:
                add('Body Text', [(f'Figure {k}.', 'b'), (' ' + cap(i).split('.', 1)[1].strip(), None)])
            else:
                WARN.append(f'caption {k} missing')
        elif payload == 'fig5':
            # SEM figure dropped from main in Nick's scheme -> skip (now Table S1/Fig S3)
            continue
        elif payload == 'fig9':
            continue  # conglomerate panels live in Fig 8o-t
        elif payload == 'fig10' or payload == 'fig5g':
            place_src_fig(5)
        elif n:
            place_src_fig(n)
    elif style == 'TABLE':
        place_table(payload)
    else:
        add(style, payload)

hr = heading_range('Acknowledgments')
add('Heading 1', [('Acknowledgments', None)])
if hr:
    ack = ' '.join(SP[j].text for j in range(hr[0] + 1, hr[1]) if SP[j].text.strip())
    ack = re.sub(r'\s*We thank the reviewers[^.]*\.', '', ack)
    add('Body Text', [(ack, None)])
add('Heading 1', [('Data Availability', None)])
add('Body Text', [('All paleomagnetic measurements and component fits are archived in the MagIC '
    'database [DOI to be inserted]. Geochemical data, the reversible-jump unmixing code and all '
    'figure-generation scripts are available at '
    'https://github.com/yicolas/2024_Laos_Australasian_Impactor [Zenodo DOI on acceptance].', None)])
hr = heading_range('References')
add('Heading 1', [('References', None)])
if hr:
    for j in range(hr[0] + 1, hr[1]):
        if SP[j].text.strip():
            add('Body Text', [(SP[j].text.strip(), None)])
doc.save('manuscript_LEAD_5.docx')

# ---------------- SI ----------------
si = docx.Document(SRC)
b2 = si.element.body
for el in list(b2):
    if not el.tag.endswith('}sectPr'):
        b2.remove(el)

def sadd(style, segments): return add(style, segments, d=si)
def sadd_pics(files, width=6.3): add_pics(files, width, d=si)

def copy_range(a, b, skip_media=True):
    for j in range(a, b):
        p = SP[j]; m = par_media(p); t = p.text.strip()
        if m and not skip_media:
            sadd_pics(m)
            if t:
                sadd('Body Text', [(t, None)])
            continue
        if m and skip_media:
            continue
        if not t:
            continue
        if skip_media and re.match(r'^Figure \d+\.', t):
            continue
        st = p.style.name
        segs = []
        if p.runs and (p.runs[0].bold or p.runs[0].italic):
            lead = p.runs[0].text.strip()
            fmt = ('b' if p.runs[0].bold else '') + ('i' if p.runs[0].italic else '')
            if lead and t.startswith(lead) and len(lead) < len(t):
                segs = [(lead, fmt), (t[len(lead):], None)]
        sadd(st, segs or [(t, None)])

sadd('Title', [('Supporting Information for “Paleomagnetic and Geochemical Investigation of '
    'the Bolaven Plateau Volcanic Field: Testing the Australasian Impact Crater Hypothesis, '
    'Southern Laos”', None)])
sadd('Author', [('Nicolas Anderson, Paolo Sanchez, Kerry Sieh, and Joseph L. Kirschvink', None)])
sadd('Body Text', [('Contents: Text S1, sedimentology and stratigraphy of the target succession; '
    'Text S2, supplementary methods; Text S3, site-by-site paleomagnetic documentation; Text S4, '
    'supplementary geochemistry; Figures S1–S3; Table S1; Figure set S4 (complete '
    'demagnetization and directional figures, A1–A62).', None)])

sadd('Heading 1', [('Text S1. Sedimentology and stratigraphy of the target succession', None)])
hr = heading_range('Sedimentology and Stratigraphy')
if hr: copy_range(hr[0] + 1, hr[1])

sadd('Heading 1', [('Text S2. Supplementary methods', None)])
for sec in ['Sample Collection and Preparation', 'Laboratory Procedures', 'Paleomagnetic Analysis',
            'Rock Magnetic Characterization', 'Microscopy and Shock Analysis', 'Geochemical Analysis']:
    hr = heading_range(sec)
    if hr:
        sadd('Heading 2', [(sec, None)])
        copy_range(hr[0] + 1, hr[1])
    else:
        WARN.append('SI methods section missing: ' + sec)

sadd('Heading 1', [('Text S3. Site-by-site paleomagnetic documentation', None)])
a = find_par('Sites with confirmed polarity matches')
b = find_par('Table 1.')
if a and b and b > a:
    sadd('Heading 2', [('Polarity localities: full demagnetization results', None)])
    copy_range(a, b)
else:
    WARN.append('polarity per-site block not located')
a = find_par('Localities passing the conglomerate test')
b = find_par('Of the six boulder localities tested')
if a and b and b > a:
    sadd('Heading 2', [('Conglomerate-test localities: full results', None)])
    copy_range(a, b)
else:
    WARN.append('conglomerate per-site block not located')
hr = heading_range('Detailed Site-by-Site Paleomagnetic Results')
if hr:
    sadd('Heading 2', [('Detailed site descriptions', None)])
    copy_range(hr[0] + 1, hr[1])

sadd('Heading 1', [('Text S4. Supplementary geochemistry and figures', None)])
for k in ('S1', 'S2'):
    i = SCAPI.get(k)
    if i is None:
        WARN.append(f'Figure {k} missing in LEAD_4'); continue
    sadd_pics(images_before(i))
    sadd('Body Text', [(f'Figure {k}.', 'b'), (' ' + cap(i).split('.', 1)[1].strip(), None)])
sem = f'{NEWFIG}/Fig4/LS-H18_Area1_BSE.png'
if os.path.exists(sem):
    sadd_pics([sem])
    sadd('Body Text', [('Figure S3.', 'b'), (' Back-scattered-electron image of fresh Bolaven '
        'basalt specimen LS-H18 (Area 1) with the analysed points of Table S1. Bright grains are '
        'Fe–Ti oxides (titanomagnetite); the groundmass is labradorite plus an Fe–Mg '
        'silicate. No exotic, shock, or metallic phases are present.', None)])
else:
    WARN.append('SEM BSE png missing')

hr = heading_range('Supplementary: SEM/EDS mineral chemistry of specimen LS-H18')
sadd('Heading 1', [('Table S1. SEM/EDS point analyses of specimen LS-H18', None)])
if hr:
    copy_range(hr[0] + 1, hr[1])
b2.append(copy.deepcopy(src.tables[2]._tbl))

hr = heading_range('Notebook-generated figures (for review)')
sadd('Heading 1', [('Figure set S4. Complete demagnetization, directional and VGP figures '
    '(A1–A62)', None)])
if hr:
    copy_range(hr[0] + 1, hr[1], skip_media=False)

si.save('Supporting_Information_LEAD_5.docx')
print('WARNINGS:'); [print(' -', w) for w in WARN] or print(' none')
print('built both docs')
