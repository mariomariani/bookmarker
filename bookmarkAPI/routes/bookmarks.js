var express = require('express');
var auth = require('../middlewares/authorize');
var Bookmark = require('../models/bookmark');
var utils = require('../utils');

var bookmarks = express.Router();

bookmarks.get('/', function(req, res) {
  var user = req.user;
  var filter = {};

  if (!user.admin) {
    filter.userId = user._id;
  }
  
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
    _id: BookmarkId,
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
    _id: BookmarkId,
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

  Bookmark.remove({ _id: bookmarkId })
  .then(function() {
    return res.status(200).json({
      message: 'Bookmark removed: ' + bookmarkId
    });
  })
  .catch(function(err) {
    return res.status(500).json(err);
  });
});

module.exports = bookmarks;
