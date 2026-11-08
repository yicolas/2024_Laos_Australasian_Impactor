import os
import json
S = json.load(open(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'figures', 'summary.json')))
M = S['main']['summ']; MT = S['mix_traces']
def w(name, run='main'):
    d = S[run]['summ'].get(name, {'mean': 0, 'sd': 0, 'p_present': 0}); return d['mean'], d['sd'], d['p_present']
def f(x): return f'{x:.0f}'
def sens_line():
    out = []
    lab = {'no_random': 'without the random component', 'no_alkali': 'with Na2O and K2O excluded',
           'local_only': 'with only the regional lithologies (no PAAS or random component)',
           'precision': 'with analytical-precision-only uncertainties'}
    for k in ['no_random', 'no_alkali', 'local_only', 'precision']:
        if k not in S: continue
        reg = sum(w(n, k)[0] for n in ['Lateritic saprolite', 'Sedimentary laterite', 'Diamicton / "catastro-loess"'])
        cana = w('Unweathered shale (PAAS)', k)[0] + w('Metatuff', k)[0]
        out.append(f"{lab[k]}: sandstone {f(w('Khorat sandstone', k)[0])} %, unweathered shale plus metatuff {f(cana)} %, "
                   f"basalt {f(bas(k)[0])} ± {f(bas(k)[1])} %, weathered regolith {reg:.1f} %")
    return '; '.join(out)

def bas(run='main'):
    d = S[run]['summ'].get('All basalt', {'mean': 0, 'sd': 0, 'p_present': 0}); return d['mean'], d['sd'], d['p_present']
BAS_MAX = max(bas(k)[0] + bas(k)[1] for k in ['main', 'no_random', 'no_alkali', 'local_only'] if k in S)
reg_main = sum(w(n)[0] for n in ['Lateritic saprolite', 'Sedimentary laterite', 'Diamicton / "catastro-loess"'])
reg_p = max(w(n)[2] for n in ['Lateritic saprolite', 'Sedimentary laterite', 'Diamicton / "catastro-loess"'])
Ks = sorted(int(k) for k in S['main']['K']); lls = list(S['main']['chain_ll'].values())
iqr = S['main']['resid_iqr']; worst = max(max(abs(a), abs(b)) for o, (a, b) in iqr.items() if o != 'MnO')

R_INTRO = [("", None), (
"The impact hypothesis makes a testable geochemical prediction: if the Australasian tektites are melts of the Bolaven target "
"column, their composition should be reproducible as a mixture of the local Mesozoic (Khorat Group) sediments and Bolaven "
"basalts (Sieh et al., 2019) – a claim contested on geochemical grounds (Mizera, 2022). Previous work on Indochinite and "
"Muong Nong-type tektites established that their parent was a fine-grained, quartz-rich sediment with a Jurassic-age crustal "
"Sr–Nd signature and a near-surface ¹⁰Be inventory, possibly with a minor mafic contribution (Blum et al., 1992; Koeberl, 1992; "
"Ma et al., 2004; Amare & Koeberl, 2006). We ask what our new data add to this, restricting claims to what the data can "
"support: (i) which analyses are reliable, (ii) which of the regional lithologies a Bayesian unmixing model requires, (iii) whether "
"trace-element ratios agree, and (iv) whether a projectile signature is resolvable.")]

R_QC = [("Data quality. ", True), (
"Only 82 of the 153 EPMA analyses, on four tektites, have oxide totals of at least 97 wt% (Fig. 14a). The rejected analyses (totals "
"33–97 wt%, including every analysis of MNG24_A3_2, MNG24_A3_3 and MNG24_C2) are not interpreted. The accepted analyses lie within the field of "
"published Indochinite and Muong Nong tektites on every Harker diagram (Fig. 14b–h); tektite means span 70.8–80.6 wt% SiO2, with "
"CaO 1.0–2.4, Na2O 1.2–1.6 and K2O 2.4–2.8 wt% (anhydrous), the most siliceous being KK24_T1 from Thailand. The LA-ICP-MS data "
"come from only two tektites from one sample (MNG24_A3), and their absolute concentrations carry a calibration offset of up to "
"~30 % (Methods; Fig. 16a); they characterise two specimens, not the strewn field. Their inter-element ratios nonetheless reproduce "
"the regional tektite signature: Th/Sc = 1.14 and 1.20, Eu/Eu* = 0.69 and 0.66 and La/Th = 2.8 and 2.5, against literature "
"medians of 1.33, 0.62 and 2.8.")]

