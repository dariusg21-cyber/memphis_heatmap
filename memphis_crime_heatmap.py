

import pandas as pd
import folium
from folium.plugins import HeatMap

# Load your dataset
df = pd.read_csv("memphis_crime.csv")

# Preview columns
print("Columns:", df.columns)

# 🔑 Adjust if needed based on your file
lat_col = "Latitude"
lon_col = "Longitude"

# Clean data
df = df.dropna(subset=[lat_col, lon_col])

# Create base map (Memphis center)
memphis_map = folium.Map(
    location=[35.1495, -90.0490],
    zoom_start=11,
    tiles="cartodbpositron"
)

# Convert to list
heat_data = df[[lat_col, lon_col]].values.tolist()

# Add heatmap layer
HeatMap(
    heat_data,
    radius=12,
    blur=18,
    min_opacity=0.2
).add_to(memphis_map)

# Save map
memphis_map.save("output/heatmap.html")

print(" Heatmap created → output/heatmap.html")
