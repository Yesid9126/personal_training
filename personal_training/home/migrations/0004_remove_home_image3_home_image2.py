# Generated by Django 4.2.5 on 2024-01-23 20:02

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("home", "0003_rename_titl5_home_title5"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="home",
            name="image3",
        ),
        migrations.AddField(
            model_name="home",
            name="image2",
            field=models.ImageField(blank=True, null=True, upload_to="home/seccion2"),
        ),
    ]