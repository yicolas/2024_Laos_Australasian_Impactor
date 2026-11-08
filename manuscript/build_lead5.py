# -*- coding: utf-8 -*-
"""Build manuscript_LEAD_5.docx (MAPS main) + Supporting_Information_LEAD_5.docx from the FINAL
manuscript_LEAD_4.docx (7 main figures, Tables 1-3, embedded Supplementary Figs S1-S17 and
Tables S1-S5). Anchored on caption/heading text; warns instead of dying."""
import copy, os, re, zipfile
import docx
from docx.shared import Inches
from lead5_content import MAIN, ABSTRACT

SRC = '/home/claude/manuscript_work/manuscript_LEAD_4.docx'
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

def images_before(idx, lookback=6):
    out, j = [], idx - 1
    while j >= 0 and idx - j <= lookback:
        m = par_media(SP[j]); t = SP[j].text.strip()
        if m: out = m + out
        elif t: break
        j -= 1
    return out

def cap(idx): return re.sub(r'\s+', ' ', SP[idx].text).strip()

# ---------------- MAIN ----------------
doc = docx.Document(SRC)
body = doc.element.body
for el in list(body):
    if not el.tag.endswith('}sectPr'):
        body.remove(el)


def append_el(el, d):
    b = d.element.body
    sect = None
    for ch in b:
        if ch.tag.endswith('}sectPr'):
            sect = ch
    if sect is not None:
        sect.addprevious(el)
    else:
        b.append(el)

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
        d.add_paragraph().add_run().add_picture(f, width=Inches(width))

add('Title', [('Paleomagnetic and Geochemical Investigation of the Bolaven Plateau Volcanic '
    'Field: Testing the Australasian Impact Crater Hypothesis, Southern Laos', None)])
add('Author', [('Nicolas Anderson¹·*, Paolo Sanchez¹, Kerry Sieh², and Joseph '
    'L. Kirschvink¹  ¹Division of Geological and Planetary Sciences, California Institute '
    'of Technology, Pasadena, CA 91125, USA  ²Earth Observatory of Singapore, Nanyang '
    'Technological University, Singapore 639798  *Corresponding author: nanderson@caltech.edu', None)])
add('Abstract', [(ABSTRACT, None)])

def place_src_fig(n):
    i = find_par(f'Figure {n}.')
    if i is None:
        WARN.append(f'Figure {n} caption missing'); return
    add_pics(images_before(i))
    add('Body Text', [(f'Figure {n}.', 'b'), (' ' + cap(i).split('.', 1)[1].strip(), None)])

def place_table(n):
    i = find_par(f'Table {n}.')
    if i is None:
        WARN.append(f'Table {n} caption missing'); return
    add('Body Text', [(f'Table {n}.', 'b'), (' ' + cap(i).split('.', 1)[1].strip(), None)])
    append_el(copy.deepcopy(src.tables[n - 1]._tbl), doc)
    add('Body Text', [('', None)])

# content FIG keys -> final LEAD_4 figure numbers (None = skip)
FIGMAP = {'fig1': 1, 'fig2': 2, 'fig3': 3, 'fig4': 4, 'fig5': None, 'fig6': 6,
          'fig7': None, 'fig8': 7, 'fig9': 'T3', 'fig10': 5}

# Results order: rockmag -> geochem -> magnetostrat -> conglomerate (matches LEAD_4)
def find_h2(title):
    for i, (st, seg) in enumerate(MAIN):
        if st == 'Heading 2' and seg[0][0] == title:
            return i
    return None
i_pol = find_h2('Polarity of dated flows and magnetostratigraphy')
i_geo = find_h2('Tektite geochemistry')
i_disc = next(i for i, (st, seg) in enumerate(MAIN) if st == 'Heading 1' and seg[0][0] == 'Discussion')
order = (list(range(0, i_pol)) + list(range(i_geo, i_disc)) +
         list(range(i_pol, i_geo)) + list(range(i_disc, len(MAIN))))

for style, payload in [MAIN[i] for i in order]:
    if style == 'FIG':
        m = FIGMAP.get(payload)
        if m == 'T3':
            place_table(3)
        elif m:
            place_src_fig(m)
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

def copy_range(a, b, skip_media=True, skip_caps=True):
    for j in range(a, b):
        p = SP[j]; m = par_media(p); t = p.text.strip()
        if m and skip_media:
            continue
        if m and not skip_media:
            sadd_pics(m)
            if t: sadd('Body Text', [(t, None)])
            continue
        if not t:
            continue
        if skip_caps and re.match(r'^(Figure|Table) \d+\.', t):
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
    'Text S2, supplementary methods; Text S3, site-by-site paleomagnetic documentation; Figures '
    'S1–S17; Tables S1–S5.', None)])

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

# Supplementary figures S1-S16: copy images + captions verbatim
hr = heading_range('Supplementary figures')
sadd('Heading 1', [('Supplementary Figures', None)])
if hr:
    copy_range(hr[0] + 1, hr[1], skip_media=False, skip_caps=False)
else:
    WARN.append('Supplementary figures section missing')

# Supplementary tables S1-S5: captions + table elements in order
hr = heading_range('Supplementary tables')
sadd('Heading 1', [('Supplementary Tables', None)])
if hr:
    tbl_idx = 3  # tables[3..7] follow main Tables 1-3 in document order
    for j in range(hr[0] + 1, hr[1]):
        t = SP[j].text.strip()
        if not t: continue
        mcap = re.match(r'^(Table S\d+\.)', t)
        if mcap:
            lead = mcap.group(1)
            sadd('Body Text', [(lead, 'b'), (' ' + t[len(lead):].strip(), None)])
            if tbl_idx < len(src.tables):
                append_el(copy.deepcopy(src.tables[tbl_idx]._tbl), si)
                sadd('Body Text', [('', None)])
                tbl_idx += 1
        else:
            sadd('Body Text', [(t, None)])
else:
    WARN.append('Supplementary tables section missing')

si.save('Supporting_Information_LEAD_5.docx')
print('WARNINGS:'); [print(' -', w) for w in WARN] or print(' none')
print('built both docs')
