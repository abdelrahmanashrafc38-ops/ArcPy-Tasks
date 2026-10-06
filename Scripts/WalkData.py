import arcpy
arcpy.env.workspace = r"D:\Learning\iti\CoursesDoc\GIS\Course10_ArcPY\LPA\Data"
dataList = []
for dirPath , dirNames , fileNames in arcpy.da.Walk(datatype="FeatureClass",type=["Point","Polyline"]):
    for filename in fileNames:
        dataList.append(r"{0}\{1}".format(dirPath,filename))
print(dataList)
print("-"*60)
print(f"\n found {len(dataList)} data elements in {arcpy.env.workspace} ")

print("-"*30 + "Script Completed!!!!!"+ "-"*30)