var express = require('express');
var auth = require('../middlewares/authorize');
var Bookmark = require('../models/bookmark');
var utils = require('../utils');

var bookmarks = express.Router();

bookmarks.get('/', auth.isAdmin(), function(req, res) {
  Bookmark.find()
  .then(function(bookmarks) {
    res.status(200).json(bookmarks);
  })
  .catch(function(err) {
    res.status(500).json(err);
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
    res.status(201).json({
      message: 'Bookmark created: ' + createdBookmark.url
    });
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
    bookmarkId: bookmarkId,
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
      res.status(200).json({
        message: 'Bookmark updated: ' + createdBookmark.url
      });
    });
  })
  .catch(function(err) {
    return res.status(500).json(err);
  });
});

module.exports = bookmarks;
