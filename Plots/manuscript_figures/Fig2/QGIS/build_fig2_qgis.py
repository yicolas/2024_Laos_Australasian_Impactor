"""PyQGIS 3.40: Fig2_southern_Laos.qgz — styled layers + 'Figure 2' print layout
(regional geology map, Bolaven zoom inset, SE Asia locator, legend, scale bar, north arrow)."""
import sys, os
from qgis.core import *
from qgis.PyQt.QtGui import QColor, QFont
from qgis.PyQt.QtCore import QPointF

GPKG = os.path.abspath(sys.argv[1]); OUTQ = os.path.abspath(sys.argv[2]); PDF = sys.argv[3] if len(sys.argv) > 3 else None
app = QgsApplication([], False); app.initQgis()
P = QgsProject.instance(); P.setCrs(QgsCoordinateReferenceSystem('EPSG:32648'))
P.setFilePathStorage(Qgis.FilePathType.Relative); P.setFileName(OUTQ)
MM = QgsUnitTypes.LayoutMillimeters

def L(name, title, subset=None):
    l = QgsVectorLayer(f'{GPKG}|layername={name}', title, 'ogr'); assert l.isValid(), name
    if subset: l.setSubsetString(subset)
    l.setCrs(QgsCoordinateReferenceSystem('EPSG:4326'))
    P.addMapLayer(l, False); return l
def fill(c, oc='#6e6e6e', ow=0.08):
    return QgsFillSymbol.createSimple({'color': c, 'outline_color': oc, 'outline_width': str(ow)})
def line(c, w, dash=None):
    s = QgsLineSymbol.createSimple({'line_color': c, 'line_width': str(w)})
    if dash: s.symbolLayer(0).setUseCustomDashPattern(True); s.symbolLayer(0).setCustomDashVector(dash)
    return s
def mk(shape, c, size, oc='black', ow=0.2):
    return QgsMarkerSymbol.createSimple({'name': shape, 'color': c, 'size': str(size), 'outline_color': oc, 'outline_width': str(ow)})
def tf(size, color='#222222', bold=False, italic=False, buf=True):
    f = QgsTextFormat(); fo = QFont('Arial'); fo.setBold(bold); fo.setItalic(italic); f.setFont(fo); f.setSize(size); f.setColor(QColor(color))
    if buf:
        b = QgsTextBufferSettings(); b.setEnabled(True); b.setSize(0.5); b.setColor(QColor(255, 255, 255, 220)); f.setBuffer(b)
    return f
def lab(l, expr, fmt, placement=None, dist=1.0, ddx=None, ddy=None, isexpr=True):
    s = QgsPalLayerSettings(); s.fieldName = expr; s.isExpression = isexpr; s.setFormat(fmt); s.dist = dist
    if placement is not None: s.placement = placement
    if ddx:
        s.placement = Qgis.LabelPlacement.OverPoint
        p = s.dataDefinedProperties(); p.setProperty(QgsPalLayerSettings.OffsetXY, QgsProperty.fromExpression(f'array({ddx},{ddy}*-1)'))
        s.offsetUnits = QgsUnitTypes.RenderMillimeters
        cs = s.callout() if False else None
    s.displayAll = True
    l.setLabeling(QgsVectorLayerSimpleLabeling(s)); l.setLabelsEnabled(True)

UNITS = [('Q', '#fdf5b0', 'Q — Alluvium (Mekong and Sekong rivers)'),
         ('QB', '#f6bf9f', 'Qβ — Alkaline basalt'),
         ('Mz3', '#9fd39a', 'Mz₃ — Riverine sandstones, evaporites'),
         ('Mz2', '#c9dbee', 'Mz₂ — Marine sandstones, coal'),
         ('Mz1', '#c1a7d8', 'Mz₁ — Marine clastics, rhyolite, dacite, tuff'),
         ('Pz3', '#e6edb4', 'Pz₃ — Upper Paleozoic sandstone, shale, limestone, volcanics'),
         ('Pz2', '#ddd0a6', 'Pz₂ — Middle Paleozoic mudrock, sandstone, limestone, volcanics'),
         ('Pz1', '#8ed1d8', 'Pz₁ — Lower Paleozoic mudrock, sandstone, wacke, volcanics'),
         ('Tgr', '#e0675c', 'γ — Granitoids'),
         ('PR', '#ece3f4', 'PR — Proterozoic gneiss, schist'),
         ('H2O', '#bfe3f5', 'Water')]
