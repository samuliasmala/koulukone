from pyproj import Transformer
from sqlite_utils import Database

# Create a transformation from EPSG:3067 (EUREF-FIN) to EPSG:4326 (WGS84)
transformer = Transformer.from_crs("EPSG:3067", "EPSG:4326")

# Connect to the database
db = Database("data/yle-koulukone.db")

# Add new columns if they don't exist
db["locations"].add_column("latitude", float)
db["locations"].add_column("longitude", float)

# Prepare batch updates
updates = []
for row in db["locations"].rows:
    try:
        latitude, longitude = transformer.transform(
            row["euref_x"], row["euref_y"])
        updates.append({
            "tunn": row["tunn"],
            "latitude": latitude,
            "longitude": longitude
        })
    except Exception as e:
        print(f"Error transforming coordinates for row {row['tunn']}: {e}")

# Perform batch update
db["locations"].upsert_all(updates, pk="tunn")

print("Transformation complete!")
