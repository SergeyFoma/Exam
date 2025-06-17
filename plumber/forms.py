from django import forms
from .models import AnswersUser

class TestForm(forms.ModelForm):
    otvet=forms.CharField(widget=forms.CheckboxInput())