from django.contrib import admin
from .models import Car

# Register your models here.
class CarAdmin(admin.ModelAdmin):
  list_display = ("name", "year", "description","km","price","created")
  
admin.site.register(Car, CarAdmin)