R_MIX = [("Bayesian unmixing. ", True), (
f"All twelve chains reproduce the 82 accepted analyses equally well (median log-likelihoods {min(lls):.0f} to {max(lls):.0f}; "
f"interquartile per-analysis residuals within ±{worst:.0f} % for every oxide except MnO; Fig. 15d), but they do so with "
f"between {min(Ks)} and {max(Ks)} components, so the number of components is not constrained by the data (Fig. 15a,b). "
f"What is reproducible among chains is the type of material required (Fig. 15c). "
f"(1) The deeply weathered lithologies that now cover the plateau – lateritic saprolite on basalt, sedimentary laterite and "
f"bauxite, and the tektite-hosting diamicton or “loess” – are not required (combined weight {reg_main:.1f} %, present in at most "
f"{100*reg_p:.0f} % of posterior samples). "
f"(2) A quartz-rich sand classified as Khorat sandstone ({w('Khorat sandstone')[0]:.0f} ± {w('Khorat sandstone')[1]:.0f} %) is "
f"required in {100*w('Khorat sandstone')[2]:.0f} % of samples. "
f"(3) The remainder must be a fine-grained aluminous component carrying ~1.5–2 wt% each of CaO and Na2O. No sampled Khorat "
f"sediment supplies this, because all are intensely leached (median CaO ≤ 0.04 and Na2O ≤ 0.15 wt%; Fig. 14e,f), so the model "
f"assigns it to the unweathered-shale ({w('Unweathered shale (PAAS)')[0]:.0f} ± {w('Unweathered shale (PAAS)')[1]:.0f} %) and "
f"felsic metatuff ({w('Metatuff')[0]:.0f} ± {w('Metatuff')[1]:.0f} %) types, whose posterior compositions move toward the tektite "
f"composition itself. These two types should be read as proxies for unleached, Na–K-bearing fine-grained material, not as "
f"identified source rocks: PAAS is a global average, and the field context of the regional metatuff is not documented. "
f"(4) A Ca–Mg-rich component is permitted but not uniquely identified: Bolaven basalt contributes {bas()[0]:.1f} ± "
f"{bas()[1]:.1f} % (tholeiite {w('Bolaven tholeiite')[0]:.1f} %, alkali basalt {w('Bolaven alkali basalt')[0]:.1f} %; present in "
f"{100*bas()[2]:.0f} % of samples) – in this run the alkali basalts, despite their higher K2O and Na2O, are scarcely used – and an unconstrained “random” "
f"component of intermediate composition takes {w('Random')[0]:.0f} ± {w('Random')[1]:.0f} %, which itself indicates that the "
f"dictionary does not contain an adequate parent. The basalt and random components trade off: without the random component, "
f"basalt rises to {bas('no_random')[0]:.0f} ± {bas('no_random')[1]:.0f} % (tholeiite {w('Bolaven tholeiite','no_random')[0]:.0f} %, alkali basalt "
f"{w('Bolaven alkali basalt','no_random')[0]:.0f} %) and becomes required. Otherwise the sensitivity runs give the same picture ({sens_line()}; Fig. 15e). Restricted to the regional lithologies, the model substitutes "
f"felsic metatuff ({w('Metatuff', 'local_only')[0]:.0f} ± {w('Metatuff', 'local_only')[1]:.0f} %), the only sampled regional rock that is not "
f"leached of Na and K. Lateritic saprolite is never used. The unmixing "
f"therefore supports a sediment-dominated parent, in agreement with earlier work, but shows that the tektites cannot be melts of "
f"the Khorat sediments and regolith as they are exposed today. A less-weathered equivalent – fresh Khorat mudstone at depth, or "
f"the unweathered sediment that preceded the Pleistocene laterite – would be required, and no such material has yet been analysed.")]

