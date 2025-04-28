from django.contrib import admin
from materials.models import UploadedFile

@admin.register(UploadedFile)
class UploadedFileAdmin(admin.ModelAdmin):
    list_display=['file','uploaded_at']
