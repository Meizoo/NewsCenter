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

from django.utils.translation import ugettext_lazy as _
from django.utils.translation import activate

from app import support
from app.support import render_structs, utilities
from app.support.render_structs import *
from app.support.utilities import *

def index(request):
	"""Renders the home page."""
	assert isinstance(request, HttpRequest)

	art = News.objects.filter(date__gt=date.today()).order_by("-date")

	if len(art) == 0:
		return render(
			request,
			'app/home/index.html',
			{
				'title': _('Brak nadchodzących wydarzeń'),
				'year':datetime.now().year,
				'auth': is_logged(request),
				'article' : None,
				'admin' : is_admin(request)
			}
		)
	return render(
		request,
		'app/home/index.html',
		{
			'title': _('Nadchodzące wydarzenie'),
			'year':datetime.now().year,
			'auth': is_logged(request),
			'article' : art[0],
			'admin' : is_admin(request)
		}
	)

def contact(request):
	"""Renders the contact page."""
	assert isinstance(request, HttpRequest)
	return render(
		request,
		'app/home/contact.html',
		{
			'title': _('Kontakt'),
			'year':datetime.now().year,
			'auth': is_logged(request),
			'admin' : is_admin(request)
		}
	)

def about(request):
	"""Renders the about page."""
	assert isinstance(request, HttpRequest)
	return render(
		request,
		'app/home/about.html',
		{
			'title': _('O nas'),
			'year':datetime.now().year,
			'auth': is_logged(request),
			'admin' : is_admin(request)
		}
	)
