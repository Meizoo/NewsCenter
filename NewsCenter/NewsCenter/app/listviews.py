from django.views import generic
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from .models import *

import math

class ArticleListView(generic.ListView):
	def __init__(self):
		self.querytable = [[]]
		queryset = News.objects.all()
		for i in range(0, math.ceil(len(queryset) / row)):
			self.querytable.append([queryset[i * row + j] for j in range(0, row) if i * row + j < len(queryset)])
		row = 3
