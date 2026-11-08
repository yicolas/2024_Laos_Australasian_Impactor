"""Push 4: S3 restricted to coherent AF paths; S2 caption note. Usage: python push4.py in.docx out.docx"""
import sys
sys.argv_saved = list(sys.argv)
exec(open('/home/claude/push/push3.py').read().split("O = '/mnt/user-data/outputs/'")[0].replace("IN, OUTF = sys.argv[1], sys.argv[2]", "IN, OUTF = sys.argv_saved[1], sys.argv_saved[2]"))
S3 = ("AF demagnetization paths of the NRM in geographic coordinates (rotated with the corrected sample orientations), coloured by AF peak field "
      "(0–94 mT); filled = lower, open = upper hemisphere. Purple squares are thermal HT (ChRM) means of the same core (Fig. 7) where available; "
      "stars are the GAD directions. Only specimens with coherent AF paths are shown: PKQ-A-0H, -2M, -3H and -9I converge on the thermal HT "
      "direction, PKQ-A-6M, PKS-J-3A and PKS-F-4A decay along smooth paths, and PKS-F-8H is AF-stable. Four further specimens measured on the "
      "sample changer in 2025–26 (NWF-B-3I, NWF-C-7A, PKS-G-8E, WBE-A-1J) are omitted: their directions jump along small circles at "
      "near-constant inclination from step to step, a rotational artefact of the measurement rather than a demagnetization path, so their AF "
      "directions carry no information. Their thermal results (Fig. 7; Figs. S5–S16) are unaffected.")
c = para_starting('Figure S3.'); set_image(prev_img(c), 'S3.png'); set_caption(c, 'Figure S3.', S3); log.append('S3 replaced')
c2 = para_starting('Figure S2.')
ts = [t for t in c2.iter(qn('w:t')) if t.text]
note = (' NWF-B-3I, NWF-C-7A, PKS-G-8E and WBE-A-1J show the measurement rotation described in Fig. S3; their intensity-based parameters '
        'are shown, but their AF directions are not used.')
if 'measurement rotation' not in W(c2): ts[-1].text = ts[-1].text.rstrip() + note; log.append('S2 note')
used = set(e.get(qn('r:embed')) for e in body.iter(qn('a:blip')))
for rId, rel in list(doc.part.rels.items()):
    if rel.reltype.endswith('/image') and rId not in used: doc.part.drop_rel(rId)
doc.save(OUTF); print('\n'.join(log))
