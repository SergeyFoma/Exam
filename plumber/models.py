from django.db import models

class Questions(models.Model):
    name=models.CharField(max_length=255)
    text=models.TextField()

class Answers(models.Model):
    answer=models.TextField()
    active=models.BooleanField(blank=True, null=True)
    ques=models.ForeignKey(Questions, on_delete=models.CASCADE)
