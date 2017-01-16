var express = require('express');
var passport = require('passport');
var users = require('./users');
var auth = require('./auth');

var isAuthenticated = passport.authenticate('jwt', { session: false });

var registerApiRoutes = function(app) {
  var api = express.Router();

  app.use('/api', api);

  api.use('/', auth);
  
  // /api/users
  api.use('/users', isAuthenticated, users);
};

module.exports = registerApiRoutes;