def geo_renderer(opacity_outline='#6e6e6e', water=True):
    cats = [QgsRendererCategory(u, fill(c, opacity_outline, 0.06), t) for u, c, t in UNITS if water or u != 'H2O']
    return QgsCategorizedSymbolRenderer('unit', cats)

# basemaps (render only with internet; off by default)
def xyz(name, url, zmax=19):
    l = QgsRasterLayer(f'type=xyz&url={url}&zmax={zmax}&zmin=0', name, 'wms'); P.addMapLayer(l, False); return l
img = xyz('Esri World Imagery', 'https://server.arcgisonline.com/ArcGIS/rest/services/World_Imagery/MapServer/tile/%7Bz%7D/%7By%7D/%7Bx%7D')
hs = xyz('Esri World Hillshade', 'https://services.arcgisonline.com/arcgis/rest/services/Elevation/World_Hillshade/MapServer/tile/%7Bz%7D/%7By%7D/%7Bx%7D', 16)

geo_in = L('geology', 'Geology, Laos (1998 Geological Map of Lao PDR)', '"in_laos" = 1'); geo_in.setRenderer(geo_renderer(water=False))
geo_out = L('geology', 'Geology, neighbouring countries (USGS geo3bl, generalised)', '"in_laos" = 0')
geo_out.setRenderer(geo_renderer('#9a9a9a')); geo_out.setOpacity(0.5)
riv = L('rivers', 'Rivers'); riv.setRenderer(QgsSingleSymbolRenderer(line('#3a8fd0', 0.45)))
lab(riv, 'name', tf(5.5, '#2a6fb0', italic=True), Qgis.LabelPlacement.Curved, isexpr=False)
flt = L('faults', 'Faults'); flt.setRenderer(QgsSingleSymbolRenderer(line('#1a1a1a', 0.35)))
lb = L('laos_border', 'Laos border'); lb.setRenderer(QgsSingleSymbolRenderer(line('#444444', 0.35, [3, 1, 0.5, 1])))
crat = L('crater_outlines', 'Crater outlines')
crat.setRenderer(QgsCategorizedSymbolRenderer('name', [
    QgsRendererCategory('gravity crater', QgsFillSymbol.createSimple({'color': '0,0,0,0', 'outline_color': '#111111', 'outline_width': '0.5', 'outline_style': 'dash'}), 'Bouguer gravity anomaly (Sieh et al., 2020)'),
    QgsRendererCategory('geology crater', QgsFillSymbol.createSimple({'color': '0,0,0,0', 'outline_color': '#b5179e', 'outline_width': '0.45', 'outline_style': 'dot'}), 'Geologic crater outline (Sieh et al., 2020)')]))
SITE = lambda: [('In situ basalt flow', mk('circle', '#d7191c', 2.8)),
        ('Basalt clasts in diamicton (conglomerate test)', mk('triangle', '#2c7bb6', 3.0)),
        ('Anomalous corestone (ex situ)', mk('diamond', '#ffffff', 2.8))]
