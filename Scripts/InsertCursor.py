import arcpy

arcpy.env.overwriteOutput = True

"""fGDB = r"D:\Learning\iti\CoursesDoc\GIS\Course10_ArcPY\LPA\Projects\CursorProject\CursorProject.gdb"
tableName= "TestTable"
fGDBTable = r"{fGDB}\{tableName}".format(fGDB=fGDB, tableName=tableName)
arcpy.CreateTable_management(fGDB, tableName)
arcpy.AddField_management(fGDBTable, "TestField", "TEXT", field_length=5)
arcpy.AddField_management(fGDBTable, "IntField", "integer")
arcpy.AddField_management(fGDBTable, "FloatField","FLOAT")

fieldList = ["TestField", "IntField", "FloatField"]
with arcpy.da.InsertCursor(fGDBTable,fieldList) as cursor:
    cursor.insertRow(["A",1,0.0])
    cursor.insertRow(["B",2,5.5])
    cursor.insertRow(["C",3,9.90])
    
with arcpy.da.SearchCursor(fGDBTable,fieldList) as cursor:
    for row in cursor:
        print(row)"""
        
#----------------------------------------------------------------------------------------------

"""shp = r"D:\Learning\iti\CoursesDoc\GIS\Course10_ArcPY\LPA\Data\ne_10m_admin_0_countries.shp"
fc = r"D:\Learning\iti\CoursesDoc\GIS\Course10_ArcPY\LPA\Projects\CursorProject\CursorProject.gdb\Countries"
arcpy.management.CopyFeatures(shp,fc)

with arcpy.da.InsertCursor(fc,["shape@","NAME"]) as cursor:
    srWGS84 = arcpy.SpatialReference("WGS 1984")
    nullIslandPoint = arcpy.Point(0,0)
    nullIslandGeometry = arcpy.PointGeometry(nullIslandPoint, srWGS84).buffer(5)
    cursor.insertRow([nullIslandGeometry,"Null Island"])"""
#----------------------------------------------------------------------------------------------
fGDB = r"D:\Learning\iti\CoursesDoc\GIS\Course10_ArcPY\LPA\Projects\CursorProject\CursorProject.gdb"
shp = r"D:\Learning\iti\CoursesDoc\GIS\Course10_ArcPY\LPA\Data\ne_10m_admin_0_countries.shp"
fieldList = ["NAME","CONTINENT","Pop_EST","GDP_MD_EST"]
fieldLengthList = []
for field in fieldList:
    fieldLengthList.append(max([len(str(row[0])) for row in arcpy.da.SearchCursor(shp, [field])]))
print(fieldLengthList)
print(max(fieldLengthList))
print("Script Completed!!!")