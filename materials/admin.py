from django.contrib import admin
from materials.models import CategoryMaterials, UploadedFile

@admin.register(CategoryMaterials)
class CategoryMaterialsAdmin(admin.ModelAdmin):
    list_display=['name','slug','photo']
    prepopulated_fields={'slug':("name",)}
@admin.register(UploadedFile)
class UploadedFileAdmin(admin.ModelAdmin):
    list_display=['type_file','file','uploaded_at', 'cat']
