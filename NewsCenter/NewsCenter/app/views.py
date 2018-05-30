"""
Definition of views.
"""

from django.shortcuts import render,render_to_response,get_object_or_404
from django.http import HttpRequest,Http404,HttpResponseRedirect
from django.template import RequestContext
from django.utils.safestring import mark_safe
from django.utils.html import conditional_escape
from app.calendar_pattern import *
from datetime import datetime, date
from calendar import HTMLCalendar
from .models import *
from .forms import EntryForms

def home(request):
	"""Renders the home page."""
	assert isinstance(request, HttpRequest)
	return render(
		request,
		'app/home/index.html',
		{
			'title':'Home',
			'year':datetime.now().year,
		}
	)

def contact(request):
	"""Renders the contact page."""
	assert isinstance(request, HttpRequest)
	return render(
		request,
		'app/home/contact.html',
		{
			'title':'Contact',
			'message':'Contact page',
			'year':datetime.now().year,
		}
	)

def about(request):
	"""Renders the about page."""
	assert isinstance(request, HttpRequest)
	return render(
		request,
		'app/home/about.html',
		{
			'title':'About',
			'message':'Project description',
			'year':datetime.now().year,
		}
	)

def register(request, template_name, authentication_form, extra_context):
	"""Renders the register page."""
	assert isinstance(request, HttpRequest)
	return render(
		request,
		'app/home/register.html',
		{
			'title':'Register',
			'message':'User registration',
			'year':datetime.now().year,
		}
	)

def show_news(request):
    news = News.objects.all()
    return render(request, 'app/news/news.html', {'news': news})

def show_users(request):
    users = User.objects.all()
    return render(request, 'app/users.html', {'users': users})

def show_comments(request):
    comments = Comment.objects.all()
    return render(request, 'app/comments.html', {'comments': comments})

def details(request, pk):
	new = News.objects.get(id=pk)
	return render(request, 'app/news/details.html', {'new': new})

def add(request):

	if request.method == 'POST':
		form = EntryForms(request.POST)

		if form.is_valid():
			######
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
			
			return HttpResponeRedirect('/news')
	else:
		form = EntryForms()	

	return render(request, 'app/news/form.html', {'form': form})

def delete(request, pk):

	if request.method == 'DELETE':
		new = get_object_or_404(News, pk=pk)
		new.delete()

	return HttpResponseRedirect('/news')