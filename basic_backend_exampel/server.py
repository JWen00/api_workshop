# request is an object within Flask
from flask import Flask, render_template, request

# requests is library within python
import requests

# __name__ replaces it with the name of the current module
app = Flask(__name__)


@app.route('/results', methods=['POST'])
def displayResults():

    # Grab whatever was requested
    fullName = request.form['fname'] + request.form['lname']

    # open 'results.html' giving the information 'location'
    return render_template('results.html', fullName=fullName)


# Connect to index.html as the root page
@app.route('/')
def index():
    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True)
