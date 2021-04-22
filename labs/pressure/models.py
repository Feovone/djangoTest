from django.db import models
from django.urls import reverse
# Create your models here.

class AtmospherePressure(models.Model):
    sensor_location = models.CharField("Местонахождения датчика", max_length=150)
    date = models.DateField("Дата замера")
    time = models.TimeField("Время замера")
    temperature = models.SmallIntegerField("Температура")
    sensor_name = models.CharField("Название датчика", max_length=150)
    sensor_model = models.CharField("Модель датчика", max_length=150)
    url = models.SlugField(max_length=160, unique=True, null=False)


    def get_absolute_url(self):
        return reverse("atmosphere_pressure_detail", kwargs={"slug": self.url})

    def __str__(self):
        return self.sensor_name


class PdfMaker(models.Model):
    name = models.CharField("Имя", max_length=150)
    time = models.TimeField("Время публикации")
    type = models.CharField("Тип оповещения", max_length=150)
    email = models.EmailField("Почта")
    url = models.SlugField(max_length=160, unique=True, null=False)

    def get_absolute_url(self):
        return reverse("pdf_detail", kwargs={"slug": self.url})

    def __str__(self):
        return self.name
