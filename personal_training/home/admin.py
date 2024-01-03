# Dajngo
from django.contrib import admin

# Models
from personal_training.home.models.models import (
    Carousel1,
    Carousel2,
    Carousel4,
    Carousel5,
    Identifier,
    Section2,
    Section3,
    Section3Point,
    Section4,
    Section5,
)


@admin.register(Identifier)
class IdentifierAdmin(admin.ModelAdmin):
    list_display = ["pk", "name"]


@admin.register(Carousel1)
class Carousel1Admin(admin.ModelAdmin):
    list_display = ["pk", "title", "description", "image"]
    readonly_fields = ["my_image_thumbnail"]

    def delete_queryset(self, request, queryset):
        for obj in queryset:
            obj.image.delete()
        return super().delete_queryset(request, queryset)


@admin.register(Section2)
class Section2Admin(admin.ModelAdmin):
    list_display = ["pk", "title"]


@admin.register(Carousel2)
class Carousel2Admin(admin.ModelAdmin):
    list_display = ["pk", "title", "description", "image"]
    readonly_fields = ["my_image_thumbnail"]


@admin.register(Section3)
class Section3Admin(admin.ModelAdmin):
    list_display = ["pk", "title", "image"]
    readonly_fields = ["my_image_thumbnail"]


@admin.register(Section3Point)
class Section3PointAdmin(admin.ModelAdmin):
    list_display = ["pk", "title", "description", "position"]


@admin.register(Section4)
class Section4Admin(admin.ModelAdmin):
    list_display = ["pk", "title", "description"]


@admin.register(Carousel4)
class Carousel4Admin(admin.ModelAdmin):
    list_display = ["pk", "title", "description", "image"]
    readonly_fields = ["my_image_thumbnail"]


@admin.register(Section5)
class Section5Admin(admin.ModelAdmin):
    list_display = ["pk", "title", "description"]


@admin.register(Carousel5)
class Carousel5Admin(admin.ModelAdmin):
    list_display = ["pk", "title", "description", "image"]
    readonly_fields = ["my_image_thumbnail"]
