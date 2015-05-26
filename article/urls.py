from django.conf.urls import  url

urlpatterns = [
	url(r'^all/', 'article.views.articles'),
	url(r'^get/(?P<article_id>\d+)/$', 'article.views.article'),
	]