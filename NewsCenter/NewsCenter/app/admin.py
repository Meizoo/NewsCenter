from django.contrib import admin
from .models import *

class AdminNews(admin.ModelAdmin):
	list_display = ('title', 'date', 'description', 'address')

class AdminInterested(admin.ModelAdmin):
	list_display = ('id_user','id_news')

class AdminUser(admin.ModelAdmin):
	list_display = ('name','surname','age','state')

class AdminDeclaration(admin.ModelAdmin):
	list_display = ('id_user','id_news')

class AdminComment(admin.ModelAdmin):
	list_display = ('id_user','comment')

class AdminCommentNews(admin.ModelAdmin):
	list_display = ('id_comment','id_user')

class AdminAssociation(admin.ModelAdmin):
	list_display = ('name', 'owner', 'contact', 'address')

admin.site.register(Association, AdminAssociation)
admin.site.register(Declaration, AdminDeclaration)
admin.site.register(News, AdminNews)
admin.site.register(User, AdminUser)
admin.site.register(CommentNews)
admin.site.register(Interested)
admin.site.register(Comment)
