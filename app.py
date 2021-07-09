from flask import Flask, render_template, request, redirect, url_for
from gmaps import time_estimate
import googlemaps
import pprint

app = Flask(__name__)
google_maps = googlemaps.Client(key='AIzaSyBx2lGCeaLjMTNblROj3I4iNL8DWi45jvk')


@app.route('/', methods=['POST', 'GET'])
def index():
    if request.method == 'POST':
        address = request.form['address']

        try:
            geocode_result = google_maps.geocode(address)
            geocode_result = geocode_result[0]['address_components'][0]['short_name'] + ' ' + \
                             geocode_result[0]['address_components'][1]['short_name'] + ', ' + \
                             geocode_result[0]['address_components'][2]['short_name'] + ', ' + \
                             geocode_result[0]['address_components'][4]['short_name']
            if geocode_result:
                return redirect(url_for('services', address=geocode_result))
            else:
                error_msg = "Please input a valid address. Example: 6392 Truckee Court, Newark, CA"
                return render_template('index.html', error_msg=error_msg)
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
    address = request.args.get('address')
    time = time_estimate(address)
    print(time)
    return render_template('landing.html', time=time)


@app.route('/education', methods=['POST', 'GET'])
def education():
    return render_template('generic.html')
