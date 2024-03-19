# UUIDs
from uuid import uuid4

from django.db import models

# Models
from personal_training.utils.models import TrainingModel


class Coupon(TrainingModel):
    code = models.CharField(max_length=255)
    percent = models.IntegerField()
    is_active = models.BooleanField(default=False)

    def __str__(self):
        return self.code


class Checkout(TrainingModel):
    cart = models.ForeignKey("users.Cart", on_delete=models.SET_NULL, related_name="checkouts", null=True, blank=True)
    historical_cart_json = models.JSONField(null=True, blank=True)

    coupon = models.ForeignKey("users.Coupon", on_delete=models.SET_NULL, related_name="checkouts", null=True, blank=True)
    courses = models.ManyToManyField("courses.Course", related_name="checkouts_courses", null=True, blank=True)
    # products = models.ManyToManyField("products.Product", related_name="checkouts_products", null=True, blank=True)

    reference = models.UUIDField(default=uuid4, editable=False, unique=True)
    is_paid = models.BooleanField(default=False)


class Cart(TrainingModel):
    user = models.OneToOneField("users.User", on_delete=models.CASCADE, related_name="cart")
    coupon = models.ForeignKey("users.Coupon", on_delete=models.CASCADE, related_name="carts", null=True, blank=True)
    courses = models.ManyToManyField("courses.Course", related_name="carts_courses")
    # products = models.ManyToManyField("products.Product", related_name="carts_products")

    @property
    def total(self):
        return sum([course.price for course in self.courses.all()])

    @property
    def total_with_coupon(self):
        if not self.coupon:
            return self.total
        elif self.coupon.is_active:
            return self.total - ((self.total / 100) * self.coupon.percent)

    def __str__(self):
        return self.user.email
