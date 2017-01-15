var express = require('express');
var bodyParser = require('body-parser');
var morgan = require('morgan');
var passport = require('passport');
var jwtStrategy = require('./config/passport')
var registerApiRoutes = require('./app/routes/config')

var port = process.env.PORT || 3000;
var app = express();

// get our request parameters
app.use(bodyParser.urlencoded({ extended: false }));
app.use(bodyParser.json());

// log to console
app.use(morgan('dev'));

// Initialize authentication
app.use(passport.initialize());
jwtStrategy(passport);

registerApiRoutes(app);

// Start the server
app.listen(port);
console.log('Server listening on: http://localhost:' + port);