R_TRACE = [("Trace elements. ", True), (
f"On the chondrite-normalised REE diagram the two tektites match the published Indochinite pattern: light-REE-enriched with a "
f"negative Eu anomaly, at concentrations within or slightly above (≤ 20 %) the literature range (Fig. 16b). In the "
f"calibration-insensitive ratios (Fig. 16c) they fall among the regional sediments and unweathered shale (Th/Sc 0.8–2.0, "
f"Eu/Eu* 0.58–0.70) and away from the Bolaven basalts (Eu/Eu* ≈ 1.0–1.1; Th/Sc ≈ 0.07 for the tholeiites and 0.46 for the "
f"alkali basalts) and basaltic saprolite. Mixed with even the most Th-rich regional sediment (Khorat sandstone, Th/Sc ≈ 2.0), "
f"about 10 % tholeiite or 20 % alkali basalt lowers Th/Sc to the tektite value (≈ 1.2), and ~20 % alkali basalt raises "
f"Eu/Eu* above the tektite range, so the trace ratios allow at most ~10–20 % basalt-derived material, depending on the suite. "
f"The felsic metatuff has no trace-element analyses and is omitted from the following prediction. The bulk posterior mixtures predict Eu/Eu* = {MT['Eu/Eu*'][0]:.2f}–{MT['Eu/Eu*'][2]:.2f} "
f"(90 % range), consistent with the tektites, and Th/Sc = {MT['Th/Sc'][0]:.2f}–{MT['Th/Sc'][2]:.2f}, which brackets the observed values "
f"but is mostly lower (median {MT['Th/Sc'][1]:.2f}). "
f"They also under-predict absolute Zr and Th (predicted {MT['Zr'][1]:.0f} and {MT['Th'][1]:.0f} µg/g, against literature medians of "
f"299 and 14.5 µg/g), because the regional sandstones are poor in zircon (median Zr ≈ 110 µg/g). The trace-element budget therefore "
f"does not close with the existing endmember data, mirroring the major-element result: the parent sediment was less weathered, and "
f"probably richer in heavy minerals, than the Khorat rocks sampled at the surface.")]

R_PGE = [("Platinum-group elements. ", True), (
"In 34 of the 50 LA-ICP-MS analyses both ¹⁹¹Ir and ¹⁹³Ir are zero, and the non-zero values (0.3–4.4 ppb) do not agree between the "
"two isotopes (Fig. 17b). Ir is therefore below detection, with an upper limit of about 4 ppb (~1 % of CI chondrite). The reported "
"Pd (0.02–0.38 µg/g; median 0.18 µg/g) cannot be real. It would be ~350 times the upper-crustal abundance (0.52 ppb; Rudnick & Gao, "
"2003) and ~30 % of CI chondrite (McDonough & Sun, 1995), while Ir (< 1 % CI) and Ru (≈ 0.3 ppb) are at or below crustal levels – "
"a Pd/Ir and Pd/Ru fractionation unlike any terrestrial or meteoritic reservoir. Instead, the site-mean Pd/Y ratio is nearly "
"constant (0.006–0.012; Fig. 17a). On ¹⁰⁵Pd, the usual analysis mass, this corresponds to an ⁸⁹Y¹⁶O⁺/⁸⁹Y⁺ production rate "
"of 0.13–0.26 %, a typical value for LA-ICP-MS, so the reported Pd is most plausibly a yttrium-oxide interference. The isotope "
"monitored was not recorded and should be confirmed. Pd is not interpreted further. Laser ablation cannot test for a "
"projectile at the level expected here: the non-radiogenic Os of Laotian Muong Nong and splash-form tektites indicates at most "
"~0.005 % of a chondritic component (Ackerman et al., 2019), which would add ~0.02 ppb Ir – two orders of magnitude below our "
"detection limit. Ni, Co and Cr in MNG24_A3_1 (78, 18 and 62 µg/g) lie within the published Indochinite ranges (10th–90th percentiles: Ni 21–181, "
"Co 11–25, Cr 58–184 µg/g). Because the Bolaven basalt and its laterites are themselves rich in these elements (median Ni 160 and "
"210 µg/g), the siderophile elements do not discriminate between a projectile and a mafic or lateritic target contribution. Cu "
"(10–14 µg/g) and Zn (48–52 µg/g) are lower than in average upper crust (28 and 67 µg/g), as is commonly reported for tektites, "
"but given the calibration uncertainty and the unknown composition of the true parent we draw no inference from them.")]

