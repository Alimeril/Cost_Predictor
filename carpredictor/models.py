from django.db import models
from datetime import date

# Create your models here.
class Car(models.Model):
    name = models.CharField("مدل ماشین", max_length = 100)
    year = models.CharField("سال تولید", max_length = 50)
    description = models.CharField("توضیحات", max_length = 200)
    km = models.CharField("کارکرد", max_length = 50)
    price = models.CharField("قیمت", max_length = 50)
    created = models.DateField("تاریخ", default=date.today(), blank=True)

    class Meta:
        ordering = ['created']

    def __str__(self):
        return f'{self.name}-{self.year}-{self.km}-{self.created}'