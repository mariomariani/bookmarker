var jwt = require('jwt-simple');
var config = require('../config/database');

var generateToken = function(user) {
  return jwt.encode(user, config.secret);
};

module.exports = {
  generateToken: generateToken
};
