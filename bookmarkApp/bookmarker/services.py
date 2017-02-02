import requests

def merge_errors(errors=[]):
    return { 'error_message': ', '.join(errors) }

def fix_id(bookmark):
    bookmark['id'] = bookmark['_id']

def get_auth_header(user):
    return { 'Authorization': 'JWT {0}'.format(user.token) }

class BookmarkService:
    
    def __init__(self):
        self.bookmarks_url = 'http://localhost:3000/api/bookmarks'

    def getUserBookmarks(self, user):
        bookmarks = requests.get(self.bookmarks_url, 
            headers=get_auth_header(user)).json()

        for bookmark in bookmarks:
            fix_id(bookmark)

        return bookmarks

    def getBookmark(self, user, bookmark_id):
        url = '{0}/{1}'.format(self.bookmarks_url, bookmark_id)

        bookmark = requests.get(url,
            headers=get_auth_header(user)).json()

        fix_id(bookmark)
        return bookmark

    def addBookmark(self, user, bookmark):
        bookmark = requests.post(self.bookmarks_url,
            headers=get_auth_header(user), data=bookmark).json()
        return bookmark

    def updateBookmark(self, user, bookmark):
        url = '{0}/{1}'.format(self.bookmarks_url, bookmark['id'])

        bookmark = requests.put(url,
            headers=get_auth_header(user), data=bookmark).json()
        return bookmark
