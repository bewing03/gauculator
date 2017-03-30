// Express initialization
var express = require('express');
var app = express();
var fs = require('fs');
var request = require('request');
var cheerio = require('cheerio');
var path = require('path');
var bodyParser = require('body-parser');
var form = require('express-form');
var field = form.field;

// Mongo initialization, setting up a connection to a MongoDB  (on Heroku or localhost)
var mongoUri = process.env.MONGOLAB_URI || process.env.MONGOHQ_URL || 'mongodb://localhost/gauculator';
var mongo = require('mongodb');
var db = mongo.connect(mongoUri, function (error, databaseConnection) {
    db = databaseConnection;
});

app.use(express.static('public'));
app.use(bodyParser.json());
app.use(bodyParser.urlencoded({ extended: true }));

app.get('/', function (req, res) {
    res.set('Content-Type', 'text/html');
      
    url = 'http://menus.tufts.edu/foodpro/shortmenu.asp?sName=Tufts%20Dining&locationNum=09&locationName=Carmichael%20Dining%20Center&naFlag=1';
  
    request(url, function(error, response, html){
        if(!error){
            var $ = cheerio.load(html);
            var food;
            var food_items = [];
            $('.shortmenurecipes').filter(function(){
                var data = $(this);
                food = data.children().first().text().trim();
                food_items.push(food);
            })
        }
        console.log(food_items);
    })
});

app.post('/', form(field("email").trim().isEmail()), function (req, res) {
    if (!req.form.isValid) {
       console.log(req.form.errors);
    }
    
    else {
         var email = req.form.email;
         var toInsert = {
                "email": email,
        };
        db.collection('emails', function(error, coll) {
		coll.insert(toInsert, function(error, saved) {
			if (error) {
				console.log("Error: " + error);
				res.send(500);
			}
			else {
                res.sendFile(path.join(__dirname + '/../public/thankyou.html'));
			}
	    });
	   });
    }
});

// Oh joy! http://stackoverflow.com/questions/15693192/heroku-node-js-error-web-process-failed-to-bind-to-port-within-60-seconds-of
app.listen(process.env.PORT || 3000);