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
