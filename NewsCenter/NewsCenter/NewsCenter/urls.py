"""
Definition of urls for NewsCenter.
"""

from datetime import datetime
from django.conf.urls import url,include
from django.conf.urls import include
from django.contrib import admin
import django.contrib.auth.views

import app.forms
import app.views

admin.autodiscover()

urlpatterns = [

    url(r'^$', app.views.home, name='home'),
    url(r'^contact$', app.views.contact, name='contact'),
    url(r'^about', app.views.about, name='about'),
    url(r'^news', app.views.show_news, name='news'),
    url(r'^register/$',
		app.views.register,
		{
			'template_name': 'app/register.html',
			'authentication_form': app.forms.BootstrapAuthenticationForm,
			'extra_context':
			{
				'title': 'Register',
				'year': datetime.now().year,
			}
		},
		name='register'),
    url(r'^login/$',
        django.contrib.auth.views.login,
        {
            'template_name': 'app/login.html',
            'authentication_form': app.forms.BootstrapAuthenticationForm,
            'extra_context':
            {
                'title': 'Log in',
                'year': datetime.now().year,
            }
        },
        name='login'),
    url(r'^logout$',
        django.contrib.auth.views.logout,
        {
            'next_page': '/',
        },
        name='logout'),

	 url('admin/doc/', include('django.contrib.admindocs.urls')),
     url(r'^admin/', admin.site.urls),
]
