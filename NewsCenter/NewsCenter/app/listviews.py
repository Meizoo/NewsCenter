from django.views import generic
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from .models import *

import math

class ArticleListView(generic.ListView):
	def __init__(self):
		model = News
		paginate_by = 3
		queryset = News.objects.all()
		self.querytable = [[]]
		for i in range(0, math.ceil(len(queryset) / paginate_by)):
			self.querytable.append([])
			for j in range(0, paginate_by):
				length = i * paginate_by + j 
				if length < len(queryset):
					self.querytable[i].append(queryset[length])