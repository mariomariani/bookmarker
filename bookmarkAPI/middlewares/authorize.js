var isAdmin = function() {
  return (req, res, next) => {
    if (!req.user.admin) {
      return res.status(403).send('Unauthorized');
    }
    return next();
  };
};

module.exports = {
  isAdmin: isAdmin
};
