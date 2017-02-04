import requests
from bookmarker.models import User

def merge_errors(errors=[]):
    return ', '.join(errors)

def fix_id(bookmark):
    bookmark['id'] = bookmark['_id']

def get_auth_header(user):
    return { 'Authorization': 'JWT {0}'.format(user.token) }

class BookmarkService:
    
    def __init__(self):
        self.bookmarks_url = 'http://localhost:3000/api/bookmarks'

    def get_user_bookmarks(self, user):
        bookmarks = requests.get(self.bookmarks_url, 
            headers=get_auth_header(user)).json()

        for bookmark in bookmarks:
            fix_id(bookmark)

        return bookmarks

    def get_bookmark(self, user, bookmark_id):
        url = '{0}/{1}'.format(self.bookmarks_url, bookmark_id)

        bookmark = requests.get(url,
            headers=get_auth_header(user)).json()

        fix_id(bookmark)
        return bookmark

    def add_bookmark(self, user, bookmark):
        bookmark = requests.post(self.bookmarks_url,
            headers=get_auth_header(user), data=bookmark).json()
        return bookmark

    def update_bookmark(self, user, bookmark):
        url = '{0}/{1}'.format(self.bookmarks_url, bookmark['id'])

        bookmark = requests.put(url,
            headers=get_auth_header(user), data=bookmark).json()
        return bookmark

class UserService:
    
    def __init__(self):
        self.users_url = 'http://localhost:3000/api/users'
        self.signup_url = 'http://localhost:3000/api/signup'

    def create_user(self, username, password, errors=[]):
        data = {
            'username': username,
            'password': password,
        }

        response = requests.post(self.signup_url, data=data)
        if response.status_code == 201:
            backend_user = response.json()
            return backend_user
        else:
            error_message = response.json()['message']
            errors.append(error_message)


