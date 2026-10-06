import arcpy

#if arcpy.Exists(r"D:\Learning\iti\CoursesDoc\GIS\Course10_ArcPY\LPA\Data\Test.gdb"):
# arcpy.Delete_management(r"D:\Learning\iti\CoursesDoc\GIS\Course10_ArcPY\LPA\Data\Test.gdb")
arcpy.env.overwriteOutput = True
arcpy.env.workspace= r"D:\Learning\iti\CoursesDoc\GIS\Course10_ArcPY\LPA\Data\Test.gdb"
arcpy.CreateFileGDB_management(r"D:\Learning\iti\CoursesDoc\GIS\Course10_ArcPY\LPA\Data","Test")

arcpy.FeatureClassToFeatureClass_conversion(r"D:\Learning\iti\CoursesDoc\GIS\Course10_ArcPY\LPA\Data\ne_10m_admin_0_countries.shp",
                                            r"D:\Learning\iti\CoursesDoc\GIS\Course10_ArcPY\LPA\Data\Test.gdb","Countries")

print(arcpy.Exists(r"D:\Learning\iti\CoursesDoc\GIS\Course10_ArcPY\LPA\Data\Test.gdb\Countries"))
print("\n Scrips Completed!!!!!!!!")