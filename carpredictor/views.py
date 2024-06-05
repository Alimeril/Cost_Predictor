from typing import Any
from django.db.models.query import QuerySet
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.template import loader
from django.views import generic
from django.urls import reverse
from .models import Car
from . import readcar

def home(request):
    return render(request, 'carpredictor/index.html')

class CarList(generic.ListView):
    template_name = 'carpredictor/carlist.html'
    context_object_name = 'car_list'
    paginate_by = 50

    def get_queryset(self):
        car_list = Car.objects.order_by('created')
        return car_list

def GetCarData(request):
    car_list = readcar.read_data()
    for car in car_list:
        q = Car(
            name = car.name,
            year = car.year,
            description = car.description,
            km = car.km,
            price = car.price,
        )
        q.save()
    template = loader.get_template("carpredictor/confirm.html")
    return HttpResponseRedirect(template.render(request))