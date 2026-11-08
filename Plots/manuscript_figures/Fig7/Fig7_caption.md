# Figure 7 — Paleomagnetic directions, VGPs and conglomerate tests (was Fig 8; replaces LEAD_4 Figs 11–13)

(consolidates LEAD_4 Figs 12 and 13; all directions in geographic coordinates — no tilt correction is applied: the flows are sub-horizontal and the diamictons have no bedding control)

**Figure 7.** Equal-area projections of the component directions from all twelve Bolaven sites. Filled symbols are on the lower hemisphere and open symbols on the upper. Stars mark the geocentric axial dipole (GAD) direction at the site latitude (I = ±28.5°; filled = normal, open = reversed).

**(a)** Site-mean ChRM (HT) directions for the in-situ flows, computed specimen → core → site (Fisher, 1953) with α95. Colours give VGP polarity: blue normal, red reversed. Orange marks the two discordant PKS-HA cores, which are plotted individually and joined. The grey diamond is the PKS-I corestone. The inset table lists each site's declination/inclination, α95, number of cores N and VGP latitude/longitude.

**(b)** Site VGPs on a north-polar equal-area map. Reversed VGPs are plotted as their antipodes (open symbols), and A95 is drawn where α95 ≤ 60°. The dashed circle at 45° latitude separates stable-polarity from transitional VGPs. The triangle marks the sampling area.

Only specimen fits with MAD ≤ 15° are used throughout.

**(c–n)** Every site, in order of ⁴⁰Ar/³⁹Ar age and then the diamicton localities. Grey symbols are all specimen component fits. Squares are the specimen-level Fisher means of the low-temperature (LT, green), mid-temperature (MT, blue) and high-temperature (HT = ChRM, purple) components, each with its α95. Colours match Fig. 6 and the fitquest fitting interface. Each stats box gives D/I, α95, k and n for each component. PKQ-A is treated as a conglomerate of three field boulders (B1 = cores 0–4, B2 = cores 5–6, B3 = cores 7–9), so panel l shows boulder means rather than a site mean, and its stats box lists the HT mean of each boulder.

**(o–t)** Conglomerate tests on the six boulder and diamicton localities. Purple squares are boulder-mean HT directions, each with its α95. Grey symbols are the specimens. The black square is the mean of the clast population. Randomness was tested with the Watson (1956) resultant-length test. Critical values Ro95 and Ro99 come from 2 × 10⁵ Monte-Carlo draws of N random unit vectors. R < Ro95 means the population is random (the test passes: the clasts carry pre-depositional remanences). R ≥ Ro95 means it is clustered (the test fails). PKQ-A was tested on its three field boulders. For PKS-F, the McFadden & McElhinny (1988) lines-and-planes result, with unresolved specimens treated as remagnetization circles, is also given. PKS-H was tested on its three cores (HA1, HA2, HB1); with N = 3 the test has little power.

α95 circles larger than 60° are reported in the stats boxes but not drawn.

Script: `make_fig7.py` with the shared module `pmag_sites.py` (reads the corrected `pmagpy_fits` MagIC tables). Run with `python make_fig8.py <pmagpy_fits_dir> <outdir>`. The test numbers are also written to `Fig7_conglomerate_tests.json`.
