"""Write manuscript_LEAD_4.docx from LEAD_3: replace geochemistry Methods/Results, figures 14-17, drop Fig 18,
fix geochemistry statements in Abstract/Discussion/Conclusions, add references."""
import os
import copy, sys, docx, struct
from docx.shared import Emu
from text_methods import M61, M62
from text_results import RESULTS, ABSTRACT_OLD, ABSTRACT_NEW, EDITS, REFS_ADD, REF_REPLACE

SRC = os.environ.get("LEAD3_DOCX", os.path.expanduser("~/Library/Mobile Documents/com~apple~CloudDocs/Caltech Projects/Australasian Impactor/manuscript_LEAD_3.docx"))
DST = os.path.join(os.path.dirname(os.path.abspath(__file__)), "out", "manuscript_LEAD_4.docx")   # archival: the LEAD_4 master has since been edited by hand
FIG = {14: 'Fig14_EPMA_QC_Harker.png', 15: 'Fig15_rjMCMC.png', 16: 'Fig16_trace.png', 17: 'Fig17_PGE_Pd_Ir.png'}
A = '{http://schemas.openxmlformats.org/drawingml/2006/main}'
WP = '{http://schemas.openxmlformats.org/drawingml/2006/wordprocessingDrawing}'
R = '{http://schemas.openxmlformats.org/officeDocument/2006/relationships}embed'

def set_runs(p, runs):
    for r in list(p.runs): r._r.getparent().remove(r._r)
    for item in runs:
        text, bold = (item, None) if isinstance(item, str) else item
        if text: rr = p.add_run(text); rr.bold = bold or None

def png_size(path):
    with open(path, 'rb') as f: f.read(16); w, h = struct.unpack('>II', f.read(8))
    return w, h

def swap_image(d, p, path):
    blip = p._p.find('.//'+A+'blip'); part = d.part.related_parts[blip.get(R)]
    part._blob = open(path, 'rb').read()
    w, h = png_size(path)
    for ext in p._p.iter(WP+'extent'):
        cx = int(ext.get('cx')); ext.set('cy', str(int(cx*h/w)))
    for ext in p._p.iter(A+'ext'):
        if ext.get('cx'): cx = int(ext.get('cx')); ext.set('cy', str(int(cx*h/w)))

def find(d, start):
    for i, p in enumerate(d.paragraphs):
        if p.text.strip().startswith(start): return i
    raise KeyError(start)

def replace_in_par(p, old, new):
    t = p.text
    if old not in t: raise KeyError(old[:60])
    bold_lead = p.runs[0].bold if p.runs else None
    set_runs(p, [(t.replace(old, new), None)])

def main():
    d = docx.Document(SRC); P = d.paragraphs
    # ---- Methods (Geochemical Analysis heading followed by two paragraphs)
    i = find(d, 'Geochemical Analysis'); set_runs(P[i+1], M61[1:]); set_runs(P[i+2], M62[1:])
    # ---- Results block
    h = find(d, 'Geochemistry: Testing the Bolaven Source Hypothesis'); disc = find(d, 'Discussion')
    block = P[h+1:disc]
    imgs = [p for p in block if p._p.findall('.//'+A+'blip')]
    assert len(imgs) == 5, len(imgs)
    for p in block:
        if p not in imgs[:4]: p._p.getparent().remove(p._p)
    imgs[4]._p.getparent().remove(imgs[4]._p) if imgs[4]._p.getparent() is not None else None
    for n, p in zip([14, 15, 16, 17], imgs[:4]): swap_image(d, p, os.path.join(os.path.dirname(os.path.abspath(__file__)), 'figures', FIG[n]))
    anchors = {14: imgs[0], 15: imgs[1], 16: imgs[2], 17: imgs[3]}
    disc_p = d.paragraphs[find(d, 'Discussion')]
    body_style = 'Body Text'
    for item in RESULTS:
        kind = item[0]
        if kind == 'before':           # paragraph placed before figure n's image
            _, n, runs = item; q = anchors[n].insert_paragraph_before('', style=body_style); set_runs(q, runs)
        elif kind == 'caption':        # caption placed after figure n's image
            _, n, runs = item
            nxt = anchors[n]._p.getnext()
            from docx.text.paragraph import Paragraph
            q = Paragraph(nxt, anchors[n]._parent).insert_paragraph_before('', style=body_style) if nxt is not None else None
            set_runs(q, runs)
        elif kind == 'end':
            _, runs = item; q = disc_p.insert_paragraph_before('', style=body_style); set_runs(q, runs)
    # first paragraph after heading gets 'First Paragraph' style
    P = d.paragraphs; h = find(d, 'Geochemistry: Testing the Bolaven Source Hypothesis'); P[h+1].style = d.styles['First Paragraph']
    # ---- Abstract and other in-place edits
    pa = d.paragraphs[find(d, ABSTRACT_OLD[0])]; t = pa.text; k = t.index('A parallel geochemical test')
    set_runs(pa, [(t[:k] + ABSTRACT_NEW, None)])
    for start, old, new in EDITS:
        p = d.paragraphs[find(d, start)]; replace_in_par(p, old, new)
    # ---- References
    P = d.paragraphs
    for start, new in REF_REPLACE:
        set_runs(P[find(d, start)], [(new, None)])
    for before, text in REFS_ADD:
        q = d.paragraphs[find(d, before)].insert_paragraph_before('', style='Body Text'); set_runs(q, [(text, None)])
    d.save(DST); print('saved', DST)

if __name__ == '__main__':
    main()
