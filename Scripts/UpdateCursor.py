import arcpy

shp = r"D:\Learning\iti\CoursesDoc\GIS\Course10_ArcPY\LPA\Data\ne_10m_admin_0_countries.shp"
fc = r"D:\Learning\iti\CoursesDoc\GIS\Course10_ArcPY\LPA\Projects\CursorProject\CursorProject.gdb\Countries"
arcpy.env.overwriteOutput = True
arcpy.management.CopyFeatures(shp,fc)

arcpy.AddField_management(fc,"GDPperPerson","FLOAT")

with arcpy.da.UpdateCursor(fc,["NAME","GDP_MD_EST","POP_EST","GDPperPerson"]) as cursor:
    for row in cursor:
        row[0] = row[0].upper()
        
        if row[2] == 0:
            row[3]= 0
        else:   
            row[3] = (row[1]*1000000) / row[2]
        if row[3] >= 10000:
            cursor.deleteRow()
        else:
            cursor.updateRow(row)     
        print(f"{row[0]} GDPPP : US$ {int(row[3])}")  
        #print(row[0])


print("Script Completed!!!")