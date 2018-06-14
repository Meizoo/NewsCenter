from django.shortcuts import render, render_to_response, get_object_or_404, redirect

from app import models, forms

from django.contrib.auth.models import User

from django.utils.safestring import mark_safe
from django.utils.encoding import force_bytes, force_text
from django.utils.html       import conditional_escape
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.template         import RequestContext
from django.contrib          import messages
from django.http             import HttpRequest, Http404, HttpResponseRedirect,HttpResponse
from django.template import RequestContext
from django.template.loader import render_to_string
from django.contrib.sites.shortcuts import get_current_site
from django.core.mail import EmailMessage

from app.calendar_pattern import *

from datetime import datetime, date
from calendar import HTMLCalendar
from ..models import *
from ..forms import EntryForms,SignupForm, EditProfileForm
from ..token_generator import account_activation_token
from datetime import datetime, date
from calendar import HTMLCalendar

from app.calendar_pattern import *

from app import support
from app.support import render_structs, utilities
from app.support.render_structs import *
from app.support.utilities import *

from ..models    import *
from ..forms     import EntryForms, CommentForms
from ..listviews import ArticleListView

from django.utils.translation import ugettext_lazy as _
from django.utils.translation import activate

# News handlers
def index(request):
	"""Renders the articles"""
	assert isinstance(request, HttpRequest)
	if not request.user.is_authenticated:
		return render(request, 'app/news/index.html', 
		{
			'news': ArticleListView,
			'title': _('Wiadomości'),
			'year':datetime.now().year,
			'user' : find_profile(request)
		})
	return render(request, 'app/news/index.html', 
		{
			'news': ArticleListView,
			'title': _('Wiadomości'),
			'year':datetime.now().year,
			'user' : find_profile(request)
		})

def details(request, pk):
	"""Renders the article's details"""
	id_user = find_user(request)
	id_news = find_news(pk)

	if request.method == 'POST':
		form = CommentForms(request.POST)

		if form.is_valid():
			comment = Comment.objects.create(
				comment = form.cleaned_data['comment'], 
				id_user = id_user
			)
			CommentNews.objects.create(
				id_comment = comment,
				id_news = id_news
			).save()
			comment.save()
			#return HttpResponseRedirect('/news/id_news')
	else:
		form = EntryForms()	
	return render(request, 'app/news/details.html', {
		'new': id_news, 
		'comments' : find_comments(pk),
		'declaration' : declaration_to_str(not is_none_or_empty(find_declarations(id_user, id_news))),
		'interested' : interest_to_str(not is_none_or_empty(find_interested(id_user, id_news)))
	})

def declare(request, pk):
	"""Creates declaration model for given article for current user. """
	id_user = find_user(request)
	id_news = find_news(pk)

	bool = toggle_item(find_declarations(id_user, id_news), id_user, id_news, Declaration.objects)

	if declaration_to_str(bool) == 'Wezmę udział':
		current_site = get_current_site(request)
		mail_subject = 'Zadeklarowano udział w spotkaniu'
		message = render_to_string('app/user/declared_email.html', {
			'user'   : id_user,
			'domain' : current_site.domain,
			'news'   : id_news
		})
		to_email = id_user.email
		EmailMessage(mail_subject, message, to=[to_email]).send()
	return render(request, 'app/news/details.html', {
		'new': id_news, 
		'comments' : find_comments(pk),
		'declaration' : declaration_to_str(bool),
		'interested' : interest_to_str(not is_none_or_empty(find_interested(id_user, id_news)))
	})

def interest(request, pk):
	"""Creates interest model for given article for current user. """
	id_user = find_user(request)
	id_news = find_news(pk)

	bool = toggle_item(find_interested(id_user, id_news), id_user, id_news, Interested.objects)

	return render(request, 'app/news/details.html', {
		'new': id_news, 
		'comments' : find_comments(pk),
		'declaration' : declaration_to_str(not is_none_or_empty(find_declarations(id_user, id_news))),
		'interested' : interest_to_str(bool)
	})

def add(request):
	"""Adds article"""	
	if not is_mod(request):
		return Http404()

	if request.method == 'POST':
		form = EntryForms(request.POST)

		if form.is_valid():
			News.objects.create(
				title = form.cleaned_data['title'], 
				date = form.cleaned_data['date'], 
				description = form.cleaned_data['description'],
				address = form.cleaned_data['address']
			).save()			
			
			return HttpResponseRedirect('/news')
	else:
		form = EntryForms()	

	return render(request, 'app/news/create.html', {'form': form})

def delete(request, id):
	"""Deletes article of given id"""
	if not is_mod(request):
		return Http404()

	news = find_news(id)
	
	if request.method == 'POST':
		news.delete()
		return HttpResponseRedirect('/news')
	
	return render(request,'app/news/delete.html',{'news': news })

def edit(request, id):
	"""Edits article of given id"""
	if not is_mod(request):
		return Http404()

	news = find_news(id)
	return render(request,'app/news/edit.html', {'news': news})

def update(request, id):
	"""Updates article of given id"""
	if not is_mod(request):
		return Http404()

	news = find_news(id)

	if request.method == 'POST':
		news.title = request.POST['title'];
		news.date = request.POST['date'];
		news.description = request.POST['description'];
		news.address = request.POST['address'];
		news.save()
		return HttpResponseRedirect('/news')
	return HttpResponseRedirect('/edit')