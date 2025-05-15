from django.db import models
from datetime import datetime

class Professions(models.Model):
    name=models.CharField(max_length=150,verbose_name='Название профессии')
    slug=models.SlugField(unique=True)

    class Meta:
        verbose_name="Профессия"
        verbose_name_plural="Профессии"
    def __str__(self):
        return self.name

class Mashine(models.Model):
    name=models.CharField(max_length=255)
    slug=models.SlugField(max_length=255, unique=True)
    prof=models.ForeignKey(Professions, on_delete=models.PROTECT, blank=True, null=True)
    def __str__(self):
        return self.name

class Questions(models.Model):
    name=models.CharField(max_length=255, blank=True, null=True)
    text=models.TextField()
    image=models.ImageField(upload_to="questions/%Y/%m/%d", blank=True, null=True, verbose_name='IMAGE')
    mash=models.ForeignKey(Mashine, on_delete=models.CASCADE, blank=True, null=True)

    class Meta:
        verbose_name='Вопрос'
        verbose_name_plural="Вопросы"

    def __str__(self):
        return self.text

class Answers(models.Model):
    num=models.IntegerField()
    answer=models.TextField()
    active=models.BooleanField()
    ques=models.ForeignKey(Questions, on_delete=models.CASCADE)
    mash=models.ForeignKey(Mashine, on_delete=models.CASCADE, blank=True, null=True)

class AnswersUser(models.Model):
    name_user=models.CharField(max_length=255)
    question=models.CharField(max_length=255)
    answer=models.CharField(max_length=255)
    date=models.DateTimeField(auto_now_add=True)
