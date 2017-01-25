from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    token = models.TextField()
    is_admin = models.BooleanField(default=False)

class Bookmark(models.Model):
    user_id = models.CharField(max_length=100)
    url = models.URLField()
    version = models.IntegerField()
