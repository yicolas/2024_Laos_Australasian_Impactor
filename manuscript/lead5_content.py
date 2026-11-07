# -*- coding: utf-8 -*-
"""Condensed main-text content for manuscript_LEAD_5 (MAPS split).
Each entry: (style, segments) where segments = [(text, fmt)], fmt in {None,'b','i'}.
Figure/table placement markers: ('FIG', key) and ('TABLE', n) handled by the builder.
"""
AR = '⁴⁰Ar/³⁹Ar'
DEG = '°'
PM = ' ± '
MI = '−'
EN = '–'

ABSTRACT = (
 'The source crater of the Australasian tektite strewn field is proposed to lie buried beneath '
 'the Bolaven Plateau volcanic field in southern Laos. We present the first paleomagnetic test of '
 'this hypothesis, together with new tektite and target-rock geochemistry, using ~80 oriented '
 'samples from 12 basalt localities. Rock-magnetic and SEM/EDS data show primary titanomagnetite '
 'partially oxidized to maghemite by lateritic weathering yet retaining stable '
 'pseudo-single-domain remanence; no shock-related magnetic phases are present. Watson '
 'conglomerate tests show that boulders at two diamicton localities carry random, '
 'pre-depositional magnetizations ' + EN + ' consistent with, but not diagnostic of, ballistic '
 'ejecta ' + EN + ' while two others fail as weathered in-situ flows and two are statistically '
 'indeterminate. Magnetic polarities match ' + AR + ' ages at only three of six dated flows; two '
 'reversed flows with Brunhes ages require redating, and the flow thought to span the '
 'Brunhes' + EN + 'Matuyama boundary is internally discordant, so no in-situ reversal record is '
 'confirmed. Reversible-jump Bayesian unmixing of 82 quality-screened tektite analyses requires '
 'a sediment-dominated parent less weathered than any exposed Khorat Group rock, permits at most '
 '~10' + EN + '20% basalt, and cannot discriminate Bolaven from other Indochinese sources. The '
 'hypothesis survives both tests but gains no independent support; the volcanic chronology '
 'needs revision first.'
)

MAIN = []
def H1(t): MAIN.append(('Heading 1', [(t, None)]))
def H2(t): MAIN.append(('Heading 2', [(t, None)]))
def P(*segs): MAIN.append(('Body Text', list(segs)))
def FIG(key): MAIN.append(('FIG', key))
def TAB(n): MAIN.append(('TABLE', n))

# ----------------------------------------------------------- 1 INTRODUCTION
H1('Introduction')
P(('The Australasian tektite strewn field is the largest known on Earth, covering ~20% of the '
   'eastern hemisphere from Indochina to Antarctica (Glass, 1994; Folco et al., 2010) (Fig. 1). '
   'The glassy impact melts that define it formed at 788' + PM + '3 ka (Jourdan et al., 2019; '
   'Schwarz et al., 2016), yet after a century of searching their source crater remains '
   'unidentified. Tektite abundances, sizes and geochemistry point to an impact site in central '
   'Indochina onto quartz-rich siliciclastic sediments with a minor mafic component (Koeberl, '
   '1992; Blum et al., 1992; Amare & Koeberl, 2006; Goderis et al., 2017).', None))
P(('Sieh et al. (2020) proposed that the crater lies buried beneath the Bolaven Plateau '
   'volcanic field in southern Laos (Fig. 2), citing tektite chemistry consistent with mixing of '
   'local sandstone and basalt, pre- and post-impact lava flows able to bury a crater, a '
   'negative Bouguer gravity anomaly of appropriate size, proximal breccias with shocked quartz '
   '(Sieh et al., 2024), and a capping tektite-bearing diamicton. The hypothesis is contested: '
   'Mizera (2022) argues on geochemical and sedimentological grounds that the Bolaven candidate '
   'fails, and that the diamicton is ordinary loess and alluvium. The debate has so far lacked an '
   'independent physical test.', None))
