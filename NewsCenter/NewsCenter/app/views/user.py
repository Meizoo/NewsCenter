"""
	Definition of user views
"""

from django.shortcuts import render,render_to_response,get_object_or_404,redirect
from app import forms
from django.http import HttpRequest,Http404,HttpResponseRedirect,HttpResponse
from django.template import RequestContext
from django.template.loader import render_to_string
from django.utils.safestring import mark_safe
from django.utils.html import conditional_escape
from django.contrib.auth import login, authenticate
from django.contrib.auth.models import User as AuthUser
from django.contrib.sites.shortcuts import get_current_site
from django.utils.encoding import force_bytes, force_text
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.core.mail import EmailMessage

from app.calendar_pattern import *

from datetime import datetime, date
from calendar import HTMLCalendar
from ..models import *
from ..forms import EntryForms,SignupForm
from ..token_generator import account_activation_token

def signup(request):
	if request.method == 'POST':
		form = SignupForm(request.POST)
		if form.is_valid():
			user = form.save(commit=False)
			user.is_active = False
			user.save()
			current_site = get_current_site(request)
			mail_subject = 'Activate your blog account.'
			message = render_to_string('app/user/acc_active_email.html', {
				'user'   : user,
				'domain' : current_site.domain,
				'uid'	: urlsafe_base64_encode(force_bytes(user.pk)).decode(),
				'token'  : account_activation_token.make_token(user),
			})
			to_email = form.cleaned_data.get('email')
			EmailMessage(mail_subject, message, to=[to_email]).send()
			return HttpResponse('Please confirm your email address to complete the registration')
	else:
		form = SignupForm()
	return render(request, 'app/user/signup.html', {'title' : 'signup', 'form': form })

def activate(request, uidb64, token):
	try:
		uid = force_text(urlsafe_base64_decode(uidb64))
		user = AuthUser.objects.get(pk=uid)
	except(TypeError, ValueError, OverflowError, AuthUser.DoesNotExist):
		user = None
	if user is not None and account_activation_token.check_token(user, token):
		user.is_active = True
		user.save()
		login(request, user)
		return HttpResponse('Thank you for your email confirmation. Now you can login your account.')
	else:
		return HttpResponse('Activation link is invalid!')

def index(request):
	"""Renders the users"""
	return render(request, 'app/user/index.html', {'users': AuthUser.objects.all()})
