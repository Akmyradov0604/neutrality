from django.shortcuts import render
from news.models import News
from .models import Turkmen


def turkmenistan(request):
	news = News.objects.all().order_by('-id')[:5]
	articles = Turkmen.objects.all()
	return render(request, 'turkmenistan/turkmen.html', {'news': news, 'articles': articles})

def info(request, slug):
	news = News.objects.all().order_by('-id')[:5]
	q = Turkmen.objects.filter(slug__iexact = slug)
	if q.exists(): 
		q = q.first() 
	else: 
		return HttpResponse('<h1>Post Not Found</h1>')
		
	return render(request, 'turkmenistan/article.html', { 'article': q, 'news': news })