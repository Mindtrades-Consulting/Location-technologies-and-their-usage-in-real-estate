import json
import itertools
import pandas as pd
import math

with open("for_rent_estate.json") as f:
    data = json.load(f)

def closest_point(starting_point, data):
    data.sort(key=lambda x: math.sqrt((float(x.split(" ")[0]) - starting_point[0])**2 +
        (float(x.split(" ")[1]) - starting_point[1])**2))
    return data
def get_POIS():
    POI = []

    for row in data:
        POI.append(row["POI"])

    stats = []

    for row in POI:
        for x in row:
            stats.append([x["loc_name"], x["loc_types"][0], x["usr_ratings"], x["rating_average"], x["latitude"], x["longitude"]])

    df = pd.DataFrame(stats, columns = ['loc_name', 'types', "usr_ratings", "rating_average", "latitude", "longitude"]) 

    df_list = {}
    for index, row in df.iterrows():
        if row["types"] not in df_list:
            df_list[row["types"]] = []
        loc_name = row["loc_name"]
        usr_ratings = row["usr_ratings"]
        rating_average = row["rating_average"]
        latitude = row["latitude"]
        longitude = row["longitude"]
        df_list[row["types"]].append([loc_name, usr_ratings, rating_average, latitude, longitude])

    with open("poi_by_types.json", "w") as f:
        json.dump(df_list, f, indent= 4)

def get_estate():
    with open("for_rent_estate.json") as f:
        data = json.load(f)
    
    to_csv = []

    for row in data:
        try:
            _throwaway = row["bedrooms"]
        except:
            continue

        try:
            _throwaway = row["bathrooms"]
        except:
            continue

        try:
            _throwaway = row["price"]
        except:
            continue

        points_list = []
        for poi in row["POI"]:
            latitude = poi["latitude"]
            longitude = poi["longitude"]
            loc_type = poi["loc_types"][0]
            points_list.append(f"{latitude} {longitude} {loc_type}")
        closest = closest_point([row["latitude"], row["longitude"]], points_list)[0]
        closest_latitude = closest.split(" ")[0]
        closest_longitude = closest.split(" ")[1]
        closest_type = closest.split(" ")[2]
        to_csv.append([row["bedrooms"], row["bathrooms"], row["price"], row["latitude"], row["longitude"], closest_type, closest_latitude, closest_longitude])
    df = pd.DataFrame(to_csv, columns = ['bedrooms', 'bathrooms', "price", "latitude", "longitude", "closest_type", "closest_latitude", "closest_longitude"]) 
    
    df.to_csv("rental_data.csv")
get_estate()