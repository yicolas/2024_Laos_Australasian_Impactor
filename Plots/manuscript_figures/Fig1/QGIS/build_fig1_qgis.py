"""PyQGIS (3.40): build Fig1_strewn_field.qgz with styled layers + 'Figure 1' print layout.
Run with the QGIS python; paths are stored relative so the folder can be moved."""
import sys, os
from qgis.core import *
from qgis.PyQt.QtGui import QColor, QFont
from qgis.PyQt.QtCore import QPointF, QSizeF, Qt

GPKG = os.path.abspath(sys.argv[1]); OUTQ = os.path.abspath(sys.argv[2]); PDF = sys.argv[3] if len(sys.argv) > 3 else None
app = QgsApplication([], False); app.initQgis()
P = QgsProject.instance(); P.setCrs(QgsCoordinateReferenceSystem('EPSG:4326'))
P.setFilePathStorage(Qgis.FilePathType.Relative)
P.setFileName(OUTQ)

def L(name, title=None):
    lyr = QgsVectorLayer(f'{GPKG}|layername={name}', title or name, 'ogr'); assert lyr.isValid(), name
    P.addMapLayer(lyr, False); return lyr
def fill(color, outline=None, w=0):
    return QgsFillSymbol.createSimple({'color': color, 'outline_color': outline or 'transparent', 'outline_width': str(w), 'outline_style': 'solid' if outline else 'no'})
def line(color, w, dash=None):
    s = QgsLineSymbol.createSimple({'line_color': color, 'line_width': str(w), 'line_width_unit': 'MM'})
    if dash: s.symbolLayer(0).setUseCustomDashPattern(True); s.symbolLayer(0).setCustomDashVector(dash)
    return s
def marker(shape, color, size, outline='white', ow=0.15):
    return QgsMarkerSymbol.createSimple({'name': shape, 'color': color, 'size': str(size), 'outline_color': outline, 'outline_width': str(ow)})

land = L('ne_land', 'Land'); land.setRenderer(QgsSingleSymbolRenderer(fill('#e9e6df', '#8a8578', 0.1)))
bord = L('ne_borders', 'Country borders'); bord.setRenderer(QgsSingleSymbolRenderer(line('#a8a39a', 0.12, [2, 1.5])))
rings = L('distance_rings', 'Great-circle distance from crater')
rings.setRenderer(QgsSingleSymbolRenderer(line('#9a9a9a', 0.15, [0.6, 0.8]))); rings.setSubsetString('"radius_km" >= 2000')
rings_r = L('distance_rings', 'Distance from crater (inset, 100 km)')
rings_r.setRenderer(QgsSingleSymbolRenderer(line('#9a9a9a', 0.15, [0.6, 0.8]))); rings_r.setSubsetString('"radius_km" <= 400')
outl = L('strewn_field_outline', 'Strewn-field limit'); outl.setRenderer(QgsSingleSymbolRenderer(line('#3b3b3b', 0.4, [3, 1.5])))

deep = L('microtektites_deepsea', 'Microtektites, deep-sea cores (>125 µm cm⁻²)')
sym = marker('circle', '#2c6fb0', 2.2)
# size by log10 abundance (data-defined)
sym.setDataDefinedSize(QgsProperty.fromExpression('1.2 + 1.1*log10(max(coalesce("abundance_mt_per_cm2",30),1))'))
deep.setRenderer(QgsSingleSymbolRenderer(sym))
ant = L('microtektites_antarctic', 'Microtektites, Antarctica'); ant.setRenderer(QgsSingleSymbolRenderer(marker('diamond', '#2a9d8f', 2.4)))

tek = L('tektites', 'Tektites')
cats = [('Muong Nong-type (layered)', marker('square', '#c2410c', 1.3, 'transparent', 0)),
        ('Splash-form, SE Asia', marker('star', '#7b3294', 2.2, 'transparent', 0)),
        ('Australites', marker('star', '#1b1b1b', 2.2, 'transparent', 0)),
        ('This study (EPMA)', marker('circle', '#ffd23f', 2.4, 'black', 0.2))]
tek.setRenderer(QgsCategorizedSymbolRenderer('tektite_class', [QgsRendererCategory(v, s, v) for v, s in cats]))
crat = L('source_crater', 'Proposed source crater'); crat.setRenderer(QgsSingleSymbolRenderer(marker('star', '#d62728', 5, 'black', 0.25)))
inset_box = L('inset_extent', 'Inset extent'); inset_box.setRenderer(QgsSingleSymbolRenderer(fill('transparent', 'black', 0.3)))
cl = L('core_labels', 'Core labels'); cl.setRenderer(QgsSingleSymbolRenderer(marker('circle', 'transparent', 0.1, 'transparent', 0)))

def labels(lyr, field, size=6, color='#333333', place=None, dist=1.2):
    s = QgsPalLayerSettings(); s.fieldName = field
    f = QgsTextFormat(); f.setFont(QFont('Arial')); f.setSize(size); f.setColor(QColor(color))
    b = QgsTextBufferSettings(); b.setEnabled(True); b.setSize(0.6); b.setColor(QColor(255, 255, 255, 200)); f.setBuffer(b)
    s.setFormat(f); s.dist = dist
    if place is not None: s.placement = place
    lyr.setLabeling(QgsVectorLayerSimpleLabeling(s)); lyr.setLabelsEnabled(True)
