import logging
import os
import shutil

from django.conf import settings

# Preview Image
from django.contrib.admin.decorators import display
from django.db import models
from django.template.loader import get_template
from django.utils import timezone
from django.utils.translation import gettext_lazy as _

# Django
from slugify import slugify

# Models
from personal_training.utils.models import TrainingModel


class Course(TrainingModel):
    """Course model."""

    class CourseType(models.TextChoices):
        TRAINING = "TRAINING", _("Entrenamiento")
        CHALLENGE = "CHALLENGE", _("Reto")
        NUTRITION = "NUTRITION", _("Nutrición")

    course_type = models.CharField(max_length=255, choices=CourseType.choices, default=CourseType.TRAINING)
    is_active = models.BooleanField(default=True)

    name = models.CharField("Nombre del curso", max_length=255)
    slug_name = models.SlugField(unique=True, max_length=255)

    image = models.ImageField(upload_to="courses/images/", null=True, blank=True)
    url_image = models.URLField("Url Field", max_length=500, null=True, blank=True)
    duration = models.DurationField(_("Duración"), null=True, blank=True)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    old_price = models.DecimalField(max_digits=10, decimal_places=2, default=0)

    tags = models.ManyToManyField("negocio.Tags", limit_choices_to={"is_course": True}, related_name="courses", blank=True)

    @property
    def discount(self):
        percent = None
        if self.old_price:
            percent = 100 - (self.price * 100) / self.old_price
        return percent

    @property
    def is_sale(self):
        return self.old_price > 0 and self.old_price > self.price

    @property
    def is_new(self):
        return self.created >= timezone.now() - timezone.timedelta(days=7)

    def __str__(self):
        return f"Course: {self.name}"

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        try:
            self.old_file_path = os.path.join(settings.MEDIA_ROOT, self.image.name)
        except Exception as error:  # pylint: disable=broad-except
            logging.error(error)

    @display(description=_("Preview Image"))
    def my_image_thumbnail(self):
        return get_template("files/my_source_thumbnail_template.html").render(
            {
                "image": True,
                "video": False,
                "audio": False,
                "field_name": "image",
                "model_name": "course",
                "field_description": "description",
                "src": self.image.url if self.image else None,
            }
        )

    def save(self, *args, **kwargs):
        self.slug_name = slugify(self.name)
        try:
            file_path = os.path.join(settings.MEDIA_ROOT, self.image.name)
            if hasattr(self, "old_file_path") and self.old_file_path != file_path:
                # Al cambiar el nombre del archivo, borra el archivo del sistema de archivos
                if os.path.exists(self.old_file_path):
                    shutil.move(self.old_file_path, file_path)
        except Exception as error:  # pylint: disable=broad-except
            logging.error(error)
        super().save(*args, **kwargs)

    def delete(self, *args, **kwargs):
        super().delete(*args, **kwargs)
        # Al eliminar el modelo Archivo, borra el archivo del sistema de archivos
        self.image.delete()


class Class(TrainingModel):
    """Content course model."""

    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name="classes")

    number = models.PositiveIntegerField(default=1)
    name = models.CharField(max_length=255)
    slug_name = models.SlugField(unique=True, max_length=255)

    video = models.FileField(upload_to="classes/videos/", null=True, blank=True)
    source_url = models.URLField("Url Field", max_length=500, null=True, blank=True)
    duration = models.DurationField(_("Duración"), null=True, blank=True)
    description = models.TextField()

    class Meta:
        unique_together = ("course", "number")
        ordering = ["course", "number"]

    def __str__(self):
        return f"Class Number {self.number}: {self.name}"

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        try:
            self.old_file_path = os.path.join(settings.MEDIA_ROOT, self.video.name)
        except Exception as error:  # pylint: disable=broad-except
            logging.error(error)

    @display(description=_("Preview Video Url"))
    def my_video_url_thumbnail(self):
        return get_template("files/my_source_thumbnail_template.html").render(
            {
                "image": False,
                "video": True,
                "audio": False,
                "field_name": "source_url",
                "model_name": "class",
                "field_description": "description",
                "src": self.source_url if self.source_url else None,
            }
        )

    @display(description=_("Preview Video"))
    def my_video_thumbnail(self):
        return get_template("files/my_source_thumbnail_template.html").render(
            {
                "image": False,
                "video": True,
                "audio": False,
                "field_name": "video",
                "model_name": "class",
                "field_description": "description",
                "src": self.video.url if self.video else None,
            }
        )

    def save(self, *args, **kwargs):
        try:
            file_path = os.path.join(settings.MEDIA_ROOT, self.video.name)
            super().save(*args, **kwargs)
            if hasattr(self, "old_file_path") and self.old_file_path != file_path:
                # Al cambiar el nombre del archivo, borra el archivo del sistema de archivos
                if os.path.exists(self.old_file_path):
                    shutil.move(self.old_file_path, file_path)
        except Exception as error:  # pylint: disable=broad-except
            logging.error(error)
            super().save(*args, **kwargs)

    def delete(self, *args, **kwargs):
        super().delete(*args, **kwargs)
        # Al eliminar el modelo Archivo, borra el archivo del sistema de archivos
        self.video.delete()


class AttachFile(TrainingModel):
    """Content course model."""

    cource_class = models.ForeignKey(Class, on_delete=models.CASCADE, related_name="contents")

    name = models.CharField(max_length=255)
    slug_name = models.SlugField(unique=True, max_length=255)

    file = models.FileField(upload_to="contents/files/", null=True, blank=True)
    source_url = models.URLField("Url Field", max_length=500, null=True, blank=True)
    description = models.TextField()
