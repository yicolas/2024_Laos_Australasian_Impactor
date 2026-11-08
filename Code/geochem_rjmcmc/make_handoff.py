"""Write the hand-off markdown for the manuscript & figures chat from the same text modules used to build LEAD_4."""
import os
import json, importlib
import text_methods as TM, text_results as TR
importlib.reload(TM); importlib.reload(TR)
S = json.load(open(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'figures', 'summary.json')))

def runs(lst):
    out = []
    for it in lst:
        if isinstance(it, str): out.append(it)
        else:
            txt, bold = it
            if txt: out.append(f"**{txt.strip()}** " if bold else txt)
    return ''.join(out).strip()

def wt(run, name):
    d = S[run]['summ'].get(name)
    return '—' if d is None else f"{d['mean']:.0f} ± {d['sd']:.0f}"

R = []
R.append("# Hand-off: tektite geochemistry corrections for the manuscript & figures\n")
R.append("Prepared 2026-11-07 for the manuscript/figures chat. It covers every geochemistry change between "
         "`manuscript_LEAD_3.docx` and `manuscript_LEAD_4.docx`. Paleomagnetic sections are untouched.\n")
R.append("## Where things are\n"
         "- **Corrected manuscript:** `iCloud …/Caltech Projects/Australasian Impactor/manuscript_LEAD_4.docx`. LEAD_3 is kept unchanged.\n"
         "- **Code, figures and numbers:** `~/Documents/GitHub/2024_Laos_Australasian_Impactor/Code/geochem_rjmcmc/`. "
         "The figure PNGs are in `figures/`, all numbers are in `figures/summary.json`, and the README gives the commands to reproduce them.\n"
         "- **Raw data:** `Paolo_Data/` (EPMA, LA-ICP-MS and target-rock masters) and iCloud `geochem.csv` (the Sieh et al. 2019 compilation).\n")
R.append("## Why the section changed (one paragraph to brief co-authors)\n"
         "The LEAD_3 geochemistry treated 153 EPMA and 50 LA-ICP-MS analyses as independent samples. In fact they come from 7 and 2 "
         "tektites. LEAD_3 also included EPMA analyses with totals down to 33 wt%, quantified three LA-ICP-MS sites with a wrong "
         "internal standard, and reported \"low\" Pd that was actually 177 ppb, an analytical artefact. Its \"rj-MCMC\" was a "
         "15-combination model selection, and no code existed for it. LEAD_4 re-screens the data, re-implements the "
         "reversible-jump unmixing of Carter et al. (2025, G³; the Berkeley Geochronology Center model of Fuentes, Renne and co-authors) "
         "with the regional compilation of Sieh et al. (2019) as the source dictionary, and restricts the claims to what the data "
         "support and what agrees with the regional literature.\n")
R.append("## Claims the manuscript now makes (and only these)\n"
         "1. The tektites are sediment-dominated melts of a quartz-rich sand plus a fine-grained aluminous sediment. "
         "This agrees with Koeberl 1992, Blum et al. 1992 and Amare & Koeberl 2006.\n"
         "2. The Khorat sediments and lateritic regolith now exposed are too leached of Ca and Na to be the parent as sampled. "
         "A less-weathered equivalent is required, and none has been analysed.\n"
         "3. A basaltic contribution of about 5–20 % is permitted. It is required only when the model is denied an unconstrained "
         "component. Trace ratios cap it at ~10 % (tholeiite) to ~20 % (alkali basalt).\n"
         "4. Ir is below the ~4 ppb LA-ICP-MS detection limit. The reported Pd is a YO⁺ interference. The ≤ 0.005 % chondritic "
         "component inferred from Os isotopes (Ackerman et al. 2019) cannot be tested.\n"
         "5. None of these results discriminates the Bolaven location from other Indochinese sources.\n\n"
         "**Do not reinstate any of the following:** the 52/35/13 sandstone/mudstone/basalt mixture, \"reduced χ² ≈ 0.5\", "
         "\"posterior probability 0.70\", \"Pd is low\", \"saprolite Co ≈ 210 ppm explains the siderophiles\", the volatile-element "
         "figure (old Fig. 18), or \"Ackerman found no extraterrestrial component\". Ackerman et al. in fact infer a tiny one.\n")

R.append("## Key numbers (from `summary.json`)\n")
R.append("| Quantity | Value |\n|---|---|")
R.append("| EPMA accepted (totals ≥ 97 wt%) | 82 of 153 analyses on 4 tektites (MNG24_A3_1 30, MNG24_B1 17, MG24_B1 5, KK24_T1 30) |")
R.append("| LA-ICP-MS | 2 tektites (MNG24_A3_1, A3_2); 5 sites × 5 replicates; ratios only (±30 % absolute) |")
R.append("| Tektite Th/Sc, Eu/Eu* | 1.14/1.20 and 0.69/0.66 (literature medians 1.33 and 0.62) |")
R.append("| Ir | below detection (≤ ~4 ppb) |")
R.append("| Pd | artefact; site-mean Pd/Y 0.006–0.012, equivalent to ⁸⁹Y¹⁶O⁺/Y⁺ of 0.13–0.26 % |")
for run, lab in [('main', 'Main run (12 chains)'), ('no_random', 'No random component'), ('no_alkali', 'Na2O, K2O excluded'), ('local_only', 'Regional lithologies only')]:
    if run not in S: continue
    R.append(f"| {lab} | sandstone {wt(run,'Khorat sandstone')} · unweathered shale {wt(run,'Unweathered shale (PAAS)')} · felsic metatuff {wt(run,'Metatuff')} · "
             f"basalt {wt(run,'All basalt')} (tholeiite {wt(run,'Bolaven tholeiite')}, alkali {wt(run,'Bolaven alkali basalt')}) · random {wt(run,'Random')} wt% |")
