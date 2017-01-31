# from django.contrib.auth.models import User
from bookmarker.models import User
import requests

class AuthBackend(object):

    def authenticate(self, username=None, password=None, errors=[]):
        backend_user = self.backend_authenticate(username, password, errors)
        if backend_user:
            try:
                user = User.objects.get(username=username)
            except User.DoesNotExist:
                # Create a new Django user if successfully authenticated
                user = User(username=username)
                user.is_superuser = backend_user['admin']
                user.is_admin = backend_user['admin']
                user.token = backend_user['token']
                user.save()
            return user
        
    def get_user(self, id):
        return User.objects.get(id=id)

    def backend_authenticate(self, username, password, errors=[]):
        url = 'http://localhost:3000/api/authenticate'
        body = {
            "username": username,
            "password": password,
        }
        response = requests.post(url, body)

        if response.status_code == 200:
            user = response.json()['user']
            user['token'] = response.json()['token']
            return user
        else:
            error_message = response.json()['message']
            errors.append(error_message)
