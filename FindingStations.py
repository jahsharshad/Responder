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
        r = requests.get(url + 'query=' + query +
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
    return len(county_station), stationAddresses


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
        r = requests.get(url + 'query=' + query +
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
            hospitalName = y[i]['name']
            if ('Pet' not in hospitalName) and ('Vet' not in hospitalName) and ('Animal' not in hospitalName):
                if ('Cat' not in hospitalName) and ('Dog' not in hospitalName):
                    county_hospital.append((y[i]['name']))
                    hospitalAddresses.append(y[i]['formatted_address'])

    county_hospital = set(county_hospital)
    hospitalNumber = len(county_hospital)
    return hospitalNumber, hospitalAddresses

"""AlamedaStationNum, AlamedaStationAddresses = stationCalc('Alameda','CA')
AlamedaHospitalNum, AlamedaHospAddresses = hospitalCalc('Alameda','CA')
"""