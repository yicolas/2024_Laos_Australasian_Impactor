# Recomputed site statistics from the canonical fitquest/pmagpy fits
2026-11-06 · computed with pmagpy (`pmag.fisher_mean`, `pmag.dia_vgp`) by `recompute_site_stats.py`

**Conventions** (pmagpy-standard, matching LEAD_2's stated scheme):
- ChRM = component `mt` (high-T window, ~160–510 °C), geographic frame (`dir_tilt_correction` 0)
- Specimen acceptance: MAD_free ≤ 15° (8 specimens rejected, 6 of them PKSF-3/PKSF-4 — the
  450 °C-ceiling cores; list in script output)
- Specimen → sample (oriented core / block) → site Fisher averaging; unit = name prefix
- Polarity from VGP latitude, not inclination sign
- Watson (1956) randomness: Ro₉₅/Ro₉₉ by Monte Carlo (10⁶ draws) — reproduces Watson's table
  (n=8: 4.48/5.26; n=10: 5.03/5.94; n=11: 5.28/6.26; n=3: 2.62/2.83). Note: the Ro values in
  `Laos_site_interpretations.md` (2.80, 4.57, 5.10) do not match the 95% table; use these.

## Replacement Table 2 — in-situ / coherent-unit site means

| Site | N cores (spec) | Dec | Inc | α95 | k | VGP lat | Polarity | vs LEAD_2 Table 2 |
|---|---|---|---|---|---|---|---|---|
| NWF-A | 5 (15) | 11.8 | +23.7 | 11.8 | 42.9 | +78.1 | N | was 11.2/+23.9, k43.5 — ≈unchanged |
| PKS-B | 1 (7) | 190.6 | −10.6 | 3.7* | 269.8* | −75.6 | R | ≈unchanged (190.3/−11.3) |
| PKS-I | 1 (5) | 47.9 | −35.6 | 4.2* | 330.4* | +31.3 | Indet. (clast) | ≈unchanged |
| PKS-J | 3 (12) | 174.9 | −31.9 | 7.9 | 244.2 | −84.7 | R | was 175.4/−33.0, k115 — tighter now |
| PKS-K | 2 (9) | 195.1 | −33.2 | 86.6 | 10.6 | −75.3 | R | cores disagree: PKSK-1 174.9/−29.4 (near dipole), PKSK-2 216.3/−33.5 (SW-pulled) |
| WBE-A | 2 (11) | 168.1 | −34.5 | 28.0 | 81.7 | −78.0 | R | was k544/α95 10.7 — new fits separate the 2 cores by ~10° |
| PKS-HA (upper) | 2 (19) | 164.9 | −13.5 | 14.8† | 6.1† | mixed cores | Disturbed | cores 64° apart: HA1 141.2/−28.0 (k96), HA2 194.5/+9.8 (k157) |
| PKS-HB (below) | 1 (5) | 209.6 | +7.9 | 3.3* | 549.1* | −55.0 | R (by VGP) | was 210.8/+7.9, k54 — tighter |

\* specimen-level statistics (single-core unit) · † specimen-level over the 2 HA cores

**PKS-H key revision:** under the new fits *all three* cores have southern VGPs (HA1 −53°, HA2
−65°, HB1 −55°) → all reversed by VGP-latitude polarity. The old "mixed R,N,N polarity" framing
is dead; replace with: internally tight cores 34–46° off the reversed dipole, HA1–HA2 64° apart
within one horizon (⇒ HA disturbed, not in-situ), HA2–HB1 only 15° apart (shared transitional
field or shared rotation — undecidable). B–M boundary unconfirmed at the locality.

**PKS-I:** VGP lat +31° — neither N (≥+45) nor R; anomalous tight direction, rotated clast.

## Watson conglomerate tests — boulder means (THE BIG CHANGES)

| Site | n boulders | R | Ro₉₅ | Ro₉₉ | Verdict | Previous claims |
|---|---|---|---|---|---|---|
| NWF-B | 3 | 2.38 | 2.62 | 2.83 | **RANDOM — pass** | interp doc pass ✓ (R 2.37); LEAD_2 treats as failed in-situ flow → move to cong tests |
| NWF-C | 8 | 3.26 | 4.48 | 5.26 | **RANDOM — pass** | pass in all versions ✓ (R was 3.95 / 3.37) |
| PKQ-A | 10 cores | **7.27** | 5.03 | 5.94 | **CLUSTERED — fail** | LEAD_2: pass (N=4, R 2.80) |
| PKQ-A | 3 field boulders (B1={0–4}, B2={5,6}, B3={7–9}) | 2.25 | 2.62 | 2.83 | RANDOM — pass (n=3, ~no power) | reproduces interp-doc grouping exactly (272/74 k14; 141/−1 k110; 135/46 k23) |
| PKS-F | 11 boulders | **5.31** | 5.28 | 6.26 | **marginal FAIL** | LEAD_2: pass (R 4.26); interp doc: pass (R 4.17) |
| PKS-F | 10 (PKSF-1. merged into 1) | **5.13** | 5.03 | 5.94 | **marginal FAIL** | — |
| PKS-F | 11, specimens dang ≤ 15 only | **6.04** | 5.28 | — | **FAIL** | robust to dang screening |
| PKS-G | 8 | 6.58 | 4.48 | 5.26 | **CLUSTERED — fail** | fail in all versions ✓ (R was 6.68/6.70) |
| PKS-H | 3 cores | 2.52 | 2.62 | 2.83 | RANDOM — pass (n=3, ~no power) | consistent with disturbed/clast reading |

### Why PKS-F flipped, and what it means
Under the new fitquest fits, 7 of 11 PKSF boulder means fall in a NE-ish shallow cluster
(PKSF-2 30/+26, -4 53/+4, -6 35/+1, -7 33/−37, -9 15/−42, -5 346/+52, -8 81/−17), pulling R just
over Ro₉₅ at every reasonable screening. Three readings, not decidable from statistics alone:
1. **Incomplete unmixing at the 450 °C ceiling** (per `PKSF_interpretation_notes.md`: PKSF-3's
   HT component never isolates; others may share the problem) — the mt fits would then be
   overprint-contaminated and the Watson test is testing the wrong vectors. Manuscript statement
   would be "PKS-F cannot be conclusively tested at the available demagnetization level."
2. **Genuine shared component** (post-depositional CRM during lateritization, or the "boulders"
   are in-situ corestones of one flow, like PKS-G) → honest FAIL.
3. The old fits were right and the re-fits over-trimmed — argues for re-examining the PKSF
   Zijdervelds core by core before the paper claims either way.
Either way **the "3 of 4 diamicton sites pass" headline no longer survives as written.** Current
honest tally: pass = NWF-C, NWF-B (+PKS-H/PKQ-A only at the powerless n=3 level); fail = PKS-G;
PKS-F marginal-fail/untestable; PKQ-A fails at core level.

### PKQ-A
At the 10-core level the directions are strongly clustered (two antipodal-ish groups: NW-steep
B1 cores vs SE-shallow/moderate B2–B3 cores) → R 7.27 fail. Only the 3-field-boulder grouping
passes, and n=3 has essentially no power. Statements about PKQ-A should lean on the boulder
structure (3 internally-coherent, mutually discordant boulders — qualitatively pre-depositional)
rather than on a Watson "pass."

## Files
- `recomputed_unit_means.csv` — every core/boulder mean + VGP lat
- `recomputed_site_means.csv` — site means
- `recompute_site_stats.py` — reproducible script (seed 42)


## McFadden & McElhinny (1988) lines-and-planes double-check (2026-11-07)

Script: `mcfadden_gc_check.py`. Unresolved specimens (mt MAD>15 or dang>15) were re-expressed as
great circles (DE-BFP planes fit to their demag arcs in specimen coordinates, poles rotated to
geographic via per-specimen Kabsch rotations solved from that specimen's own paired lt/MT/mt fits;
rotations verified by reproducing stored mt directions, median error 0.2 deg). Boulder means then
combined lines + planes with pmag.dolnp.

| Site | n boulders | R | Ro95 | Verdict | vs line-only |
|---|---|---|---|---|---|
| NWF-B | 3 | 2.38 | 2.62 | RANDOM pass | same |
| NWF-C | 8 | 3.26 | 4.48 | RANDOM pass | same |
| PKQ-A | 10 | 7.27 | 5.03 | CLUSTERED fail | same (3-field-boulder variant still passes, R 2.25) |
| PKS-F | 11 | 6.09 | 5.28 | CLUSTERED fail | strengthens the fail (was 5.31 knife-edge) |
| PKS-F | 10 | 5.92 | 5.03 | CLUSTERED fail | strengthens |
| PKS-G | 8 | 6.58 | 4.48 | CLUSTERED fail | same |
| PKS-H | 3 | 2.50 | 2.62 | RANDOM pass (no power) | same |

Key movement: constraining PKSF-3 by great circles moves its boulder mean from 274/-24 (bad lines)
to 330/-10, and PKSF-4 to 58/-22 - both into/near the NE-shallow cluster. **PKS-F therefore fails
under every quality-controlled treatment** (MAD-screened lines; lines+planes at 10 and 11
boulders); the only configuration that ever passed was unscreened lines including the unresolved
fits. Recommended manuscript verdict upgraded from "indeterminate" to FAIL (clustered), with the
450 C ceiling noted as the reason the shared component cannot be fully isolated.
Exclusions: PKSF-4B/-4E (too few rotation pairs), PKSF-4K (angles not preserved), PKSF-6E/-6F
(plane MAD > 15); PKSH-1C plane had poor rotation validation but is 1 of 11 specimens in its
boulder (negligible effect).
