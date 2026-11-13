# -*- coding: utf-8 -*-
"""In-text citations -> MAPS author-date style: (Author 2020), (Author and Other 2020), (Author et al. 2020)."""
import re
SPECIFIC = [
    ('Ma & others, 2004', 'Ma et al. 2004'),
    ('Bunopas et al., 1998; Bunopas et al., 1999', 'Bunopas et al. 1999'),
    ('Bunopas et al., 1998', 'Bunopas et al. 1999'),
    ('; Velzen et al., 1993', ''),
    ('Glass, 1994', 'Glass and Pizzuto 1994'),
    ('Barnes, 1962, 1964', 'Barnes and Pitakpaivan 1962; Barnes 1964'),
    ('Folco et al., 2009, 2010, 2016', 'Folco et al. 2009, 2010, 2016, 2018'),
    ('orthogonal-vector (Zijderveld) diagram with', 'orthogonal-vector (Zijderveld 1967) diagram with'),
    ('Steinshouer et al., 1999, OFR 97-470-F, after UNESCO/CGMW, 1990', 'Steinshouer et al. 1999, after CGMW and UNESCO 1990'),
    ('Dunlop & Özdemir, 1997', 'Dunlop and Özdemir 1997'),
    ('Özdemir & Banerjee, 1984', 'Özdemir and Banerjee 1984'),
]
SUR = r"[A-ZÀ-ÖØ-ÞŽŘ][\wÀ-žŘřŽžÖöüé’'\-]*"
YEAR = r"(?:18|19|20)\d\d[a-z]?"
AMP = re.compile(rf"({SUR}) & ({SUR})(?=,? \(?{YEAR})")
COMMA = re.compile(rf"(et al\.|(?<![A-Za-z]){SUR}|GPTS)\s?,\s({YEAR})\b")
NOT_AUTHOR = {'Table', 'Fig', 'Figs', 'Figure', 'March', 'November', 'Dataset', 'Text', 'Laos', 'Thailand', 'Vietnam',
              'Cambodia', 'Ma'}

def convert(s):
    for a, b in SPECIFIC:
        s = s.replace(a, b)
    s = AMP.sub(r'\1 and \2', s)
    def rep(m):
        w = m.group(1)
        if w in NOT_AUTHOR: return m.group(0)
        return f'{w} {m.group(2)}'
    return COMMA.sub(rep, s)
