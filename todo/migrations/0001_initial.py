# Generated by Django 5.1 on 2024-08-23 01:34

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Todo",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("todo", models.CharField(max_length=255)),
                ("status", models.BooleanField()),
            ],
        ),
    ]
