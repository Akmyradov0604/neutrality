from django.shortcuts import render
from news.models import News
from django.core.mail import send_mail, EmailMessage
from django.conf import settings

def home(request):
	news = News.objects.all().order_by('-id')[:5]
	return render(request, 'accounts/home.html', {'news': news})

def programme(request):
	return render(request, 'accounts/about.html')

def register(request):
	return render(request, 'accounts/register.html')


def contact(request):
	if request.method == 'POST':
		message = request.POST.get('message', False)
		mail_id = request.POST.get('email', False)
		email = EmailMessage('Neutrality Contact Form', message, settings.EMAIL_HOST_USER, [mail_id])
		email.content_type = 'html'

		file  = request.FILES['attached']
		email.attach(file.name, file.read(), file.content_type)

		email.send()
	
	return render(request, 'accounts/contact.html')


