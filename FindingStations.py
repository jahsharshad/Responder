from gmaps import getCitiesInCounty, getCounty
import requests
import json

# enter your api key here
api_key = 'AIzaSyBx2lGCeaLjMTNblROj3I4iNL8DWi45jvk'
countyName = getCounty(94555)  # should come from user input
# cities = ['Alameda', 'Oakland', 'Hayward', 'Pleasanton', 'Livermore', 'San Leandro', 'Berkeley', 'Dublin',
#           'Castro Valley', 'Union City', 'Newark', 'Emeryville', 'Albany', 'San Lorenzo', 'Piedmont', 'Sunol',
#           'Piedmont', 'Sunol', 'Cherryland', 'Fairview', 'Ashland']
stateName = 'CA'  # should come from user input

county_station = []
stationAddresses = []


def stationCalc(county, state):
    global county_station
    cities = getCitiesInCounty(county)
    for city in cities:
        # url variable store url
        url = "https://maps.googleapis.com/maps/api/place/textsearch/json?"

        # The text string on which to search
        query = 'Fire station in ' + city + ', ' + state

        # get method of requests module
        # return response object
        r = requests.get(url + 'query=' + query + '&type=fire_station'
                         '&key=' + api_key)

        # json method of response object convert
        #  json format data into python format data
        x = r.json()

        # now x contains list of nested dictionaries
        # we know dictionary contain key value pair
        # store the value of result key in variable y
        y = x['results']

        # keep looping upto length of y
        for i in range(len(y)):
            # Append value corresponding to the
            # 'name' key at the ith index of y
            if county in y[i]['name'] or city in y[i]['name']:
                county_station.append((y[i]['name']))
                stationAddresses.append(y[i]['formatted_address'])

    county_station = set(county_station)
    stationNumber = len(county_station)
    county_station = list(county_station)
    return stationNumber, stationAddresses, county_station


county_hospital = []
hospitalAddresses = []


def hospitalCalc(county, state):
    global county_hospital
    global hospitalAddresses
    cities = getCitiesInCounty(county)
    for city in cities:
        # url variable store url
        url = "https://maps.googleapis.com/maps/api/place/textsearch/json?"

        # The text string on which to search
        query = 'Hospital in ' + city + ', ' + state

        # get method of requests module
        # return response object
        r = requests.get(url + 'query=' + query + '&type=hospital'
                         '&key=' + api_key)

        # json method of response object convert
        #  json format data into python format data
        x = r.json()

        # now x contains list of nested dictionaries
        # we know dictionary contain key value pair
        # store the value of result key in variable y
        y = x['results']

        # keep looping upto length of y
        hospitalRange = min(len(y),10)
        for i in range(hospitalRange):
            # Append value corresponding to the
            # 'name' key at the ith index of y
            hospitalName = y[i]['name']
            if True:
                if ('Hospital' in hospitalName):
                    county_hospital.append(y[i]['name'])
                    hospitalAddresses.append(y[i]['formatted_address'])

    county_hospital = set(county_hospital)
    hospitalNumber = len(county_hospital)
    county_hospital = list(county_hospital)
    return hospitalNumber, hospitalAddresses, county_hospital


'''AlamedaStationNum, AlamedaStationAddresses, AlamedaStationNames = stationCalc('Alameda','CA')
AlamedaHospitalNum, AlamedaHospAddresses, AlamedaHospNames = hospitalCalc('Alameda','CA')

print(AlamedaStationNames)
print(AlamedaHospNames)
'''