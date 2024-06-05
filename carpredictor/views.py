from typing import Any
from django.db.models.query import QuerySet
from django.shortcuts import render
from django.views import generic
from .models import Car

def home(request):
    return render(request, 'carpredictor/index.html')

class CarList(generic.ListView):
    template_name = 'carpredictor/carlist.html'
    context_object_name = 'car_list'
    paginate_by = 100

    def get_queryset(self):
        car_list = Car.objects.order_by('created')
        return car_list