"""
Definition of models.
"""

from django.db import models

# Create your models here.
class News(models.Model):
    title = models.CharField(max_length = 32)
    date = models.DateTimeField()
    description = models.TextField()
    address = models.CharField(max_length = 32)

class Interested(models.Model):
    id_user = models.ForeignKey(User)
    id_news = models.ForeignKey(News)

class Declaration(models.Model):
    id_user = models.ForeignKey(User)
    id_news = models.ForeignKey(News)

class Comments(models.Model):
    id_comment = models.ForeignKey(Comment)
    id_news = models.ForeignKey(News)

STATE = ( # todo rewrite into Models.field
		(1, 'BANNED'),
		(2, 'GUEST'),
		(3, 'USER'),
		(4, 'MODERATOR'),
		(5, 'ADMINISTRATOR'),
		(6, 'HEAD_ADMINISTRATOR'),	
	)

class Association(models.Model):
	name = models.CharField(max_length=32)
	owner = models.ForeignKey(User)
	contact = models.CharField(max_length=32)
	address = models.CharField(max_length=128)

class User(models.Model):
	name = models.CharField(max_length=64)
	surname = models.CharField(max_length=128)
	age = models.IntegerField()
	state = models.CharField(max_length=1, choices=STATE)

class Comment(models.Model):
	user_id = models.ForeignKey(User)
	comment = models.CharField(max_length=128)

class NewsComment(models.Model):
	news_id = models.ForeignKey(News)
	user_id = models.ForeignKey(User)
