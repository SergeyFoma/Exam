# Generated by Django 3.2.25 on 2025-06-30 03:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('plumber', '0003_answersuser_otvet'),
    ]

    operations = [
        migrations.CreateModel(
            name='FileResult',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.FileField(upload_to='uploads/result/%Y/%m/%d')),
            ],
        ),
    ]