labels(cl, 'label', 6)
labels(rings, 'label', 5.5, '#7a7a7a', Qgis.LabelPlacement.Line)
labels(rings_r, 'label', 5, '#7a7a7a', Qgis.LabelPlacement.Line)

root = P.layerTreeRoot()
for lyr in [crat, tek, cl, ant, deep, outl, rings, rings_r, inset_box, bord, land]:
    root.addLayer(lyr)

# ---------------- layout ----------------
lm = P.layoutManager(); lay = QgsPrintLayout(P); lay.initializeDefaults(); lay.setName('Figure 1')
pc = lay.pageCollection(); pc.page(0).setPageSize(QgsLayoutSize(180, 158, QgsUnitTypes.LayoutMillimeters))

m = QgsLayoutItemMap(lay); m.setId('Main map')
m.attemptMove(QgsLayoutPoint(8, 3, QgsUnitTypes.LayoutMillimeters)); m.attemptResize(QgsLayoutSize(170, 118, QgsUnitTypes.LayoutMillimeters))
m.setLayers([crat, tek, cl, ant, deep, outl, rings, inset_box, bord, land]); m.setKeepLayerSet(True)
m.setExtent(QgsRectangle(14, -88, 192, 40)); m.setFrameEnabled(True)
g = m.grid(); g.setEnabled(True); g.setIntervalX(20); g.setIntervalY(20); g.setStyle(QgsLayoutItemMapGrid.Solid)
g.setGridLineColor(QColor('#d0d0d0')); g.setGridLineWidth(0.1); g.setAnnotationEnabled(True)
g.setAnnotationFormat(QgsLayoutItemMapGrid.DegreeMinuteNoSuffix if False else QgsLayoutItemMapGrid.DecimalWithSuffix)
g.setAnnotationPrecision(0)
af = QgsTextFormat(); af.setFont(QFont('Arial')); af.setSize(6); g.setAnnotationTextFormat(af)
for side in [QgsLayoutItemMapGrid.Top, QgsLayoutItemMapGrid.Right]: g.setAnnotationDisplay(QgsLayoutItemMapGrid.HideAll, side)
lay.addLayoutItem(m)

ins = QgsLayoutItemMap(lay); ins.setId('Inset Indochina')
ins.attemptMove(QgsLayoutPoint(9.5, 4.5, QgsUnitTypes.LayoutMillimeters)); ins.attemptResize(QgsLayoutSize(44, 31, QgsUnitTypes.LayoutMillimeters))
ins.setLayers([crat, tek, rings_r, bord, land]); ins.setKeepLayerSet(True)
ins.setExtent(QgsRectangle(100.5, 12.8, 108.8, 18.6)); ins.setFrameEnabled(True); ins.setBackgroundColor(QColor('white'))
lay.addLayoutItem(ins)

leg = QgsLayoutItemLegend(lay); leg.setId('Legend'); leg.setLinkedMap(m); leg.setAutoUpdateModel(False)
leg.setTitle(''); lt = leg.model().rootGroup(); lt.clear()
for lyr in [crat, tek, deep, ant, outl, rings]: lt.addLayer(lyr)
for st in [QgsLegendStyle.SymbolLabel, QgsLegendStyle.Group, QgsLegendStyle.Subgroup]:
    f = QgsTextFormat(); f.setFont(QFont('Arial')); f.setSize(6); leg.rstyle(st).setTextFormat(f)
leg.setColumnCount(3); leg.setSymbolHeight(2.5); leg.setSymbolWidth(3.5); leg.setSplitLayer(True); leg.setBoxSpace(1.5); leg.setColumnSpace(3)
leg.attemptMove(QgsLayoutPoint(14, 128, QgsUnitTypes.LayoutMillimeters)); leg.setFrameEnabled(True)
lay.addLayoutItem(leg)

lab = QgsLayoutItemLabel(lay); lab.setText('Australasian tektite/microtektite strewn field')
f = QgsTextFormat(); f.setFont(QFont('Arial', 7, -1, True)); f.setSize(7); lab.setTextFormat(f)
lab.attemptMove(QgsLayoutPoint(118, 95, QgsUnitTypes.LayoutMillimeters)); lab.adjustSizeToText(); lay.addLayoutItem(lab)
lm.addLayout(lay)

P.write(OUTQ); print('wrote', OUTQ)
if PDF:
    ex = QgsLayoutExporter(lay); s = QgsLayoutExporter.PdfExportSettings(); s.rasterizeWholeImage = False
    print('pdf', ex.exportToPdf(PDF, s)); ims = QgsLayoutExporter.ImageExportSettings(); ims.dpi = 200
    print('png', ex.exportToImage(PDF.replace('.pdf', '.png'), ims))
app.exitQgis()
