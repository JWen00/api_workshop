# request is an object within Flask
from flask import Flask, render_template, request

# requests is library within python
import requests

# __name__ replaces it with the name of the current module
app = Flask(__name__)

ipKey = '9a1e74f96964cbac369d4c6d942de867'
mapKey = 'AIzaSyBuwAiyYR_IV5y8bD2wLyudCgPquB2qSVM'

# Connect to 'results.html' after a form has been submitted


@app.route('/results', methods=['POST'])
def displayResults():

    # Grab whatever was requested
    inputIpAddress = request.form['ipAddress']

    # Piece together the api address and sent a request
    apiAddress = 'http://api.ipstack.com/' + inputIpAddress + '?access_key=' + ipKey
    req = requests.get(apiAddress)

    # parse the response using json
    res = req.json()

    # specifically grab the country name
    lat = str(res['latitude'])
    lon = str(res['longitude'])

    info = res['country_name']
    # Add in the google maps API
    #imageLink = 'https://maps.googleapis.com/maps/api/staticmap?center=' + lat + ',' + lon + '&size=500x400&zoom=5&scale=2&key=' + mapKey
    #map = 'https://maps.googleapis.com/maps/api/staticmap?center=' + lat + ',' + lon + '&size=464x250&zoom=9&scale=1&key=AIzaSyBuwAiyYR_IV5y8bD2wLyudCgPquB2qSVM'
    map = 'https://maps.googleapis.com/maps/api/staticmap?center=-33.883300,151.100000&size=464x250&zoom=9&scale=1&key=AIzaSyBuwAiyYR_IV5y8bD2wLyudCgPquB2qSVM'
    return render_template('results.html', location=info, map=map)


# Connect to index.html as the root page
@app.route('/')
def index():
    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True)

# working site
#https: // maps.googleapis.com / maps / api / staticmap?center = -33.883300, 151.100000 & size = 464x250 & zoom = 9 & scale = 1 & key = AIzaSyBuwAiyYR_IV5y8bD2wLyudCgPquB2qSVM
# non working
#https: // maps.googleapis.com / maps / api / staticmap?center = -33.8833, 151.1 & size = 464x250 & zoom = 9 & scale = 1 & key = AIzaSyBuwAiyYR_IV5y8bD2wLyudCgPquB2qSVM
