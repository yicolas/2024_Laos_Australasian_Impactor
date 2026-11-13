# -*- coding: utf-8 -*-
"""Push 6: metatuff dropped from the rjMCMC dictionary (2026-11-13). Replace Fig 5 and Fig S1 images, rewrite every
geochem number/sentence in LEAD_4 and rebuild Table S5 from summary.json. Also patches lead5_content.py.
Usage: python push6_geochem.py in.docx out.docx summary.json fig5.png figS1.png lead5_content.py"""
import sys, json, copy
from docx import Document
from docx.oxml.ns import qn
from PIL import Image
IN, OUTF, SJ, F5, FS1, L5 = sys.argv[1:7]
R = json.load(open(SJ))
doc = Document(IN); body = doc.element.body
W = lambda e: ''.join(t.text or '' for t in e.iter(qn('w:t')))
log = []
def paras(): return list(body.iter(qn('w:p')))
def one(s):
    h = [p for p in paras() if s in W(p)]; assert len(h) == 1, (s[:50], len(h)); return h[0]
def rep(key, a, b):
    """replace a->b inside the paragraph containing key; text may span runs -> rewrite into first run of match area"""
    p = one(key); ts = [t for t in p.iter(qn('w:t'))]
    full = ''.join(t.text or '' for t in ts); assert a in full, ('missing', a[:60])
    i = full.index(a); j = i + len(a)
    # locate runs spanning [i,j)
    pos = 0; first = None
    for t in ts:
        L = len(t.text or ''); s, e = pos, pos + L
        if first is None and e > i:
            first = t; off = i - s
            t.text = (t.text or '')[:off] + b + (t.text or '')[min(L, off + (j - i)):] if e >= j else (t.text or '')[:off] + b
            t.set('{http://www.w3.org/XML/1998/namespace}space', 'preserve')
        elif first is not None and s < j:
            cut = j - s
            t.text = (t.text or '')[cut:] if cut < L else ''
        pos = e
    assert b in W(p); log.append('ok: ' + a[:50])

# ---- Methods ----
rep('felsic metatuff (8; dacitic', ', Bolaven loess (13; grouped here with the diamicton) and felsic metatuff (8; dacitic–rhyolitic, Na2O 2.6–5.7 and K2O 3.0–5.5 wt%, major elements only). Three further samples labelled metatuff in the compilation were excluded: two are altered mafic rocks (SiO2 43–57 wt%, LOI 8–9 wt%) and one is Na-leached (Na2O 0.01 wt%). The field context of the metatuff (unit, and whether it lies beneath the Khorat Group) is not documented in the compilation.',
    ' and Bolaven loess (13; grouped here with the diamicton). The eleven samples labelled metatuff in the compilation were not used. Eight are felsic (dacitic–rhyolitic) volcanic rocks with major elements only and three are altered or Na-leached; those with recorded locations come from south of the plateau (the Mekong at Don Khau Island and the plateau’s southern flank), where Triassic rhyolite, dacite and tuff of the pre-Khorat basement crop out. At the proposed crater such rocks lie beneath at least 500 m of Khorat Group and are not plausible contributors to near-surface tektite melt. In a test run that included them, the felsic metatuff took a posterior composition close to that of the tektites themselves without improving the fit.')
