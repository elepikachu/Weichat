# Generated by Django 4.1 on 2023-01-16 03:12

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="ChatInformation",
            fields=[
                (
                    "id",
                    models.IntegerField(
                        primary_key=True, serialize=False, verbose_name="数据编号"
                    ),
                ),
                (
                    "usrid",
                    models.CharField(default="", max_length=50, verbose_name="用户编号"),
                ),
                ("date", models.DateTimeField(verbose_name="时间戳")),
                (
                    "content",
                    models.CharField(default="", max_length=50, verbose_name="聊天内容"),
                ),
            ],
        ),
    ]
