from django import forms

class TestForm(forms.Form):
    otvet=forms.CharField(widget=forms.CheckboxInput())