rep('The dictionary comprises the eight regional', 'the eight regional lithology types', 'the seven regional lithology types')
# ---- Fig 5 caption ----
rep('Major-element composition of Laos and Thailand tektites', 'tholeiite and alkali basalt and the metatuff restricted to felsic samples, and', 'tholeiite and alkali basalt, and')
# ---- Results: unmixing paragraph (full rewrite) ----
m = R['main']['summ']; nr = R['no_random']['summ']; na = R['no_alkali']['summ']; lo = R['local_only']['summ']
f = lambda d, k: f"{d[k]['mean']:.0f} ± {d[k]['sd']:.0f}"
ll = list(R['main']['chain_ll'].values()); K = [int(k) for k in R['main']['K']]
weath = ['Lateritic saprolite', 'Sedimentary laterite', 'Diamicton / "catastro-loess"']
wsum = sum(m[k]['mean'] for k in weath); wmax = max(m[k]['p_present'] for k in weath)
cr = dict(zip(R['main']['comp']['Random'] and ['SiO2','TiO2','Al2O3','FeOt','MnO','MgO','CaO','Na2O','K2O'], R['main']['comp']['Random']))
U = ('Bayesian unmixing. All twelve chains reproduce the 82 accepted analyses equally well (median log-likelihoods '
     f'−{-min(ll):.0f} to −{-max(ll):.0f}; interquartile per-analysis residuals within ±3 % for every oxide except MnO; Fig. 5l), but they do so '
     f'with between {min(K)} and {max(K)} components, so the number of components is not constrained by the data (Fig. 5i,j). What is '
     'reproducible among chains is the type of material required (Fig. 5k). (1) The deeply weathered lithologies that now cover the '
     'plateau – lateritic saprolite on basalt, sedimentary laterite and bauxite, and the tektite-hosting diamicton or “loess” – are '
     f'not required (combined weight {wsum:.1f} %, present in at most {100*wmax:.0f} % of posterior samples). (2) A quartz-rich sand '
     f'classified as Khorat sandstone ({f(m,"Khorat sandstone")} %) is present in {100*m["Khorat sandstone"]["p_present"]:.0f} % of samples. (3) The remainder must be '
     'fine-grained, aluminous and unleached, carrying ~1.5–2 wt% each of CaO and Na2O. No sampled Khorat sediment supplies this, because '
     'all are intensely leached (median CaO ≤ 0.04 and Na2O ≤ 0.15 wt%; Fig. 5f,g), so the model assigns it to unweathered shale '
     f'(PAAS; {f(m,"Unweathered shale (PAAS)")} %) and to the unconstrained “random” component ({f(m,"Random")} %), whose posterior '
     f'composition (~{cr["SiO2"]:.0f} wt% SiO2, {cr["Al2O3"]:.0f} % Al2O3, {cr["CaO"]:.1f} % CaO, {cr["Na2O"]:.1f} % Na2O, {cr["K2O"]:.1f} % K2O) '
     'resembles unweathered greywacke or average upper crust. Neither is an identified source rock: PAAS is a global average, and the '
     'size of the random component shows that the dictionary does not contain an adequate parent. Khorat mudstone, leached like the '
     f'sandstone, is scarcely used ({m["Khorat mudstone"]["mean"]:.1f} %). (4) A Ca–Mg-rich component is permitted but not required: '
     f'Bolaven basalt contributes {m["All basalt"]["mean"]:.1f} ± {m["All basalt"]["sd"]:.1f} % (tholeiite {m["Bolaven tholeiite"]["mean"]:.1f} %, '
     f'alkali basalt {m["Bolaven alkali basalt"]["mean"]:.1f} %; present in {100*m["All basalt"]["p_present"]:.0f} % of samples). The basalt and '
     f'random components trade off: without the random component, basalt rises to {f(nr,"All basalt")} % (tholeiite '
     f'{nr["Bolaven tholeiite"]["mean"]:.0f} %, alkali basalt {nr["Bolaven alkali basalt"]["mean"]:.0f} %) and becomes required, and Khorat '
     f'mudstone ({nr["Khorat mudstone"]["mean"]:.0f} %) takes the place of the unleached fine fraction. The other sensitivity runs '
     f'(Fig. 5m; Table S5) give, with Na2O and K2O excluded, sandstone {na["Khorat sandstone"]["mean"]:.0f} %, unweathered shale '
     f'{na["Unweathered shale (PAAS)"]["mean"]:.0f} %, random {na["Random"]["mean"]:.0f} % and basalt {f(na,"All basalt")} %; and with only the '
     f'regional lithologies (no PAAS or random component), mudstone {lo["Khorat mudstone"]["mean"]:.0f} %, sandstone '
     f'{lo["Khorat sandstone"]["mean"]:.0f} % and basalt {lo["All basalt"]["mean"]:.0f} ± {lo["All basalt"]["sd"]:.0f} % (required). Lateritic '
     'saprolite is never used. The felsic metatuff of the regional compilation is not in the dictionary (Methods); including it does '
     'not improve the fit. The unmixing therefore supports a sediment-dominated parent, in agreement with earlier work, but shows that '
     'the tektites cannot be melts of the Khorat sediments and regolith as they are exposed today. A less-weathered equivalent – fresh '
     'Khorat mudstone at depth, or the unweathered sediment that preceded the Pleistocene laterite – would be required, and no such '
     'material has yet been analysed.')
