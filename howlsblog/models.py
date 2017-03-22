from django.db import models
from datetime import datetime
from django.contrib.auth.models import User

from urllib import error
import requests,json


class Post(models.Model):
    def __str__(self):
        return self.title
    author = models.ForeignKey(User, default="howl")
    title = models.CharField(max_length=100)
    content = models.TextField(blank=True)
    photo = models.URLField(blank=True)
    location = models.CharField(max_length=100, default="Taipei")
    created_at = models.DateTimeField(default=datetime.now)
    
class Get_url(object):
    
    token =''
    fbid = ""
    #url of FB api
    #dm_ur ='https://graph.facebook.com/v2.8/{0}/posts?limit=100&access_token={1}'
    albums_url =''    
    album_wanted_url = ''
    #3D 6D album
    album_wanted = []
    url_of_photo = {}
    url_of_album = []
    
    def __init__(self, albums):
        
        self.url_of_photo = {}
        self.url_of_album = []
        self.album_wanted = albums
        self.token = 'EAACEdEose0cBAF8IYkvW7ppia02lHJZAogO7L6SibH5EKXx7ELptaMRYpd6J7APct2hZBfLCs9ncwpjtHRyqgyfQ7ErRxLaU2Ll28QNnihESHNAsgvZBtOVHVIKBhZCe3yJHVQ7MRRu6d9RxQEZA1DTfqgaeadgYveBKGdRsvFFV7i24xA6ptotuKRIvYqKMZD'
        self.fbid = '256084424576017'
        self.albums_url ='https://graph.facebook.com/v2.8/{0}/albums?&access_token={1}'
        self.album_wanted_url = 'https://graph.facebook.com/v2.8/{0}/albums?access_token={1}&debug=all&fields=photos%7Bimages%7D&format=json&method=get&pretty=0&suppress_http_code=1'

        
    def from_album_url(self):
    # coding=utf-8
        try:
            #get photo
            album_IDs={}
            resp_album = requests.get(self.albums_url.format(self.fbid,self.token))
            jsdata_album = json.loads(resp_album.text)
            #get album IDs that we wanted.
            for data in jsdata_album['data']:
                if data['name'] in self.album_wanted:
                    album_IDs[data['id']]= data['name']
            print(album_IDs)
            #get all photos in album we wanted.
            #get URL from album
            resp_photo = requests.get(self.album_wanted_url.format(self.fbid,self.token))
            jsdata_photo = json.loads(resp_photo.text) 
            url_count = 0;
            for data in jsdata_photo['data']:
                self.url_of_album = []
                if data['id'] in album_IDs.keys():
                    for d in data['photos']['data']:
                        list_img = d['images']
                        self.url_of_album.append(list_img[0]['source'])
                        url_count += 1
                    self.url_of_photo[album_IDs[data['id']]] = self.url_of_album
            return True
        
        except error.URLError as e:
            print(e.reason)  
