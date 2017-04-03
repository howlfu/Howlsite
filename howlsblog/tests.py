#coding=utf-8
from django.test import TestCase
from urllib import error
import requests,json
from .models import Photos

from django.contrib.auth.forms import UserCreationForm
from django.db import models
from django import forms
from django.contrib.auth.models import User

# Create your tests here.
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
    current_url = []
    
    def __init__(self, albums):
        
        self.url_of_photo = {}
        self.url_of_album = []
        current_url = []
        self.album_wanted = albums
        self.token = 'EAACEdEose0cBAAwfBcuBV0EWwHKRF5D7ZASn9ZAGpZBpCVXZBiTOGPWq1rh0ilIdjRZCtPLcu9AtiQUcg8KRDZC9HvUw0N2Y0IhZB3Gf6aucoKusLkfpyGK33GfZA80I0mFspSZApn2Q3UHV6ZAZCLVWJ3OkZChDUf1SSTVqnZBVPkCtj7zZCAzeZAJnzRmqZA9omI6Qiy4ZD'
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
            #get all photos in album we wanted.
            #get URL from album
            resp_photo = requests.get(self.album_wanted_url.format(self.fbid,self.token))
            jsdata_photo = json.loads(resp_photo.text) 
            photo_list = Photos.objects.all()
            for data in jsdata_photo['data']:
                self.url_of_album = []
                # get 3D and 6D albums
                url_count = 0;
                if data['id'] in album_IDs.keys():
                    for d in data['photos']['data']:
                        list_img = d['images']
                        #get photo urls
                        self.url_of_album.append(list_img[0]['source'])
                        url_count += 1
                        #add to db
                        #photo_url = Photos.objects.create(album_name= album_IDs[data['id']],photos_url = list_img[0]['source'],photo_count = str(url_count))
                    # {id:urls}
                    self.url_of_photo[album_IDs[data['id']]] = self.url_of_album
            #get current photo in db
            for work in photo_list:
                self.current_url.append(work.photos_url)
            for album in self.url_of_photo.values():
                for new_url in album:
                   if new_url not in self.current_url:
                       print('newcoming: ' + new_url)
            return True
        
        except error.URLError as e:
            print(e.reason)  
            
class UserCreateForm(UserCreationForm):
    
    username = forms.CharField(label=u'名字',required=True)
    email = forms.EmailField(label=u'信箱',error_messages={'invalid':u'輸入正確信箱'})
    password1 = forms.CharField(label=u'密碼',help_text=u"建議長度8且帶有英文",widget=forms.PasswordInput)
    password2 = forms.CharField(label=u'確認',help_text=u"請輸入與上面一致的密碼",widget=forms.PasswordInput)
    error_messages={'password_mismatch': u'密碼不一致',
                    }
    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')   
    def save(self, commit=True):
        user = super(UserCreateForm, self).save(commit)
        user.email = self.cleaned_data["email"]
        if commit:
            user.save()
        return user  
    
        