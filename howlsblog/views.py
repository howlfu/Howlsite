#coding=utf-8
from django.shortcuts import render, render_to_response
from django.http.response import HttpResponse, HttpResponseRedirect
from django.contrib import auth #user login
from django.contrib.auth.decorators import login_required 
from django.core.mail import send_mail
from django.contrib.auth.models import User
from django.views.decorators.csrf import csrf_exempt

from datetime import datetime
from .models import Post, Photos
from .tests import Get_url, UserCreateForm


# Create your views here.    
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
    #album_wanted = ['美睫','6D','Timeline Photos']
    #works_obj = Get_url(album_wanted)
    #works_obj.from_album_url()
    photo_list = Photos.objects.all()
    #return render(request, 'works.html',{'urls': works_obj.url_of_photo} )
    return render(request, 'works.html',{'albums': photo_list})

@csrf_exempt
def login(request):
    #進入此login.html前先檢查是否註冊
    if request.method == "POST":
        if request.user.is_authenticated():
            return HttpResponseRedirect('/')
        #取得request網頁的資料
        username = request.POST.get('username', '')
        password = request.POST.get('password', '')
        #取得user資料 沒有會回傳None
        user = auth.authenticate(username=username, password=password)
        if user is not None and user.is_active:
            auth.login(request, user)
            return HttpResponseRedirect('/')
        else:
            return render(request, 'login.html',{'first': False})
    else:
        return render(request, 'login.html',{'first': True})
    
@csrf_exempt
def forget(request):
    if request.method == "POST":
        user_n = request.POST.get('username', '')
        try:
            user = User.objects.get(username=user_n)
        except:
            return render(request,'forget.html',{'first': False,'find': False})
        meg_of_password = str(user) + '您好，/n 重設密碼為:abcd1234'
        user_mail = user.email
        print(meg_of_password + user_mail)
        send_mail('蕎藝美睫密碼通知',
                meg_of_password,
                'howlfu@gmail.com',
                [user_mail],
                )
        return render(request,'forget.html',{'first': False,'find': True})
    else:
        return render(request,'forget.html',{'first': True,'find': False})

    
@csrf_exempt
def logout(request):
    auth.logout(request)
    return HttpResponseRedirect('/')

@csrf_exempt
def reg(request):
    if request.method == 'POST':
        form = UserCreateForm(request.POST)
        if form.is_valid():
            user = form.save()
            return HttpResponseRedirect('/accounts/login/')
    else:
        form = UserCreateForm()
    return render_to_response('regist.html',locals())

#＠login_required
#def message_board(request):
#    restaurants = Restaurant.objects.all()
#    return render_to_response('restaurants_list.html',locals())

def post_detail(request, pk):
    post = Post.objects.get(pk=pk)
    return render(request, 'post.html', {'post': post})
