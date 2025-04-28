from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    photo=models.ImageField(upload_to="users/%Y/%m/%d",
                blank=True,null=True,verbose_name="Фото")
    date_birth=models.DateTimeField(blank=True,
                null=True,verbose_name="Дата рождения")
    workshop=models.CharField(max_length=100, blank=True, null=True, verbose_name='Подразделение')
    profession=models.CharField(max_length=100, blank=True, null=True, verbose_name='Профессия')
# Create your models here.
