from ..models    import *

def is_none_or_empty(array):
	return array is None or len(array) == 0

def declaration_to_str(bool):
	return 'Declare' if bool else 'Undeclare'

def interest_to_str(bool):
	return 'Interesting' if bool else 'Not interesting'

def find_user(request):
	return User.objects.get(id=request.user.id)

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
