from django.db import models
from django.urls import reverse

class CategoryMaterials(models.Model):
    name=models.CharField(max_length=150, verbose_name="Название категории")
    slug=models.SlugField(max_length=150, unique=True)
    photo=models.ImageField(upload_to="category/%Y/%m/%d", default=None, blank=True, null=True, verbose_name="Фото")

    class Meta:
        verbose_name='Категория'
        verbose_name_plural="Категории"
    
    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('materials:category_post', kwargs={'cat_id':self.id})


class UploadedFile(models.Model):
    type_file=models.CharField(max_length=50, verbose_name="file or video", blank=True, null=True)
    file = models.FileField(upload_to='uploads/')
    uploaded_at = models.DateTimeField(auto_now_add=True)
    cat=models.ForeignKey(CategoryMaterials, on_delete=models.PROTECT,related_name='categ', blank=True, null=True)

    class Meta:
        verbose_name='File'
        verbose_name_plural="Files"

    def __str__(self):
        return self.type_file

