from django.db import models
from datetime import datetime

class Questions(models.Model):
    name=models.CharField(max_length=255)
    text=models.TextField()

class Answers(models.Model):
    num=models.IntegerField()
    answer=models.TextField()
    active=models.BooleanField()
    ques=models.ForeignKey(Questions, on_delete=models.CASCADE)

class AnswersUser(models.Model):
    name_user=models.CharField(max_length=255)
    question=models.CharField(max_length=255)
    answer=models.TextField()
    date=models.DateTimeField(auto_now_add=True)
