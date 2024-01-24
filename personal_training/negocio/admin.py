# Dajngo
from django.contrib import admin

# Models
from personal_training.negocio.models.models import FollowUs, Schedule, Tags, TimeSchedule


class InlineTimeSchedule(admin.TabularInline):
    model = TimeSchedule
    extra = 1


@admin.register(Schedule)
class ScheduleAdmin(admin.ModelAdmin):
    list_display = ["pk", "day"]
    inlines = [InlineTimeSchedule]


@admin.register(FollowUs)
class FollowUsAdmin(admin.ModelAdmin):
    list_display = ["pk", "facebook", "twitter", "instagram", "linkedin"]


@admin.register(Tags)
class TagsAdmin(admin.ModelAdmin):
    list_display = ["pk", "name"]
    search_fields = ["name"]
    list_filter = [
        ("is_course", admin.BooleanFieldListFilter),
        ("is_product", admin.BooleanFieldListFilter),
    ]
