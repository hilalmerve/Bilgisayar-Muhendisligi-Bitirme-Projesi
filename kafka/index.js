var express = require("express");
var app = express();
var path = require('path');
var ejsLayouts = require("express-ejs-layouts");
var bodyParser = require('body-parser');


app.set("view engine", "ejs");
app.set('views', path.join(__dirname, './views'));

app.use(bodyParser.urlencoded({extended : false}));
app.use(bodyParser.json());
app.use(ejsLayouts);

app.use('./public', express.static(path.join(__dirname, 'public')));
require('./routers/routeManager')(app);

require('events').EventEmitter.defaultMaxListeners = 15;

app.listen(7000, () => {
    console.log("7000 No'lu Port Dinleniyor..");
});