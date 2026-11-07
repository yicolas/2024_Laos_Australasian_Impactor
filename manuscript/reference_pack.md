# Reference pack — verified citations + download links (2026-11-07)

Shell downloads are blocked from the cloud workspace, so PDFs could not be fetched here.
Every link below is open-access where marked; run the wget block at the bottom on the Mac
(or click through) to collect them into `Papers/`.

## Verified and corrected in manuscript_LEAD_4/5

- **Tang, L., Zhou, W., Wang, X., Xian, F., Kong, X., Du, Y., Zhou, J., Zhao, G., Fu, Y., Chen, N.
  (2025).** ¹⁰Be records of the Matuyama–Brunhes polarity reversal in the northeastern Chinese
  Loess Plateau. *Quaternary Science Reviews*, 353, 109212.
  doi:10.1016/j.quascirev.2025.109212 — OA PDF: https://archimer.ifremer.fr/doc/00937/104914/117192.pdf
- **Mahgoub, A. N., Korte, M., Panovska, S. (2023).** Characteristics of the Matuyama–Brunhes
  magnetic field reversal based on a global data compilation. *JGR Solid Earth*, 128,
  e2022JB025286. doi:10.1029/2022JB025286 — OA copy (verify it is this paper):
  https://archimer.ifremer.fr/doc/00840/95153/102858.pdf · repo record: https://e-docs.geo-leo.de/handle/11858/11183
- **Mahgoub, A. N., Korte, M., Panovska, S., Schanner, M. (2024).** Robustness of characteristics
  of the Matuyama–Brunhes geomagnetic field reversal found in global models. *Frontiers in Earth
  Science*, 12, 1443095. doi:10.3389/feart.2024.1443095 — OA PDF:
  https://www.frontiersin.org/journals/earth-science/articles/10.3389/feart.2024.1443095/pdf
- **Suganuma, Y., Okada, M., Horie, K., Kaiden, H., Takehara, M., Senda, R., Kimura, J.-I.,
  Kawamura, K., Kazaoka, O., Head, M. J. (2015).** Age of Matuyama–Brunhes boundary constrained
  by U–Pb zircon dating of a widespread tephra. *Geology*, 43(6), 491–494. [doi:10.1130/G36625.1
  — verify] — OA copy: https://core.ac.uk/download/51489863.pdf
- **Sieh et al. crater paper → cite as 2020** (PNAS 117(3), 1346–1353; online Dec 30 2019):
  doi:10.1073/pnas.1904368116 [verify DOI]
- **Sieh et al. proximal ejecta → cite as 2024**: PNAS 121, e2400122121.
  doi:10.1073/pnas.2400122121 — https://www.pnas.org/doi/10.1073/pnas.2400122121 (+ Reply to
  Mizera & Strunga: doi:10.1073/pnas.2401580121)
- **Carter, J., Sanchez, P., Fuentes, A. J., Renne, P. R., Burns, D. H., Bermúdez, H. D. (2025).**
  Inferences of source lithologies for Chicxulub microtektites using a Bayesian approach.
  *G³*, 26, e2024GC011924. doi:10.1029/2024GC011924 (AGU OA) · code:
  doi:10.6084/m9.figshare.26972515.v2
- **Watson, G. S. (1956).** A test for randomness of directions. *MNRAS Geophysical Supplement*,
  7, 160–161. (added to refs)
- **McFadden, P. L., McElhinny, M. W. (1988).** The combined analysis of remagnetization circles
  and direct observations in palaeomagnetism. *EPSL*, 87, 161–172. (paywalled — library)

## Download block (run on the Mac in the project folder)
```bash
mkdir -p Papers && cd Papers
curl -L -o Tang_2025_QSR.pdf  "https://archimer.ifremer.fr/doc/00937/104914/117192.pdf"
curl -L -o Mahgoub_2023_JGR.pdf "https://archimer.ifremer.fr/doc/00840/95153/102858.pdf"
curl -L -o Mahgoub_2024_FrontiersES.pdf "https://www.frontiersin.org/journals/earth-science/articles/10.3389/feart.2024.1443095/pdf"
curl -L -o Suganuma_2015_Geology.pdf "https://core.ac.uk/download/51489863.pdf"
curl -L -o Carter_2025_G3.pdf "https://agupubs.onlinelibrary.wiley.com/doi/pdfdirect/10.1029/2024GC011924"
```
