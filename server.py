from flask import Flask, render_template, request
import requests
import os

app = Flask(__name__)

ipKey = os.getenv("IP_API_KEY")
mapKey = os.getenv("MAP_API_KEY")

# Connect to 'results.html' after a form has been submitted
@app.route('/results', methods=['POST'])
def displayResults():

    # Get input
    inputIpAddress = request.form['ipAddress']

    # Piece together the api address and sent a request
    apiAddress = 'http://api.ipstack.com/' + inputIpAddress + '?access_key=' + ipKey
    req = requests.get(apiAddress)
    res = req.json()

    lat = str(res['latitude'])
    lon = str(res['longitude'])

    info = res['country_name']
    # Add in the google maps API
    map = 'https://maps.googleapis.com/maps/api/staticmap?center=' + lat + ',' + lon + '&size=464x250&zoom=5&scale=2&key=' + mapKey
    return render_template('results.html', location=info, map=map, lon=lon, lat=lat)


# Connect to index.html as the root page
@app.route('/')
def index():
    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True)
