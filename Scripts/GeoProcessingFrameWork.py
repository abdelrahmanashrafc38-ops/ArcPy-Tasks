import arcpy

arcpy.env.overwriteOutput = True
arcpy.env.workspace = r"D:\Learning\iti\CoursesDoc\GIS\Course10_ArcPY\LPA\Projects\FrameWorkProject\FrameWorkProject.gdb"


srcFC_Cou = r"D:\Learning\iti\CoursesDoc\GIS\Course10_ArcPY\LPA\Data\ne_10m_admin_0_countries.shp"
srcFC_Pop_Places = r"D:\Learning\iti\CoursesDoc\GIS\Course10_ArcPY\LPA\Data\ne_10m_populated_places.shp"

try:
    Egypt = arcpy.Select_analysis(srcFC_Cou,"Egypt","NAME = 'Egypt'")
    EgyBuffer = arcpy.Buffer_analysis(Egypt,"EgyBuffer","200 Kilometers")
except Exception as e :
    print(e)
    arcpy.AddMessage(e)
else:
    popPlacesLy = arcpy.MakeFeatureLayer_management(srcFC_Pop_Places,"pop_Places")


try:
    SelectedFC1 = arcpy.SelectLayerByLocation_management(popPlacesLy,"INTERSECT",EgyBuffer,None,"NEW_SELECTION")
    arcpy.CopyFeatures_management(popPlacesLy,"SelectedFC1")
    SelectedFC2 = arcpy.SelectLayerByLocation_management(popPlacesLy,"INTERSECT",Egypt,"200 Kilometers","NEW_SELECTION")
    arcpy.CopyFeatures_management(popPlacesLy,"SelectedFC2")
except Exception as e :
    print(e)
    arcpy.AddMessage(e)
else:
    print("Script run successfully!!!!")
    arcpy.AddMessage("Script run successfully!!!!")

