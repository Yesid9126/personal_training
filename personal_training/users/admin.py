from django.contrib import admin, auth
from django.contrib.auth import admin as auth_admin
from django.contrib.sites.models import Site
from django.utils.translation import gettext_lazy as _
from django_celery_beat.models import ClockedSchedule, CrontabSchedule, IntervalSchedule, PeriodicTask, SolarSchedule

# Forms
from personal_training.users.forms import UserChangeForm

# Models
from personal_training.users.models import Checkout, Coupon, User

try:
    from rest_framework.authtoken.models import TokenProxy as DRFToken
except ImportError:
    from rest_framework.authtoken.models import Token as DRFToken


@admin.register(User)
class UserAdmin(auth_admin.UserAdmin):
    fieldsets = (
        (None, {"fields": ("phone_number", "password")}),
        (_("Personal info"), {"fields": ("first_name", "last_name", "email")}),
        (
            _("Permissions"),
            {
                "fields": (
                    "is_active",
                    "is_staff",
                    "is_superuser",
                    "groups",
                    "user_permissions",
                ),
            },
        ),
        (_("Important dates"), {"fields": ("last_login", "date_joined")}),
    )
    form = UserChangeForm
    list_display = ["username", "email", "is_superuser"]
    search_fields = ["name"]


@admin.register(Coupon)
class CouponAdmin(admin.ModelAdmin):
    list_display = ["code", "percent", "is_active"]
    list_filter = ["is_active"]
    search_fields = ["code"]


@admin.register(Checkout)
class CheckoutAdmin(admin.ModelAdmin):
    list_display = ["reference", "email", "is_paid", "created"]
    list_filter = ["is_paid"]

    def email(self, obj):
        return obj.historical_cart_json["user"]["email"]

    def has_delete_permission(self, request, obj=None):
        return False

    def has_change_permission(self, request, obj=None):
        return False


admin.site.unregister(auth.models.Group)
admin.site.unregister(DRFToken)
admin.site.unregister(Site)
admin.site.unregister(SolarSchedule)
admin.site.unregister(ClockedSchedule)
admin.site.unregister(PeriodicTask)
admin.site.unregister(IntervalSchedule)
admin.site.unregister(CrontabSchedule)
