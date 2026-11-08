// Tables 1 & 2 (updated) -> Tables_1_2_updated.docx. Data from tables_data.json (make_tables_data.py).
const fs = require('fs');
const { Document, Packer, Paragraph, TextRun, Table, TableRow, TableCell, WidthType, BorderStyle, AlignmentType,
        PageOrientation, ShadingType, VerticalAlign } = require('docx');
const X = JSON.parse(fs.readFileSync("extra_data.json", "utf8").replace(/\bNaN\b/g, "null"));
const FONT = 'Times New Roman', SZ = 18;               // 9 pt
const f1 = (x, d = 1) => (x === null || x === undefined || Number.isNaN(Number(x))) ? '–' : Number(x).toFixed(d).replace('-', '−');
const sg = (x, d = 1) => (Number(x) >= 0 ? '+' : '') + f1(x, d);
const run = (t, o = {}) => new TextRun({ text: t, font: FONT, size: o.size || SZ, bold: o.bold, italics: o.italics, superScript: o.sup });
function para(parts, o = {}) {
  parts = typeof parts === 'string' ? [run(parts, o)] : parts;
  return new Paragraph({ children: parts, alignment: o.align || AlignmentType.CENTER, spacing: { before: 20, after: 20 } });
}
const NONE = { style: BorderStyle.NONE, size: 0, color: 'FFFFFF' };
const RULE = { style: BorderStyle.SINGLE, size: 6, color: '000000' };
function cell(content, w, o = {}) {
  return new TableCell({
    width: { size: w, type: WidthType.DXA }, verticalAlign: VerticalAlign.CENTER,
    margins: { top: 30, bottom: 30, left: 60, right: 60 },
    shading: o.shade ? { type: ShadingType.CLEAR, fill: 'F2F2F2', color: 'auto' } : undefined,
    borders: { top: o.top ? RULE : NONE, bottom: o.bottom ? RULE : NONE, left: NONE, right: NONE },
    children: [para(content, { align: o.align, bold: o.bold, italics: o.italics })] });
}
function table(widths, header, rows) {
  const total = widths.reduce((a, b) => a + b, 0);
  const tr = [new TableRow({ tableHeader: true, children: header.map((h, i) => cell(h, widths[i], { top: true, bottom: true, bold: true, align: i === 0 ? AlignmentType.LEFT : AlignmentType.CENTER })) })];
  rows.forEach((r, j) => {
    const last = j === rows.length - 1;
    tr.push(new TableRow({ children: r.cells.map((c, i) => cell(c, widths[i], { bottom: last, italics: r.sub, shade: r.shade,
      align: i === 0 ? AlignmentType.LEFT : AlignmentType.CENTER, bold: r.boldFirst && i === 0 })) }));
  });
  return new Table({ width: { size: total, type: WidthType.DXA }, columnWidths: widths, rows: tr });
}
const caption = (lab, text) => new Paragraph({ spacing: { before: 120, after: 80 }, children: [run(lab + ' ', { bold: true, size: 20 }), run(text, { size: 20 })] });
const note = text => new Paragraph({ spacing: { before: 30, after: 0 }, children: [run(text, { size: 16 })] });


const pm = (m, sd) => `${f1(m)} ± ${f1(sd)}`;
// ---------------- Table 3: conglomerate tests ----------------
const t3 = table([900, 1500, 900, 650, 650, 650, 1150, 600, 650, 800, 1000],
  ['Locality', 'Units tested', 'N (n spec)', 'R', 'Ro95', 'Ro99', 'Clast mean D/I (°)', 'k', 'α95 (°)', 'R (lines + planes)', 'Verdict'],
  X.t3.map(r => ({ shade: r.verdict === 'Clustered', cells: [r.site, r.mat, `${r.N} (${r.nspec})`, f1(r.R, 2), f1(r.r95, 2), f1(r.r99, 2),
    `${f1(r.dec, 0)}/${sg(r.inc, 0)}`, f1(r.k), r.a95 >= 90 ? '–' : f1(r.a95, 0), f1(r.lp, 2), r.verdict] })));
// ---------------- Table 4: rj-MCMC weights ----------------
const RUNS = ['main', 'no_random', 'no_alkali', 'local_only'];
const ROWS = [['Khorat sandstone', 'Khorat sandstone'], ['Khorat mudstone', 'Khorat mudstone'], ['Unweathered shale (PAAS)', 'Unweathered shale (PAAS)'],
  ['Metatuff', 'Felsic metatuff'], ['Bolaven tholeiite', 'Bolaven tholeiite'], ['Bolaven alkali basalt', 'Bolaven alkali basalt'], ['All basalt', 'All basalt (sum)'],
  ['Lateritic saprolite', 'Lateritic saprolite'], ['Sedimentary laterite', 'Sedimentary laterite / bauxite'], ['Diamicton / "catastro-loess"', 'Diamicton / loess'], ['Random', 'Random (unconstrained)']];
const t4 = table([2400, 1750, 1750, 1750, 1750],
  ['Lithology type', `Full model (${X.t4n.main} chains)`, `No random (${X.t4n.no_random})`, `Na₂O, K₂O excluded (${X.t4n.no_alkali})`, `Regional only (${X.t4n.local_only})`],
  ROWS.map(([k, lab]) => ({ boldFirst: k === 'All basalt', cells: [lab, ...RUNS.map(r => X.t4[r][k] ? `${pm(X.t4[r][k].mean, X.t4[r][k].sd)} (${f1(100 * X.t4[r][k].p_present, 0)})` : 'excluded')] })));
