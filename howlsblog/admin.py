from django.contrib import admin

# Register your models here.
from .models import Post,Photos,user_regist

admin.site.register(Post)
admin.site.register(Photos)
admin.site.register(user_regist)
