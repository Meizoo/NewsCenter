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
from ..forms import EntryForms,SignupForm, EditProfileForm
from ..token_generator import account_activation_token


from app import support
from app.support import render_structs, utilities
from app.support.render_structs import *
from app.support.utilities import *

from django.utils.translation import ugettext_lazy as _
from django.utils.translation import activate

def signup(request):
	if request.method == 'POST':
		form = SignupForm(request.POST)
		if form.is_valid():
			human = True
			user = form.save(commit=False)
			user.is_active = False
			user.save()
			current_site = get_current_site(request)
			mail_subject = 'NewsCenter: Weryfikacja adresu e-mail'
			message = render_to_string('app/user/acc_active_email.html', {
				'user'   : user,
				'domain' : current_site.domain,
				'uid'	 : urlsafe_base64_encode(force_bytes(user.pk)).decode(),
				'token'  : account_activation_token.make_token(user),
			})
			to_email = form.cleaned_data.get('email')
			EmailMessage(mail_subject, message, to=[to_email]).send()
			message2 = 'Potwierdź swój adres e-mail w celu weryfikacji konta.'
			return render(request, 'app/user/signup_done.html', {'user': user, 'message': message2})
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
		UserProfile.objects.create(user=user, role='użytkownik')
		login(request, user)
		message = 'Dziękujemy za potwierdzenie adresu skrzynki odbiorczej. Twoje konto zostało aktywowane.'
	else:
		message = 'Nieprawidłowy URL aktywacyjny!'
	return render(request, 'app/user/signup_confirm.html', {'user': user, 'message': message})

def index(request):
	"""Renders the users"""
	return render(request, 'app/user/index.html', {
		'profiles' : UserProfile.objects.all()
	})

def details(request):
	id_user = UserProfile.objects.get(id=request.user.id)
	is_input = False
	submitbutton= request.POST.get('submit')
	if submitbutton:
		is_input = True
	return render(request, 'app/user/user_details.html',{'user': id_user, 'is_input': is_input, 'submitbutton': submitbutton})

def edit(request):
	"""Edits article of given id"""
	if not is_mod(request):
		return Http404()

	user = find_profile(request)
	return render(request,'app/user/edit.html', {'news': user})

def update(request, id):
	"""Updates article of given id"""
	if not is_mod(request):
		return Http404()

	user = find_profile(request)

	if request.method == 'POST':
		user.user.username = request.POST['username'];
		user.user.name = request.POST['name'];
		user.user.surname = request.POST['surname'];
		user.user.age = request.POST['age'];
		user.user.email = request.POST['email'];
		user.user.save()
		return HttpResponseRedirect('/news')
	return HttpResponseRedirect('/edit')
