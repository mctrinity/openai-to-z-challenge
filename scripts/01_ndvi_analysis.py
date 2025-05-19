# 01_ndvi_analysis.py
# NDVI Analysis with Google Earth Engine

import ee
import geemap
import os
from dotenv import load_dotenv

# Load .env variables for GEE project
load_dotenv()
project_id = os.getenv("GEE_PROJECT")

# Initialize Earth Engine
if not ee.data._initialized:
    ee.Initialize(project=project_id)

# Define area of interest (example: small patch in Brazil)
aoi = ee.Geometry.Rectangle([-55.5, -12.5, -54.0, -11.0])

# Load Sentinel-2 imagery and filter
s2 = (
    ee.ImageCollection("COPERNICUS/S2_SR_HARMONIZED")
    .filterDate("2024-06-01", "2024-06-30")
    .filterBounds(aoi)
    .filter(ee.Filter.lt("CLOUDY_PIXEL_PERCENTAGE", 20))
    .median()
)

# Compute NDVI
ndvi = s2.normalizedDifference(["B8", "B4"]).rename("NDVI")

# Visualization parameters
ndvi_vis = {
    "min": 0.1,
    "max": 0.8,
    "palette": ["white", "green"]
}

# Display NDVI on interactive map
Map = geemap.Map()
Map.centerObject(aoi, 9)
Map.addLayer(ndvi.clip(aoi), ndvi_vis, "NDVI")
Map.addLayer(s2.clip(aoi), {"bands": ["B4", "B3", "B2"], "min": 0, "max": 3000}, "True Color")
Map
