# built-funtions
import logging
import os
import shutil

from django.conf import settings

# Preview Image
from django.contrib.admin.decorators import display

# Django
from django.db import models
from django.db.models.signals import pre_delete
from django.dispatch import receiver
from django.template.loader import get_template
from django.utils.text import slugify
from django.utils.translation import gettext_lazy as _

# Models
from personal_training.utils.models import TrainingModel


class Folder(TrainingModel):
    name = models.CharField(_("Nombre de la carpeta"), max_length=255, unique=True, blank=False)
    slug_name = models.SlugField(unique=True, max_length=255)
    objetivo = models.TextField(_("Objetivo"), default="", blank=True)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.slug_name = slugify(self.name)
        # Al guardar el modelo folder, crea la folder en el sistema de archivos
        if not os.path.exists(os.path.join(settings.MEDIA_ROOT, self.slug_name)):
            os.makedirs(os.path.join(settings.MEDIA_ROOT, self.slug_name))
        super().save(*args, **kwargs)

    def delete(self, *args, **kwargs):
        # Al eliminar el modelo Folder, borra la Folder y su contenido del sistema de archivos
        folder_path = os.path.join(settings.MEDIA_ROOT, self.slug_name)
        super().delete(*args, **kwargs)
        if os.path.exists(folder_path):
            for root, dirs, files in os.walk(folder_path, topdown=False):
                for slug_name in files:
                    os.remove(os.path.join(root, slug_name))
                for slug_name in dirs:
                    os.rmdir(os.path.join(root, slug_name))
            os.rmdir(folder_path)


@receiver(pre_delete, sender=Folder)
def delete_folder(sender, instance, **kwargs):
    # Al eliminar un modelo Carpeta, borra la carpeta del sistema de archivos
    folder_path = os.path.join(settings.MEDIA_ROOT, instance.slug_name)
    if os.path.exists(folder_path):
        for root, dirs, files in os.walk(folder_path, topdown=False):
            for slug_name in files:
                os.remove(os.path.join(root, slug_name))
            for slug_name in dirs:
                os.rmdir(os.path.join(root, slug_name))
        os.rmdir(folder_path)


def file_upload_to(instance, filename):
    file_path = os.path.join(settings.MEDIA_ROOT, instance.folder.slug_name, instance.slug_name)
    if os.path.exists(file_path):
        os.remove(file_path)
    return f"{instance.folder.slug_name}/{instance.slug_name}"


class File(models.Model):
    name = models.CharField(_("Nombre del archivo"), max_length=255, blank=False)
    slug_name = models.SlugField(unique=True, max_length=255)
    folder = models.ForeignKey(Folder, verbose_name=_("Carpeta"), on_delete=models.CASCADE)
    title = models.CharField(_("Título"), max_length=255, default="", blank=True)
    description = models.TextField(_("Descripción"), default="", blank=True)
    order = models.IntegerField(_("Órden"), default=0)
    file = models.FileField(_("Archivo"), upload_to=file_upload_to)

    @display(description=_("Preview"))
    def my_image_thumbnail(self):
        return get_template("files/my_image_thumbnail_template.html").render(
            {
                "field_name": "file",
                "model_name": "file",
                "field_description": "description",
                "src": self.file.url if self.file else None,
            }
        )

    class Meta:
        unique_together = (
            "folder_id",
            "name",
        )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        try:
            self.old_file_path = os.path.join(settings.MEDIA_ROOT, self.folder.slug_name, self.slug_name)
        except Exception as error:  # pylint: disable=broad-except
            logging.error(error)

    def __str__(self):
        return f"{self.folder.slug_name}: {self.slug_name}"

    def save(self, *args, **kwargs):
        self.slug_name = slugify(self.name)
        super().save(*args, **kwargs)
        file_path = os.path.join(settings.MEDIA_ROOT, self.folder.slug_name, self.slug_name)
        if hasattr(self, "old_file_path") and self.old_file_path != file_path:
            # Al cambiar el nombre del archivo, borra el archivo del sistema de archivos
            if os.path.exists(self.old_file_path):
                shutil.move(self.old_file_path, file_path)

    def delete(self, *args, **kwargs):
        # Al eliminar el modelo Archivo, borra el archivo del sistema de archivos
        file_path = os.path.join(settings.MEDIA_ROOT, self.folder.slug_name, self.slug_name)
        if os.path.exists(file_path):
            os.remove(file_path)
        super().delete(*args, **kwargs)
