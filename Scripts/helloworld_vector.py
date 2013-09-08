# get active layer
layer = iface.activeLayer()

# select all features
layer.selectAll()

# meta data about layer
layer.featureCount()
layer.metadata()

# qgis data provider
layer.dataProvider()

# geometry type
layer.geometryType()

# get feature from selected features
# returns a list of features
feats = layer.selectedFeatures()
# get first one
feat = feats[0]

# get geometry of feat
geom = feat.geometry()

# get vertexs
pts = geom.asPolyline()

# number of vertexes
len(pts)

## calculate the length between each vertex
# crude
d1 = pts[1][0] - pts[0][0]
# TODO: dev way to do all segments

## calculate azimuth between 2 points
p1 = QgsPoint(pts[0][0],pts[0][1])
p2 = QgsPoint(pts[1][0],pts[1][1])
p1.azimuth(p2)

# TODO: dev way to calc between all segments

