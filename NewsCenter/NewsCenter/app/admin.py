from django.contrib import admin
from django.contrib.auth.models import User
from .models import *

class AdminUserProfile(admin.ModelAdmin):
	list_display = ('user','role')

class AdminNews(admin.ModelAdmin):
	list_display = ('title', 'date', 'description', 'address')

class AdminInterested(admin.ModelAdmin):
	list_display = ('id_user','id_news')

class AdminDeclaration(admin.ModelAdmin):
	list_display = ('id_user','id_news')

class AdminComment(admin.ModelAdmin):
	list_display = ('id_user','comment')

class AdminCommentNews(admin.ModelAdmin):
	list_display = ('id_comment','id_user')

class AdminAssociation(admin.ModelAdmin):
	list_display = ('name', 'owner', 'contact', 'address')

admin.site.register(UserProfile, AdminUserProfile)
admin.site.register(Association, AdminAssociation)
admin.site.register(Declaration, AdminDeclaration)
admin.site.register(News, AdminNews)
admin.site.register(CommentNews)
admin.site.register(Interested)
admin.site.register(Comment)
