from django.db import models
from datetime import datetime

class Mashine(models.Model):
    name=models.CharField(max_length=255)
    slug=models.SlugField(max_length=255)

class Questions(models.Model):
    name=models.CharField(max_length=255)
    text=models.TextField()
    mash=models.ForeignKey(Mashine, on_delete=models.CASCADE, blank=True, null=True)

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
