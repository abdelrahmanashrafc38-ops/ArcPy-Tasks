import arcpy

arcpy.env.overwriteOutput = True
arcpy.env.workspace = r"D:\Learning\iti\CoursesDoc\GIS\Course10_ArcPY\LPA\Projects\GeomProject\GeomProject.gdb"
srWGS84 = arcpy.SpatialReference("WGS 1984")

if arcpy.Exists("FishnetLines"):
    arcpy.Delete_management("FishnetLines")
    

arcpy.management.CreateFishnet(
    out_feature_class="FishnetLines",
    origin_coord="0 0",
    y_axis_coord="0 1",
    cell_width=0,
    cell_height=1,
    number_rows=10,
    number_columns=15,
    corner_coord="10 10",
    labels="LABELS",
    template='0 0 10 10 PROJCRS["WGS_1984_Web_Mercator_Auxiliary_Sphere",BASEGEOGCRS["GCS_WGS_1984",DYNAMIC[FRAMEEPOCH[1990.5],MODEL["AM0-2"]],DATUM["D_WGS_1984",ELLIPSOID["WGS_1984",6378137.0,298.257223563]],PRIMEM["Greenwich",0.0],CS[ellipsoidal,2],AXIS["Latitude (lat)",north,ORDER[1]],AXIS["Longitude (lon)",east,ORDER[2]],ANGLEUNIT["Degree",0.0174532925199433]],CONVERSION["Mercator_Auxiliary_Sphere",METHOD["Mercator_Auxiliary_Sphere"],PARAMETER["False_Easting",0.0],PARAMETER["False_Northing",0.0],PARAMETER["Central_Meridian",0.0],PARAMETER["Standard_Parallel_1",0.0],PARAMETER["Auxiliary_Sphere_Type",0.0]],CS[Cartesian,2],AXIS["Easting (X)",east,ORDER[1]],AXIS["Northing (Y)",north,ORDER[2]],LENGTHUNIT["Meter",1.0],ID["EPSG","3857"]]',
    geometry_type="POLYLINE"
)

if arcpy.Exists("FishnetPoints"):
    arcpy.Delete_management("FishnetPoints")
arcpy.Rename_management("FishnetLines_label","FishnetPoints")

if arcpy.Exists("FishnetPolys"):
    arcpy.Delete_management("FishnetPolys")

arcpy.management.CreateFishnet(
    out_feature_class="FishnetPolys",
    origin_coord="0 0",
    y_axis_coord="0 1",
    cell_width=1,
    cell_height=1,
    number_rows=4,
    number_columns=6,
    corner_coord="10 10",
    labels="NO_LABELS",
    template='0 0 10 10 PROJCRS["WGS_1984_Web_Mercator_Auxiliary_Sphere",BASEGEOGCRS["GCS_WGS_1984",DYNAMIC[FRAMEEPOCH[1990.5],MODEL["AM0-2"]],DATUM["D_WGS_1984",ELLIPSOID["WGS_1984",6378137.0,298.257223563]],PRIMEM["Greenwich",0.0],CS[ellipsoidal,2],AXIS["Latitude (lat)",north,ORDER[1]],AXIS["Longitude (lon)",east,ORDER[2]],ANGLEUNIT["Degree",0.0174532925199433]],CONVERSION["Mercator_Auxiliary_Sphere",METHOD["Mercator_Auxiliary_Sphere"],PARAMETER["False_Easting",0.0],PARAMETER["False_Northing",0.0],PARAMETER["Central_Meridian",0.0],PARAMETER["Standard_Parallel_1",0.0],PARAMETER["Auxiliary_Sphere_Type",0.0]],CS[Cartesian,2],AXIS["Easting (X)",east,ORDER[1]],AXIS["Northing (Y)",north,ORDER[2]],LENGTHUNIT["Meter",1.0],ID["EPSG","3857"]]',
    geometry_type="POLYGON"
)

for geoType in ["Polys","Points","Lines"]:
    
    arcpy.management.DefineProjection(
    in_dataset= f"Fishnet{geoType}",
    coor_system= srWGS84
)



"""arcpy.management.DefineProjection(
    in_dataset="FishnetLines_label",
    coor_system= srWGS84

arcpy.management.DefineProjection(
    in_dataset="FishnetLines",
    coor_system= srWGS84
)"""



print("Script Completed!!!!!")