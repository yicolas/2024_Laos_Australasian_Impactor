# pmagpy_fits — component fits from the pmagpy interface

Paleomagnetic component fits for all 12 Laos sites, made in the pmagpy
fitting app (`fitgame_v15.html`). 1062 fits across 364 specimens.

## Contents
- `pmagpy_Laos_allsites.redo` — all fits in pmagpy demag_gui format
  (import via demag_gui.py → File → Import interpretations from a redo file).
- `pmagpy_Laos_magic.txt` — complete MagIC 3.0 contribution (single upload file).
- `locations.txt`, `sites.txt`, `samples.txt`, `specimens.txt`, `measurements.txt`
  — the same contribution split into the standard MagIC per-table files.
  `specimens.txt` has each fit in BOTH geographic (dir_tilt_correction 0) and
  tilt-corrected (100) frames; dang is reported on the terminal component only.
  `sites.txt` carries the Fisher ChRM site means.

## Note
These are NOT the same as the repo's existing `Magnetometer_Data_corrected/`
tables (the April-2025 / Aug-2026 manuscript-basis fits). These are the new
pmagpy re-fits. Decide deliberately before promoting any of these over the
working files; they are kept in this separate folder so nothing is clobbered.

## Orientation / unit fix (2026-11-07; re-applied 2026-11-08 after the repo sync reverted it)
The export wrote each core's field strike and hade (PmagPy orientation convention #2) into the MagIC
`azimuth`/`dip` columns, which MagIC defines as the lab-arrow azimuth and plunge, and wrote `magn_moment`
in emu. `fix_orientation_units.py` converts samples (azimuth = strike − 90, dip = −hade) and measurements
(emu → A m², ×1e-3) in `samples.txt`, `measurements.txt` and `pmagpy_Laos_magic.txt`. With the fix,
standard MagIC rotation (`pmag.dogeo`) reproduces all 1062 stored geographic fits (median 0.1°).
