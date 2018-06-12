"""
	Definition of views.
"""

from django.shortcuts import render,render_to_response,get_object_or_404

from app import forms

from django.http import HttpRequest,Http404,HttpResponseRedirect
from django.template import RequestContext
from django.utils.safestring import mark_safe
from django.utils.html import conditional_escape
from django import forms
from captcha.fields import CaptchaField

from app.calendar_pattern import *

from datetime import datetime, date
from calendar import HTMLCalendar

from ..models import *
from ..forms import EntryForms
from ..listviews import ArticleListView

from django.utils.translation import ugettext_lazy as _
from django.utils.translation import activate

# Other
def comments(request):
	"""Renders all of the comments"""
	return render(request, 'app/comments.html', 
	{
		'title': _('Komentarze'),
		'year':datetime.now().year,
		'collection': Comment.objects.all()
	})

def organizers(request):
	"""Renders all of the organizers"""
	return render(request, 'app/organizers.html', 
	{
		'title' : _('Organizatorzy'),
		'collection' : Association.objects.all() 
	})