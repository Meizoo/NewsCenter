"""
	Definition of urls for NewsCenter.
"""

from datetime import datetime

from django.conf.urls import url,include
from django.conf.urls import include
from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.urls	import path

from app import views

from app.views import default, article, other, user

import django.contrib.auth.views
import app.forms

admin.autodiscover()

#newspatterns = [url()]

urlpatterns = [
	path(''         , app.views.default.index   , name='home'    ),
	path('contact'  , app.views.default.contact , name='contact' ),
	path('about'    , app.views.default.about   , name='about'   ),

	path('user'					, app.views.user.index		, name='user'   ),
	path('user/user_details'    , app.views.user.details    , name='details'),
	path('user/edit'			, app.views.user.edit		, name='edit'   ),
	path('user/update'			, app.views.user.update     , name='update' ),

	url(r'^signup/$', app.views.user.signup, name='signup'),
	url(r'^login/$', auth_views.LoginView.as_view(template_name='app/user/login.html'), name='login'),
	url(r'^activate/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
		app.views.user.activate, name='activate'),

    url(r'^reset/$',
        auth_views.PasswordResetView.as_view(
            template_name='app/user/pswd_reset/password_reset.html',
            email_template_name='app/user/pswd_reset/password_reset_email.html',
            subject_template_name='app/user/pswd_reset/password_reset_subject.txt'
        ),
        name='password_reset'),
    url(r'^reset/done/$',
        auth_views.PasswordResetDoneView.as_view(template_name='app/user/pswd_reset/password_reset_done.html'),
        name='password_reset_done'),
    url(r'^reset/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
        auth_views.PasswordResetConfirmView.as_view(template_name='app/user/pswd_reset/password_reset_confirm.html'),
        name='password_reset_confirm'),
    url(r'^reset/complete/$',
        auth_views.PasswordResetCompleteView.as_view(template_name='app/user/pswd_reset/password_reset_complete.html'),
        name='password_reset_complete'),
	url(r'^captcha/', include('captcha.urls')),
	path('logout',
		django.contrib.auth.views.logout,
		{
			'next_page': '/',
		},
		name='logout'),


	path('comments'        , app.views.other.comments   , name='comments'),
	path('organizers'      , app.views.other.organizers , name='organizers'),

	path('news'             , app.views.article.index   , name='news'    ),
	path('details/<int:pk>' , app.views.article.details , name='details' ),
	path('add'              , app.views.article.add     , name='add'     ),
	path('delete/<int:id>'  , app.views.article.delete  , name='delete'  ),
	path('update/<int:id>'  , app.views.article.update  , name='update'  ),
	path('edit/<int:id>'    , app.views.article.edit    , name='edit'    ),
	path('declare/<int:pk>' , app.views.article.declare , name='declare' ),
	path('interest/<int:pk>', app.views.article.interest, name='interest'),
	
	path('admin/doc/', include('django.contrib.admindocs.urls')),
	path('admin', admin.site.urls),
]