P(('Paleomagnetism offers one. Magnetic polarities of dated flows test the ' + AR + ' framework '
   'that underpins the burial argument; conglomerate tests on diamicton boulders establish '
   'whether they were magnetized before or after deposition; rock magnetism can reveal '
   'shock-related phases; and the impact’s timing ' + EN + ' within the extended '
   '(~800' + EN + '770 ka) transitional interval of the Brunhes' + EN + 'Matuyama (B' + EN + 'M) '
   'reversal (Singer et al., 2019; Mahgoub et al., 2024) ' + EN + ' makes any in-situ record of '
   'the reversal at Bolaven doubly valuable. Here we present the first paleomagnetic and '
   'magnetostratigraphic study of the Bolaven volcanic field, with new rock-magnetic, SEM/EDS and '
   'tektite geochemical data, as an independent test of the impact hypothesis.', None))

FIG('fig1')
FIG('fig2')

# ----------------------------------------------------------- 2 GEOLOGICAL SETTING
H1('Geological Setting')
P(('The Bolaven Plateau rises ~1 km above the surrounding lowlands of southern Laos, east of the '
   'Mekong River (Fig. 2). It is underlain by nearly flat-lying Jurassic' + EN + 'Cretaceous '
   'Khorat Group red beds, at least 500 m thick: an upper 200' + EN + '250 m of massive to '
   'cross-bedded quartz-rich fluvial sandstone over ~250 m of friable mudstone and siltstone '
   '(Fig. 3b). These two lithologies ' + EN + ' a mature quartz arenite and an '
   'illite/kaolinite-rich mudrock ' + EN + ' are the compositional poles from which any '
   'Bolaven-sourced tektite must be built, and their laterally uniform blanket geometry means '
   'ejecta or melt from anywhere in the Khorat Basin would inherit a similar bulk composition '
   '(Sieh et al., 2020). Prolonged tropical weathering has converted the exposed Mesozoic and '
   'basaltic surfaces alike to laterite, bauxite and saprolite, strongly leached of Ca, Na and '
   'other mobile elements (Sanematsu et al., 2011).', None))
P(('A basaltic volcanic field of ~5,000 km² and ~910 km³ caps the plateau, reaching '
   '300 m thickness in the summit region ' + EN + ' sufficient to hide a crater up to 15 km in '
   'diameter. ' + AR + ' ages span ~16 Ma to 27 ka, with eruptions before and after the 790 ka '
   'impact; flows directly above the proposed crater centre are all younger than 790 ka, '
   'supporting burial (Sieh et al., 2020). The field is a typical intraplate assemblage of '
   'scattered scoria cones and fissure-fed flows with no large central volcano, making a buried '
   'caldera unlikely (Valentine & Gregg, 2008).', None))
P(('The candidate impact deposits are the youngest element: an unsorted, matrix-supported '
   'polymict breccia exposed 10' + EN + '20 km southeast of the proposed centre, with '
   'stratigraphic inversion, jigsaw-fit clasts and quartz grains carrying planar deformation '
   'features, overlain by a massive sandy silt ("catastro-loess") containing tektite fragments '
   '(Sieh et al., 2024) (Fig. 3c). Mizera (2022) interprets the same deposits as fluvial and '
   'aeolian. The boulder-bearing diamicton that hosts our conglomerate-test sites belongs to this '
   'contested unit.', None))
P(('The impact at ~790 ka barely predates the B' + EN + 'M reversal, whose directional midpoint '
   'is at 773' + PM + '3 ka but whose full process ' + EN + ' dipole collapse below ~5 ZAm², '
   'precursory transitional episodes, completion at ~773' + EN + '768 ka ' + EN + ' spans roughly '
   '800' + EN + '770 ka (Singer et al., 2019; Mahgoub et al., 2023, 2024); new ¹⁰Be '
   'records independently anchor the boundary at 773' + PM + '3 ka (Tang et al., 2025). The '
   'impact therefore fell within the reversal’s transitional interval, so pre-impact flows '
   'should be reversed, immediately post-impact flows could record transitional directions, and '
   'any impact-reset magnetization would have recorded a weak, unstable field.', None))

FIG('fig3')

