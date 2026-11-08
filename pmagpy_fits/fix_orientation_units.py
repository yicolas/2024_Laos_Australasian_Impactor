"""One-off fix (2026-11-07, re-applied 2026-11-08) of the pmagpy_fits MagIC export.
samples: the export wrote the field core strike/hade (PmagPy orientation convention #2) into azimuth/dip;
MagIC needs the lab-arrow azimuth and plunge -> azimuth = (strike - 90) % 360, dip = -hade.
measurements: magn_moment was exported in emu -> A m^2 (x 1e-3).
Applies to samples.txt, measurements.txt and the combined pmagpy_Laos_magic.txt. Idempotence guard: refuses to run
if NWFA-1B already has azimuth 156.1."""
import sys, io, re, pandas as pd
def fix_samples(df):
    df['azimuth'] = (df['azimuth'] - 90) % 360; df['dip'] = -df['dip']; return df
def fix_meas(df):
    df['magn_moment'] = df['magn_moment'] * 1e-3; return df
def rw(path, fn):
    head = open(path).readline(); df = pd.read_csv(path, sep='\t', skiprows=1, low_memory=False)
    df = fn(df); open(path, 'w').write(head + df.to_csv(sep='\t', index=False))
s = pd.read_csv('samples.txt', sep='\t', skiprows=1).set_index('sample')
if abs(s.loc['NWFA-1B', 'azimuth'] - 156.1) < 0.05: sys.exit('already fixed')
rw('samples.txt', fix_samples); rw('measurements.txt', fix_meas)
txt = open('pmagpy_Laos_magic.txt').read()
parts = re.split(r'(?m)^(?=tab\t)', txt)          # sections start with "tab<TAB>name"
out = []
for b in parts:
    if not b.strip(): out.append(b); continue
    lines = b.rstrip('\n').split('\n'); name = lines[0].split('\t')[1].strip()
    if name in ('samples', 'measurements'):
        df = pd.read_csv(io.StringIO('\n'.join(lines[1:])), sep='\t', low_memory=False)
        df = fix_samples(df) if name == 'samples' else fix_meas(df)
        b = lines[0] + '\n' + df.to_csv(sep='\t', index=False)
    out.append(b)
open('pmagpy_Laos_magic.txt', 'w').write(''.join(out))
print('fixed')
