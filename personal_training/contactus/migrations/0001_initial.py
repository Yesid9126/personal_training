# Generated by Django 4.2.5 on 2024-01-09 20:02

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Contacts",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                (
                    "created",
                    models.DateTimeField(
                        auto_now_add=True, help_text="Date time on which the object was created.", verbose_name="created at"
                    ),
                ),
                (
                    "modified",
                    models.DateTimeField(
                        auto_now=True, help_text="Date time on which the object was last modified.", verbose_name="modified at"
                    ),
                ),
                ("name", models.CharField(max_length=255)),
                ("email", models.EmailField(max_length=255)),
                ("phone", models.CharField(max_length=255)),
                ("send_contact", models.BooleanField(default=False)),
            ],
            options={
                "verbose_name": "Contacto",
                "verbose_name_plural": "Contactos",
            },
        ),
        migrations.CreateModel(
            name="ContactUs",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                (
                    "created",
                    models.DateTimeField(
                        auto_now_add=True, help_text="Date time on which the object was created.", verbose_name="created at"
                    ),
                ),
                (
                    "modified",
                    models.DateTimeField(
                        auto_now=True, help_text="Date time on which the object was last modified.", verbose_name="modified at"
                    ),
                ),
                ("title1", models.CharField(max_length=255)),
                ("description1", models.TextField()),
                ("title2", models.CharField(max_length=255)),
                ("title3", models.CharField(max_length=255)),
            ],
            options={
                "verbose_name": "Titulos",
                "verbose_name_plural": "Titulos",
            },
        ),
        migrations.CreateModel(
            name="Location",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                (
                    "created",
                    models.DateTimeField(
                        auto_now_add=True, help_text="Date time on which the object was created.", verbose_name="created at"
                    ),
                ),
                (
                    "modified",
                    models.DateTimeField(
                        auto_now=True, help_text="Date time on which the object was last modified.", verbose_name="modified at"
                    ),
                ),
                ("name", models.CharField(blank=True, max_length=255, null=True)),
                ("address", models.CharField(max_length=255)),
                ("latitude", models.CharField(max_length=255)),
                ("longitude", models.CharField(max_length=255)),
            ],
            options={
                "verbose_name": "Ubicacion",
                "verbose_name_plural": "Ubicaciones",
            },
        ),
    ]