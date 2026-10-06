import arcpy 

dataElement = r"D:\Learning\iti\CoursesDoc\GIS\Course10_ArcPY\LPA\Data\Sample.gdb"
descDictionary = arcpy.da.Describe(dataElement)
for i,key in enumerate(descDictionary) :
    print(f"{i+1}.{key} : {descDictionary[key]}")




"""desc = arcpy.Describe(dataElement)
print("Name: "+desc.name)
print("dataType: "+desc.dataType)
print("catalogPath: "+desc.catalogPath)

for child in desc.children:
    if child.dataType == "FeatureClass":
        print(f"for Feature class {child.name}\n" + "-"*60 )
        for field in child.fields:
            print(f"{field.name} is an Attribute with {field.type} data type")
        print("-"*60)"""


"""print(desc.children)
for child in desc.children :
    print("Name: "+child.name)
    print("dataType: "+child.dataType)
    print("catalogPath: "+child.catalogPath)
    print ("contain {0} files inside".format(len(child.children)))
    print("-----------------------------------------------------")
    print(child.__dict__)"""
    



print ("\nScript Completed!!!!!!!")