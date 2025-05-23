# Generated by Django 5.2 on 2025-05-16 02:54

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="AnswersUser",
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
                ("name_user", models.CharField(max_length=255)),
                ("question", models.CharField(max_length=255)),
                ("answer", models.CharField(max_length=255)),
                ("date", models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name="Professions",
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
                (
                    "name",
                    models.CharField(max_length=150, verbose_name="Название профессии"),
                ),
                ("slug", models.SlugField(unique=True)),
            ],
            options={
                "verbose_name": "Профессия",
                "verbose_name_plural": "Профессии",
            },
        ),
        migrations.CreateModel(
            name="Mashine",
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
                ("name", models.CharField(max_length=255)),
                ("slug", models.SlugField(max_length=255, unique=True)),
                (
                    "prof",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.PROTECT,
                        to="plumber.professions",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Questions",
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
                ("name", models.CharField(blank=True, max_length=255, null=True)),
                ("text", models.TextField()),
                (
                    "image",
                    models.ImageField(
                        blank=True,
                        null=True,
                        upload_to="questions/%Y/%m/%d",
                        verbose_name="IMAGE",
                    ),
                ),
                (
                    "mash",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="plumber.mashine",
                    ),
                ),
            ],
            options={
                "verbose_name": "Вопрос",
                "verbose_name_plural": "Вопросы",
            },
        ),
        migrations.CreateModel(
            name="Answers",
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
                ("num", models.IntegerField()),
                ("answer", models.TextField()),
                ("active", models.BooleanField()),
                (
                    "mash",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="plumber.mashine",
                    ),
                ),
                (
                    "ques",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="plumber.questions",
                    ),
                ),
            ],
        ),
    ]
