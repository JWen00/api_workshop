# request is an object within Flask
from flask import Flask, render_template, request

# requests is library within python
import requests

# __name__ replaces it with the name of the current module
# app = Flask(__name__)

# Changed it to make it work with repl 
app = Flask(__name__, static_folder='.', root_path='/root/runner') 

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
    lat = res['latitude']
    long = res['longitude']
    
    # Add in the google maps API 
    imageLink = 'https://maps.googleapis.com/maps/api/staticmap?center=' + lat + ',' + long + '&size=464x250&zoom=9&scale=1&key=' + mapKey
    
    # open 'results.html' giving the information 'location'
    return render_template('results.html', location=info, map=imageLink)


# Connect to index.html as the root page
@app.route('/')
def index():
    return render_template('index.html')


if __name__ == '__main__':
    # app.run() 
    # Changed it to work on repl.it 
    app.run(host='0.0.0.0', port='3000')
