var JwtStrategy = require('passport-jwt').Strategy;
var User = require('../app/models/user');
var config = require('./database');
 
module.exports = function(passport) {
  var opts = { secretOrKey: config.secret };

  var jwtAuthentication = function(jwtPayload, done) {
    var findById = { id: jwtPayload.id };

    User.findOne(findById, function(err, user) {
      if (err) {
        return done(err, false);
      }

      if (user) {
        done(null, user);
      } else {
        done(null, false);
      }
    });
  };

  passport.use(new JwtStrategy(opts, jwtAuthentication));
};