p = one('Bayesian unmixing. All twelve chains'); ts = list(p.iter(qn('w:t')))
lead = ts[0].text if ts[0].text and ts[0].text.strip().startswith('Bayesian unmixing') and len(ts[0].text) < 30 else None
if lead:
    ts[1].text = U[len(lead):]; [setattr(t, 'text', '') for t in ts[2:]]
else:
    ts[0].text = U; [setattr(t, 'text', '') for t in ts[1:]]
for t in ts: t.set('{http://www.w3.org/XML/1998/namespace}space', 'preserve')
log.append('unmixing paragraph rewritten')
# ---- trace paragraph ----
mt = R['mix_traces']
rep('Trace elements. On the chondrite', 'The felsic metatuff has no trace-element analyses and is omitted from the following prediction. ', '')
rep('Trace elements. On the chondrite', 'predict Eu/Eu* = 0.59–0.71 (90 % range), consistent with the tektites, and Th/Sc = 0.73–1.42, which brackets the observed values but is mostly lower (median 0.95)',
    f'predict Eu/Eu* = {mt["Eu/Eu*"][0]:.2f}–{mt["Eu/Eu*"][2]:.2f} (90 % range), consistent with the tektites, and Th/Sc = {mt["Th/Sc"][0]:.2f}–{mt["Th/Sc"][2]:.2f} (median {mt["Th/Sc"][1]:.2f}), at or below the low end of the observed values')
rep('Trace elements. On the chondrite', '(predicted 151 and 9 µg/g', f'(predicted {mt["Zr"][1]:.0f} and {mt["Th"][1]:.0f} µg/g')
# ---- summary, discussion, abstract ----
bm = m['All basalt']['mean']; hi = max(nr['All basalt']['mean'], lo['All basalt']['mean'])
RANGE = f'about {bm:.0f}–{hi:.0f} %'
rep('Summary. Within the limits of the data', 'a basaltic contribution of about 5–20 % is permitted, depending on the model variant;',
    f'a basaltic contribution of {RANGE} is permitted, depending on the model variant ({bm:.1f} ± {m["All basalt"]["sd"]:.1f} % in the full model);')
rep('This is compatible with the proposed incorporation', '(about 5 %, at most ~10–20 %)',
    f'(about {bm:.0f} % in the full model, up to ~{hi:.0f} % in restricted variants, and capped at ~10–20 % by trace-element ratios)')
rep('A parallel geochemical test points the same way', 'A basaltic contribution of about 5–20 % is permitted', f'A basaltic contribution of {RANGE} is permitted')
# ---- S1 caption ----
rep('Figure S1. Trace elements of tektites', 'source lithologies (stars; the felsic metatuff has no trace-element data) and the bulk posterior mixtures of Fig. 5 (green; metatuff omitted).',
    'source lithologies (stars) and the bulk posterior mixtures of Fig. 5 (green).')
# ---- Table S5 caption + table ----
rep('Table S5. Posterior mixing weights', '"Excluded" marks types removed from the dictionary in that run.',
    '"Excluded" marks types removed from the dictionary in that run. The felsic metatuff of the regional compilation is not included (Methods).')
cap = one('Table S5. Posterior mixing weights'); tbl = cap.getnext()
while tbl is not None and tbl.tag != qn('w:tbl'): tbl = tbl.getnext()
from docx.table import Table
T = Table(tbl, doc._body)
ROWS = [('Khorat sandstone', 'Khorat sandstone'), ('Khorat mudstone', 'Khorat mudstone'), ('Unweathered shale (PAAS)', 'Unweathered shale (PAAS)'),
        ('Bolaven tholeiite', 'Bolaven tholeiite'), ('Bolaven alkali basalt', 'Bolaven alkali basalt'), ('All basalt (sum)', 'All basalt'),
        ('Lateritic saprolite', 'Lateritic saprolite'), ('Sedimentary laterite / bauxite', 'Sedimentary laterite'),
        ('Diamicton / loess', 'Diamicton / "catastro-loess"'), ('Random (unconstrained)', 'Random')]
