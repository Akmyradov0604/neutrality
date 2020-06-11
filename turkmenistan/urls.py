from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.turkmenistan, name='turkmen'),
    path('<slug:slug>', views.info, name='info'),
]
