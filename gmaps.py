from datetime import datetime
import googlemaps

global api_key
api_key = 'AIzaSyBx2lGCeaLjMTNblROj3I4iNL8DWi45jvk'


def generateMap(address):
    gmaps = googlemaps.Client(key=api_key)
    # example address = "6392 Truckee Court, Newark, CA"
    now = datetime.now()

    clipped_address = address.replace(",", "")
    clipped_address = clipped_address.split(" ")
    clipped_address = clipped_address[:5]
    clipped_address = " ".join(str(i) for i in clipped_address)

    directions_result1 = gmaps.directions(clipped_address, "fire station near "+clipped_address,
                                        mode="driving",
                                        departure_time=now)
    directions_result2 = gmaps.directions(clipped_address, "hospital near "+clipped_address,
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
        distance = directions_result2[0]['legs'][0]['distance']['text']
        destination_address = directions_result2[0]['legs'][0]['end_address']

    print("Destination:", destination_address)
    print("Address:", address)

    destination_address = destination_address.replace(",", "")
    destination_address = destination_address.split(" ")

    address = address.replace(",", "")
    address = address.split(" ")

    src = "https://www.google.com/maps/embed/v1/directions?key=" + api_key + "&origin=" + str(destination_address[0]) + "%20" + str(destination_address[1]) + "%20" + str(destination_address[2]) + "%2C%20" + str(destination_address[3]) + "%2C%20" + str(destination_address[4]) + "%20" + str(destination_address[5]) + "%2C20" + str(destination_address[6]) + "&destination=" + str(address[0]) + "%20" + str(address[1]) + "%20" + str(address[2]) + "%2C%20" + str(address[3]) + "%2C%20" + str(address[4]) + "%20" + str(address[5]) + "%2C20" + str(address[6]) + "&mode=driving&maptype=roadmap"
    return src

print(generateMap("3749 Armour Court, Fremont, CA 94555 USA"))


def time_estimate(address="6392 Truckee Court, Newark, CA"):
    gmaps = googlemaps.Client(key='AIzaSyBx2lGCeaLjMTNblROj3I4iNL8DWi45jvk')

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
    return time, destination_address, distance


'''
Reference"
    <iframe width="600" height="450" style="border:0" loading="lazy" src="https://www.google.com/maps/embed/v1/directions?key=AIzaSyBx2lGCeaLjMTNblROj3I4iNL8DWi45jvk&origin=35659%20Fremont%20Blvd%2C%20Fremont%2C%20CA%2094536%2C20USA&destination=3749%20Armour%20Court%2C%20Fremont%2C%20CA%2094555%2C20USA&mode=driving&maptype=roadmap"></iframe>
'''
