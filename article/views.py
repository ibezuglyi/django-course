from django.shortcuts import render
from django.http import HttpResponse
from django.template.loader import get_template
from django.template  import Context
from django.shortcuts import render_to_response
from django.views.generic.base import TemplateView
from article.models import Article


def articles(request):
	return render_to_response('articles.html',{
		'articles':Article.objects.all()})

def article(request, article_id=1):
	return render_to_response('article.html', 
							{'article':Article.objects.get(id=article_id)})
