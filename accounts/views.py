from django.shortcuts import render, redirect
from news.models import News
from django.template.defaultfilters import filesizeformat
from django.core.exceptions import ValidationError
from django.core.mail import send_mail, EmailMessage
from django.conf import settings
from accounts.models import Account
from django.contrib import auth

def home(request):
	news = News.objects.all().order_by('-id')[:5]
	return render(request, 'accounts/home.html', {'news': news})

def programme(request):
	return render(request, 'accounts/about.html')

def register(request):
	error = []
	if request.method == "POST":
		if request.POST.get('privacy') == 'on':
	  		privacy = True
		else:
	   		privacy = False
		passport_image = request.FILES['passport_image']
		photo = request.FILES['photo']
		passportsize = passport_image.size
		photosize = photo.size

		if passportsize > 5242880: 
			error.append('Passpor file must be below 5MB')
		if photosize > 5242880: 
			error.append('Photo must be below 5MB')
		if privacy == False:
		 	error.append('Please agree to privacy policy')

		if not error: 
			user = Account.objects.create_user(
				request.POST.get('first_name'),
				request.POST.get('last_name'),
				request.POST.get('state'),
				request.POST.get('country'),
				request.POST.get('title'),
				request.POST.get('organization'),
				request.POST.get('position'),
				request.POST.get('position_delegation'),
				request.POST.get('gender'),
				request.POST.get('date_of_birth'),
				request.POST.get('place_of_birth'),
				request.POST.get('passport_number'),
				request.FILES['passport_image'],
				request.FILES['photo'],
				request.POST.get('mobile_phone'),
				request.POST.get('email'),
				privacy
			)
			auth.login(request, user)
			return render(request, 'accounts/home.html', {'success': 'You have successfully registered!!!'})
		else:
			return render(request, 'accounts/register.html', {'error': error})
	else:
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


