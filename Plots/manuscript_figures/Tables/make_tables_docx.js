// Tables 1 & 2 (updated) -> Tables_1_2_updated.docx. Data from tables_data.json (make_tables_data.py).
const fs = require('fs');
const { Document, Packer, Paragraph, TextRun, Table, TableRow, TableCell, WidthType, BorderStyle, AlignmentType,
        PageOrientation, ShadingType, VerticalAlign } = require('docx');
const D = JSON.parse(fs.readFileSync("tables_data.json", "utf8").replace(/\bNaN\b/g, "null"));
const U = Object.fromEntries(D.units.map(u => [u.unit, u]));
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

// ---------------- Table 1 ----------------
const GPS = D.gps, ll = s => [f1(GPS[s][0], 3), f1(GPS[s][1], 3)];
const T1 = [
  ['PKS-K', 'PKS24-K', 'PKSK', 'In-situ flow', '407 ± 18', 'C1n', 'N', U.PKSK.vgp_lat, 'R', 'Mismatch'],
  ['NWF-A', 'NWF24-A', 'NWFA', 'In-situ flow', '518 ± 6', 'C1n', 'N', U.NWFA.vgp_lat, 'N', 'Match'],
  ['PKS-I', 'PKS24-I / PKS15-I', 'PKSI', 'Corestone (ex situ)', '553 ± 20', 'C1n', 'N', U.PKSI.vgp_lat, 'Indet.ᵃ', 'Displaced clast'],
  ['PKS-J', 'PKS24-J', 'PKSJ', 'In-situ flow', '601 ± 44', 'C1n', 'N', U.PKSJ.vgp_lat, 'R', 'Mismatch'],
  ['PKS-HA', 'PKS24-HA', 'PKSH', 'Upper horizon', '770.5 ± 9.3', 'C1n / C1r.1rᵇ', 'N or R', null, 'R, R (64° apart)ᶜ', 'Discordant'],
  ['PKS-HB', 'PKS24-HB', 'PKSH', 'Lower flow, 5.5 m below HA', '> 770.5ᵈ', 'C1n / C1r.1rᵇ', 'N or R', U['PKSH-HB'].vgp_lat, 'R', 'Consistent if > 773 ka'],
  ['NWF-B', 'NWF24-B', 'NWFB', 'Blocks (transported)', '934 ± 30', 'C1r.1r', 'R', U.NWFB.vgp_lat, 'Indet.ᵃ', 'Random clasts (Fig. 8o)'],
  ['PKS-B', 'PKS24-BA-1', 'PKSB', 'In-situ flow', '1155 ± 2ᵉ', 'C1r.2r', 'R', U.PKSB.vgp_lat, 'R', 'Match'],
  ['WBE-A', 'WBE24-A', 'WBEA', 'Basal flow', '1397 ± 13', 'C1r.3r', 'R', U.WBEA.vgp_lat, 'R', 'Match'],
];
const ha = U['PKSH-HA'].cores.map(c => sg(c.vgp_lat, 1)).join(' / ');
const t1rows = T1.map(r => ({ cells: [r[0], r[1], ...ll(r[2]), r[3], r[4], r[5], r[6], r[7] === null ? ha : sg(r[7]), r[8], r[9]],
                              shade: r[9] === 'Mismatch' }));
const t1 = table([820, 1350, 850, 950, 1650, 1200, 1350, 950, 1200, 1350, 1950],
  ['Site', 'Sample (Sieh et al.)', 'Lat (°N)', 'Lon (°E)', 'Setting', '⁴⁰Ar/³⁹Ar age (ka ± 2σ)', 'Expected chron (GPTS 2020)', 'Exp. polarity', 'VGP lat (°)', 'Measured polarity', 'Age–polarity agreement'], t1rows);

// ---------------- Table 2 ----------------
const T2 = ['PKSK', 'NWFA', 'PKSI', 'PKSJ', 'PKSH-HA', 'PKSH-HB', 'NWFB', 'PKSB', 'WBEA'];
const AGE = { PKSK: '407 ± 18', NWFA: '518 ± 6', PKSI: '553 ± 20', PKSJ: '601 ± 44', 'PKSH-HA': '770.5 ± 9.3', 'PKSH-HB': '> 770.5',
              NWFB: '934 ± 30', PKSB: '1155 ± 2', WBEA: '1397 ± 13' };
const EXP = { PKSK: 'N', NWFA: 'N', PKSI: 'N', PKSJ: 'N', 'PKSH-HA': 'N/R', 'PKSH-HB': 'N/R', NWFB: 'R', PKSB: 'R', WBEA: 'R' };
const RES = { PKSK: 'Mismatch', NWFA: 'Match', PKSI: 'Clast', PKSJ: 'Mismatch', 'PKSH-HA': 'Discordant', 'PKSH-HB': 'Coherent',
              NWFB: 'Random (congl.)', PKSB: 'Match', WBEA: 'Match' };
