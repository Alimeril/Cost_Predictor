from django.urls import path
from . import views

app_name = 'carpredictor'
url_patterns = [
    path('', views.home, name = 'home'),
]