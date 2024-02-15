from django.db import models

# Models
from personal_training.utils.models import TrainingModel


class Checkout(TrainingModel):
    user = models.ForeignKey("users.User", on_delete=models.CASCADE, related_name="checkouts")
    courses = models.ManyToManyField("courses.Course", related_name="checkouts_courses")


class Cart(TrainingModel):
    user = models.OneToOneField("users.User", on_delete=models.CASCADE, related_name="cart")
    courses = models.ManyToManyField("courses.Course", related_name="carts_courses")
