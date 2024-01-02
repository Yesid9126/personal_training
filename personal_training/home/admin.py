# Dajngo
from django.contrib import admin

# Models
from personal_training.home.models.models import (
    CarouselFiS,
    CarouselFoS,
    CarouselSS,
    FifthSection,
    FourthSection,
    HeadCarousel,
    HomeSection,
    PointTS,
    SecondSection,
    ThirdSection,
)


@admin.register(HomeSection)
class HomeSectionAdmin(admin.ModelAdmin):
    list_display = ["name"]


@admin.register(HeadCarousel)
class HeadCarouselAdmin(admin.ModelAdmin):
    list_display = ["title", "description", "image"]


@admin.register(SecondSection)
class SecondSectionAdmin(admin.ModelAdmin):
    list_display = ["title"]


@admin.register(CarouselSS)
class CarouselSSAdmin(admin.ModelAdmin):
    list_display = ["title", "description", "image"]


@admin.register(ThirdSection)
class ThirdSectionAdmin(admin.ModelAdmin):
    list_display = ["title", "image"]


@admin.register(PointTS)
class PointTSAdmin(admin.ModelAdmin):
    list_display = ["title", "description", "position"]


@admin.register(FourthSection)
class FourthSectionAdmin(admin.ModelAdmin):
    list_display = ["title", "description"]


@admin.register(CarouselFoS)
class CarouselFoSAdmin(admin.ModelAdmin):
    list_display = ["title", "description", "image"]


@admin.register(FifthSection)
class FifthSectionAdmin(admin.ModelAdmin):
    list_display = ["title", "description"]


@admin.register(CarouselFiS)
class CarouselFiSAdmin(admin.ModelAdmin):
    list_display = ["title", "description", "image"]
