var express = require('express');
var auth = require('../middlewares/authorize');
var User = require('../models/user');
var utils = require('../utils');

var users = express.Router();

users.get('/', auth.isAdmin(), function(req, res) {
  User.find()
  .then(function(users) {
    res.status(200).json(users);
  })
  .catch(function(err) {
    res.status(500).json(err);
  });
});

module.exports = users;
