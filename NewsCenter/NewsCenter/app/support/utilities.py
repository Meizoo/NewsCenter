from ..models    import *

from django.utils.translation import ugettext_lazy as _
from django.utils.translation import activate

def is_none_or_empty(array):
	return array is None or len(array) == 0

def declaration_to_str(bool):
	return _('Wezmę udział') if bool else _('Nie wezmę udziału')

def interest_to_str(bool):
	return _('Zainteresowany') if bool else _('Niezainteresowany')

def find_user(request):
	return User.objects.get(id=request.user.id)

def find_profile(request):
	try:
		return UserProfile.objects.get(user=request.user)
	except:
		return None

def is_admin(request):
	if find_profile(request) is None:
		return False
	return is_mod(request)

def is_mod(request):
	user = UserProfile.objects.get(user=request.user)
	return user.role == 'moderator' or user.role == 'administrator'

def find_news(pk):
	return News.objects.get(id=pk)

def find_comments(pk):
	return Comment.objects.filter(id__in=CommentNews.objects.filter(id_news=pk).values_list('id_comment', flat=True))

def find_news(pk):
	return News.objects.get(id=pk)

def find_declarations(user, news):
	return Declaration.objects.filter(id_user=user).filter(id_news=news)

def find_interested(user, news):
	return Interested.objects.filter(id_user=user).filter(id_news=news)

def toggle_item(item, user, news, collection):
	if is_none_or_empty(item):
		collection.create(
			id_user = user,
			id_news = news
		).save()
		return True
	item.delete()
	return False	

def is_logged(request):
	return 'yes' if request.user.is_authenticated else 'no'
