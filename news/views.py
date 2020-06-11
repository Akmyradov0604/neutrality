from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator
from .models import News

def news(request):
	news = News.objects.all()
	paginator = Paginator(news, 9)
	page = request.GET.get('page')
	news = paginator.get_page(page)

	return render(request, 'news/news.html', {'news': news})

def detail(request, news_id):
	newsdet = get_object_or_404(News, pk=news_id)
	return render(request, 'news/detail.html', {'news': newsdet})