const POL = u => u.unit === 'PKSI' || u.unit === 'NWFB' ? 'Indet.' : (u.vgp_lat > 0 ? 'N' : 'R');
const SHOWCORES = ['PKSK', 'PKSH-HA', 'NWFB', 'WBEA'];
const t2rows = [];
T2.forEach(k => {
  const u = U[k], single = u.ncores === 1;
  const a95 = single ? f1(u.spec_a95) + '*' : (u.a95 === null || u.a95 >= 90 ? '–' : f1(u.a95));
  const kk = single ? f1(u.spec_k) + '*' : f1(u.k);
  t2rows.push({ boldFirst: true, shade: RES[k] === 'Mismatch', cells: [u.name, AGE[k], `${u.ncores} (${u.nspec}/${u.ntot})`, f1(u.dec), sg(u.inc), a95, kk,
    sg(u.vgp_lat), f1(u.vgp_lon), POL(u), EXP[k], RES[k]] });
  if (SHOWCORES.includes(k)) u.cores.forEach(c => t2rows.push({ sub: true, cells: ['   ' + c.core.replace('PKSH-1', 'HA1').replace('PKSH-2', 'HA2'),
    '', `1 (${c.n})`, f1(c.dec), sg(c.inc), f1(c.a95), f1(c.k), sg(c.vgp_lat), '', '', '', ''] }));
});
const t2 = table([1150, 1200, 1350, 950, 950, 950, 950, 1100, 1100, 1100, 1100, 1700],
  ['Site / core', 'Age (ka ± 2σ)', 'N cores (n spec acc./meas.)', 'Dec (°)', 'Inc (°)', 'α95 (°)', 'k', 'VGP lat (°)', 'VGP lon (°E)', 'Polarity (VGP)', 'Expected (GPTS)', 'Result'], t2rows);

const sect = ch => ({ properties: { page: { size: { width: 12240, height: 15840, orientation: PageOrientation.LANDSCAPE },
  margin: { top: 1080, bottom: 1080, left: 1080, right: 1080 } } }, children: ch });
const doc = new Document({ styles: { default: { document: { run: { font: FONT, size: 20 } } } }, sections: [
 sect([
  caption('Table 1.', 'Comparison of ⁴⁰Ar/³⁹Ar ages (Sieh et al., 2019; PKS-B and PKS-H updated, K. Sieh, written communication, 2026) with measured paleomagnetic polarity for the dated Bolaven sites, in order of age. Expected chron and polarity are those spanned by the age ± 2σ on the GPTS 2020 (Ogg, 2020; Brunhes–Matuyama boundary 773 ka; Jaramillo 990–1071 ka; Cobb Mountain 1180–1215 ka). Measured polarity is assigned from the latitude of the site-mean virtual geomagnetic pole (VGP; Table 2), not from the sign of inclination. Coordinates are means of the 2024 GPS waypoints (WGS84). Shaded rows are polarity mismatches.'),
  t1,
  note('ᵃ VGP latitude between −45° and +45° (PKS-I) or a random clast population (NWF-B, Watson test, Fig. 8o): polarity not assigned.'),
  note('ᵇ The 770.5 ± 9.3 ka age (761–780 ka) spans the Brunhes–Matuyama boundary at 773 ka and the ~800–770 ka reversal-transition interval.'),
  note(`ᶜ Core-level VGP latitudes of the two PKS-HA cores (HA1 / HA2), both reversed; the cores are internally tight but 64° apart (Table 2).`),
  note('ᵈ PKS-HB is not independently dated; it underlies the dated HA horizon by 5.5 m and is therefore older than 770.5 ka.'),
  note('ᵉ Updated age for sample PKS24-BA-1 (K. Sieh, written communication, 2026); previously reported as ~1.0 Ma.'),
 ]),
 sect([
  caption('Table 2.', `Sample-to-site paleomagnetic statistics for the dated Bolaven localities, computed by specimen → sample (oriented core or block) → site Fisher (1953) averaging of the high-temperature (HT, ChRM) component in geographic coordinates (no tilt correction; flows are sub-horizontal). Specimen fits are from the pmagpy re-fits (fitquest; deposited in MagIC) and are accepted where MAD ≤ ${D.madcut}°; n spec gives accepted/measured specimens. α95 and k are core-level statistics; for single-core sites (*) they are specimen-level. Indented italic rows give individual core means where the cores of a site disagree or are few. VGPs are computed at each site's GPS coordinates (Table 1). Polarity is from VGP latitude. Dashes denote statistics that are undefined (single core) or meaningless (α95 ≥ 90°). Shaded rows are polarity mismatches.`),
  t2,
  note('Sites in order of age. PKS-H is reported as its two stratigraphic horizons (HA upper, dated; HB 5.5 m below). PKS-I and NWF-B are included for completeness: PKS-I is an ex-situ corestone and NWF-B a random clast population (conglomerate test, Fig. 8o).'),
 ]),
]});
Packer.toBuffer(doc).then(b => { fs.writeFileSync('Tables_1_2_updated.docx', b); console.log('ok'); });
