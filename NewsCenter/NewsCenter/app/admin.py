from django.contrib import admin
from .models import *

myModels = [User,News,Interested,Declaration,Comment,CommentNews,Association]

admin.site.register(myModels)