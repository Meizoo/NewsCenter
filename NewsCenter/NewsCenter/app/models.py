"""
	Definition of models.
"""

from django.db import models
from django.contrib.auth.models import User

STATE = (
		(1, 'BANNED'),
		(2, 'GUEST'),
		(3, 'USER'),
		(4, 'MODERATOR'),
		(5, 'ADMINISTRATOR'),
		(6, 'HEAD_ADMINISTRATOR'),
	)

class News(models.Model):
	title	   = models.CharField(max_length = 32)
	date		= models.DateTimeField()
	description = models.TextField()
	address	 = models.CharField(max_length = 32)
	created	 = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return f'{self.title} {self.date}'

	class Meta:
		verbose_name_plural = 'News'

class Interested(models.Model):
	id_user = models.ForeignKey(User, null=True, on_delete=models.DO_NOTHING)
	id_news = models.ForeignKey(News, null=True, on_delete=models.DO_NOTHING)

	def __str__(self):
		return f'{self.id_user} interested to {self.id_news}'

class Declaration(models.Model):
	id_user = models.ForeignKey(User, null=True, on_delete=models.DO_NOTHING)
	id_news = models.ForeignKey(News, null=True, on_delete=models.DO_NOTHING)

	def __str__(self):
		return f'{self.id_user} declaration to {self.id_news}'

class Comment(models.Model):
	id_user = models.ForeignKey(User, on_delete=models.PROTECT)
	comment = models.CharField(max_length=128)

	def __str__(self):
		return f'{self.id_user} comment'

class CommentNews(models.Model):
	id_comment = models.ForeignKey(Comment, on_delete=models.CASCADE)
	id_news	= models.ForeignKey(News, on_delete=models.CASCADE)

	def __str__(self):
		return f'{self.id_comment} commented to {self.id_news}'

	class Meta:
		verbose_name_plural = 'CommentNews'

class Association(models.Model):
	name	= models.CharField(max_length=32)
	owner   = models.ForeignKey(User, on_delete=models.PROTECT)
	contact = models.CharField(max_length=32)
	address = models.CharField(max_length=128)

	def __str__(self):
		return self.name