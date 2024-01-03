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


class Identifier(TrainingModel):
    name = models.CharField(max_length=255)

    class Meta:
        verbose_name = "Identificador"
        verbose_name_plural = "Identificadores"

    def __str__(self):
        return f"{self.name if self.name else 'Sin nombre'}"


class Carousel1(TrainingModel):
    identifier = models.ForeignKey(Identifier, on_delete=models.CASCADE, related_name="carousels")
    title = models.CharField(max_length=255, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    image = models.ImageField(upload_to="home/carousel1")  # 1470 x 870

    class Meta:
        verbose_name = "Seccion 1 Elemento"
        verbose_name_plural = "Seccion 1 Elementos"

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


class Section2(TrainingModel):
    identifier = models.OneToOneField(Identifier, on_delete=models.CASCADE, related_name="section2")
    title = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        verbose_name = "Seccion 2"
        verbose_name_plural = "Seccion 2"

    def __str__(self):
        return f"{self.identifier.name if self.identifier.name else 'Sin nombre'} : {self.title if self.title else 'Sin titulo'}"


class Carousel2(TrainingModel):
    section2 = models.ForeignKey(Section2, on_delete=models.CASCADE, related_name="carousels")
    position = models.PositiveIntegerField()
    title = models.CharField(max_length=255, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    image = models.ImageField(upload_to="home/carousel2")  # 550 x 400

    class Meta:
        verbose_name = "Seccion 2 Elemento"
        verbose_name_plural = "Seccion 2 Elementos"
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


class Section3(TrainingModel):
    identifier = models.OneToOneField(Identifier, on_delete=models.CASCADE, related_name="section3")
    title = models.CharField(max_length=255, blank=True, null=True)
    image = models.ImageField(upload_to="home/section3")  # 610 x 630

    class Meta:
        verbose_name = "Seccion 3"
        verbose_name_plural = "Seccion 3"

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        try:
            self.old_file_path = os.path.join(settings.MEDIA_ROOT, self.image.name)
        except Exception as error:  # pylint: disable=broad-except
            logging.error(error)

    def __str__(self):
        return f"{self.identifier.name if self.identifier.name else 'Sin nombre'} : {self.title if self.title else 'Sin titulo'}"

    @display(description=_("Preview"))
    def my_image_thumbnail(self):
        return get_template("files/my_image_thumbnail_template.html").render(
            {
                "field_name": "image",
                "model_name": "section3",
                "field_description": "title",
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


class Section3Point(TrainingModel):
    section3 = models.ForeignKey(Section3, on_delete=models.CASCADE, related_name="points")
    title = models.CharField(max_length=255)
    description = models.TextField()
    position = models.PositiveIntegerField()

    class Meta:
        verbose_name = "Seccion 3 Punto"
        verbose_name_plural = "Seccion 3 Puntos"
        ordering = ["position"]

    def __str__(self):
        return f"{self.pk}"


class Section4(TrainingModel):
    identifier = models.OneToOneField(Identifier, on_delete=models.CASCADE, related_name="section4")
    title = models.CharField(max_length=255, blank=True, null=True)
    description = models.TextField(blank=True, null=True)

    class Meta:
        verbose_name = "Seccion 4"
        verbose_name_plural = "Seccion 4"

    def __str__(self):
        return f"{self.identifier.name if self.identifier.name else 'Sin nombre'} : {self.title if self.title else 'Sin titulo'}"


class Carousel4(TrainingModel):
    section4 = models.ForeignKey(Section4, on_delete=models.CASCADE, related_name="carousels")
    position = models.PositiveIntegerField()
    title = models.CharField(max_length=255, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    image = models.ImageField(upload_to="home/carousel4")  # 810 x 450

    class Meta:
        verbose_name = "Seccion 4 Elemento"
        verbose_name_plural = "Seccion 4 Elementos"
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


class Section5(TrainingModel):
    identifier = models.OneToOneField(Identifier, on_delete=models.CASCADE, related_name="section5")
    title = models.CharField(max_length=255, blank=True, null=True)
    description = models.TextField(blank=True, null=True)

    class Meta:
        verbose_name = "Seccion 5"
        verbose_name_plural = "Seccion 5"

    def __str__(self):
        return f"{self.identifier.name if self.identifier.name else 'Sin nombre'} : {self.title if self.title else 'Sin titulo'}"


class Carousel5(TrainingModel):
    section5 = models.ForeignKey(Section5, on_delete=models.CASCADE, related_name="carousels")
    date = models.DateField()
    title = models.CharField(max_length=255, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    image = models.ImageField(upload_to="home/carousel5")  # 550 x 400

    class Meta:
        verbose_name = "Seccion 5 Elemento"
        verbose_name_plural = "Seccion 5 Elementos"

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
                "model_name": "carousel5",
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
        self.image.delete()
