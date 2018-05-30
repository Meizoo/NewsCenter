"""
Definition of urls for NewsCenter.
"""

from datetime import datetime
from django.conf.urls import url,include
from django.conf.urls import include
from django.contrib import admin
from django.urls import path
from app import views

import django.contrib.auth.views
import app.forms
import app.views

admin.autodiscover()

#newspatterns = [url()]

urlpatterns = [
	path(''                , app.views.home         , name='home'    ),
	path('contact'         , app.views.contact      , name='contact' ),
	path('about'           , app.views.about        , name='about'   ),
	path('news'            , app.views.articles     , name='news'    ),
	path('users'           , app.views.users        , name='users'   ),
	path('comments'        , app.views.comments     , name='comments'),
	path('details/<int:pk>', app.views.details      , name='details' ),
	path('add'             , app.views.add          , name='add'     ),
	path('delete/<int:id>' , app.views.delete       , name='delete'  ),
	path('update/<int:id>' , app.views.update       , name='update'  ),
	path('register/'       ,
		app.views.register ,
		{
			'template_name': 'app/home/register.html',
			'authentication_form': app.forms.BootstrapAuthenticationForm,
			'extra_context':
			{
				'title': 'Register',
				'year': datetime.now().year,
			}
		},
		name='register'),
	path('login',
		django.contrib.auth.views.login,
		{
			'template_name': 'app/home/login.html',
			'authentication_form': app.forms.BootstrapAuthenticationForm,
			'extra_context':
			{
				'title': 'Log in',
				'year': datetime.now().year,
			}
		},
		name='login'),
	path('logout',
		django.contrib.auth.views.logout,
		{
			'next_page': '/',
		},
		name='logout'),

	path('admin/doc/', include('django.contrib.admindocs.urls')),
	path('admin', admin.site.urls),]
