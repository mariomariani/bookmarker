var express = require('express');
var bodyParser = require('body-parser');
var morgan = require('morgan');
var passport = require('passport');
var mongoose = require('mongoose');
var dbConf = require('./config/database')
var jwtStrategy = require('./config/passport')
var registerApiRoutes = require('./routes/config')

var port = process.env.PORT || 3000;
var app = express();

// Get request parameters
app.use(bodyParser.urlencoded({ extended: false }));
app.use(bodyParser.json());

// Log requests to console
app.use(morgan('dev'));

// Initialize authentication
app.use(passport.initialize());
jwtStrategy(passport);

// Set mongoose to work with Promises
mongoose.Promise = global.Promise;
mongoose.connect(dbConf.database);

// Register routes
registerApiRoutes(app);

// Start the server
app.listen(port);
console.log('Server listening on: http://localhost:' + port);
