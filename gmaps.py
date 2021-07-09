from datetime import datetime
import googlemaps


def time_estimate(address="6392 Truckee Court, Newark, CA"):
    gmaps = googlemaps.Client(key='AIzaSyBx2lGCeaLjMTNblROj3I4iNL8DWi45jvk')

    now = datetime.now()
    directions_result = gmaps.directions(address, "fire station near "+address,
                                         mode="driving",
                                         departure_time=now)

    time = directions_result[0]['legs'][0]['duration']['text']
    destination_address = directions_result[0]['legs'][0]['end_address']
    return time, destination_address
