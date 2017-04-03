from django.db import models
from datetime import datetime
from django.contrib.auth.models import User
from django import forms

#requests to get html
#json to analysis Java script


class Post(models.Model):
    def __str__(self):
        return self.title
    author = models.ForeignKey(User, default="howl")
    title = models.CharField(max_length=100)
    content = models.TextField(blank=True)
    photo = models.URLField(blank=True)
    location = models.CharField(max_length=100, default="Taipei")
    created_at = models.DateTimeField(default=datetime.now)
    
class Photos(models.Model):
    def __str__(self):
        return self.album_name
    album_name = models.CharField(max_length=100)
    photo_count = models.CharField(max_length=100)
    photos_url = models.URLField(blank=True)

class user_regist(models.Model):
    def __str__(self):
        return self.name
        name = models.CharField(max_length=100)
        email = models.EmailField(max_length=100)
        pw = models.CharField(max_length=100)
        created_at = models.DateTimeField(default=datetime.now)
 
    