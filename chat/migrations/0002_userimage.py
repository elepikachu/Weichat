# Generated by Django 4.1 on 2023-01-31 00:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("chat", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="UserImage",
            fields=[
                (
                    "username",
                    models.CharField(
                        max_length=50,
                        primary_key=True,
                        serialize=False,
                        verbose_name="username",
                    ),
                ),
                ("img", models.ImageField(upload_to="images")),
            ],
        ),
    ]
