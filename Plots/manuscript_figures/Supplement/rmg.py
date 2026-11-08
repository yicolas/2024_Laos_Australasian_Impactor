import csv, numpy as np, os, glob
def read_rmg(path):
    rows = list(csv.reader(open(path, encoding='latin-1')))
    out = []
    for r in rows[4:]:
        if len(r) < 17 or not r[0].strip(): continue
        t = r[0].strip()
        try: lev = float(r[1]); bias = float(r[2]); dec = float(r[14]); inc = float(r[15]); M = float(r[16])
        except ValueError: continue
        out.append((t, lev, bias, dec, inc, M))
    segs, cur, last = [], [], None
    for row in out:
        t = row[0]
        if t == 'AFmax' or (last is not None and t != last and not (last == 'NRM' and t == 'AF')):
            if cur: segs.append(cur)
            cur = []
        if t != 'AFmax': cur.append(row)
        last = t
    if cur: segs.append(cur)
    return segs
if __name__ == '__main__':
    for f in sorted(glob.glob('RockMag/*/*.rmg')):
        segs = read_rmg(f); print(os.path.basename(f), [(s[0][0], len(s), s[0][1], s[-1][1], f'{s[-1][2]:.2f}') for s in segs])
