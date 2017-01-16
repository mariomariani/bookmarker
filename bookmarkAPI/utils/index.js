var jwt = require('jwt-simple');
var config = require('../config/database');

var generateToken = function(user) {
  return jwt.encode(user, config.secret);
};

var decodeToken = function(requestToken) {
  // Remove JWT prefix from requestToken
  var token = requestToken.split(' ')[1];
  return jwt.decode(token, config.secret);
};

module.exports = {
  generateToken: generateToken,
  decodeToken: decodeToken
};
