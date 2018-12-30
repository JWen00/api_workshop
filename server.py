# request is an object within Flask
from flask import Flask, render_template, request

# requests is library within python
import requests

# __name__ replaces it with the name of the current module
app = Flask(__name__)

apiKey = '9a1e74f96964cbac369d4c6d942de867'

# Connect to 'results.html' after a form has been submitted
@app.route('/results', methods=['POST'])
def displayResults():

    # Grab whatever was requested
    inputIpAddress = request.form['ipAddress']

    # Piece together the api address and sent a request
    apiAddress = 'http://api.ipstack.com/' + inputIpAddress + '?access_key=' + apiKey
    req = requests.get(apiAddress)

    # parse the response using json
    res = req.json()

    # specifically grab the country name
    info = res['country_name']

    # open 'results.html' giving the information 'location'
    return render_template('results.html', location=info)


# Connect to index.html as the root page
@app.route('/')
def index():
    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True)
