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
		'app/index.html',
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
		'app/contact.html',
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
		'app/about.html',
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
		'app/register.html',
		{
			'title':'Register',
			'message':'User registration',
			'year':datetime.now().year,
		}
	)

def show_news(request):
    news = News.objects.all()
    return render(request, 'app/news.html', {'news': news})

def show_users(request):
    users = User.objects.all()
    return render(request, 'app/users.html', {'users': users})

def show_comments(request):
    comments = Comment.objects.all()
    return render(request, 'app/comments.html', {'comments': comments})

def details(request, pk):
	new = News.objects.get(id=pk)
	return render(request, 'app/details.html', {'new': new})

def add(request):

	if request.method == 'POST':
		form = EntryForms(request.POST)
		if form.is_valid():
			######
			name = form.cleaned_data['title']
			date = form.cleaned_data['title']
			description = form.cleaned_data['title']
			address = form.cleaned_data['title']
			
			News.objects.create(title = title, 
				date = falase, 
				description = description	).save()			
			
			return HttpResponeRedirect('/')
	else:
		form = EntryForms()

	return render(request, 'app/form.html', {'form': form})