# ----------------------------------------------------------- 3 METHODS
H1('Methods')
H2('Sampling and laboratory procedures')
P(('We collected 64 oriented drill cores and block samples (364 specimens) from 12 basalt '
   'localities across the '
   'Bolaven Plateau in November 2023 (Fig. 2; Tables 1, S1): six interpreted in-situ flows for '
   'magnetostratigraphy and six boulder populations in diamicton for conglomerate testing. '
   'Orientations used sun compass where possible, with magnetic-declination corrections '
   'otherwise. Block samples were re-oriented in the laboratory and cored; all specimens were '
   'measured on a 2G Enterprises three-axis SQUID magnetometer in the magnetically shielded room '
   'at Caltech. Specimens underwent progressive thermal demagnetization, typically in '
   '30' + DEG + 'C steps, with alternating-field demagnetization of pilot specimens; full '
   'protocols are given in Supporting Information Text S2.', None))
H2('Paleomagnetic analysis')
P(('Characteristic remanent magnetizations (ChRM) were fit by principal component analysis '
   '(Kirschvink, 1980) with MAD ≤ 15' + DEG + '; free-line fits were additionally required to '
   'trend toward the origin (deviation angle ≤ 15' + DEG + '). Because fine-grained '
   'maghemite breaks down on heating, demagnetization could not usefully proceed beyond '
   '~450' + EN + '510 ' + DEG + 'C, and specimens that failed to isolate a stable endpoint below '
   'that ceiling were fit as remagnetization circles and combined with the lines by the method of '
   'McFadden & McElhinny (1988). Site statistics follow a specimen → oriented core → '
   'site Fisher hierarchy, and polarity is assigned from virtual geomagnetic pole (VGP) latitude '
   'rather than inclination sign, which matters for the shallow, anomalously declined directions '
   'encountered here. Conglomerate tests use the Watson (1956) randomness test on boulder-mean '
   'directions, with critical values from Monte Carlo simulation (10⁶ draws), and every '
   'verdict was double-checked with lines-plus-circles boulder means (Text S2). All analyses used '
   'PmagPy; fits and data are archived in the MagIC database (see Data Availability).', None))
H2('Rock magnetism and electron microscopy')
P(('Hysteresis loops, back-field curves and first-order reversal curves (FORCs) were measured on '
   'paired fresh-interior and weathered-rind chips with a Princeton Measurements vibrating sample '
   'magnetometer at the University of Tokyo, and low-temperature remanence cycling on a Quantum '
   'Design MPMS (Fig. 4). Opaque phases in a fresh basalt were identified by SEM with '
   'energy-dispersive spectroscopy (Fig. 4k,l; Table S4). Petrographic screening for shock features '
   'used transmitted-light microscopy and SEM.', None))
H2('Tektite and target-rock geochemistry')
P(('Major elements of seven Australasian tektites from Laos and Thailand were measured by EPMA '
   '(153 spots); analyses with oxide totals below 97 wt% were rejected as compromised, following '
   'Carter et al. (2025), leaving 82 analyses on four tektites. Trace elements were measured by '
   'LA-ICP-MS on two tektites; absolute concentrations are accurate to no better than '
   '±30%, so interpretation relies on calibration-insensitive ratios (Th/Sc, Eu/Eu*, '
   'rare-earth pattern shape). Candidate target rocks (Khorat sandstone and mudstone, basalt, '
   'saprolite, diamicton) were analysed by XRF and ICP-MS and combined with the regional '
   'compilation of Sieh et al. (2020), screened and divided into tholeiitic and alkaline basalt '
   'suites (Macdonald & Katsura, 1964). Tektite source lithologies were inferred with a '
   're-implementation of the reversible-jump Bayesian unmixing model of Carter et al. (2025); '
   'instrument details, priors and sensitivity runs are given in Text S2 and S4.', None))

