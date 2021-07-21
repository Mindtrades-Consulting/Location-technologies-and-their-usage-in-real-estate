import json
import pandas as pd

with open("poi_by_types.json") as f:
    data = json.load(f)

for k, v in data.items():
    to_csv = []
    for row in v:
        to_csv.append([row[0], row[1], row[2], row[3], row[4]])

    df = pd.DataFrame(to_csv, columns = ['loc_name', "usr_ratings", "rating_average", "latitude", "longitude"]) 

    df.to_csv(f"POIs/{k}.csv")