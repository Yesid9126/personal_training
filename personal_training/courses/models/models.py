# Django
from django.db import models
from django.utils.translation import gettext_lazy as _

# Models
from personal_training.utils.models import TrainingModel



class Course(TrainingModel):
    """Course model."""

    class CourseType(models.TextChoices):
        TRAINING = 'TRAINING', _('Entrenamiento')
        CHALLENGE = 'CHALLENGE', _('Reto')
        NUTRITION = 'NUTRITION', _('Nutrición')

    name = models.CharField('Nombre del curso', max_length=255)

    slug_name = models.SlugField(unique=True, max_length=255)

    description = models.TextField()

    course_type = models.CharField(max_length=255, choices=CourseType.choices, default=CourseType.TRAINING)


class Content(TrainingModel):
    """Content course model."""

    name = models.CharField(max_length=255)

    slug_name = models.SlugField(unique=True, max_length=255)

    description = models.TextField()

    course = models.ForeignKey("Course", on_delete=models.CASCADE, related_name="content_course")

    file_content = models.FileField(_("Cargar video"), upload_to='videos/')

    url = models.URLField(
        'Url Field',
        max_length=500,
        null=True,
        blank=True
    )