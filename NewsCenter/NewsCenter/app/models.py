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
