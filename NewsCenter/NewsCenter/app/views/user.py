"""
	Definition of user views
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

def index(request):
	"""Renders the users"""
	return render(request, 'app/user/index.html', {'users': User.objects.all()})

def register(request, template_name, authentication_form, extra_context):
	"""Renders the register page."""
	assert isinstance(request, HttpRequest)
	return render(
		request,
		'app/user/register.html',
		{
			'title':'Register',
			'message':'User registration',
			'year':datetime.now().year,
		}
	)

