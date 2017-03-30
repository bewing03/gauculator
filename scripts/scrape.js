var request = require('request');
var cheerio = require('cheerio');

var carm_url = "http://menus.tufts.edu/foodpro/shortmenu.asp?sName=Tufts%20Dining&locationNum=09&locationName=Carmichael%20Dining%20Center&naFlag=1";
var dewick_url = "http://menus.tufts.edu/foodpro/shortmenu.asp?sName=Tufts%20Dining&locationNum=11&locationName=Dewick-MacPhie%20Dining%20Center&naFlag=1";

function scrape(url) {
    request(url, function(error, response, body) {
        var $ = cheerio.load(body);
        $(".shortmenurecipes > a").each(function() {
            var item = $(this);
            console.log(item);
        });
    });
}

scrape(carm_url);
scrape(dewick_url);