from django.shortcuts import render,render_to_response,get_object_or_404
from app import models
from app import forms

from django.http import HttpRequest,Http404,HttpResponseRedirect
from django.template import RequestContext
from django.utils.safestring import mark_safe
from django.utils.html import conditional_escape
from django.contrib import messages
from app.calendar_pattern import *

from datetime import datetime, date
from calendar import HTMLCalendar
from ..models import *
from ..forms import EntryForms

from ..listviews import ArticleListView

# News handlers
def articles(request):
	"""Renders the articles"""
	return render(request, 'app/news/index.html', {'news': ArticleListView})

def details(request, pk):
	"""Renders the article's details"""
	return render(request, 'app/news/details.html', {'new': News.objects.get(id=pk)})

def add(request):
	"""Adds article"""
	if request.method == 'POST':
		form = EntryForms(request.POST)

		if form.is_valid():
			title = form.cleaned_data['title']
			date = form.cleaned_data['date']
			description = form.cleaned_data['description']
			address = form.cleaned_data['address']
			News.objects.create(
				title = title, 
				date = date, 
				description = description,
				address = address	
			).save()			
			
			return HttpResponseRedirect('/news')
	else:
		form = EntryForms()	

	return render(request, 'app/news/create.html', {'form': form})

def delete(request, id):

	news = News.objects.get(id=id)
	
	if request.method == 'POST':
		news.delete()
		return HttpResponseRedirect('/news')
	
	return render(request,'app/news/delete.html',{'news': news})

