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

from app import support
from app.support import render_structs, utilities
from app.support.render_structs import *
from app.support.utilities import *


# Other
def comments(request):
	"""Renders all of the comments"""
	return render(request, 'app/comments.html', 
	{
		'title': _('Komentarze'),
		'auth': is_logged(request),
		'year':datetime.now().year,
		'admin' : is_admin(request),
		'collection': Comment.objects.all()
	})

def organizers(request):
	"""Renders all of the organizers"""
	return render(request, 'app/organizers.html', 
	{
		'title' : _('Organizatorzy'),
		'auth': is_logged(request),
		'year':datetime.now().year,
		'admin' : is_admin(request),
		'collection' : Association.objects.all() 
	})