import math
# coding: utf8
from pymongo import MongoClient
from math import radians, cos, sin, asin, sqrt
import json
import sys
# coding: utf8

# sys.setdefaultencoding("utf-8")


client = MongoClient(port=27017)
db = client["macedonia_osm"]
cities_collection = db["cities"]
streets_collection = db["streets"]



center_point = {"lat": 42.008325, "lon":21.367214}
query = {"city" : "Скопје"}
cities_cursor = cities_collection.find()

streets = streets_collection.find(query)


from math import radians, sin, cos, asin, sqrt
def haversine(lon1, lat1, lon2, lat2):
    lon1, lat1, lon2, lat2 = map(radians, [lon1, lat1, lon2, lat2])
    dlon = lon2 - lon1
    dlat = lat2 - lat1
    a = sin(dlat / 2) ** 2 + cos(lat1) * cos(lat2) * sin(dlon / 2) ** 2
    return 2 * 6371 * asin(sqrt(a))




streets_within = []
i = 0
for street in streets:
    # street = street.encode('utf-8')

    isWithin = False

    # if street["city"] == "Skopje" or street["city"] == "Скопје":
        
    if len(street["locations"]) > 0:
        for location in street["locations"]:

            test_point = {
                "lat": float(location["lat"]),
                 "lon": float(location["lon"]),
            }

               
                # radius is in km

            radius = 3
            c = haversine(
                center_point['lat'],
                center_point['lon'],
                test_point['lat'],
                test_point['lon']
            )

            if c <= radius:
                isWithin = True
        
        if isWithin == True:
            i+=1
            
            print(i,street['street'])
            

            streets_within.append({"city": street["city"], "street": street["street"]})

# print(streets_within)
with open("streetsInRadius.json", "w", encoding='utf-8') as f:
    json.dump(streets_within, f, ensure_ascii= False)

print("Done, you may check your json file.")




