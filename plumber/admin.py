from django.contrib import admin
from plumber.models import Questions, Answers, AnswersUser, Mashine, Professions, FileResult

@admin.register(Professions)
class ProfessionsAdmin(admin.ModelAdmin):
    list_display=['id', 'name', 'slug', 'image']
    prepopulated_fields={'slug':('name',)}

@admin.register(Mashine)
class MashineAdmin(admin.ModelAdmin):
    list_display=['id','name', 'slug', 'prof']
    prepopulated_fields={'slug':('name',)}

@admin.register(Questions)
class QuestionsAdmin(admin.ModelAdmin):
    list_display=['name','image','text', 'mash']

@admin.register(Answers)
class AnswersAdmin(admin.ModelAdmin):
    list_display=['num','answer','active', 'ques', 'mash']

@admin.register(AnswersUser)
class AnswersUserAdmin(admin.ModelAdmin):
    list_display=['name_user', 'otvet','question', 'answer', 'date']

@admin.register(FileResult)
class FileResultAdmin(admin.ModelAdmin):
    list_display=['name',]



