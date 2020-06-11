from django.shortcuts import render
from news.models import News

def home(request):
	news = News.objects.all().order_by('-id')[:5]
	return render(request, 'accounts/home.html', {'news': news})

def programme(request):
	return render(request, 'accounts/about.html')

def register(request):
	return render(request, 'accounts/register.html')


def contact(request):
	return render(request, 'accounts/contact.html')