sites = L('paleomag_sites', 'Paleomagnetic sites (this study)')
sites.setRenderer(QgsCategorizedSymbolRenderer('site_type', [QgsRendererCategory(v, s, v) for v, s in SITE()]))
lab(sites, '"label_main"', tf(6, bold=True), Qgis.LabelPlacement.AroundPoint, dist=1.2)
sites_z = L('paleomag_sites', 'Paleomagnetic sites (zoom labels)')
sites_z.setRenderer(QgsCategorizedSymbolRenderer('site_type', [QgsRendererCategory(v, s, v) for v, s in SITE()]))
lab(sites_z, '"site"', tf(6, bold=True), ddx='"lab_dx"', ddy='"lab_dy"')
towns = L('towns', 'Towns'); towns.setRenderer(QgsSingleSymbolRenderer(mk('circle', '#ffffff', 1.6, '#111111', 0.3)))
lab(towns, 'name', tf(6, '#111111'), Qgis.LabelPlacement.AroundPoint, dist=0.8, isexpr=False)
cty = L('country_labels', 'Country names'); cty.setRenderer(QgsSingleSymbolRenderer(mk('circle', '#00000000', 0.1, '#00000000', 0)))
lab(cty, 'name', tf(7, '#7a7a7a', bold=True, buf=False), Qgis.LabelPlacement.OverPoint, isexpr=False)
zbox = L('zoom_extent', 'Zoom extent'); zbox.setRenderer(QgsSingleSymbolRenderer(fill('#00000000', '#000000', 0.35)))
land = L('land_regional', 'Land (locator)'); land.setRenderer(QgsSingleSymbolRenderer(fill('#e4e1da', '#9c978d', 0.1)))
nb = L('borders_ne', 'Borders (locator)'); nb.setRenderer(QgsSingleSymbolRenderer(line('#9c978d', 0.15)))
fbox = L('fig2_extent', 'Figure 2 extent'); fbox.setRenderer(QgsSingleSymbolRenderer(fill('#00000000', '#d7191c', 0.5)))

root = P.layerTreeRoot()
for l in [sites, sites_z, towns, cty, crat, flt, riv, lb, zbox, geo_in, geo_out, fbox, nb, land, hs, img]:
    root.addLayer(l)
for l in [sites_z, fbox, nb, land, hs, img]:
    root.findLayer(l.id()).setItemVisibilityChecked(False)

utm = QgsCoordinateReferenceSystem('EPSG:32648'); wgs = QgsCoordinateReferenceSystem('EPSG:4326')
xf = QgsCoordinateTransform(wgs, utm, P)
def ext(x0, y0, x1, y1): return xf.transformBoundingBox(QgsRectangle(x0, y0, x1, y1))

lay = QgsPrintLayout(P); lay.initializeDefaults(); lay.setName('Figure 2')
lay.pageCollection().page(0).setPageSize(QgsLayoutSize(180, 178, MM))
def grid(m, step, size=5.5):
    g = m.grid(); g.setEnabled(True); g.setCrs(wgs); g.setIntervalX(step); g.setIntervalY(step)
    g.setStyle(QgsLayoutItemMapGrid.Solid); g.setGridLineColor(QColor(80, 80, 80, 120)); g.setGridLineWidth(0.1)
    g.setAnnotationEnabled(True); g.setAnnotationFormat(QgsLayoutItemMapGrid.DegreeMinute); g.setAnnotationPrecision(0)
    g.setAnnotationTextFormat(tf(size, buf=False))
    for side in [QgsLayoutItemMapGrid.Right, QgsLayoutItemMapGrid.Top]: g.setAnnotationDisplay(QgsLayoutItemMapGrid.HideAll, side)
    g.setAnnotationDirection(QgsLayoutItemMapGrid.Vertical, QgsLayoutItemMapGrid.Left)
    g.setFrameStyle(QgsLayoutItemMapGrid.InteriorTicks if False else QgsLayoutItemMapGrid.NoFrame)

main = QgsLayoutItemMap(lay); main.setId('Main map')
main.attemptMove(QgsLayoutPoint(8, 3, MM)); main.attemptResize(QgsLayoutSize(118, 108, MM))
main.setLayers([sites, towns, cty, crat, flt, riv, lb, zbox, geo_in, geo_out]); main.setKeepLayerSet(True)
main.setCrs(utm); main.zoomToExtent(ext(105.35, 14.45, 107.65, 16.3)); main.setFrameEnabled(True); grid(main, 0.5)
lay.addLayoutItem(main)

zoom = QgsLayoutItemMap(lay); zoom.setId('Bolaven zoom')
zoom.attemptMove(QgsLayoutPoint(129, 3, MM)); zoom.attemptResize(QgsLayoutSize(48, 44, MM))
zoom.setLayers([sites_z, towns, crat, flt, riv, geo_in]); zoom.setKeepLayerSet(True)
zoom.setCrs(utm); zoom.zoomToExtent(ext(106.07, 15.085, 106.39, 15.30)); zoom.setFrameEnabled(True); grid(zoom, 0.1, 5)
lay.addLayoutItem(zoom)

