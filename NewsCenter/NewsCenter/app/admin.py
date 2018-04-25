from django.contrib import admin
from .models import *

models_db = [User,News,Interested,Declaration,Comment,CommentNews,Association]

admin.site.register(models_db)