# ----------------------------------------------------------- 4 RESULTS
H1('Results')
H2('Rock magnetism and magnetic mineralogy')
P(('Paired fresh' + EN + 'weathered measurements show a single coherent story (Fig. 4): the '
   'carrier is fine-grained, low-coercivity titanomagnetite (SEM/EDS: FeO 63' + EN + '74 wt%, '
   'TiO₂ 16' + EN + '22 wt%; Fig. 4k,l; Table S4) progressively oxidized to (titano)maghemite in '
   'lateritic rinds. Hysteresis loops close by ~300 mT with no high-coercivity phase; all '
   'specimens plot in the pseudo-single-domain (PSD) field of the Day plot, and every one of '
   'seven fresh→weathered pairs shifts the same way, weathering lowering the squareness '
   'ratio (mean Mᵣ/Mₛ 0.29 → 0.23) independent of site type or eruption age '
   '(553' + EN + '1155 ka). Low-temperature remanence of the most weathered clast shows no '
   'Verwey transition, confirming oxidation of primary magnetite. FORC diagrams show a '
   'weakly-interacting central ridge at 10' + EN + '17 mT in both states; the anomalous '
   'corestone PKS-I is the exception, with a multidomain-like fresh interior (≤5 mT) and a '
   '~15 mT weathered rind. Thermal demagnetization loses most remanence by ~450 ' + DEG + 'C '
   'even under nitrogen, consistent with fine-grained maghemite inversion (Dunlop & Özdemir, '
   '1997); this sets the demagnetization ceiling used throughout. Critically, no shock-related '
   'phases ' + EN + ' anomalous coercivities, strong interactions, or exotic oxide compositions '
   + EN + ' are present in any sample. Weathering, not impact processing, controls the magnetic '
   'mineralogy; per-site details are given in Text S3.', None))
FIG('fig4'); FIG('fig5')
H2('Polarity of dated flows and magnetostratigraphy')
P(('Six localities of interpreted in-situ flows with ' + AR + ' ages (Sieh et al., 2020), plus '
   'the two-horizon locality PKS-H, were tested against the geomagnetic polarity timescale '
   '(Fig. 3a; Tables 1, 2). An updated age of 1155' + PM + '2 ka for the PKS-B flow (sample '
   'PKS24-BA-1; K. Sieh, written communication, 2026) supersedes the preliminary '
   '906' + PM + '12 ka assignment and places that flow in the C1r.2r reversed subchron.', None))
P(('Three flows match expectation. NWF-A (518' + PM + '6 ka) is normal (five cores: dec = '
   '11.8' + DEG + ', inc = +23.7' + DEG + ', k = 43, VGP +78' + DEG + '), consistent with its '
   'Brunhes age (Fig. 6a). PKS-B (1155 ka) and WBE-A (1397' + PM + '13 ka) are reversed with '
   'near-dipole directions (190.6' + DEG + '/' + MI + '10.6' + DEG + ' and 168.1' + DEG + '/'
   + MI + '34.5' + DEG + '; VGPs ' + MI + '76' + DEG + ' and ' + MI + '78' + DEG + '), '
   'consistent with their Matuyama ages (Fig. 6c,d) and anchoring the pre-impact stratigraphy.', None))
P(('Two flows contradict their ages. PKS-J (601' + PM + '44 ka) and PKS-K (407' + PM + '18 ka) '
   'both carry well-defined reversed magnetizations (174.9' + DEG + '/' + MI + '31.9' + DEG + ', '
   'k = 244; 195.1' + DEG + '/' + MI + '33.2' + DEG + ') despite Brunhes-age assignments that '
   'predict normal polarity (Fig. 6b). The tight, near-dipole reversed directions argue against '
   'remagnetization; the flows are most simply older than 773 ka ' + EN + ' kipukas of older '
   'lava within younger fields, or mis-assigned dates ' + EN + ' and both are being resampled '
   'for redating. PKS-I (553' + PM + '20 ka) is a lone roadside corestone with a tightly '
   'clustered direction (47.9' + DEG + '/' + MI + '35.6' + DEG + ', k = 330) ~49' + DEG + ' from '
   'any dipole direction and a VGP latitude of +31' + DEG + ': a rotated, displaced block that '
   'cannot test its assigned age.', None))
P(('PKS-H, interpreted by Sieh et al. (2020) as an in-situ flow at the B' + EN + 'M boundary '
   '(770.5' + PM + '9.3 ka), resolves into two units. The upper horizon (HA) yields two '
   'internally tight cores (k = 96 and 157) whose means diverge by 64' + DEG + ' (Fig. 6e,f): it '
   'cannot be an intact cooling unit. The lower boulder horizon (HB) is coherent (209.6' + DEG +
   '/+7.9' + DEG + ', k = 549) and demagnetizes univectorially (Fig. 6g). Assigned by VGP '
   'latitude, all three cores are reversed (' + MI + '53' + DEG + ', ' + MI + '65' + DEG + ', '
   + MI + '55' + DEG + ') ' + EN + ' HA2’s positive inclination is offset by its SSW '
   'declination ' + EN + ' yet all sit 34' + EN + '46' + DEG + ' from the reversed dipole, and '
   'HA2 and HB1 lie within 15' + DEG + ' of each other. The units either record the anomalous '
   'transitional field of the latest Matuyama, consistent with the impact falling inside the '
   'reversal’s transitional window (Mahgoub et al., 2024), or share a common '
   'post-emplacement rotation; one core per boulder cannot separate these. Either way, HA’s '
   'internal discordance means no in-situ B' + EN + 'M boundary is confirmed at this locality; '
   'the boulders are being redated.', None))
