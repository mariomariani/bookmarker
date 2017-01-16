var express = require('express');

var users = express.Router();

users.get('/', function(req, res) {
  res.status(200).json(req);
});

module.exports = users;
