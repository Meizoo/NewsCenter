"""
Definition of views.
"""
from django.shortcuts import render,render_to_response
from django.http import HttpRequest
from django.template import RequestContext
from django.utils.safestring import mark_safe
from django.utils.html import conditional_escape
from app.calendar_pattern import *
from datetime import datetime, date
from calendar import HTMLCalendar

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
def calendar(request, year, month):
  my_workouts = Workouts.objects.order_by('my_date').filter(
    my_date__year=year, my_date__month=month
  )
  cal = calendar_pattern(my_workouts).formatmonth(year, month)
  return render_to_response('layout.html', {'calendar': mark_safe(cal),})

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
