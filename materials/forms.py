from django import forms
from .models import UploadedFile

class UploadFileForm(forms.ModelForm):
    type_file=forms.CharField(label="Файл или видео", widget=forms.TextInput(attrs={'class':'form-input'}))
    #file=forms.CharField(widget=forms.FileInput(attrs={'class':'form-file-input'}))
    class Meta:
        model = UploadedFile
        fields = ('type_file','file','cat')
        labels={'file':'Кнопка выбора файла'}
        widgets={
            #'type_file':forms.TextInput(attrs={'class':'form-input'}),
            'file':forms.FileInput(attrs={'class':'form-file-input'}),
            'cat':forms.Select(attrs={'class':'form-input-select'}),
        }

