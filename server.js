const express = require('express');
const request = require('request');
const bodyParser = require('body-parser');

// API-KEYconst
apiKey = '9a1e74f96964cbac369d4c6d942de867'


// Create an instance of express
const app = express()

// Use this to render stuff
app.set('view engine', 'ejs');

// Allows access to the 'public' folder
app.use(express.static('public'));

// Used to make of req.body (??)
app.use(bodyParser.urlencoded({extended: true}));

app.get('/', function (req, res) {
    // Render sends the equivalent of index.html to the client
  res.render('index');

});

app.post('/', function(req, res) {
    res.render('index');

    // Grab the addresss from the input information
    // (body --> html body)
    // (address --> input<'name="address'>)
    let address = req.body.address

    // We use php (`) & ${___} to fill information
    request(`http://api.ipstack.com/${address}?access_key=${apiKey}`,
            function(err, response, body) {
        // Checks if the api is working
        if (err) {
            console.log('index', {type: null, error:'Error, please try again'});

        // Api works
        } else {

             // Tokenise the information
             let information = JSON.parse(body)

             // Check that it's a valid ip address
             if (information.type == null) {

                // Display the site: uh oh! something went wrong
                res.render('index', {type:null, error: 'Error, please enter a valid IP address'});
                // Debugging
                let msg = `I'm sorry, ${information.ip} doesn't exist.`
                console.log(msg);

             } else {
                let msg = `We've got information from you! The IP address is from ${information.city}.`;

                // Debugging
                console.log(msg);

                res.render('index', {type: msg, error:null});


             }


        }
    });

})

app.listen(3000, function () {
  console.log('Listening on port 3000!')
})
