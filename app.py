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

        try:
            geocode_result = google_maps.geocode(address)
            if geocode_result:
                return redirect(url_for('services', address=geocode_result[0]['formatted_address']))
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
    destination = "None"
    try:
        address = request.args.get('address')
        time, destination = time_estimate(address)
        go_home = False
    except:
        go_home = True
    return render_template('landing.html', time=time, destination=destination, go_home=go_home)


@app.route('/education', methods=['POST', 'GET'])
def education():
    return render_template('generic.html')
