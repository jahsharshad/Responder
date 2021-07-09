from datetime import datetime
import googlemaps

gmaps = googlemaps.Client(key='AIzaSyBx2lGCeaLjMTNblROj3I4iNL8DWi45jvk')

address = "6392 Truckee Court, Newark, CA"  # should actually come from input
now = datetime.now()
directions_result = gmaps.directions(address, "fire station near "+address,
                                     mode="driving",
                                     departure_time=now)

time = directions_result[0]['legs'][0]['duration']['text']
print(time)
