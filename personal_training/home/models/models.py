# Django
from django.db import models

# Models
from personal_training.utils.models import TrainingModel

# from django.utils.translation import gettext_lazy as _


class HomeSection(TrainingModel):
    name = models.CharField(max_length=255)

    class Meta:
        verbose_name = "Home Section"
        verbose_name_plural = "Home Sections"

    def __str__(self):
        return f"{self.name}"


class HeadCarousel(TrainingModel):
    homesection = models.ForeignKey(HomeSection, on_delete=models.CASCADE, related_name="headcarousels")
    title = models.CharField(max_length=255, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    image = models.ImageField(upload_to="home/head_carousel")  # 1470 x 870

    class Meta:
        verbose_name = "Head Carousel"
        verbose_name_plural = "Head Carousels"


class SecondSection(TrainingModel):
    homesection = models.OneToOneField(HomeSection, on_delete=models.CASCADE, related_name="secondsection")
    title = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        verbose_name = "Second Section"
        verbose_name_plural = "Second Sections"

    def __str__(self):
        return f"{self.title}"


class CarouselSS(TrainingModel):
    second_section = models.ForeignKey(SecondSection, on_delete=models.CASCADE, related_name="carousels")
    position = models.PositiveIntegerField()
    title = models.CharField(max_length=255, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    image = models.ImageField(upload_to="home/area_expertise")  # 550 x 400

    class Meta:
        verbose_name = "Carousel SS"
        verbose_name_plural = "Carousels SS"
        ordering = ["position"]


class ThirdSection(TrainingModel):
    homesection = models.OneToOneField(HomeSection, on_delete=models.CASCADE, related_name="thirdsection")
    title = models.CharField(max_length=255, blank=True, null=True)
    image = models.ImageField(upload_to="home/why_choose_us")  # 610 x 630

    class Meta:
        verbose_name = "Third Section"
        verbose_name_plural = "Third Sections"

    def __str__(self):
        return f"{self.title}"


class PointTS(TrainingModel):
    third_section = models.ForeignKey(ThirdSection, on_delete=models.CASCADE, related_name="points")
    title = models.CharField(max_length=255)
    description = models.TextField()
    position = models.PositiveIntegerField()

    class Meta:
        verbose_name = "Point TS"
        verbose_name_plural = "Points TS"
        ordering = ["position"]


class FourthSection(TrainingModel):
    homesection = models.OneToOneField(HomeSection, on_delete=models.CASCADE, related_name="fourthsection")
    title = models.CharField(max_length=255, blank=True, null=True)
    description = models.TextField(blank=True, null=True)

    class Meta:
        verbose_name = "Fourth Section"
        verbose_name_plural = "Fourth Sections"

    def __str__(self):
        return f"{self.title}"


class CarouselFoS(TrainingModel):
    fourth_section = models.ForeignKey(FourthSection, on_delete=models.CASCADE, related_name="carousels")
    position = models.PositiveIntegerField()
    title = models.CharField(max_length=255, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    image = models.ImageField(upload_to="home/area_expertise")  # 810 x 450

    class Meta:
        verbose_name = "Carousel FoS"
        verbose_name_plural = "Carousels FoS"
        ordering = ["position"]


class FifthSection(TrainingModel):
    homesection = models.OneToOneField(HomeSection, on_delete=models.CASCADE, related_name="fifthsection")
    title = models.CharField(max_length=255, blank=True, null=True)
    description = models.TextField(blank=True, null=True)

    class Meta:
        verbose_name = "Fifth Section"
        verbose_name_plural = "Fifth Sections"

    def __str__(self):
        return f"{self.title}"


class CarouselFiS(TrainingModel):
    fifth_section = models.ForeignKey(FifthSection, on_delete=models.CASCADE, related_name="carousels")
    date = models.DateField()
    title = models.CharField(max_length=255, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    image = models.ImageField(upload_to="home/area_expertise")  # 550 x 400

    class Meta:
        verbose_name = "Carousel FiS"
        verbose_name_plural = "Carousels FiS"
