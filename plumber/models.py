from django.db import models

class Questions(models.Model):
    name=models.CharField(max_length=255)

class Answers(models.Model):
    name=models.CharField(max_length=255)
    ques=models.ForeignKey(Questions, on_delete=models.CASCADE)
