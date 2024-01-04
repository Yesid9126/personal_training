import logging
import os
import shutil

from django.conf import settings

# Preview Image
from django.contrib.admin.decorators import display

# Django
from django.db import models
from django.template.loader import get_template
from django.utils.translation import gettext_lazy as _

# Models
from personal_training.utils.models import TrainingModel

# from django.utils.translation import gettext_lazy as _


class Home(TrainingModel):
    identifier = models.CharField(max_length=255)
    title1 = models.CharField(max_length=255)
    title2 = models.CharField(max_length=255)
    title3 = models.CharField(max_length=255)
    image3 = models.ImageField(upload_to="home/seccion3")
    title4 = models.CharField(max_length=255)
    description4 = models.TextField()
    titl5 = models.CharField(max_length=255)
    title6 = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.identifier if self.identifier else 'Sin identificador'}"

    class Meta:
        verbose_name = "Titulos"
        verbose_name_plural = "Titulos"

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        try:
            self.old_file_path = os.path.join(settings.MEDIA_ROOT, self.image3.name)
        except Exception as error:  # pylint: disable=broad-except
            logging.error(error)

    @display(description=_("Preview"))
    def my_image_thumbnail(self):
        return get_template("files/my_image_thumbnail_template.html").render(
            {
                "field_name": "image3",
                "model_name": "home",
                "field_description": "title3",
                "src": self.image3.url if self.image3 else None,
            }
        )

    def save(self, *args, **kwargs):
        try:
            file_path = os.path.join(settings.MEDIA_ROOT, self.image3.name)
            super().save(*args, **kwargs)
            if hasattr(self, "old_file_path") and self.old_file_path != file_path:
                # Al cambiar el nombre del archivo, borra el archivo del sistema de archivos
                if os.path.exists(self.old_file_path):
                    shutil.move(self.old_file_path, file_path)
        except Exception as error:  # pylint: disable=broad-except
            logging.error(error)

    def delete(self, *args, **kwargs):
        super().delete(*args, **kwargs)
        # Al eliminar el modelo Archivo, borra el archivo del sistema de archivos
        self.image3.delete()


class Carousel1(TrainingModel):
    home = models.ForeignKey(Home, on_delete=models.CASCADE, related_name="carousels1")
    title = models.CharField(max_length=255, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    image = models.ImageField(upload_to="home/carousel1")  # 1470 x 870

    class Meta:
        verbose_name = "Elemento carusel primera seccion"
        verbose_name_plural = "Elementos carusel primera seccion"

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        try:
            self.old_file_path = os.path.join(settings.MEDIA_ROOT, self.image.name)
        except Exception as error:  # pylint: disable=broad-except
            logging.error(error)

    def __str__(self):
        return f"{self.pk}"

    @display(description=_("Preview"))
    def my_image_thumbnail(self):
        return get_template("files/my_image_thumbnail_template.html").render(
            {
                "field_name": "image",
                "model_name": "carousel1",
                "field_description": "description",
                "src": self.image.url if self.image else None,
            }
        )

    def save(self, *args, **kwargs):
        try:
            file_path = os.path.join(settings.MEDIA_ROOT, self.image.name)
            super().save(*args, **kwargs)
            if hasattr(self, "old_file_path") and self.old_file_path != file_path:
                # Al cambiar el nombre del archivo, borra el archivo del sistema de archivos
                if os.path.exists(self.old_file_path):
                    shutil.move(self.old_file_path, file_path)
        except Exception as error:  # pylint: disable=broad-except
            logging.error(error)

    def delete(self, *args, **kwargs):
        super().delete(*args, **kwargs)
        # Al eliminar el modelo Archivo, borra el archivo del sistema de archivos
        self.image.delete()


class Carousel2(TrainingModel):
    home = models.ForeignKey(Home, on_delete=models.CASCADE, related_name="carousels2")
    position = models.PositiveIntegerField()
    title = models.CharField(max_length=255, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    image = models.ImageField(upload_to="home/carousel2")  # 550 x 400

    class Meta:
        verbose_name = "Elementos carusel segunda seccion"
        verbose_name_plural = "Elementos carusel segunda seccion"
        ordering = ["position"]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        try:
            self.old_file_path = os.path.join(settings.MEDIA_ROOT, self.image.name)
        except Exception as error:  # pylint: disable=broad-except
            logging.error(error)

    def __str__(self):
        return f"{self.pk}"

    @display(description=_("Preview"))
    def my_image_thumbnail(self):
        return get_template("files/my_image_thumbnail_template.html").render(
            {
                "field_name": "image",
                "model_name": "carousel2",
                "field_description": "description",
                "src": self.image.url if self.image else None,
            }
        )

    def save(self, *args, **kwargs):
        try:
            file_path = os.path.join(settings.MEDIA_ROOT, self.image.name)
            super().save(*args, **kwargs)
            if hasattr(self, "old_file_path") and self.old_file_path != file_path:
                # Al cambiar el nombre del archivo, borra el archivo del sistema de archivos
                if os.path.exists(self.old_file_path):
                    shutil.move(self.old_file_path, file_path)
        except Exception as error:  # pylint: disable=broad-except
            logging.error(error)

    def delete(self, *args, **kwargs):
        super().delete(*args, **kwargs)
        # Al eliminar el modelo Archivo, borra el archivo del sistema de archivos
        self.image.delete()


class Point3(TrainingModel):
    home = models.ForeignKey(Home, on_delete=models.CASCADE, related_name="points3")
    title = models.CharField(max_length=255)
    description = models.TextField()
    position = models.PositiveIntegerField()

    class Meta:
        verbose_name = "Puntos tercera seccion"
        verbose_name_plural = "Puntos tercera seccion"
        ordering = ["position"]

    def __str__(self):
        return f"{self.pk}"


class Carousel4(TrainingModel):
    home = models.ForeignKey(Home, on_delete=models.CASCADE, related_name="carousels4")
    position = models.PositiveIntegerField()
    title = models.CharField(max_length=255, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    image = models.ImageField(upload_to="home/carousel4")  # 810 x 450

    class Meta:
        verbose_name = "Elementos carusel cuarta seccion"
        verbose_name_plural = "Elementos carusel cuarta seccion"
        ordering = ["position"]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        try:
            self.old_file_path = os.path.join(settings.MEDIA_ROOT, self.image.name)
        except Exception as error:  # pylint: disable=broad-except
            logging.error(error)

    def __str__(self):
        return f"{self.pk}"

    @display(description=_("Preview"))
    def my_image_thumbnail(self):
        return get_template("files/my_image_thumbnail_template.html").render(
            {
                "field_name": "image",
                "model_name": "carousel4",
                "field_description": "description",
                "src": self.image.url if self.image else None,
            }
        )

    def save(self, *args, **kwargs):
        try:
            file_path = os.path.join(settings.MEDIA_ROOT, self.image.name)
            super().save(*args, **kwargs)
            if hasattr(self, "old_file_path") and self.old_file_path != file_path:
                # Al cambiar el nombre del archivo, borra el archivo del sistema de archivos
                if os.path.exists(self.old_file_path):
                    shutil.move(self.old_file_path, file_path)
        except Exception as error:  # pylint: disable=broad-except
            logging.error(error)

    def delete(self, *args, **kwargs):
        super().delete(*args, **kwargs)
        # Al eliminar el modelo Archivo, borra el archivo del sistema de archivos
        self.image.delete()
