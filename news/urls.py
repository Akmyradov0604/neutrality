from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.news, name='news'),
    path('<int:news_id>/', views.detail, name='detail'),
]
