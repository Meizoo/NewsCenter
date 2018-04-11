"""
Definition of models.
"""

from django.db import models
from enum import Enum

# Create your models here.

class Association(models.Model):
	name    = name
	owner   = owner
	contact = contact
	address = address

class User(models.Model):
	name    = name
	surname = surname
	age     = age
	state   = state

class State(Enum):
	BANNED             = 1
	GUEST              = 2
	USER               = 3
	MODERATOR          = 4
	ADMINISTRATOR      = 5
	HEAD_ADMINISTRATOR = 6

class Comment(models.Model):
	user_id = models.ForeignKey(User)
	comment = models.CharField(max_length=128)

class NewsComment(models.Model):
	news_id = models.ForeignKey(News)
	user_id = models.ForeignKey(User)
