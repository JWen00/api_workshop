from flask import Flask, render_template, request
import requests
app = Flask(__name__)
# name replaces it with the name of the module

apiKey = '9a1e74f96964cbac369d4c6d942de867'
# we need to call the API


@app.route('/results', methods=['POST'])
def displayResults():
    inputIpAddress = request.form['ipAddress']
    apiAddress = 'http://api.stack.com/' + inputIpAddress + '?access_key=' + apiKey
    req = requests.get(apiAddress)
    res = req.text
    return res
    #info = str(response['country_name'])
    # return render_template('results.html')


@app.route('/')
def index():
    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True)

# @5:35 (Line 15) I'm not too sure about the logistics of the request.get() Because it's slightly different I'm not sure if they one on the website is suitable only for nodejs
