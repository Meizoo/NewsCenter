"""
Definition of urls for NewsCenter.
"""

from datetime         import datetime
from django.conf.urls import url,include
from django.conf.urls import include
from django.contrib   import admin
from django.urls      import path

from app.views import default
from app.views import other
from app.views import article

import django.contrib.auth.views
import app.forms

admin.autodiscover()

#newspatterns = [url()]

urlpatterns = [

	path(''                , app.views.default.home         , name='home'    ),
	path('contact'         , app.views.default.contact      , name='contact' ),
	path('about'           , app.views.default.about        , name='about'   ),
	path('register/'       ,
		app.views.default.register ,
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

	path('users'           , app.views.other.users        , name='users'   ),
	path('comments'        , app.views.other.comments     , name='comments'),

	path('news'            , app.views.article.articles     , name='news'    ),
	path('details/<int:pk>', app.views.article.details      , name='details' ),
	path('add'             , app.views.article.add          , name='add'     ),
	path('delete/<int:pk>' , app.views.article.delete       , name='delete'  ),

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
