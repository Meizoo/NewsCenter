"""
Definition of forms.
"""

from django import forms
from django.contrib.auth.forms import AuthenticationForm,UserCreationForm, UserChangeForm
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.models import User
from django.forms.widgets import *
from captcha.fields import CaptchaField
from app import models

class SignupForm(UserCreationForm):
	email   = forms.EmailField(max_length=200, help_text='Required', 
							widget=forms.EmailInput({
								'class': 'form-control',
								'placeholder': 'Email'
								}))
	name	= forms.CharField(max_length=64, 
							widget=forms.TextInput({
								'class': 'form-control',
								'placeholder': 'Name'
								}))
	surname = forms.CharField(max_length=128, 
						    widget=forms.TextInput({
								'class': 'form-control',
								'placeholder': 'Surname'
								}))
	age		= forms.IntegerField(
							widget=forms.TextInput({
								'class': 'form-control',
								'placeholder': 'Age'
								}))
	captcha = CaptchaField()
	password1 = forms.CharField(widget=forms.PasswordInput({'class': 'form-control', 'placeholder': 'Password'}))
	password2 = forms.CharField(widget=forms.PasswordInput({'class': 'form-control', 'placeholder': 'Password confirmation'}))
	#state   = forms.IntegerField(choices=STATE)

	class Meta:
		model = User
		fields = ('username','name','surname','age')
		widgets = {
			'username': forms.TextInput({'class': 'form-control'}),
			#'password1': forms.PasswordInput({'class': 'form-control'}),
			#'password2': forms.PasswordInput({'class': 'form-control'})
			}

class EditProfileForm(UserChangeForm):

	class Meta:
		model = User
		fields = ('username',)

class BootstrapAuthenticationForm(AuthenticationForm):
	"""Authentication form which uses boostrap CSS."""
	username = forms.CharField(max_length=254,
							   widget=forms.TextInput({
									'class': 'form-control',
									'placeholder': 'User name'}))
	password = forms.CharField(label=_("Password"),
							   widget=forms.PasswordInput({
									'class': 'form-control',
									'placeholder':'Password'}))

class EntryForms(forms.Form):
	title	   = forms.CharField(max_length=32,widget=forms.TextInput({
									'class': 'form-control',
									'placeholder': 'Title'}))
	date= forms.DateTimeField(widget=forms.DateTimeInput({'class': 'form-control'}))
	description = forms.CharField(widget = forms.Textarea({'class': 'form-control',
									'placeholder': 'Description'}))
	address	 = forms.CharField(max_length = 32,widget=forms.TextInput({
									'class': 'form-control',
									'placeholder': 'Address'}))	

class CommentForms(forms.Form):
	comment = forms.CharField(max_length=128)
