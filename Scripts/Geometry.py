import arcpy

arcpy.env.overwriteOutput = True
arcpy.env.workspace = r"D:\Learning\iti\CoursesDoc\GIS\Course10_ArcPY\LPA\Projects\GeomProject\GeomProject.gdb"

geomList = arcpy.CopyFeatures_management("FishnetPolys",arcpy.Geometry())
area = 0.0
for geom in geomList:
    if area == 0.0:
        sr = geom.spatialReference
    area += geom.area
print("Spatial Reference of Fishnet is: ",sr.name)  
print("Total Area of Fishnet is: ",area)

pt = arcpy.Point(2.5,1.75)
ptGeom = arcpy.PointGeometry(pt)
arcpy.CopyFeatures_management(ptGeom,"ptGeom")

pt1 = arcpy.Point(2.5,1.75)
pt1Geom = arcpy.PointGeometry(pt1) 
pt2 = arcpy.Point(7.5,1.25)
pt2Geom = arcpy.PointGeometry(pt2)
pt3 = arcpy.Point(2.75,1.5)
pt3Geom = arcpy.PointGeometry(pt3)
arcpy.CopyFeatures_management([pt1Geom,pt2Geom,pt3Geom],"ptGeom2")

coordLists = [[(1.1,2.4),(4.9,2.6),(3.2,7.3)],[(6.1,8.8),(5.2,7.6),(7.1,2.3),(9.1,5.3)]]
multiPtGeom = []
for coorList in coordLists:
    multiPtGeom.append(
        arcpy.Multipoint(
            arcpy.Array([arcpy.Point(*coor) for coor in coorList])
            )
        )
arcpy.CopyFeatures_management(multiPtGeom,"multiPtGeom")
#----------------------------------------------------------------------------------------------
polyLineGeom = []
for coorList in coordLists:
    polyLineGeom.append(arcpy.Polyline(arcpy.Array([arcpy.Point(*coor) for coor in coorList])))
arcpy.CopyFeatures_management(polyLineGeom,"polyLineGeom")
#----------------------------------------------------------------------------------------------
polygonGeom = []
for coorList in coordLists:
    polygonGeom.append(arcpy.Polygon(arcpy.Array([arcpy.Point(*coor) for coor in coorList])))
arcpy.CopyFeatures_management(polygonGeom,"polygonGeom")
#----------------------------------------------------------------------------------------------
arryList1 = []
for coorList in coordLists:
    arryList1.append(
        arcpy.Array([arcpy.Point(*coor) for coor in coorList]))
    
multipartLineGeom = arcpy.Polyline(arcpy.Array(arryList1))
arcpy.CopyFeatures_management(multipartLineGeom,"multipartLineGeom")
#----------------------------------------------------------------------------------------------
arrayList2 = []
for coorList in coordLists:
    arrayList2.append(
        arcpy.Array([arcpy.Point(*coor) for coor in coorList])
    )
multipartPolygonGeom = arcpy.Polygon(arcpy.Array(arrayList2))    
arcpy.CopyFeatures_management(multipartPolygonGeom,"multipartPolygonGeom")
#----------------------------------------------------------------------------------------------
bufferGeom = multipartPolygonGeom.buffer(0.5)
arcpy.CopyFeatures_management(bufferGeom,"bufferGeom")

print("\n Script Completed!!!")