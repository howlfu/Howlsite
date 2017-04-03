"""Howlsite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from howlsblog.views import home
from howlsblog.views import about
from howlsblog.views import map
from howlsblog.views import env
from howlsblog.views import works
from howlsblog.views import login
from howlsblog.views import logout
from howlsblog.views import reg
from howlsblog.views import post_detail
from howlsblog.views import forget

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', home, name='home'),
    url(r'^about/$', about, name='about'),
    url(r'^map/$', map, name='map'),
    url(r'^env/$', env, name='env'),
    url(r'^works', works, name='works'),
    url(r'accounts/login/$', login, name='login'),
    url(r'accounts/logout/$', logout, name='logout'),
    url(r'accounts/regist/$', reg, name='reg'),
    url(r'accounts/login/forget/$', forget, name='forget'),
    url(r'^post/(?P<pk>\d+)/$', post_detail, name='post_detail'),
]
