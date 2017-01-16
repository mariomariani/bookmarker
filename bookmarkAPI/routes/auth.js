var express = require('express');
var User = require('../models/user')

var auth = express.Router();

auth.post('/signup', function(req, res) {
  var username = req.body.username;
  var password = req.body.password;

  if (!username || !password) {
    return res.status(401).json({
      message: 'Username and Password required.'
    });
  }

  User.findOne({ username: username })
  .then(function(user) {
    if (user) {
      return res.status(409).json({
        message: 'Username already taken.'
      });
    }

    var newUser = new User({
      username: username,
      password: password,
      admin: false
    });
  
    newUser.save()
    .then(function(createdUser) {
      res.status(201).json({
        message: 'User created: ' + createdUser.username
      });
    })
  })
  .catch(function(err) {
    return res.status(500).json(err);
  });
});

module.exports = auth;