loc = QgsLayoutItemMap(lay); loc.setId('Locator')
loc.attemptMove(QgsLayoutPoint(129, 50, MM)); loc.attemptResize(QgsLayoutSize(48, 40, MM))
loc.setLayers([fbox, nb, land]); loc.setKeepLayerSet(True); loc.setCrs(wgs)
loc.setExtent(QgsRectangle(96, 6, 114, 24)); loc.setFrameEnabled(True); loc.setBackgroundColor(QColor('#eef6fb'))
lay.addLayoutItem(loc)

sb = QgsLayoutItemScaleBar(lay); sb.setLinkedMap(main); sb.setStyle('Single Box'); sb.setUnits(QgsUnitTypes.DistanceKilometers)
sb.setUnitLabel('km'); sb.setNumberOfSegments(2); sb.setNumberOfSegmentsLeft(0); sb.setUnitsPerSegment(25); sb.setHeight(1.5)
sb.setTextFormat(tf(6, buf=False)); sb.attemptMove(QgsLayoutPoint(11, 101, MM)); sb.setBackgroundEnabled(True)
lay.addLayoutItem(sb)
na = QgsLayoutItemPicture(lay); na.setPicturePath(':/images/north_arrows/layout_default_north_arrow.svg')
na.setLinkedMap(main); na.setNorthMode(QgsLayoutItemPicture.GridNorth)
na.attemptMove(QgsLayoutPoint(117, 96, MM)); na.attemptResize(QgsLayoutSize(6, 10, MM)); lay.addLayoutItem(na)

leg = QgsLayoutItemLegend(lay); leg.setId('Legend'); leg.setLinkedMap(main); leg.setAutoUpdateModel(False); leg.setTitle('')
rg = leg.model().rootGroup(); rg.clear()
gg = rg.addGroup('Geology (1998 Geological Map of Lao PDR; outside Laos: USGS OFR 97-470-F, faded)')
gg.addLayer(geo_in)
og = rg.addGroup('Other features')
for l in [sites, crat, flt, riv, lb, towns]: og.addLayer(l)
for st in [QgsLegendStyle.SymbolLabel, QgsLegendStyle.Group, QgsLegendStyle.Subgroup]:
    leg.rstyle(st).setTextFormat(tf(6, buf=False, bold=(st == QgsLegendStyle.Group)))
leg.setColumnCount(2); leg.setSymbolHeight(2.6); leg.setSymbolWidth(4.5); leg.setSplitLayer(True)
leg.setBoxSpace(1.5); leg.setColumnSpace(4)
# hide layer-name headers (show only class symbols)
for l in [geo_in, sites, crat]:
    n = leg.model().rootGroup().findLayer(l.id()); QgsLegendRenderer.setNodeLegendStyle(n, QgsLegendStyle.Hidden)
leg.attemptMove(QgsLayoutPoint(8, 114, MM)); leg.setFrameEnabled(False)
lay.addLayoutItem(leg); leg.updateLegend()

for t, x, y in [('a', 9, 4), ('b', 130, 4), ('c', 130, 51)]:
    lb_ = QgsLayoutItemLabel(lay); lb_.setText(t); lb_.setTextFormat(tf(9, bold=True)); lb_.attemptMove(QgsLayoutPoint(x, y, MM))
    lb_.adjustSizeToText(); lay.addLayoutItem(lb_)
P.layoutManager().addLayout(lay)
P.write(OUTQ); print('wrote', OUTQ)
if PDF:
    ex = QgsLayoutExporter(lay); s = QgsLayoutExporter.PdfExportSettings(); s.rasterizeWholeImage = False
    print('pdf', ex.exportToPdf(PDF, s)); i = QgsLayoutExporter.ImageExportSettings(); i.dpi = 300
    print('png', ex.exportToImage(PDF.replace('.pdf', '.png'), i))
app.exitQgis()
