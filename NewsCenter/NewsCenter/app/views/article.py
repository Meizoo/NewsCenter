from django.shortcuts import render,render_to_response,get_object_or_404

from app import models, forms

from django.http             import HttpRequest,Http404,HttpResponseRedirect
from django.template         import RequestContext
from django.utils.safestring import mark_safe
from django.utils.html       import conditional_escape
from django.contrib          import messages

from datetime import datetime, date
from calendar import HTMLCalendar

from app.calendar_pattern import *

from ..models    import *
from ..forms     import EntryForms
from ..listviews import ArticleListView

# News handlers
def index(request):
	"""Renders the articles"""
	return render(request, 'app/news/index.html', {'news': ArticleListView})

def details(request, pk):
	"""Renders the article's details"""
	return render(request, 'app/news/details.html', {
		'new': News.objects.get(id=pk), 
		'comments' : Comment.objects.filter(pk=pk)
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

	return render(request, 'app/news/upgrade.html', {'news': news})