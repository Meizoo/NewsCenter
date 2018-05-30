function deleteNews(news) {
	var $news = $(news)
	$(news).parent().remove()
	var id = $news.data('id')
	console.log(id)
}