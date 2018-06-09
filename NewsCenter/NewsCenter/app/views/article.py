from django.shortcuts import render, render_to_response, get_object_or_404

from app import models, forms

from django.contrib.auth.models import User

from django.utils.safestring import mark_safe
from django.utils.html       import conditional_escape
from django.template         import RequestContext
from django.contrib          import messages
from django.http             import HttpRequest, Http404, HttpResponseRedirect

from datetime import datetime, date
from calendar import HTMLCalendar

from app.calendar_pattern import *

from app import support
from app.support import render_structs, utilities
from app.support.render_structs import *
from app.support.utilities import *

from ..models    import *
from ..forms     import EntryForms, CommentForms
from ..listviews import ArticleListView

# News handlers
def index(request):
	"""Renders the articles"""
	return render(request, 'app/news/index.html', {'news': ArticleListView})

def details(request, pk):
	"""Renders the article's details"""
	id_user = User.objects.get(id=request.user.id)
	id_news = News.objects.get(id=pk)

	if request.method == 'POST':
		form = CommentForms(request.POST)

		if form.is_valid():
			comment = Comment.objects.create(
				comment = form.cleaned_data['comment'], 
				id_user = id_user
			)
			CommentNews.objects.create(
				id_comment = comment,
				id_news = id_news
			).save()
			comment.save()
			return HttpResponseRedirect('/news')
	else:
		form = EntryForms()	

	return render(request, 'app/news/details.html', {
		'new': News.objects.get(id=pk), 
		'comments' : Comment.objects.filter(id__in=CommentNews.objects.filter(id_news=pk).values_list('id_comment', flat=True)),
		'declaration' : RenderDeclared(not is_none_or_empty(Declaration.objects.filter(id_user=id_user).filter(id_news=id_news))),
		'interested' : RenderInterest(not is_none_or_empty(Interested.objects.filter(id_user=id_user).filter(id_news=id_news)))
	})

def declare(request, pk):
	"""Creates declaration model for given article for current user. """
	id_user = User.objects.get(id=request.user.id)
	id_news = News.objects.get(id=pk)

	d = Declaration.objects.filter(id_user=id_user).filter(id_news=id_news)

	bool = is_none_or_empty(d)

	if bool:
		Declaration.objects.create(
				id_user = id_user,
				id_news = id_news
		).save()
	else:
		d.delete()

	return render(request, 'app/news/details.html', {
		'new': News.objects.get(id=pk), 
		'comments' : Comment.objects.filter(
			id__in=CommentNews.objects.filter(id_news=pk).values_list('id_comment', flat=True)
		),
		'declaration' : RenderDeclared(bool),
		'interested' : RenderInterest(not is_none_or_empty(Interested.objects.filter(id_user=id_user).filter(id_news=id_news)))
	})

def interest(request, pk):
	"""Creates interest model for given article for current user. """
	id_user = User.objects.get(id=request.user.id)
	id_news = News.objects.get(id=pk)

	d = Interested.objects.filter(id_user=id_user).filter(id_news=id_news)

	bool = is_none_or_empty(d)

	if bool:
		Interested.objects.create(
				id_user = id_user,
				id_news = id_news
		).save()
	else:
		d.delete()

	return render(request, 'app/news/details.html', {
		'new': News.objects.get(id=pk), 
		'comments' : Comment.objects.filter(
			id__in=CommentNews.objects.filter(id_news=pk).values_list('id_comment', flat=True)
		),
		'declaration' : RenderDeclared(not is_none_or_empty(Declaration.objects.filter(id_user=id_user).filter(id_news=id_news))),
		'interested' : RenderInterest(bool)
	})

def add(request):
	"""Adds article"""
	if request.method == 'POST':
		form = EntryForms(request.POST)

		if form.is_valid():
			News.objects.create(
				title = form.cleaned_data['title'], 
				date = form.cleaned_data['date'], 
				description = form.cleaned_data['description'],
				address = form.cleaned_data['address']
			).save()			
			
			return HttpResponseRedirect('/news')
	else:
		form = EntryForms()	

	return render(request, 'app/news/create.html', {'form': form})

def delete(request, id):
	"""Deletes article of given id"""
	news = News.objects.get(id=id)
	
	if request.method == 'POST':
		news.delete()
		return HttpResponseRedirect('/news')
	
	return render(request,'app/news/delete.html',{'news': news})

def edit(request, id):
	"""Edits article of given id"""
	news = News.objects.get(id=id)
	return render(request,'app/news/edit.html', {'news': news})

def update(request, id):
	"""Updates article of given id"""
	news = News.objects.get(id=id)

	if request.method == 'POST':
		news.title = request.POST['title'];
		news.date = request.POST['date'];
		news.description = request.POST['description'];
		news.address = request.POST['address'];
		news.save()
		return HttpResponseRedirect('/news')
	return HttpResponseRedirect('/edit')