P(('In sum, the magnetostratigraphy anchors the framework at three flows but contradicts it at '
   'two, reclassifies one site as a clast and one as disturbed (Figs. 6i, 7a,b). The ' + AR + ' '
   'chronology that underpins the burial argument is therefore more complex than previously '
   'assumed, and its revision is prerequisite to tying the volcanic stratigraphy to the impact.', None))
FIG('fig6'); TAB(1); TAB(2); FIG('fig7'); FIG('fig8')
H2('Conglomerate tests of the diamicton boulders')
P(('Six boulder populations were tested with the Watson (1956) randomness test on boulder-mean '
   'directions (Fig. 7o' + EN + 't, Table 3; critical values Ro by Monte Carlo). Random, pre-depositional '
   'magnetizations indicate transported clasts; clustering indicates an in-situ flow weathered '
   'into corestones or post-depositional remagnetization. All verdicts are unchanged when '
   'unresolved specimens contribute remagnetization circles instead of lines (McFadden & '
   'McElhinny, 1988).', None))
P(('Two localities pass. NWF-C (eight boulders) is unambiguously random (R = 3.26 < '
   'Ro₉₅ = 4.48), with boulder means spanning all quadrants and both polarities. NWF-B '
   '(three boulders), originally sampled as an in-situ flow, has internally tight but mutually '
   'discordant cores and passes as a conglomerate (R = 2.38 < 2.62): transported boulders, '
   'consistent with its stream-bed setting, whose 934 ka date therefore cannot anchor '
   'polarity.', None))
P(('Two localities fail. PKS-G (eight boulders) clusters strongly (R = 6.58 > '
   'Ro₉₉ = 5.26) around a shallow southeasterly reversed direction: an in-situ, '
   'pre-reversal flow weathered into separated corestones, not ejecta; a boulder has been '
   'collected for redating to test this. PKS-F (eleven boulders) appeared to pass in early '
   'fitting rounds but fails under every quality-controlled treatment (screened lines '
   'R = 5.31 > 5.28; lines-plus-circles R = 6.09 > 5.28): seven boulders share a NE-shallow '
   'direction ~130' + DEG + ' from the reversal-era field and ~50' + DEG + ' from the present '
   'field ' + EN + ' neither an impact-age nor a modern overprint, but either a secondary '
   'component unremovable below the maghemite ceiling or in-place corestones of an anomalously '
   'directed flow (only ~30' + DEG + ' from PKS-I).', None))
P(('Two are indeterminate. PKQ-A fails at the ten-core level (R = 7.27 > 5.03) ' + EN + ' the '
   'cores group into three internally coherent, mutually discordant boulders ' + EN + ' and is '
   'random only at the powerless three-boulder grouping (R = 2.25 < 2.62); it is qualitatively '
   'consistent with transport but statistically unproven. PKS-H’s three cores are likewise '
   'formally random (R = 2.50 < 2.62) without power at N = 3.', None))
P(('The passes at NWF-C and NWF-B rule out in-situ formation there, a necessary condition for '
   'ballistic ejecta ' + EN + ' but fluvial or mass-wasting reworking randomizes clasts equally '
   'well (Mizera, 2022), so the test cannot by itself establish an impact origin. The failures '
   'are equally instructive: boulder trains in this deeply weathered terrain cannot be assigned '
   'to the diamicton by field appearance alone. Per-boulder statistics are tabulated in Text '
   'S3.', None))
