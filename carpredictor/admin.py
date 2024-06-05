from django.contrib import admin

# Register your models here.
class BookAdmin(admin.ModelAdmin):
  list_display = ("name", "year", "description","km","price","created")
  
admin.site.register(Car, CarAdmin)