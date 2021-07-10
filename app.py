from flask import Flask, render_template, request, redirect, url_for, jsonify
from gmaps import generateMap, generateCountyMap
from FindingStations import stationCalc, hospitalCalc
import googlemaps
import regex as re
import urllib
import pprint

app = Flask(__name__)
google_maps = googlemaps.Client(key='AIzaSyBx2lGCeaLjMTNblROj3I4iNL8DWi45jvk')


@app.route('/', methods=['POST', 'GET'])
def index():
    if request.method == 'POST':
        address = request.form['address']
        try:
            pattern = re.compile("[0-9]+ ([a-zA-Z]+ )?([a-zA-Z]+ )?([a-zA-Z]+ )?([a-zA-Z]+ )?[a-zA-Z]+, ([a-zA-Z]+ )?"
                                 "([a-zA-Z]+ )?([a-zA-Z]+ )?([a-zA-Z]+ )?[a-zA-Z]+, ([a-zA-Z]+ )?[a-zA-Z]+ [0-9]+, "
                                 "([a-zA-Z]+ )?[a-zA-Z]+")
            geocode_result = google_maps.geocode(address)
            geocode_input = geocode_result[0]['formatted_address']
            if re.search(pattern, geocode_input):
                return redirect(url_for('services', address=geocode_input))
            else:
                error_msg = "Please input a valid address. Example: 6392 Truckee Court, Newark, CA"
        except:
            error_msg = "Please input an address. Example: 6392 Truckee Court, Newark, CA"
        return render_template('index.html', error_msg=error_msg)
    else:
        return render_template('index.html')


@app.route('/about-us', methods=['POST', 'GET'])
def about_us():
    return render_template('elements.html')


@app.route('/services', methods=['POST', 'GET'])
def services():
    time = 0
    destination = src = distance = county_src = "None"
    locations = {'hospital': [40.3453453, -79.8327498]}
    go_home = False
    if request.method == 'POST':
        latitude = request.get_json()[0]
        longitude = request.get_json()[1]
        address = google_maps.reverse_geocode((latitude, longitude))[0]['formatted_address']
        address = {'address': urllib.parse.urlencode({'address': address})}
        return jsonify(address)
    try:
        address = request.args.get('address')
        address_components = google_maps.geocode(address)
        # print("Got address")
        #
        # county = address_components[0]['address_components'][3]['long_name']
        # state = address_components[0]['address_components'][4]['short_name']
        # print("Got county and state")
        #
        # # _, station_addresses = stationCalc(county, state)
        # # _, hospital_addresses = hospitalCalc(county, state)
        # # print("Got station and hospital addresses")
        # #
        # # county_src, locations = generateCountyMap(address, station_addresses, hospital_addresses)
        # # print("Generated county map")
        src, time, distance, destination = generateMap(address)
        print("Generated map")
    except:
        go_home = True

    markers = []
    for location in locations:
        loc_lat_long = [locations[location][0], locations[location][1], location,
                        '/static/images/favicon_red_marker.png']
        markers.append(loc_lat_long)
    return render_template('landing.html',
                           time=time,
                           destination=destination,
                           distance=distance,
                           go_home=go_home,
                           src=src,
                           county_src=county_src,
                           markers=markers)


@app.route('/education', methods=['POST', 'GET'])
def education():
    return render_template('generic.html')
