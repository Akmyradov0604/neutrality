from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('programme/', views.programme, name='about'),
    path('registration/', views.register, name='register'),
    path('contact_us/', views.contact, name='contact'),
]
