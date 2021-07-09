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


@app.route('/about', methods=['POST', 'GET'])
def about():
    return render_template('about.html')


@app.route('/maps', methods=['POST', 'GET'])
def maps():

    return render_template('landing.html')


@app.route('/elements', methods=['POST', 'GET'])
def elements():
    return render_template('elements.html')


@app.route('/generic', methods=['POST', 'GET'])
def generic():
    return render_template('generic.html')
