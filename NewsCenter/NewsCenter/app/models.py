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
	state = models.IntegerField(choices=STATE)

class Interested(models.Model):
    id_user = models.ForeignKey(User, on_delete=models.PROTECT)
    id_news = models.ForeignKey(News, on_delete=models.PROTECT)

class Declaration(models.Model):
    id_user = models.ForeignKey(User, on_delete=models.PROTECT)
    id_news = models.ForeignKey(News, on_delete=models.PROTECT)

class Comment(models.Model):
	id_user = models.ForeignKey(User, on_delete=models.PROTECT)
	comment = models.CharField(max_length=128)

class CommentNews(models.Model):
    id_comment = models.ForeignKey(Comment, on_delete=models.PROTECT)
    id_news = models.ForeignKey(News, on_delete=models.PROTECT)

class Association(models.Model):
	name = models.CharField(max_length=32)
	owner = models.ForeignKey(User, on_delete=models.PROTECT)
	contact = models.CharField(max_length=32)
	address = models.CharField(max_length=128)
