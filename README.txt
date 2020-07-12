NoSQL-2 Kol OSM Luka Zec 270377

Importing OSM into MongoDB using python 

py files:

	1. exportToMongo.py - reads and parses an OSM file and exports it to  MongoDB 
	2. searchInRadius.py- searches all streets in Skopje within given radius and writes them to "streetsInRadius.json"


References :
	https://medium.com/@petehouston/calculate-distance-of-two-locations-on-earth-using-python-1501b1944d97 calculating distance between 2 points on sphere (haversine formula)



Execution:


1. Run MongoDB on port 27017  using mongod command

2. Get an OSM  data from http://download.geofabrik.de/europe/macedonia-latest.osm.bz2

(run python files using python's built in IDLE instead of visual studio code to avoid encoding errors(at least this is bug on my pc))

3. Run exportToMongo.py and wait until it says that the data was exported to mongo

4. Run searchInRadius.py this will search for all the streets within given radius

5. Open  file "streetsInRadius.json" to find all the streets that are in selected radius;
