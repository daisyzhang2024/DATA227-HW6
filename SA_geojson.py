import geopandas as gpd

world = gpd.read_file("https://naciscdn.org/naturalearth/50m/cultural/ne_50m_admin_0_countries.zip")
sea = ["MMR","THA","LAO","KHM","VNM","MYS","SGP","BRN","IDN","PHL","TLS"]
neighbors = ["CHN","IND","BGD","PNG","AUS","TWN"]  # for gray context
region = world[world["ADM0_A3"].isin(sea + neighbors)][["ADM0_A3", "NAME", "geometry"]]
region.to_crs("EPSG:4326").to_file("sea.geojson", driver="GeoJSON")