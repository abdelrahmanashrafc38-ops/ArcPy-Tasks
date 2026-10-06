import arcpy


def print_Message(msg):
    print(msg)
    arcpy.AddMessage(msg)

# set the environment
arcpy.env.overwriteOutput = True
arcpy.env.workspace = r"D:\Learning\iti\CoursesDoc\GIS\Course10_ArcPY\LPA\Data\Sample.gdb"


#fc = r"D:\Learning\iti\CoursesDoc\GIS\Course10_ArcPY\LPA\Data\ne_10m_admin_0_countries.shp"
fc= arcpy.GetParameterAsText(0)
if fc == "":
    fc = r"D:\Learning\iti\CoursesDoc\GIS\Course10_ArcPY\LPA\Data\ne_10m_admin_0_countries.shp"
numFeatures = int(arcpy.GetCount_management(fc)[0])
messsage = f"{fc} feature class has {numFeatures} features"
print_Message(messsage)

arcpy.CreateFileGDB_management(r"D:\Learning\iti\CoursesDoc\GIS\Course10_ArcPY\LPA\Data","Sample")
arcpy.Select_analysis(fc,"Egypt","NAME = 'Egypt'")

print_Message("Script Completed!!!")