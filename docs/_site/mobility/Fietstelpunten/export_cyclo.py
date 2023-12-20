import osmnx as ox
import geopandas as gpd

def download_cycle_map(place_name, filename):
    """
    Download cycle map of a specified area from OpenStreetMap and save as a shapefile.

    :param place_name: Name of the place or area to download (e.g., 'Manhattan, New York City, New York, USA').
    :param filename: Path to save the shapefile.
    """
    # Configure osmnx to retrieve only cycling-related streets
    ox.config(use_cache=True, log_console=True)
    custom_filter = '["highway"~"cycleway|path|footway|pedestrian|track"]'

    # Retrieve data
    cycle_map = ox.graph_from_place(place_name, custom_filter=custom_filter)
    cycle_map_gdf = ox.graph_to_gdfs(cycle_map, nodes=False)

    # Save to shapefile
    cycle_map_gdf.to_file(filename, driver='ESRI Shapefile')

    print(f"Cycle map for {place_name} saved as {filename}")

# Example usage
place = "Vlaanderen, Belgium"
file_path = "cycle_map"
download_cycle_map(place, file_path)
