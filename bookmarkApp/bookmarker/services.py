import requests

class BookmarkService:
    
    def getUserBookmarks(self, user):
        url = 'http://localhost:3000/api/bookmarks'
        bookmarks = requests.get(url, headers={ 
            'Authorization': 'JWT {0}'.format(user.token) 
        }).json()
        return bookmarks

    def getBookmark(self, bookmark_id):
    	pass

    def addBookmark(self, user, bookmark):
        url = 'http://localhost:3000/api/bookmarks'
        return requests.post(url, headers={ 
            'Authorization': 'JWT {0}'.format(user.token) 
        }, data = {
        	'url': bookmark.url
        })
