var JwtStrategy = require('passport-jwt').Strategy;
var ExtractJwt = require('passport-jwt').ExtractJwt;
var User = require('../app/models/user');
var config = require('./database');
 
var jwtStrategy = function(passport) {
  var opts = {};
  opts.jwtFromRequest = ExtractJwt.fromAuthHeader();
  opts.secretOrKey = config.secret;

  var jwtAuthentication = function(jwtPayload, done) {
    var findById = { id: jwtPayload.id };

    User.findOne(findById, function(err, user) {
      if (err) {
        return done(err, false);
      }

      return done(null, user);
    });
  };

  passport.use(new JwtStrategy(opts, jwtAuthentication));
};

module.exports = jwtStrategy;
