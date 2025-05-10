from django import forms
from .models import UploadedFile

class UploadFileForm(forms.ModelForm):
    type_file=forms.CharField(label="file or video", widget=forms.TextInput())
    class Meta:
        model = UploadedFile
        fields = ('type_file','file','cat')

