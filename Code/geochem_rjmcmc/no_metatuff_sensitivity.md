# Sensitivity: rj-MCMC without the felsic metatuff (2026-11-13)

`python3 run.py no_metatuff 30000 4` and `python3 run.py local_no_metatuff 30000 4` (seeds 1000–1003), summarised with
`summarize.summarise` (all chains within 50 log-likelihood units). Mean ± 1σ wt%, P = fraction of posterior samples > 1 %.

| Run | Sandstone | PAAS shale | Mudstone | Metatuff | Random | Basalt (thol + alk) | Sed. laterite | Chain log-L |
|---|---|---|---|---|---|---|---|---|
| main (12 chains, summary.json) | 36 ± 15 | 27 ± 23 | 3 ± 6 | 10 ± 6 | 18 ± 13 | 4.8 ± 5.4 (3.7 + 1.1), P 0.64 | 1.6 | −265 to −220 |
| **no metatuff** | 25 ± 15 | 42 ± 29 | 9 ± 6 | – | 8 ± 9 | **10.0 ± 6.6 (7.8 + 2.2), P 1.00** | 5.9 | −262 to −220 |
| local only (no PAAS/random) | 25 ± 11 | – | 26 ± 12 | 31 ± 13 | – | 18.2 ± 2.3 (6.3 + 11.9), P 1.00 | 0 | −268 to −220 |
| **local only, no metatuff** | 29 ± 30 | – | 44 ± 31 | – | – | **25.1 ± 1.3 (15.7 + 9.3), P 1.00** | 1.6 | −263 to −239 |

- The fit does not degrade when the metatuff is removed (same log-likelihood range; bulk misfit < 0.5 % for every oxide).
- The metatuff's posterior composition (SiO2 ~77–78, Na2O ~2.5–3.3, K2O ~3.0–3.4 wt%) sits on the tektite composition itself:
  it acts as a catch-all for "unleached, Na–K-bearing siliceous material", not as an identified source.
- Its weight goes mainly to PAAS (and mudstone), and basalt becomes required (present in every posterior sample):
  ~10 % with PAAS/random available, ~25 % with regional lithologies only. Sandstone falls (36 → 25 %), i.e. the metatuff
  was not displacing the sandstone.
- Provenance of the 8 felsic "metatuff" analyses (Sieh et al. 2020 compilation, geochem.csv): CCN19-A-1, CCS19-A/C/D/E/F
  (no coordinates in geochem1.csv or the 2018 field log), H1818-I-1 (14°42′58″N 106°12′25″E, "mauve silicic crystal-rich
  volcanic", southern flank of the plateau). DKI18-A-1 (Don Khau Island, Mekong, Mz1 Triassic rhyolite/dacite/tuff) is
  already excluded as Na-leached. These are pre-Khorat (Triassic) arc volcanics that crop out south of the plateau and
  lie beneath ≥500 m of Khorat Group at the proposed crater.
