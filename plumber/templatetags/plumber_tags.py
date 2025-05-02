from django import template
import plumber.views as views
from materials.models import UploadedFile

register = template.Library()

@register.simple_tag
def up_fil():
    return UploadedFile.objects.all()