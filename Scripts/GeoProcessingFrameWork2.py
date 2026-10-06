import arcpy

arcpy.env.overwriteOutput = True
arcpy.env.workspace = r"D:\Learning\iti\CoursesDoc\GIS\Course10_ArcPY\LPA\Projects\FrameWorkProject\FrameWorkProject.gdb"


srcFC_Cou = r"D:\Learning\iti\CoursesDoc\GIS\Course10_ArcPY\LPA\Data\ne_10m_admin_0_countries.shp"
srcFC_Pop_Places = r"D:\Learning\iti\CoursesDoc\GIS\Course10_ArcPY\LPA\Data\ne_10m_populated_places.shp"
countryName = arcpy.GetParameterAsText (0)
clause = "NAME = \'{0}\'".format(countryName.capitalize())
try:
    cou_fc = arcpy.Select_analysis(srcFC_Cou,f"{countryName}",clause)
    fc_Buffer = arcpy.Buffer_analysis(cou_fc,f"{countryName}_Buffer","200 Kilometers")
    Clipped_places = arcpy.Clip_analysis(srcFC_Pop_Places,fc_Buffer,"Clipped_Pop_Places")
except Exception as e :
    print(e)
    arcpy.AddMessage(e)
else:
    count = arcpy.GetCount_management(Clipped_places)
    arcpy.AddMessage(f"Successfuly Finished!!!\nnumber of features are {count}")