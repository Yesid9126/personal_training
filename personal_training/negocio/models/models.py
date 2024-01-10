# Django
from django.db import models

# Utils
# Models
from personal_training.utils.models import Days, TrainingModel


class Schedule(TrainingModel):
    day = models.CharField(max_length=9, choices=Days.choices, default=Days.LUNES)

    class Meta:
        verbose_name = "Horario"
        verbose_name_plural = "Horarios"

    def __str__(self):
        return "Horario"


class TimeSchedule(TrainingModel):
    schedule = models.ForeignKey(Schedule, on_delete=models.CASCADE, related_name="times")
    hour_init = models.TimeField()
    hour_end = models.TimeField()

    class Meta:
        verbose_name = "Horario"
        verbose_name_plural = "Horarios"

    def __str__(self):
        return "Horario"


class FollowUs(TrainingModel):
    facebook = models.CharField(max_length=255, null=True, blank=True)
    twitter = models.CharField(max_length=255, null=True, blank=True)
    instagram = models.CharField(max_length=255, null=True, blank=True)
    linkedin = models.CharField(max_length=255, null=True, blank=True)

    class Meta:
        verbose_name = "Socials"
        verbose_name_plural = "Socials"

    def __str__(self):
        return "Socials"


class Tags(TrainingModel):
    name = models.CharField(max_length=255)
    is_product = models.BooleanField(default=False)
    is_service = models.BooleanField(default=False)

    class Meta:
        verbose_name = "Filtro"
        verbose_name_plural = "Filtros"

    def __str__(self):
        return self.name
