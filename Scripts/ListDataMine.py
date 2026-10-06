import arcpy
import os

arcpy.env.workspace = r"D:\Learning\iti\CoursesDoc\GIS\Course10_ArcPY\LPA"
gdbLiastAll = list()
for root, dirs, files in os.walk(arcpy.env.workspace):
    for folder in dirs:
        if folder.endswith(".gdb"):
            full_path = os.path.join(root, folder)
            gdbLiastAll.append(full_path)
            #print(full_path)
            # #print(gdbLiastAll)

"""for gdb in gdbLiastAll :
    arcpy.env.workspace = gdb
    featureClasses = arcpy.ListFeatureClasses() 
    print(f"{gdb} contains {featureClasses}")"""