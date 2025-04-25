from django.contrib import admin
from plumber.models import Questions, Answers, AnswersUser

@admin.register(Questions)
class QuestionsAdmin(admin.ModelAdmin):
    list_display=['name','text']

@admin.register(Answers)
class AnswersAdmin(admin.ModelAdmin):
    list_display=['num','answer','active', 'ques']

@admin.register(AnswersUser)
class AnswersUserAdmin(admin.ModelAdmin):
    list_display=['name_user','question', 'answer', 'date']
