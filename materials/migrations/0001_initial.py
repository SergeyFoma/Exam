from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CategoryMaterials',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150, verbose_name='Название категории')),
                ('slug', models.SlugField(max_length=150, unique=True)),
                ('photo', models.ImageField(blank=True, default=None, null=True, upload_to='category/%Y/%m/%d', verbose_name='Фото')),
            ],
            options={
                'verbose_name': 'Категория',
                'verbose_name_plural': 'Категории',
            },
        ),
        migrations.CreateModel(
            name='UploadedFile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type_file', models.CharField(blank=True, max_length=50, null=True, verbose_name='file or video')),
                ('file', models.FileField(upload_to='uploads/')),
                ('uploaded_at', models.DateTimeField(auto_now_add=True)),
                ('cat', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='categ', to='materials.categorymaterials')),
            ],
            options={
                'verbose_name': 'File',
                'verbose_name_plural': 'Files',
            },
        ),
    ]
