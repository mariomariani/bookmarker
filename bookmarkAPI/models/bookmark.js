var mongoose = require('mongoose');
var Schema = mongoose.Schema;
var ObjectId = Schema.ObjectId;
  
// set up a mongoose model
var BookmarkSchema = new Schema({
  userId: ObjectId,
  url: String,
});
 
module.exports = mongoose.model('Bookmark', BookmarkSchema);