R_SUM = [("Summary. ", True), (
"Within the limits of the data – four tektites with reliable major elements and two with trace elements – the geochemistry "
"establishes four points, each consistent with the regional literature. First, the tektites are sediment-dominated melts of a "
"quartz-rich sand plus a fine-grained aluminous sediment. Second, that parent was much less weathered than any Khorat sediment "
f"or regolith now exposed on the Bolaven Plateau, which cannot supply the tektites’ Ca and Na. Third, a basaltic "
f"contribution of about 5–20 % is permitted; it is required only when the model is denied an unconstrained component, and the "
f"trace-element ratios cap it at ~10 % (tholeiite) to ~20 % (alkali basalt). Fourth, LA-ICP-MS cannot detect a projectile "
"component at the ≤ 0.005 % level indicated by Os isotopes. None of these results discriminates the Bolaven location from any "
"other Indochinese source with a similar sedimentary cover; a decisive test would need analyses of unweathered Khorat sediment "
"from depth and isotopic (Sr–Nd, ¹⁰Be) comparison with the tektites.")]

CAP14 = [("Figure 14. ", True), (
"EPMA data quality and major elements. (a) Oxide totals of all 153 analyses by tektite. Filled symbols are accepted analyses "
"(≥ 97 wt%); open symbols are rejected. (b–h) Anhydrous Harker diagrams of the 82 accepted analyses, coloured by tektite, compared with "
"published Indochinite and Muong Nong tektites (grey; n = 262) and with the median compositions of the candidate source lithologies "
"(stars; this study and the compilation of Sieh et al., 2019; metatuff = felsic samples only) and of unweathered post-Archean shale (PAAS; Taylor & McLennan, 1985). "
"CaO, Na2O, MgO and K2O are on log scales to show how strongly the regional sediments and regolith are leached.")]

CAP15 = [("Figure 15. ", True), (
"Reversible-jump MCMC unmixing of the accepted tektite EPMA analyses, following the formulation of Carter et al. (2025). (a) "
"Log-likelihood and (b) number of components K for twelve chains started at K = 2–30; the dotted line marks the end of burn-in. "
"All chains reach the same quality of fit with very different K. (c) Posterior mixing weights by lithology type (mean of all "
"analyses). Bars show the mean ± 1σ, combining within- and between-chain variance; dots are chain means. (d) Per-analysis residuals "
"of the posterior-mean model. (e) Mixing weights in the sensitivity runs.")]

CAP16 = [("Figure 16. ", True), (
"Trace elements of tektites MNG24_A3_1 and MNG24_A3_2 (LA-ICP-MS). (a) Accuracy check. Red bars: LA-ICP-MS/EPMA on the same tektite "
"for four major elements. Blue bars: LA-ICP-MS relative to the median of published Indochinite and Muong Nong analyses. The shaded "
"band is ±20 %. (b) CI-chondrite-normalised REE (Sun & McDonough, 1989) compared with the literature 10–90 % range and with source "
"lithology medians. (c) Th/Sc versus Eu/Eu*, which are insensitive to the internal standard and to dilution, for the tektites, "
"the literature (Eu* from Sm and Tb), source lithologies (stars; the felsic metatuff has no trace-element data) and the bulk posterior mixtures of Fig. 15 (green; metatuff omitted).")]

CAP17 = [("Figure 17. ", True), (
"Platinum-group elements by LA-ICP-MS. (a) Reported “Pd” against Y. Small symbols are individual analyses; large symbols are "
"ablation-site means. Lines show the apparent ¹⁰⁵Pd produced by ⁸⁹Y¹⁶O⁺ at oxide production rates of 0.1–0.4 %. (b) "
"¹⁹¹Ir against ¹⁹³Ir: most analyses are zero and the non-zero values do not agree between isotopes, so Ir is below detection. (c) "
"CI-normalised Ru, Pd and Ir compared with CI chondrite, upper continental crust (Rudnick & Gao, 2003) and crust plus 0.05 % CI. "
"Detecting a projectile component at the ≤ 0.005 % level inferred from Os isotopes (Ackerman et al., 2019) is beyond LA-ICP-MS.")]

RESULTS = [('before', 14, R_INTRO), ('before', 14, R_QC), ('caption', 14, CAP14),
           ('before', 15, R_MIX), ('caption', 15, CAP15),
           ('before', 16, R_TRACE), ('caption', 16, CAP16),
           ('before', 17, R_PGE), ('caption', 17, CAP17),
           ('end', R_SUM)]

