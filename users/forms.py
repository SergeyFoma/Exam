from django import forms 
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import get_user_model


class RegisterUserForm(UserCreationForm):
    username = forms.CharField(label="Логин",widget=forms.TextInput(attrs={"class":"form-input"}))
    password1 = forms.CharField(label="Пароль", widget=forms.PasswordInput(attrs={"class":"form-input"}))
    password2 = forms.CharField(label="Пароль-2", widget=forms.PasswordInput(attrs={"class":"form-input"}))
    class Meta:
        model=get_user_model()
        fields = ['username', 'email', 'first_name', 'last_name', 'password1', 'password2']

class LoginUserForm(AuthenticationForm):
    username=forms.CharField(label="login", widget=forms.TextInput(attrs={"class":"form-input"}))
    password=forms.CharField(label='password', widget=forms.PasswordInput(attrs={"class":"form-input"}))
    class Meta:
        model=get_user_model()
        fields=['username', 'password']