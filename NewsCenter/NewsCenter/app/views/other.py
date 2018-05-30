"""
	Definition of views.
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

from ..listviews import ArticleListView

# Other
def users(request):
	"""Renders the users"""
	return render(request, 'app/users/index.html', {'users': User.objects.all()})

def comments(request):
	"""Renders all of the comments"""
	return render(request, 'app/comments.html', {'comments': Comment.objects.all()})