FIG('fig9')
H2('Tektite geochemistry')
P(('Only 82 of 153 EPMA analyses, on four tektites, have oxide totals ≥ 97 wt% (Fig. 5a); '
   'the accepted analyses lie within the published Indochinite field on every Harker diagram, '
   'and the two tektites with LA-ICP-MS data reproduce the regional trace-element signature '
   '(Th/Sc = 1.14 and 1.20, Eu/Eu* = 0.69 and 0.66). Reversible-jump unmixing of the accepted '
   'analyses (Fig. 5i' + EN + 'm) constrains the type of parent material even though the number of '
   'components is unconstrained: a quartz-rich sand classified as Khorat sandstone '
   '(29' + PM + '17%) is required; the deeply weathered lithologies that now cover the plateau '
   '(saprolite, laterite, the diamicton itself) are not used; and the balance must be a '
   'fine-grained aluminous sediment carrying ~1.5' + EN + '2 wt% each of CaO and Na₂O ' + EN +
   ' which no sampled Khorat rock supplies, because all are intensely leached (median CaO ≤ '
   '0.04 wt%). The model assigns that component to unweathered-shale (37' + PM + '25%) and '
   'metatuff (15' + PM + '8%) proxies for unleached fine-grained material, i.e., the '
   'tektite parent was much less weathered than anything now exposed.', None))
P(('Basalt is permitted but not demanded: 5' + PM + '4% in the main run ' + EN + ' with an '
   'unconstrained "random" component taking 11' + PM + '10%, itself a sign that the dictionary '
   'lacks an adequate parent ' + EN + ' and no more than ~10% in any sensitivity variant, becoming '
   'required only when the model is denied that component. Trace-element ratios cap the basaltic contribution '
   'independently ' + EN + ' ~10% tholeiite or ~20% alkali basalt brings Th/Sc down to the '
   'tektite value, and more alkali basalt pushes Eu/Eu* out of range ' + EN + ' while absolute '
   'Zr and Th are under-predicted by the posterior mixtures, mirroring the major-element result '
   'that the sampled endmembers are inadequate. Iridium is below the ~4 ppb detection limit, two orders '
   'of magnitude above the ≤0.005% chondritic component indicated by Os isotopes (Ackerman '
   'et al., 2019), and the apparent Pd signal is an ⁸⁹Y¹⁶O⁺ '
   'interference (Fig. S4), so no projectile test is possible with these data. The mild '
   'Ni' + EN + 'Cr' + EN + 'Co enrichment of the tektites is matched by weathered basalt and '
   'carries no meteoritic fingerprint. None of these results discriminates the Bolaven location '
   'from any other Indochinese source with similar sedimentary cover; details, data-quality '
   'figures and sensitivity runs are given in Fig. 5m, Fig. S1 and Table S5.', None))
FIG('fig10')

# ----------------------------------------------------------- 5 DISCUSSION
H1('Discussion')
H2('A fair but non-confirmatory test')
P(('Our results are best read as a secondary, and largely non-confirmatory, test of the Bolaven '
   'impact hypothesis. The basalts are high-fidelity recorders ' + EN + ' stable, '
   'single-component ChRMs carried by PSD grains ' + EN + ' so the lack of any positive impact '
   'signature is not a consequence of poor material. The conglomerate tests isolate two '
   'diamicton localities whose clasts were magnetized before deposition, which excludes in-situ '
   'formation there but cannot separate ballistic emplacement from ordinary sedimentary '
   'transport; the other four boulder populations are not demonstrably transported at all, and '
   'two are most simply weathered in-situ flows. The resolution of PKS-H into a disturbed upper '
   'horizon and a coherent reversed lower unit shows both the difficulty of field identification '
   'in deeply weathered terrain and the value of VGP-based polarity assignment; its far-sided '
   'reversed directions permit ' + EN + ' but do not prove ' + EN + ' a record of the '
   'transitional late-Matuyama field in which the impact occurred.', None))
P(('The magnetostratigraphy does not corroborate the published ' + AR + ' chronology. Only '
   'NWF-A, PKS-B (at its revised 1155 ka age) and WBE-A carry the expected polarity; PKS-J and '
   'PKS-K are reversed where Brunhes ages predict normal; NWF-B and PKS-I are not in-situ flows '
   'at all. Rather than validating the age framework, the paleomagnetism indicates that several '
   'units are mis-dated or misidentified ' + EN + ' a complication that must be resolved before '
   'the volcanic stratigraphy can date the burial of the proposed crater. Redating of PKS-J, '
   'PKS-K, the PKS-G corestones and the PKS-H boulders is underway.', None))
