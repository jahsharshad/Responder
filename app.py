from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)


@app.route('/', methods=['POST', 'GET'])
def index():
    if request.method == 'POST':
        address = request.form['address']

        print(address)
        try:
            return redirect(url_for('maps', address=address))
        except:
            return "Lol"
    else:
        return render_template('index.html')


@app.route('/about-us', methods=['POST', 'GET'])
def about_us():
    return render_template('elements.html')


@app.route('/services', methods=['POST', 'GET'])
def services():

    return render_template('landing.html')


@app.route('/education', methods=['POST', 'GET'])
def education():
    return render_template('generic.html')
