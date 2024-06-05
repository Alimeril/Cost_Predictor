from django.urls import path
from . import views

app_name = 'carpredictor'
urlpatterns = [
    path('', views.home, name = 'home'),
    path('CarList/', views.CarList.as_view(), name='CarList'),
]