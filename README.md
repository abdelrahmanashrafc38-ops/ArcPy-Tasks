# ArcPy Geoprocessing and Data Management Portfolio

## 1. Repository Overview
This repository serves as a portfolio of practical ArcPy tasks and GIS automation workflows. It is designed to demonstrate proficiency in automating spatial data management and analysis using Python. The main areas of GIS programming covered include data access through cursors, programmatic geometry construction, batch geodatabase mining, and automated geoprocessing workflows.

## 2. Environment
- **ArcGIS Pro**: Required for the arcpy Python environment.
- **Python Environment**: ArcPy (Python 3.x), bundled with ArcGIS Pro.
- **Libraries**: `arcpy`
- **Development Environment**: Visual Studio Code / Jupyter Notebooks / IDLE.

## 3. GIS Automation Concepts
- **Geoprocessing**: Automating standard ArcMap/ArcGIS Pro tools.
- **Data Management**: Copying features, renaming layers, and creating datasets programmatically.
- **Spatial Analysis**: Performing spatial selections and proximity analysis (buffers).
- **GIS Automation**: Scripting repetitive tasks such as projecting multiple feature classes.
- **File and Folder Management**: Walking through workspace directories to locate specific GIS data types.
- **Feature Class/Table Manipulation**: Using cursors to read, insert, and modify attribute data based on geometric or mathematical logic.

## 4. Tasks / Scripts

### Data Access and Mining
**Objective**: Programmatically explore geodatabases and read attribute/spatial data.

- **Input**: Shapefiles (`ne_10m_admin_0_countries.shp`) and File Geodatabases.
- **Processing**: Iterating over feature classes, extracting geometries, and reading database schemas.
- **Output**: Python lists, sets, dictionaries containing spatial and attribute data, and console summaries of schema information.
- **ArcPy Tools / Functions**: `arcpy.da.SearchCursor`, `arcpy.da.Walk`, `arcpy.da.Describe`.

### Attribute and Geometry Updates
**Objective**: Modify existing feature class attributes based on mathematical operations and manage tabular data dynamically.

- **Input**: Existing country shapefiles.
- **Processing**: Creating new fields, calculating GDP per capita, filtering rows, and deleting unneeded records.
- **Output**: Updated File Geodatabase feature classes with newly calculated fields and cleaned records.
- **ArcPy Tools / Functions**: `arcpy.AddField_management`, `arcpy.da.UpdateCursor`, `arcpy.da.InsertCursor`, `arcpy.PointGeometry`.

### Custom Geometry Construction
**Objective**: Build and manipulate spatial geometries programmatically from raw coordinate data.

- **Input**: Nested Python lists representing coordinate pairs.
- **Processing**: Constructing Point, Multipoint, Polyline, and Polygon objects.
- **Output**: Output feature classes representing the newly constructed geometries and buffers.
- **ArcPy Tools / Functions**: `arcpy.Point`, `arcpy.Array`, `arcpy.Polygon`, `arcpy.CopyFeatures_management`.

### Automated Geoprocessing Framework
**Objective**: Execute a robust, multi-step spatial analysis workflow with error handling.

- **Input**: Country boundaries and populated places shapefiles.
- **Processing**: Selecting a specific feature, creating a proximity buffer, generating a feature layer, and intersecting features.
- **Output**: Newly selected and exported feature classes stored in a project geodatabase.
- **ArcPy Tools / Functions**: `arcpy.Select_analysis`, `arcpy.Buffer_analysis`, `arcpy.MakeFeatureLayer_management`, `arcpy.SelectLayerByLocation_management`, `arcpy.AddMessage`.

### Grid Network Generation (Fishnet)
**Objective**: Create spatial grids consisting of lines, points, and polygons for spatial indexing.

- **Input**: Origin and corner coordinates, row/column specifications.
- **Processing**: Generating fishnet features and assigning spatial references.
- **Output**: `FishnetLines`, `FishnetPoints`, and `FishnetPolys` feature classes.
- **ArcPy Tools / Functions**: `arcpy.management.CreateFishnet`, `arcpy.management.DefineProjection`, `arcpy.SpatialReference`.

## 5. Key ArcPy Topics
- `arcpy`
- `AddMessage`
- `SearchCursor`
- `UpdateCursor`
- `InsertCursor`
- `MakeFeatureLayer`
- `Select`
- `Buffer`
- `SelectLayerByLocation`
- File Geodatabases
- Shapefiles
- `os`
- Python lists
- Sets
- Dictionaries
- List comprehensions
- Error handling

## 6. Example Workflow

**Automated Spatial Intersection Workflow:**

Input GIS Data
      ↓
Data Preparation
      ↓
Geoprocessing
      ↓
Spatial Analysis
      ↓
Output GIS Data

## 7. Code Structure
- **Scripts/**: Contains all standalone `.py` python scripts categorized by workflow (Cursors, Geometry, Frameworks).
- **Data/**: Contains raw input shapefiles and other datasets used by the scripts.
- **Projects/**: Contains `.gdb` File Geodatabases and `.aprx` ArcGIS Pro projects for storing script outputs.
- **README.md**: The documentation file explaining the repository structure and purpose.

## 8. How to Run
- **Required ArcGIS Pro Version**: ArcGIS Pro 2.x or 3.x (to support Python 3 and `arcpy`).
- **Python Environment**: The ArcGIS Pro default Python environment (`arcgispro-py3`).
- **Required Datasets**: Ensure the `Data/` folder contains the referenced shapefiles.
- **Parameters**: Currently, paths are hardcoded to the local workspace. Update the `arcpy.env.workspace` and data variables (`shp`, `fc`) in the scripts to match your local repository path before running.
- **Execution**: Scripts can be executed directly from a command prompt using the ArcGIS Python executable, from the ArcGIS Pro Python window, or via an IDE like Visual Studio Code.

## 9. Lessons Learned
This project reinforced the practical application of GIS programming and Python automation. Key technical skills demonstrated include the ability to bypass the standard graphical interface to programmatically generate spatial data, implement iterative cursors for rapid attribute processing, and handle geoprocessing failures gracefully using error handling block structures. It firmly establishes a foundational capability in manipulating both the geometric and tabular aspects of spatial datasets.
