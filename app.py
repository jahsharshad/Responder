from flask import Flask, render_template, request, redirect, url_for
from gmaps import time_estimate
import googlemaps
import pprint

app = Flask(__name__)
google_maps = googlemaps.Client(key='AIzaSyBx2lGCeaLjMTNblROj3I4iNL8DWi45jvk')


@app.route('/', methods=['POST', 'GET'])
def index():
    yourl = "https://www.google.com/maps/embed/v1/directions?origin=place_id:ChIJJ2jwac6_j4ARF0TwRREqtMA&destination=39039%20Cherry%20St%2C%20Newark%2C%20CA%2094560%2C%20USA&key=AIzaSyBx2lGCeaLjMTNblROj3I4iNL8DWi45jvk"

    if request.method == 'POST':
        address = request.form['address']
        yourl = "https://www.google.com/maps/embed/v1/directions?origin=place_id:ChIJJ2jwac6_j4ARF0TwRREqtMA&destination=Washington%20Hospital%20Healthcare%20System%2C%202000%20Mowry%20Ave%2C%20Fremont%2C%20CA%2094538&key=AIzaSyBx2lGCeaLjMTNblROj3I4iNL8DWi45jvk"

        try:
            geocode_result = google_maps.geocode(address)
            if geocode_result:
                return redirect(url_for('services', address=geocode_result[0]['formatted_address']))
        except:
            error_msg = "Please input an address. Example: 6392 Truckee Court, Newark, CA"
            return render_template('index.html', error_msg=error_msg, src=yourl)
    else:
        return render_template('index.html', src=yourl)


@app.route('/about-us', methods=['POST', 'GET'])
def about_us():
    return render_template('elements.html')


@app.route('/services', methods=['POST', 'GET'])
def services():
    address = request.args.get('address')
    time, destination = time_estimate(address)
    return render_template('landing.html', time=time, destination=destination)


@app.route('/education', methods=['POST', 'GET'])
def education():
    return render_template('generic.html')