H2('No impact-imposed magnetization')
P(('The impact fell in the reversed, transitional latest Matuyama, so any clast heated above its '
   'Curie temperature at 790 ka would have acquired a common reversed-to-transitional '
   'thermoremanence ' + EN + ' as the Muong Nong tektites did (Gattacceca et al., 2022) ' + EN +
   ' and a suite of such clasts would fail the conglomerate test with a shared reversed '
   'direction. Instead the passing diamicton sites retain diverse polarities including normal: '
   'the clasts were emplaced cold and never thermally reset. The same logic applies to the '
   'pre-impact flows, where any impact reset would have recorded the weak transitional field '
   'rather than a stable dipole direction: WBE-A, the oldest and stratigraphically lowest flow, '
   'where shock and heating should be greatest, carries a tight, dipole-consistent primary '
   'remanence, as does PKS-B despite its field designation as "shockwave breccia." At the '
   'locations where an impact overprint should be strongest, none is resolved. Paleomagnetism '
   'thus rejects hot emplacement or impact reheating for every unit sampled ' + EN + ' a real, '
   'if negative, constraint: if these diamicton boulders are ejecta, they travelled and landed '
   'cold.', None))
H2('Implications for the Bolaven hypothesis')
P(('The geochemistry points the same way as the magnetism. The tektite parent was a quartz-rich '
   'sand plus a fine-grained, unleached aluminous sediment with ~5' + EN + '20% basalt permitted '
   'and ~10' + EN + '20% as the upper bound '
   + EN + ' consistent with a Khorat-type target anywhere in Indochina, and specifically '
   'inconsistent with the deeply weathered rocks now exposed on the plateau. A decisive '
   'geochemical test would require unweathered Khorat sediment from depth and isotopic '
   '(Sr' + EN + 'Nd, ¹⁰Be) comparison; a decisive magnetic test would have to target '
   'the tektite-bearing diamicton itself, which is too magnetically incoherent to measure by '
   'standard methods. Neither our magnetism nor our geochemistry refutes the Bolaven hypothesis '
   + EN + ' burial by post-impact flows survives both ' + EN + ' but after this first independent '
   'test the hypothesis rests where it did: on the gravity anomaly, the proximal breccia, and a '
   'volcanic chronology that our data show needs revision. While our dataset provides no '
   'evidence for impact-triggered geomagnetic change, the coincidence of the impact with the '
   'B' + EN + 'M transitional interval warrants continued attention as candidate sections are '
   'dated.', None))

# ----------------------------------------------------------- 6 CONCLUSIONS
H1('Conclusions')
P(('1. Bolaven basalts carry stable PSD titanomagnetite/maghemite remanence despite intense '
   'lateritic weathering, and none of 364 specimens shows shock-related magnetic phases.', None))
P(('2. Watson conglomerate tests show boulders at NWF-C and NWF-B were magnetized before '
   'deposition (transport required, impact not); PKS-G and PKS-F fail as weathered in-situ '
   'flows; PKQ-A and PKS-H are statistically indeterminate. Boulder fields in this terrain '
   'cannot be assigned to the ejecta-bearing diamicton by field appearance alone.', None))
P(('3. Magnetic polarity matches the ' + AR + ' ages at only three of six dated flows; PKS-J '
   'and PKS-K require redating, and no in-situ Brunhes' + EN + 'Matuyama boundary is confirmed. '
   'The chronology underpinning the burial argument needs revision.', None))
P(('4. The tektite parent was a sediment-dominated, little-weathered Khorat-type target; basalt '
   'is permitted at ~5' + EN + '20% and capped by trace-element ratios at ~10' + EN + '20%. No '
   'projectile signature is detectable at available limits. Nothing in either dataset '
   'discriminates Bolaven from other Indochinese candidates.', None))
P(('The Bolaven impact hypothesis survives this first paleomagnetic test uncontradicted but '
   'unconfirmed. The way forward is concrete: redate the discordant flows, sample unweathered '
   'Khorat sediment at depth, and develop methods capable of interrogating the diamicton '
   'itself.', None))
