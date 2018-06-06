"""
	Definition of urls for NewsCenter.
"""

from datetime import datetime

from django.conf.urls import url,include
from django.conf.urls import include
from django.contrib import admin
from django.urls	import path

from app import views

from app.views import default, article, other, user

import django.contrib.auth.views
import app.forms

admin.autodiscover()

#newspatterns = [url()]

urlpatterns = [
	path(''		 , app.views.default.index   , name='home'	),
	path('contact'  , app.views.default.contact , name='contact' ),
	path('about'	, app.views.default.about   , name='about'   ),

	path('user'	, app.views.user.index   , name='user'   ),
	path('register', app.views.user.register,
		{
			'template_name': 'app/user/register.html',
			'authentication_form': app.forms.BootstrapAuthenticationForm,
			'extra_context':
			{
				'title': 'Register',
				'year': datetime.now().year,
			}
		},
		name='register'),
	 url(r'^signup/$', app.views.user.signup, name='signup'),
	 url(r'^activate/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
		app.views.user.activate, name='activate'),

	path('login',
		django.contrib.auth.views.login,
		{
			'template_name': 'app/user/login.html',
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


	path('comments'		, app.views.other.comments , name='comments'),

	path('news'			, app.views.article.index	, name='news'	),
	path('details/<int:pk>', app.views.article.details  , name='details' ),
	path('add'			 , app.views.article.add	  , name='add'	 ),
	path('delete/<int:id>' , app.views.article.delete   , name='delete'  ),
	path('update/<int:id>' , app.views.article.update   , name='update'  ),
	path('edit/<int:id>'   , app.views.article.edit	 , name='edit'	),
	
	path('admin/doc/', include('django.contrib.admindocs.urls')),
	path('admin', admin.site.urls),
]
