from django.contrib import admin
from plumber.models import Questions, Answers, AnswersUser, Mashine

@admin.register(Questions)
class QuestionsAdmin(admin.ModelAdmin):
    list_display=['name','text', 'mash']

@admin.register(Answers)
class AnswersAdmin(admin.ModelAdmin):
    list_display=['num','answer','active', 'ques', 'mash']

@admin.register(AnswersUser)
class AnswersUserAdmin(admin.ModelAdmin):
    list_display=['name_user','question', 'answer', 'date']

@admin.register(Mashine)
class MashineAdmin(admin.ModelAdmin):
    list_display=['name', 'slug']
    prepopulated_fields={'slug':('name',)}