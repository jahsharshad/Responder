from datetime import datetime
import googlemaps

gmaps = googlemaps.Client(key='AIzaSyBx2lGCeaLjMTNblROj3I4iNL8DWi45jvk')

address = "6392 Truckee Court, Newark, CA"  # should actually come from input
now = datetime.now()
directions_result1 = gmaps.directions(address, "fire station near "+address,
                                     mode="driving",
                                     departure_time=now)
directions_result2 = gmaps.directions(address, "hospital near "+address,
                                     mode="driving",
                                     departure_time=now)


timeString1 = directions_result1[0]['legs'][0]['duration']['text']
timeString2 = directions_result2[0]['legs'][0]['duration']['text']


time1 = int(timeString1.split()[0])
time2 = int(timeString2.split()[0])

if time1 < time2:
    time = timeString1
    distance = directions_result1[0]['legs'][0]['distance']['text']
    destination_address = directions_result1[0]['legs'][0]['end_address']
else:
    time = timeString2
    distance = directions_result1[0]['legs'][0]['distance']['text']
    destination_address = directions_result1[0]['legs'][0]['end_address']

print(time)
print(distance)
print(destination_address)


def time_estimate(address="6392 Truckee Court, Newark, CA"):
    gmaps = googlemaps.Client(key='AIzaSyBx2lGCeaLjMTNblROj3I4iNL8DWi45jvk')

    now = datetime.now()
    directions_result = gmaps.directions(address, "fire station near "+address,
                                         mode="driving",
                                         departure_time=now)

    time = directions_result[0]['legs'][0]['duration']['text']
    destination_address = directions_result[0]['legs'][0]['end_address']
    return time, destination_address