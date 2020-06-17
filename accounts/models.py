from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager

class MyAccountManager(BaseUserManager):
	def create_user(self,first_name, last_name, state, country, title, organization, position, position_delegation, gender, date_of_birth, place_of_birth, passport_number, passport_image, photo, mobile_phone, email, privacy):
		if not last_name:
			raise ValueError("Please fill out your Last Name")
		if not first_name:
			raise ValueError("Please fill out your First Name")
		if not state:
			raise ValueError("Please select your state")
		if not country:
			raise ValueError("Please select your country")
		if not title:
			raise ValueError("Please fill out your Title")
		if not organization:
			raise ValueError("Please select your Organization")
		if not position:
			raise ValueError("Please fill out your Position")
		if not position_delegation:
			raise ValueError("Please select your position in delegation ")
		if not gender:
			raise ValueError("Please select your gender")
		if not date_of_birth:
			raise ValueError("Please fill out your Date of Birth")
		if not place_of_birth:
			raise ValueError("Please fill out your Place of Birth")
		if not passport_number:
			raise ValueError("Please fill out your Passport Number")
		if not passport_image:
			raise ValueError("Please upload your Passport Image")
		if not photo:
			raise ValueError("Please upload your photo")
		if not mobile_phone:
			raise ValueError("Please fill out your mobile number")
		if not email:
			raise ValueError("Please fill out your email Address")
		if not privacy:
			raise ValueError("Please agree to privacy data")

		user = self.model(
				email=self.normalize_email(email),
				first_name=first_name,
				last_name=last_name,
				state=state,
				country= country,
				title=title,
				organization=organization,
				position=position,
				position_delegation=position_delegation,
				gender=gender,
				date_of_birth=date_of_birth,
				place_of_birth=place_of_birth,
				passport_number=passport_number,
				passport_image=passport_image,
				photo=photo,
				mobile_phone=mobile_phone,
				privacy=privacy
			)
		user.save(using=self._db)
		return user

	def create_superuser(self, email, username, password):
		user = self.create_user(
			email=self.normalize_email(email),
			password=password,
			username=username,
		)
		user.is_admin = True
		user.is_staff = True
		user.is_superuser = True
		user.save(using=self._db)
		return user

class Account(AbstractBaseUser):
	STATE = (
		('Government institution', 'Government institution'),
		('Intergovernmental Organization', 'Intergovernmental Organization'),
		('NGO', 'NGO'),
		('Company', 'Company'),
		('Press', 'Press'),
		('Other', 'Other'),
	)
	COUNTRIES = (
		('Afghanistan', 'Afghanistan'),
		('Turkmenistan', 'Turkmenistan'),
		('Turkey', 'Turkey'),
		('USA', 'USA'),
		('UK', 'UK'),
		)
	POSITION = (
		('Head of delegation', ' Head of delegation'),
		('Deputy', 'Deputy'),
		('Protocol officer', 'Protocol officer'),
		('Security', 'Security'),
		('Press', 'Press'),
		('Other', 'Other'),
		)
	GENDER = (
		('Male', 'Male'),
		('Female', 'Female')
		)
	CITIZENSHIP = (
		('Afghanistan', 'Afghanistan'),
		('Turkmenistan', 'Turkmenistan'),
		('Turkey', 'Turkey'),
		('USA', 'USA'),
		('UK', 'UK'),
		)
	title = models.CharField(max_length=100)
	state = models.CharField(max_length=100, default='Government institution', choices=STATE)
	country = models.CharField(max_length=100, default='Select your country', choices=COUNTRIES)
	last_name = models.CharField(max_length=100)
	first_name = models.CharField(max_length=100)
	organization = models.CharField(max_length=100)
	position = models.CharField(max_length=100)
	position_delegation = models.CharField(max_length=100, default='Select your position', choices=POSITION)
	citizenship = models.CharField(max_length=100, default='Select your citizenship', choices=CITIZENSHIP)
	gender = models.CharField(max_length=30, default='Select your gender', choices=GENDER)
	date_of_birth = models.DateField(auto_now=False)
	place_of_birth = models.CharField(max_length=100)
	passport_image = models.ImageField(upload_to='images/')
	photo = models.ImageField(upload_to='images/')
	passport_number = models.CharField(max_length=100)
	expiry_date = models.DateField(auto_now=False, null=True)
	office_phone = models.CharField(max_length=100,  null=True)
	mobile_phone = models.CharField(max_length=100)
	email = models.EmailField(verbose_name="email", max_length=60, unique=True)
	email2 = models.EmailField(verbose_name="email", max_length=60, unique=True, null=True)
	address =  models.CharField(max_length=100, null=True)
	means_of_transport = models.CharField(max_length=100, null=True)
	arr_date = models.DateField(auto_now=False, null=True)
	arr_flight_number = models.CharField(max_length=100, null=True)
	dep_date = models.DateField(auto_now=False, null=True)
	dep_flight_number = models.CharField(max_length=100, null=True )
	nda_required = models.BooleanField(default=False, null=True)
	privacy = models.BooleanField(default=False)


	date_joined = models.DateTimeField(verbose_name='date joined', auto_now_add=True)
	last_login = models.DateTimeField(verbose_name='last login', auto_now=True)
	is_admin = models.BooleanField(default=False)
	is_active = models.BooleanField(default=True)
	is_staff = models.BooleanField(default=False)
	is_superuser = models.BooleanField(default=False)

	USERNAME_FIELD = 'first_name'

	REQUIRED_FIELDS = ['first_name','last_name', 'state', 'country', 'title', 'organization', 'position', 'position_delegation', 'gender', 'date_of_birth', 'place_of_birth', 'passport_number', 'passport_image', 'photo', 'mobile_phone', 'email', 'privacy']

	objects = MyAccountManager()

	def __str__(self):
		return self.first_name

	def has_perm(self, perm, obj=None):
		return self.is_admin

	def has_module_perms(self, app_label):
		return True


