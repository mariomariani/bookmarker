import requests
from bookmarker.models import User

def merge_errors(errors=[]):
    return ', '.join(errors)

def fix_ids(mongo_objs):
    for obj in mongo_objs:
        fix_id(obj)
    return mongo_objs

def fix_id(mongo_obj):
    mongo_obj['id'] = mongo_obj['_id']
    return mongo_obj

def get_auth_header(user):
    return { 'Authorization': 'JWT {0}'.format(user.token) }

class BookmarkService:
    
    def __init__(self):
        self.bookmarks_url = 'http://localhost:3000/api/bookmarks'

    def get_user_bookmarks(self, user):
        response = requests.get(self.bookmarks_url, 
            headers=get_auth_header(user))
        
        if response.status_code == 200:
            bookmarks = response.json()
            return fix_ids(bookmarks)

    def get_bookmark(self, user, bookmark_id):
        url = '{0}/{1}'.format(self.bookmarks_url, bookmark_id)

        response = requests.get(url,
            headers=get_auth_header(user))

        if response.status_code == 200:
            bookmark = response.json()
            return fix_id(bookmark)

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

    def get_users(self, user):
        users = requests.get(self.users_url, 
            headers=get_auth_header(user)).json()

        return fix_ids(users)