runs = ['main', 'no_random', 'no_alkali', 'local_only']
def setcell(c, txt):
    ts = [t for t in c._tc.iter(qn('w:t'))]
    ts[0].text = txt; [setattr(t, 'text', '') for t in ts[1:]]
for r in list(T.rows):
    if r.cells[0].text.strip() == 'Felsic metatuff': r._tr.getparent().remove(r._tr); log.append('metatuff row removed')
for r in T.rows[1:]:
    lab = r.cells[0].text.strip(); key = dict(ROWS).get(lab)
    assert key, lab
    for j, run in enumerate(runs):
        d = R[run]['summ'].get(key)
        setcell(r.cells[j + 1], 'excluded' if d is None else f"{d['mean']:.1f} ± {d['sd']:.1f} ({100*d['p_present']:.0f})")
log.append('Table S5 rebuilt')
# ---- images ----
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
for key, png in [('Major-element composition of Laos and Thailand tektites', F5), ('Figure S1. Trace elements of tektites', FS1)]:
    set_image(prev_img(one(key)), png); log.append('image ' + png.split('/')[-1])
used = set(e.get(qn('r:embed')) for e in body.iter(qn('a:blip')))
for rId, rel in list(doc.part.rels.items()):
    if rel.reltype.endswith('/image') and rId not in used: doc.part.drop_rel(rId)
doc.save(OUTF)

# ---------------- LEAD_5 content ----------------
s = open(L5).read()
PM = "' + PM + '"; EN = "' + EN + '"
pairs = [
 ("'a sediment-dominated parent less weathered than any exposed Khorat Group rock, permits at most '\n '~10' + EN + '20% basalt,",
  f"'a sediment-dominated parent less weathered than any exposed Khorat Group rock, permits ~{bm:.0f}' + EN + '{hi:.0f}% basalt '\n '(capped at ~10' + EN + '20% by trace-element ratios),"),
 ("'(36' + PM + '15%) is required;", f"'({m['Khorat sandstone']['mean']:.0f}' + PM + '{m['Khorat sandstone']['sd']:.0f}%) is required;"),
 ("'0.04 wt%). The model assigns that component to unweathered-shale (27' + PM + '23%) and '\n   'metatuff (10' + PM + '6%) proxies for unleached fine-grained material, i.e., the '",
  f"'0.04 wt%). The model assigns that component to unweathered shale (PAAS, {m['Unweathered shale (PAAS)']['mean']:.0f}' + PM + '{m['Unweathered shale (PAAS)']['sd']:.0f}%) and '\n   'an unconstrained component ({m['Random']['mean']:.0f}' + PM + '{m['Random']['sd']:.0f}%) resembling unweathered greywacke, i.e., the '"),
 ("'Basalt is permitted but not demanded: 4.8' + PM + '5.4% in the main run ' + EN + ' with an '\n   'unconstrained \"random\" component taking 18' + PM + '13%, itself a sign that the dictionary '\n   'lacks an adequate parent ' + EN + ' rising to 19' + PM + '9% and becoming required only when the model is denied that component.",
  f"'Basalt is permitted but not demanded: {bm:.1f}' + PM + '{m['All basalt']['sd']:.1f}% in the main run ' + EN + ' the size of the '\n   'unconstrained component being itself a sign that the dictionary '\n   'lacks an adequate parent ' + EN + ' rising to {nr['All basalt']['mean']:.0f}' + PM + '{nr['All basalt']['sd']:.0f}% (and {lo['All basalt']['mean']:.0f}% with regional lithologies only) and becoming required only when the model is denied that component. The regional felsic \"metatuff\", pre-Khorat basement exposed only south of the plateau, is not used."),
 ("'sand plus a fine-grained, unleached aluminous sediment with ~5' + EN + '20% basalt permitted '",
  f"'sand plus a fine-grained, unleached aluminous sediment with ~{bm:.0f}' + EN + '{hi:.0f}% basalt permitted '"),
 ("'is permitted at ~5' + EN + '20% and capped", f"'is permitted at ~{bm:.0f}' + EN + '{hi:.0f}% and capped"),
]
for a, b in pairs:
    assert s.count(a) == 1, ('LEAD5 missing', a[:70]); s = s.replace(a, b)
open(L5, 'w').write(s); log.append('lead5_content patched (%d)' % len(pairs))
print('\n'.join(log))
