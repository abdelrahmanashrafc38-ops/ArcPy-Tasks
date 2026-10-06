import arcpy

shp = r"D:\Learning\iti\CoursesDoc\GIS\Course10_ArcPY\LPA\Data\ne_10m_admin_0_countries.shp"

"""for key , fieldName in enumerate(arcpy.ListFields(shp)):
    print(f"{key} : {fieldName.name}")\
        
print("_"*50)

with arcpy.da.SearchCursor(shp, ["NAME", "POP_EST"]) as cursor:
    for key , row in enumerate(cursor):
        print(f"{key+1} :{row}")"""
#----------------------------------------------------------------------------------------------
"""with arcpy.da.SearchCursor(shp, ["NAME","shape@xy","shape@Area","shape@length","POP_EST"]) as cursor:
    for row in cursor:
        print(f"Centroid of {row[0]} is {row[1]} and its area is {row[2]} and its perimeter is {row[3]}")"""
#----------------------------------------------------------------------------------------------
"""countryList = []
with arcpy.da.SearchCursor(shp, ["NAME"]) as cursor:
    for row in cursor:
        countryList.append(row[0])
countryList = [row[0] for row in arcpy.da.SearchCursor(shp,["NAME"]) ]
print(countryList)
print(len(countryList))"""
#----------------------------------------------------------------------------------------------
"""countryList = [row[0] for row in arcpy.da.SearchCursor(shp,["CONTINENT"]) ]
print(set(countryList))
print(len(set(countryList)))
print(sorted(set(countryList)))"""
#----------------------------------------------------------------------------------------------
"""CountryContinentList = [[row[0],row[1]] for row in arcpy.da.SearchCursor(shp,["NAME","CONTINENT"])]
print(CountryContinentList)
print(len(CountryContinentList))
print(CountryContinentList[2])
print(CountryContinentList[2][1])"""
#----------------------------------------------------------------------------------------------
"""fidCountryDict = {row[0]:row[1]for row in arcpy.da.SearchCursor(shp,["FID","NAME"],"FID<10")}
print(fidCountryDict)
print(fidCountryDict[4])"""
#----------------------------------------------------------------------------------------------
fidCountryDict = {
    row[0]:[row[1],row[2],"{:,}".format(row[3])]
    for row in arcpy.da.SearchCursor(shp,["FID","NAME","CONTINENT","POP_EST"],"FID<10")}
print(fidCountryDict)
print(fidCountryDict[4])
print(fidCountryDict[4][2])



print("Script Completed!!!")
