from django.contrib import admin
from plumber.models import Questions, Answers, AnswerUser

@admin.register(Questions)
class QuestionsAdmin(admin.ModelAdmin):
    display_list=['name','text']

@admin.register(Answers)
class AnswersAdmin(admin.ModelAdmin):
    display_list=['answer', 'ques']

@admin.register(AnswerUser)
class AnswerUserAdmin(admin.ModelAdmin):
    display_list=['question', 'answer_num', 'answer', 'active']
