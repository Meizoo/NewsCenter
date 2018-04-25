"""
This file demonstrates writing tests using the unittest module. These will pass
when you run "manage.py test".
"""

import django
django.setup()

from app import models
from django.test import TestCase

# TODO: Configure your database in settings.py and sync before running tests.

class ViewTest(TestCase):
	"""Tests for the application views."""

	def test_home(self):
		"""Tests the home page."""
		response = self.client.get('/')
		self.assertContains(response, 'Home Page', 1, 200)

	def test_contact(self):
		"""Tests the contact page."""
		response = self.client.get('/contact')
		self.assertContains(response, 'Contact', 4, 200)

	def test_about(self):
		"""Tests the about page."""
		response = self.client.get('/about')
		self.assertContains(response, 'About', 3, 200)

	def test_register(self):
		"""Tests the register page."""
		response = self.client.get('/register')
		self.assertContains(response, 'Register', 3, 200)

class UserTest(TestCase):
	"""Tests for User model."""
	def test_user_created(self):
		user = User.objects.create(
			name='TestUserName',
			surname='TestUserSurname',
			age=15,
			state=4
		)
		self.assertContains(user.age, 12, 3, 200)
