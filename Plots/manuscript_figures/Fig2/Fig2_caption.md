# Figure 2 — caption draft

**Figure 2.** (a) Geologic map of southern Laos and the Bolaven Plateau showing the paleomagnetic sites of this study: in situ basalt flows (red circles), basalt clasts in diamicton sampled for conglomerate tests (blue triangles), and the anomalous corestone locality PKS-I (white diamond). Geology within Laos from the 1998 Geological Map of Lao PDR (digitised for this study); geology of neighbouring Thailand, Cambodia and Vietnam (faded) generalised from the USGS Geology of Southeast Asia (Steinshouer et al., 1999, OFR 97-470-F, after UNESCO/CGMW, 1990) and reclassified to the Lao map units. Dashed black outline: Bouguer gravity anomaly; dotted magenta outline: geologic crater outline of the proposed source crater (Sieh et al., 2020). Box shows the area of (b). (b) Enlargement of the central Bolaven Plateau sites; PKS-B, -G and -H lie within ~200 m of one another. (c) Location of (a) in mainland Southeast Asia.

## Notes for Nick
- Inside Laos the polygons are your `geo_polygons.shp` (99.7% coverage of southern Laos, clipped to the Lao border); Pgr was merged into γ (granitoids).
- Pz₂ / Pz₃ legend descriptions ("Middle/Upper Paleozoic sedimentary rocks") are placeholders — check against the 1998 map legend.
- geo3bl → Lao-legend reclassification: Q, TQ → Q; NQ/TQ volcanics → Qβ; K → Mz₃; J, JK, TrJ → Mz₂; Tr, PTr → Mz₁; CmO, OS → Pz₁; D, DC, PZ, PZMZ → Pz₂; CP, P, PZu → Pz₃; any intrusive (TYPE = i) → γ; Pt* → PR. Approximate correlations only (Khorat Group J–K ≈ Mz₂–Mz₃).
- Town positions for Pakse, Salavan, Attapeu, Champasak and Khong Sedone come from the GCPs you placed on the 1998 map; Paksong is approximate.
- Site positions = mean of the 2024 GPS waypoints per site (all_samples_laos.shp); PKS-G = the PKS24-HF waypoints.
- QGIS project has Esri World Imagery and Esri World Hillshade basemaps (off by default; they load with internet) if you want relief under the faded neighbour geology.
