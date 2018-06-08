"""
Definition of forms.
"""

from django import forms
from django.contrib.auth.forms import AuthenticationForm,UserCreationForm
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.models import User

class SignupForm(UserCreationForm):
	email = forms.EmailField(max_length=200, help_text='Required')
	class Meta:
		model = User
		fields = ('username', 'email', 'password1', 'password2')

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
	title	   = forms.CharField(max_length=32)
	date		= forms.DateTimeField()
	description = forms.CharField(widget = forms.Textarea)
	address	 = forms.CharField(max_length = 32)

class CommentForms(forms.Form):
	comment = forms.CharField(max_length=128)
