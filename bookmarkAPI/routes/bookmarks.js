var express = require('express');
var auth = require('../middlewares/authorize');
var Bookmark = require('../models/bookmark');
var utils = require('../utils');

var bookmarks = express.Router();

bookmarks.get('/', function(req, res) {
  var user = req.user;
  var filter = {};

  if (user.admin) {
    Bookmark
    .aggregate()
    .group({ 
      _id: '$userId',
      bookmarks: { $push: '$$ROOT' },
    })
    .lookup({
      from: 'users',
      localField: '_id',
      foreignField: '_id',
      as: 'user',
    })
    .exec(function(err, bookmarks) {
      if (err) {
        return res.status(500).json(
          { message: 'Error getting data' });
      }
      return res.status(200).json(bookmarks);
    });
    
    return;
  }

  filter.userId = user._id;
  
  // Find by userId
  Bookmark.find(filter)
  .then(function(bookmarks) {
    return res.status(200).json(bookmarks);
  })
  .catch(function(err) {
    return res.status(500).json(err);
  });
});

bookmarks.post('/', function(req, res) {
  var user = req.user;
  var url = req.body.url;

  if (!url) {
    return res.status(400).json({
      message: 'Url required.'
    });
  }

  var newBookmark = new Bookmark({
    userId: user._id,
    url: url
  });

  newBookmark.save()
  .then(function(createdBookmark) {
    return res.status(201).json(createdBookmark);
  })
  .catch(function(err) {
    return res.status(500).json(err);
  });
});

bookmarks.get('/:bookmarkId', function(req, res) {
  var user = req.user;
  var bookmarkId = req.params.bookmarkId;

  if (!bookmarkId) {
    return res.status(400).json({
      message: 'BookmarkId required.'
    });
  }

  Bookmark.findOne({
    _id: bookmarkId,
    userId: user._id
  })
  .then(function(bookmark) {
    if (!bookmark) {
      return res.status(404).json({
        message: 'Bookmark not found.'
      });
    }

    return res.status(200).json(bookmark);
  })
  .catch(function(err) {
    return res.status(500).json(err);
  });
});

bookmarks.put('/:bookmarkId', function(req, res) {
  var user = req.user;
  var url = req.body.url;
  var bookmarkId = req.params.bookmarkId;

  if (!url || !bookmarkId) {
    return res.status(400).json({
      message: 'Url and BookmarkId required.'
    });
  }

  Bookmark.findOne({
    _id: bookmarkId,
    userId: user._id
  })
  .then(function(bookmark) {
    if (!bookmark) {
      return res.status(404).json({
        message: 'Bookmark not found.'
      });
    }

    bookmark.url = url;
    bookmark.save()
    .then(function(updatedBookmark) {
      return res.status(200).json(updatedBookmark);
    });
  })
  .catch(function(err) {
    return res.status(500).json(err);
  });
});

bookmarks.delete('/:bookmarkId', function(req, res) {
  var user = req.user;
  var bookmarkId = req.params.bookmarkId;

  if (!bookmarkId) {
    return res.status(400).json({
      message: 'BookmarkId required.'
    });
  }

  Bookmark.findOne({
    _id: bookmarkId,
    userId: user._id
  })
  .then(function(bookmark) {
    if (!bookmark) {
      return res.status(404).json({
        message: 'Bookmark not found.'
      });
    }

    bookmark.remove()
    .then(function() {
      return res.status(200).json({
        message: 'Bookmark removed: ' + bookmarkId
      });
    });
  })
  .catch(function(err) {
    return res.status(500).json(err);
  });
});

module.exports = bookmarks;
