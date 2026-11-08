# Tektite geochemistry and rj-MCMC source unmixing (Bolaven / Australasian impactor paper)

This folder rebuilds manuscript Figs 14–17 and the numbers in the LEAD_4 geochemistry section.

## Inputs (not in git)
- `Paolo_Data/AAT Laos - Geochem data/` beside `Code/` in the local repo, holding the EPMA, LA-ICP-MS and target-rock masters and the AAT literature list. It is deliberately not pushed. Override the location with `GEOCHEM_ROOT`.
- iCloud `Caltech Projects/Australasian Impactor/geochem.csv` (the Sieh et al. 2019 compilation; override with `GEOCHEM_SICAT`) and `Dataset_S4_Basalt geochemical data.xlsx` (override with `GEOCHEM_S4`).

## Outputs
- `figures/`: Figs 14–17 and `summary.json`, which holds every number quoted in the manuscript.
- `geochem_handoff_LEAD4.md`: the correction hand-off for the manuscript chat (regenerate it with `make_handoff.py`).
- `res_*.pkl` chain files (~30 MB each) are not committed. Re-running takes about 1–2 h on two cores.
- `build_docx.py` is archival. It produced the first LEAD_4 from LEAD_3; the LEAD_4 master in `manuscript/` has been edited since, so do not re-run it over the master.

## Files
| file | role |
|---|---|
| `load.py` | Loads the data and applies QC. EPMA: keep totals ≥ 97 wt%. LA-ICP-MS: re-standardise MNG24_A3_2 to the MNG24_A3_1 SiO2. Sources: this study plus the regional compilation; basalts screened (LOI ≤ 3 wt%, totals 98.5–101.5 wt%) and split into tholeiite vs alkali basalt (Macdonald & Katsura 1964). |
| `rjmcmc.py` | Reversible-jump MCMC unmixing following Carter et al. (2025, G³). Model Y = C·M with per-analysis Dirichlet weights. Poisson(10) prior on K, truncated-normal priors on each lithology type, Gaussian clr likelihood. Moves: birth/death/split/merge, type swap, composition and weights. |
| `run.py` | Builds the lithology dictionary and runs the chains. Configs: `main`, `no_random`, `no_alkali`, `local_only`, `precision`. |
| `summarize.py` | Summarises the chains and makes Fig 15 (inversion) and Fig 16 (trace elements). Writes `figures/summary.json`. |
| `figs_data.py` | Makes Fig 14 (EPMA QC and Harker diagrams) and Fig 17 (PGE: Ir below detection, Pd as a YO⁺ interference). |
| `text_methods.py`, `text_results.py`, `build_docx.py` | Write manuscript_LEAD_4.docx from LEAD_3. |

## Reproduce
```
python3 run.py main 60000 12
python3 run.py no_random 30000 4
python3 run.py no_alkali 30000 4
python3 run.py local_only 30000 4
python3 figs_data.py
python3 summarize.py
python3 make_handoff.py
```

## Known limitations (also stated in the manuscript)
- Between-model moves are rarely accepted once a chain has converged. The posterior on K is therefore represented by the spread among chains, as in Carter et al. (2025). The data do not constrain K: chains with 5 to 27 components fit equally well.
- Lithology-type priors are broad, so component compositions can drift toward the tektite composition. Read type weights as "what kind of material is required", not as exact proportions.
- LA-ICP-MS: the data cover only two tektites. Absolute concentrations are accurate to about ±30 %, so only ratios are interpreted. Pd is an artefact; Ir is below detection.
- Still needed from P. Sanchez: EPMA and LA-ICP-MS instrument conditions and standards, and which Pd isotope was monitored.
