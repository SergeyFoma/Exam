from django.db import models

class Questions(models.Model):
    name=models.CharField(max_length=255)
    text=models.TextField()

class Answers(models.Model):
    num=models.IntegerField(blank=True, null=True)
    answer=models.TextField()
    active=models.BooleanField(blank=True, null=True)
    ques=models.ForeignKey(Questions, on_delete=models.CASCADE)

class AnswerUser(models.Model):
    question=models.CharField(max_length=255)
    answer_num=models.IntegerField(blank=True, null=True)
    answer=models.TextField()
    active=models.BooleanField()