// ---------------- Table S2: rock-magnetic pairs ----------------
const ts2 = table([1000, 1250, 1300, 950, 750, 750, 750, 1000, 1000, 800, 800],
  ['Site', 'Setting', 'Sample', 'Chip', 'Mass (g)', 'Hc (mT)', 'Hcr (mT)', 'Mr (µA m²)', 'Ms (µA m²)', 'Mr/Ms', 'Hcr/Hc'],
  X.ts2.map((r, i) => ({ shade: r.state === 'weathered', cells: [i % 2 ? '' : r.site, i % 2 ? '' : r.kind, i % 2 ? '' : r.sample, r.state, f1(r.mass, 3), f1(r.Hc, 1), f1(r.Hcr, 1), f1(r.Mr, 1), f1(r.Ms, 1), f1(r.MrMs, 3), f1(r.HcrHc, 2)] })));
// ---------------- Table S3: paleomagnetic sample inventory ----------------
const ts3 = table([900, 950, 950, 1700, 800, 1900, 1100, 1100, 1250, 1000],
  ['Site', 'Lat (°N)', 'Lon (°E)', 'Setting', 'Sample type', 'Orientation', 'Cores / blocks', 'Specimens', 'HT accepted (MAD ≤ 15°)', 'Component fits'],
  X.ts3.map(r => ({ cells: [r.site, f1(r.lat, 4), f1(r.lon, 4), r.setting, r.stype, r.orient, String(r.nsamp), String(r.nspec), String(r.nacc), String(r.nfits)] })));
// ---------------- Table S4: tektites ----------------
const ts4 = table([1600, 3000, 1300, 1500, 1800, 1800],
  ['Tektite', 'Locality', 'EPMA spots', 'Accepted (≥ 97 wt%)', 'Total range (wt%)', 'LA-ICP-MS'],
  X.ts4.map(r => ({ shade: r.nacc === 0, cells: [r.tek, r.loc, String(r.n), String(r.nacc), `${f1(r.tmin, 1)}–${f1(r.tmax, 1)}`, r.la] })));
const sect = ch => ({ properties: { page: { size: { width: 12240, height: 15840, orientation: PageOrientation.LANDSCAPE },
  margin: { top: 1080, bottom: 1080, left: 1080, right: 1080 } } }, children: ch });
const doc = new Document({ styles: { default: { document: { run: { font: FONT, size: 20 } } } }, sections: [
 sect([caption('Table 3.', 'Conglomerate tests on the six boulder and diamicton localities (Fig. 7o–t). Specimen HT (ChRM) directions with MAD ≤ 15° were averaged to their parent boulder, block or core, and the unit means were tested for randomness with the Watson (1956) resultant-length test. Ro95 and Ro99 are the critical resultant lengths for N random unit vectors from 2 × 10⁵ Monte-Carlo draws. R < Ro95: the clast directions are random and the clasts were magnetized before deposition (test passes). R ≥ Ro95: they are clustered (test fails). Clast mean = Fisher mean of the unit means. The lines-and-planes column repeats the test with unresolved specimens treated as remagnetization circles (McFadden & McElhinny, 1988). PKQ-A is tested on its three field boulders (cores 0–4, 5–6 and 7–9). Tests with N = 3 (NWF-B, PKQ-A, PKS-H) have little power. Shaded rows fail.'), t3,
  new Paragraph({ children: [] }),
  caption('Table S5.', 'Posterior mixing weights (wt%, mean ± 1σ combining within- and between-chain variance) of each lithology type in the reversible-jump MCMC unmixing of the 82 accepted EPMA analyses (Fig. 5k, m). The number in parentheses is the percentage of posterior samples in which the type is present. Full model: 12 chains × 6 × 10⁴ iterations; sensitivity runs: 4 chains × 3 × 10⁴ iterations. "Excluded" marks types removed from the dictionary in that run.'), t4]),
 sect([
  caption('Table S3.', 'Hysteresis parameters of the seven fresh-interior / weathered-rind chip pairs plotted in Fig. 4c (MicroMag VSM; Hc and Mr/Ms from the slope-corrected loops, Hcr from backfield remanence). Shaded rows are weathered chips. PKS24-I and PKS24-HB were filed as PKQ24-… in the instrument files.'), ts2,
  new Paragraph({ children: [] }),
  caption('Table S1.', 'Paleomagnetic sample inventory. Coordinates are means of the 2024 GPS waypoints (WGS84). Orientation from the sample-header files: sun compass, or magnetic compass corrected to IGRF declination. Specimens: thermally demagnetized specimens with fitted components; HT accepted: specimens whose HT (ChRM) fit has MAD ≤ 15°; component fits: all LT, MT and HT fits.'), ts3,
  new Paragraph({ children: [] }),
  caption('Table S2.', 'Tektites analysed in this study. EPMA spots with oxide totals below 97 wt% are rejected (shaded: no accepted analyses). LA-ICP-MS: five ablation sites with five replicates each.'), ts4]),
]});
Packer.toBuffer(doc).then(b => { fs.writeFileSync('Tables_3_4_S.docx', b); console.log('ok'); });