R.append("")

R.append("## Section-by-section text\n")
R.append("Paste the replacement text verbatim. Bold lead-ins are run-in headings in the docx.\n")
R.append("### Abstract\nReplace everything from *\"A parallel geochemical test …\"* to the end of the abstract with:\n")
R.append("> " + TR.ABSTRACT_NEW + "\n")
R.append("In the sentence *\"We complemented the magnetic work …\"*, replace *\"inverted for the tektite parent materials with a "
         "Bayesian (reversible-jump Monte-Carlo) source-unmixing model.\"* with *\"evaluated with a reversible-jump Markov-chain "
         "Monte-Carlo source-unmixing model.\"*\n")
R.append("### Methods → Geochemical Analysis (replaces both paragraphs)\n")
R.append(TM.M61[1] + "\n\n" + TM.M62[1] + "\n")
R.append("Fill the bracketed placeholders from Paolo: the EPMA and LA-ICP-MS instrument, conditions and standards, and the Pd isotope monitored.\n")
R.append("### Results → Geochemistry: Testing the Bolaven Source Hypothesis (replaces the whole subsection)\n")
order = [('para', TR.R_INTRO), ('para', TR.R_QC), ('fig', 14, TR.CAP14), ('para', TR.R_MIX), ('fig', 15, TR.CAP15),
         ('para', TR.R_TRACE), ('fig', 16, TR.CAP16), ('para', TR.R_PGE), ('fig', 17, TR.CAP17), ('para', TR.R_SUM)]
for it in order:
    if it[0] == 'para': R.append(runs(it[1]) + "\n")
    else: R.append(f"*[Figure {it[1]} here]*\n\n" + runs(it[2]) + "\n")
R.append("### Discussion and Conclusions (in-place edits)\n")
for start, old, new in TR.EDITS[1:]:
    R.append(f"- In the paragraph beginning *\"{start}…\"*, replace\n  > {old}\n\n  with\n  > {new}\n")
R.append("### References\n"
         "- **Add:**\n" + "\n".join(f"  - {t}" for _, t in TR.REFS_ADD) + "\n"
         "- **Replace** Gallagher et al. (2011) with:\n  - " + TR.REF_REPLACE[0][1] + "\n"
         "- **Check:** Gallagher et al. (2011) is no longer cited, and Ma et al. (2004) is cited as \"Ma et al., 2004\" in the "
         "new text but as \"Ma & others, 2004\" elsewhere. Harmonise the two.\n")

R.append("## Figures\n")
R.append("| Fig. | File (`Code/geochem_rjmcmc/figures/`) | Status | Made by |\n|---|---|---|---|")
R.append("| 8 | unchanged (SEM/EDS, LS-H18) | keep | — |")
R.append("| 14 | `Fig14_EPMA_QC_Harker.png` | **new** — EPMA totals screening, plus Harker diagrams against the literature and source medians | `figs_data.py` |")
R.append("| 15 | `Fig15_rjMCMC.png` | **new** — rj-MCMC chains, K, source weights, residuals, sensitivity runs | `summarize.py` |")
R.append("| 16 | `Fig16_trace.png` | **new** — LA accuracy check, REE, Th/Sc–Eu/Eu* with posterior mixtures | `summarize.py` |")
R.append("| 17 | `Fig17_PGE_Pd_Ir.png` | **new** — Pd vs Y (YO⁺ interference), ¹⁹¹Ir vs ¹⁹³Ir, CI-normalised PGE | `figs_data.py` |")
R.append("| 18 | — | **delete** (volatiles); renumber any later figure references | — |\n")
R.append("**Figure notes for the styling pass**\n"
         "- Labels: \"Felsic metatuff\" means the 8 felsic samples only. Basalt appears as two types, \"Bolaven tholeiite\" and \"Bolaven alkali basalt\".\n"
         "- Fig. 16c has no metatuff star, because the felsic metatuff has no trace-element data.\n"
         "- If the figures are restyled, regenerate them from the scripts rather than editing the PNGs. The numbers in the "
         "captions and text come from `summary.json`.\n"
         "- Fig. 14 x-axes run from 30 to 100 wt% SiO₂ so the laterites are visible.\n")
R.append("## Open items\n"
         "- **Paolo:** EPMA and LA-ICP-MS conditions and standards; which Pd isotope was monitored, and the oxide production rate for that session.\n"
         "- **Kerry/Nick:** field context of the metatuff (CCN19/CCS19/H1818 samples). What unit is it, and does it lie beneath the Khorat "
         "Group? Also, the decimal and degrees–minutes coordinates in `geochem1.csv` disagree (e.g. DKI18-A-1).\n"
         "- **Data gap that would decide the source question:** unweathered Khorat sediment (drill core or deep exposure), plus "
         "Sr–Nd and ¹⁰Be comparison with the tektites.\n"
         "- **Optional:** run the published Carter et al. figshare code (doi:10.6084/m9.figshare.26972515.v2) on the 82 accepted "
         "analyses as a cross-check of the re-implementation.\n")
open(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'geochem_handoff_LEAD4.md'), 'w').write('\n'.join(R))
print('written', sum(len(x) for x in R), 'chars')
