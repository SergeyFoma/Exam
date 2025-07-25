from django import forms 
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, PasswordChangeForm
from django.contrib.auth import get_user_model
import datetime


class RegisterUserForm(UserCreationForm):
    username = forms.CharField(label="Логин",widget=forms.TextInput(attrs={"class":"form-input"}))
    password1 = forms.CharField(label="Пароль", widget=forms.PasswordInput(attrs={"class":"form-input"}))
    password2 = forms.CharField(label="Пароль-2", widget=forms.PasswordInput(attrs={"class":"form-input"}))
    # first_name=forms.CharField(label='Имя',widget=forms.TextInput(attrs={"class":'form-input'}))
    workshop = forms.CharField(label="Подразделение",widget=forms.TextInput(attrs={"class":"form-input"}))
    profession=forms.CharField(label='Профессия', widget=forms.TextInput(attrs={'class':'form-input'}))
    class Meta:
        model=get_user_model()
        fields = ['username', 'email', 'first_name', 'last_name', 'password1', 'password2','workshop', 'profession']
        labels={
            'first_name': 'Имя',
            'last_name': 'Фамилия',
            'email': 'Email',
        }
        widgets={
            'first_name': forms.TextInput(attrs={'class':'form-input'}),
            'last_name': forms.TextInput(attrs={'class':'form-input'}),
            'email': forms.TextInput(attrs={'class':'form-input'}),
        }

class LoginUserForm(AuthenticationForm):
    username=forms.CharField(label="Логин", widget=forms.TextInput(attrs={"class":"form-input"}))
    password=forms.CharField(label='Пароль', widget=forms.PasswordInput(attrs={"class":"form-input"}))
    class Meta:
        model=get_user_model()
        fields=['username', 'password']

class ProfileUserForm(forms.ModelForm):
    username=forms.CharField(disabled=True, label='Login',widget=forms.TextInput(attrs={'class':'form-input'}))
    email=forms.CharField(disabled=True,required=False, label='Email',widget=forms.TextInput(attrs={'class':'form-input'}))
    workshop=forms.CharField(disabled=False,required=False, label='Подразделение', widget=forms.TextInput(attrs={'class':'form-input'}))
    profession=forms.CharField(disabled=False,required=False, label='Профессия', widget=forms.TextInput(attrs={'class':'form-input'}))
    this_year=datetime.date.today().year
    date_birth=forms.DateField(widget=forms.SelectDateWidget(years=tuple(range(this_year-100, this_year-5))))

    class Meta:
        model=get_user_model()
        fields=['photo', 'username','email', 'date_birth', 'first_name', 'last_name', 'workshop','profession']
        labels={
            'first_name': 'Имя',
            'last_name': 'Фамилия',
        }
        widgets={
            'first_name': forms.TextInput(attrs={'class':'form-input'}),
            'last_name': forms.TextInput(attrs={'class':'form-input'}),
        }

class UserPasswordChangeForm(PasswordChangeForm):
    old_password=forms.CharField(label="Старый пароль",widget=forms.PasswordInput(attrs={"class":"form-input"}))
    new_password1=forms.CharField(label="Новый пароль", widget=forms.PasswordInput(attrs={"class":"form-input"}))
    new_password2=forms.CharField(label="Повторите пароль", widget=forms.PasswordInput(attrs={"class":"form-input"}))