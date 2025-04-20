from django.contrib import admin
from plumber.models import Questions, Answers

@admin.register(Questions)
class QuestionsAdmin(admin.ModelAdmin):
    display_list=['name']

@admin.register(Answers)
class AnswersAdmin(admin.ModelAdmin):
    display_list=['name',['ques']]