ABSTRACT_OLD = ('The source crater for the Australasian tektite strewn field', None)
ABSTRACT_NEW = (
"A parallel geochemical test points the same way. A reversible-jump Bayesian unmixing of 82 quality-screened electron-microprobe "
"analyses of four tektites shows that they are melts of a quartz-rich sand and a fine-grained aluminous sediment, consistent with "
"earlier work. A basaltic contribution of about 5–20 % is permitted, but it is required only when no unconstrained component is "
"allowed, and trace-element ratios cap it at ~10–20 %. Neither the Khorat Group sediments nor the "
"lateritic regolith now exposed on the Bolaven Plateau can be the parent as sampled: they are too leached of Ca and Na, and the "
"trace-element budget does not close with them. Iridium is below the ~4 ppb LA-ICP-MS detection limit, too high to test the trace "
"(≤ 0.005 %) chondritic component inferred from Os isotopes, and an apparent Pd signal is an analytical (YO⁺) interference. "
"Neither the magnetism nor the geochemistry therefore corroborates the impact interpretation or detects an impact-specific "
"signature. The paleomagnetism shows the volcanic stratigraphy and its radiometric framework to be more complex than previously "
"assumed. The geochemistry is consistent with a sediment-dominated Indochinese source but is not diagnostic of the Bolaven "
"location.")

EDITS = [
 ('The source crater for the Australasian tektite strewn field',
  'inverted for the tektite parent materials with a Bayesian (reversible-jump Monte-Carlo) source-unmixing model.',
  'evaluated with a reversible-jump Markov-chain Monte-Carlo source-unmixing model.'),
 ('Consistent with the magnetic data, our preliminary petrographic',
  'and no anomalous platinum-group-element or iridium enrichment have been found.',
  'have been identified, and iridium in the tektites is below the ~4 ppb detection limit of our LA-ICP-MS analyses, too high to test the trace chondritic component inferred from Os isotopes (Ackerman et al., 2019).'),
 ('The presence of both normal and reversed polarity clasts',
  'This is compatible with the geochemical evidence for incorporation of local basaltic material into the Australasian tektites (Sieh et al., 2019), though it does not by itself require an impact origin for the diamicton.',
  'This is compatible with the proposed incorporation of local basaltic material into the Australasian tektites (Sieh et al., 2019), which our unmixing permits as a minor (about 5–20 %) but not uniquely required component, and it does not by itself require an impact origin for the diamicton.'),
 ('No shock signature:',
  '(no shocked grains, no PGE/Ir anomaly)',
  '(no shocked grains; tektite Ir below the ~4 ppb LA-ICP-MS detection limit)'),
]

REF_REPLACE = [('Gallagher, K., Bodin, T., Sambridge, M.',
  'Gallagher, K., Charvin, K., Nielsen, S., Sambridge, M., Stephenson, J. (2009). Markov chain Monte Carlo (MCMC) sampling methods to determine optimal models, model resolution and model choice for Earth Science problems. Marine and Petroleum Geology, 26, 525–535.')]

REFS_ADD = [
 ('Mahgoub, Ahmed Nasser', 'Macdonald, G. A., Katsura, T. (1964). Chemical composition of Hawaiian lavas. Journal of Petrology, 5, 82–133.'),
 ('D. J. Dunlop, Ö. Özdemir', 'Carter, J., Sanchez, P., Fuentes, A. J., Renne, P. R., Burns, D. H., Bermúdez, H. D. (2025). Inferences of source lithologies for Chicxulub microtektites using a Bayesian approach. Geochemistry, Geophysics, Geosystems, 26, e2024GC011924. https://doi.org/10.1029/2024GC011924'),
 ('McFadden, P. L., McElhinny', 'McDonough, W. F., Sun, S.-S. (1995). The composition of the Earth. Chemical Geology, 120, 223–253.'),
 ('Sanematsu, K., Moriyama', 'Rudnick, R. L., Gao, S. (2003). Composition of the continental crust. In: Treatise on Geochemistry, vol. 3, pp. 1–64. Elsevier.'),
 ('Sanematsu, K., Moriyama', 'Saminpanya, S., Duangkrayom, J., Jintasakul, P., Hanta, R. (2014). Petrography, mineralogy and geochemistry of Cretaceous sediment samples from western Khorat Plateau, Thailand, and considerations on their provenance. Journal of Asian Earth Sciences, 83, 13–34.'),
]
