import requests
import json

with open("for_sale_estate.json", "r", encoding="utf-8") as f:
    data = json.load(f)
for i in range(len(data)):

    print(f"INFO: Scraping {i+1} of {len(data)}")

    try:
        latitude = data[i]["latitude"]
        longitude = data[i]["longitude"]
    except:
        print("ERROR: Property doesn't have latitude/longitude, skipping")
        del data[i]
        continue
    # Google Places API request endpoint
    url = f"https://maps.googleapis.com/maps/api/place/nearbysearch/json?location={latitude},{longitude}&radius=1600&key=AIzaSyAaB1v70ggMHPxULXranfZiRFjT9WQky_E"
    
    r = requests.get(url)
    
    r_object = r.json()

    POI = []

    # Iterate over Google Places Latitude & Longitude API results
    for x in range(len(r_object["results"])):
        result_name = r_object["results"][x]["name"]

        loc_type = r_object["results"][x]["types"]

        try:
            usr_ratings = r_object["results"][x]["user_ratings_total"]
        except:
            usr_ratings = "N/A"

        try: 
            rating = r_object["results"][x]["rating"]
        except:
            rating = "N/A"

        try: 
            lat = r_object["results"][x]["geometry"]["location"]["lat"]
            lng = r_object["results"][x]["geometry"]["location"]["lng"]
        except:
            lat = "N/A"
            lng = "N/A"

        if "locality" in loc_type:
            print(f"INFO: Locality {result_name} in {i} skipped due to having blacklisted type")
            continue

        POI.append({
            "loc_name":result_name,
            "loc_types":loc_type,
            "usr_ratings":usr_ratings,
            "rating_average":rating,
            "latitude":lat,
            "longitude":lng
        })

    data[i]["POI"] = POI

    with open("for_sale_estate.json", "w") as f:
        json.dump(data, f, indent=4)
