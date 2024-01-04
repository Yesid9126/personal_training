# Django
from django.db import models

# Models
from personal_training.utils.models import TrainingModel

# from django.utils.translation import gettext_lazy as _


class ContactUs(TrainingModel):
    title1 = models.CharField(max_length=255)
    description1 = models.TextField()
    title2 = models.CharField(max_length=255)
    title3 = models.CharField(max_length=255)
    description3 = models.TextField()

    class Meta:
        verbose_name = "Contacto"
        verbose_name_plural = "Contactos"

    def __str__(self):
        return "Contacto"


class Location(TrainingModel):
    address = models.CharField(max_length=255)
    latitude = models.CharField(max_length=255)
    longitude = models.CharField(max_length=255)

    class Meta:
        verbose_name = "Ubicacion"
        verbose_name_plural = "Ubicaciones"

    def __str__(self):
        return "Ubicacion"
