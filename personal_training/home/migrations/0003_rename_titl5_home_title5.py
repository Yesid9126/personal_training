# Generated by Django 4.2.5 on 2024-01-23 19:56

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("home", "0002_remove_home_title6"),
    ]

    operations = [
        migrations.RenameField(
            model_name="home",
            old_name="titl5",
            new_name="title5",
        ),
    ]
