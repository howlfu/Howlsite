#coding=utf-8
from django.shortcuts import render
from django.http.response import HttpResponse
from datetime import datetime
from .models import Post, Get_url

# Create your views here.
#def home(request):
#    post_list = Post.objects.all()
#    return render(request, 'home.html', {
#        'post_list': post_list,
#    })
    
def home(request):
    post_list = Post.objects.all()
    return render(request, 'home.html')
def about(request):
    return render(request, 'about.html')
def map(request):
    return render(request, 'map.html')
def env(request):
    return render(request, 'env.html')
def works(request):
    album_wanted = ['美睫','6D']
    works_obj = Get_url(album_wanted)
    works_obj.from_album_url()
    return render(request, 'works.html',{'urls': works_obj.url_of_photo} )

def post_detail(request, pk):
    post = Post.objects.get(pk=pk)
    return render(request, 'post.html', {'post': post})
