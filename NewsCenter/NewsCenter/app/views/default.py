"""
	Definition of home views.
"""

from django.shortcuts import render,render_to_response,get_object_or_404
from app import forms
from django.http import HttpRequest,Http404,HttpResponseRedirect
from django.template import RequestContext
from django.utils.safestring import mark_safe
from django.utils.html import conditional_escape

from app.calendar_pattern import *

from datetime import datetime, date
from calendar import HTMLCalendar
from ..models import *
from ..forms import EntryForms

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

