from django import template
import plumber.views as views
from materials.models import UploadedFile, CategoryMaterials
from plumber.models import Mashine
from plumber.views import que_count

register = template.Library()

@register.simple_tag
def up_fil():
    #return UploadedFile.objects.all()
    items=UploadedFile.objects.select_related('cat')
    return items

@register.simple_tag
def mashine_tag():
    return Mashine.objects.all()

@register.simple_tag
def category_tag():
    return CategoryMaterials.objects.all()

@register.filter
def timing(a,b):
    tim2=int(a)+int(b)
    return tim2
