from django.views import generic
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from .models import *

import math

class ArticleListView(generic.ListView):
	model = News
	template_name = 'NewsCenter/article.html'
	context_object_name = 'articles'
	paginate_by = 3
	queryset = News.objects.all()
	querytable = [[]]
	for i in range(0, math.ceil(len(queryset) / paginate_by)):
		querytable.append([])
		for j in range(0, paginate_by):
			length = i * paginate_by + j 
			if length < len(queryset):
				querytable[i].append(queryset[length])
