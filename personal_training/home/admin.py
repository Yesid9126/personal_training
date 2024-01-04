# Dajngo
from django.contrib import admin

# Models
from personal_training.home.models.models import Carousel1, Carousel2, Carousel4, Home, Point3


@admin.register(Home)
class IdentifierAdmin(admin.ModelAdmin):
    list_display = ["pk", "identifier"]
    readonly_fields = ["my_image_thumbnail"]

    def delete_queryset(self, request, queryset):
        for obj in queryset:
            obj.image3.delete()
        return super().delete_queryset(request, queryset)


@admin.register(Carousel1)
class Carousel1Admin(admin.ModelAdmin):
    list_display = ["pk", "title", "description", "image"]
    readonly_fields = ["my_image_thumbnail"]

    def delete_queryset(self, request, queryset):
        for obj in queryset:
            obj.image.delete()
        return super().delete_queryset(request, queryset)


@admin.register(Carousel2)
class Carousel2Admin(admin.ModelAdmin):
    list_display = ["pk", "title", "description", "image"]
    readonly_fields = ["my_image_thumbnail"]

    def delete_queryset(self, request, queryset):
        for obj in queryset:
            obj.image.delete()
        return super().delete_queryset(request, queryset)


@admin.register(Point3)
class Section3PointAdmin(admin.ModelAdmin):
    list_display = ["pk", "title", "description", "position"]


@admin.register(Carousel4)
class Carousel4Admin(admin.ModelAdmin):
    list_display = ["pk", "title", "description", "image"]
    readonly_fields = ["my_image_thumbnail"]

    def delete_queryset(self, request, queryset):
        for obj in queryset:
            obj.image.delete()
        return super().delete_queryset(request, queryset)
