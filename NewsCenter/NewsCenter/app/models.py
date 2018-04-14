"""
Definition of models.
"""

from django.db import models

STATE = ( # todo rewrite into Models.field
		(1, 'BANNED'),
		(2, 'GUEST'),
		(3, 'USER'),
		(4, 'MODERATOR'),
		(5, 'ADMINISTRATOR'),
		(6, 'HEAD_ADMINISTRATOR'),	
	)

class News(models.Model):
    title = models.CharField(max_length = 32)
    date = models.DateTimeField()
    description = models.TextField()
    address = models.CharField(max_length = 32)

class User(models.Model):
	name = models.CharField(max_length=64)
	surname = models.CharField(max_length=128)
	age = models.IntegerField()
	state = models.IntegerField(max_length=1, choices=STATE)

class Interested(models.Model):
    id_user = models.ForeignKey(User)
    id_news = models.ForeignKey(News)

class Declaration(models.Model):
    id_user = models.ForeignKey(User)
    id_news = models.ForeignKey(News)

class Comment(models.Model):
	id_user = models.ForeignKey(User)
	comment = models.CharField(max_length=128)

class CommentNews(models.Model):
    id_comment = models.ForeignKey(Comment)
    id_news = models.ForeignKey(News)

class Association(models.Model):
	name = models.CharField(max_length=32)
	owner = models.ForeignKey(User)
	contact = models.CharField(max_length=32)
	address = models.CharField(max_length=128)
