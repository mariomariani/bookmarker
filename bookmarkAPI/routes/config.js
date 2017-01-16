var express = require('express');
var passport = require('passport');
var auth = require('./auth');
var users = require('./users');
var bookmarks = require('./bookmarks');

var isAuthenticated = passport.authenticate('jwt', { session: false });

var registerApiRoutes = function(app) {
  var api = express.Router();

  app.use('/api', api);

  api.use('/', auth);
  // /api/users
  api.use('/users', isAuthenticated, users);
  // /api/bookmarks
  api.use('/bookmarks', isAuthenticated, bookmarks);
};

module.exports = registerApiRoutes;
