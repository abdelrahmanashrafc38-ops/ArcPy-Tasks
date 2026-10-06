# ArcPy Geoprocessing and Data Management Portfolio

This repository contains a collection of Python scripts utilizing the `arcpy` library, developed as part of a comprehensive GIS programming curriculum. These scripts demonstrate a wide range of skills in spatial data management, automated geoprocessing, and custom geometry creation.

## 🚀 Skills & Technologies Demonstrated

- **Geoprocessing Frameworks**: Automating ArcMap/ArcGIS Pro geoprocessing tools (Buffer, Intersect, CopyFeatures, SelectLayerByLocation).
- **Data Access Module (`arcpy.da`)**: 
  - Iterating through datasets with `SearchCursor`, `InsertCursor`, and `UpdateCursor`.
  - Directory walking with `arcpy.da.Walk` to index specific spatial data types.
  - Generating descriptions and schema information using `arcpy.da.Describe`.
- **Geometry Operations**:
  - Building Point, Multipoint, Polyline, and Polygon geometries from coordinate arrays.
  - Applying geometric operations (e.g., calculating areas, buffering).
- **Feature Class Management**: Creating fields, defining spatial references, deleting/updating rows based on queries.
- **Environment Settings**: Managing spatial workspaces and enforcing environment parameters (`arcpy.env`).

## 📁 Repository Structure & Scripts Overview

The codebase is organized into several key scripts within the `Scripts` directory:

### 1. Data Access and Cursors
- **`SearchCursor.py`**: Queries feature classes to extract fields and geometries. Demonstrates dictionary comprehensions for rapid attribute retrieval and parsing spatial extents.
- **`UpdateCursor.py`**: Performs dynamic calculations (e.g., GDP per person), alters field values, and executes conditional row deletion/updating for data cleanup.
- **`InsertCursor.py`**: Demonstrates the creation of new tables and fields from scratch, and inserts new geometric features (e.g., "Null Island" coordinates) directly into a geodatabase.

### 2. Geometry Construction and Manipulation
- **`Geometry.py`**: Programmatically generates spatial geometries (Points, Lines, Polygons) from nested coordinate lists. Demonstrates reading existing feature geometry, parsing spatial references, calculating areas, and generating buffers.
- **`CreateFishnet.py`**: Uses `arcpy.management.CreateFishnet` to establish a grid network of lines, points, and polygons. Programmatically defines the WGS 1984 Spatial Reference for the resulting layers.

### 3. Geoprocessing Workflows
- **`GeoProcessingFrameWork.py`**: Implements a standard spatial analysis workflow. Selects specific features (e.g., Egypt), applies a buffer, and utilizes `SelectLayerByLocation_management` to find intersecting populated places. Highlights robust error handling using `try/except` and `arcpy.AddMessage`.

### 4. Data Mining and Exploration
- **`DescribeDataMine.py`**: Dynamically accesses geodatabase schema using `arcpy.da.Describe`. Extracts dataset properties, field types, and catalog paths without opening the datasets manually.
- **`WalkData.py`**: Scans directories for specific spatial file types (e.g., Point and Polyline Feature Classes) using `arcpy.da.Walk`, functioning similarly to Python's `os.walk` but optimized for spatial data.

## 💼 CV / Portfolio Usage
These scripts demonstrate a firm grasp of the `arcpy` site package, moving beyond simple tool execution to dynamic geometric generation, advanced data access, and script optimization. It is an excellent showcase of automating GIS workflows using Python.
