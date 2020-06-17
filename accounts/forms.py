from django import forms
from django.contrib.auth.forms import UserCreationForm

from accounts.models import Account

class RegistrationForm(forms.ModelForm):
	
	class Meta:
		model = Account
		fields = ("email", "first_name", "first_name", "last_name", "state", "country", "title", "organization", "position", "position_delegation", "gender", "date_of_birth", "place_of_birth", "passport_number", "passport_image", "photo", "mobile_phone", "email", "privacy")