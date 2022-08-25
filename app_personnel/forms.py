from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.models import User

from .models import *


class DateInput(forms.DateInput):
    input_type = 'date'


class AddEmployeeForm(forms.Form, forms.ModelForm, forms.DateInput):
    employment_date = forms.DateField(widget=DateInput)
    class Meta:
        model = Personnel
        fields = ['last_name', 'first_name']
        widget = {'employment_date': DateInput()}


class RegisterUserForm(UserCreationForm):
    username = forms.CharField(label='Логин', widget=forms.TextInput(attrs={'class': 'form-input'}))
    first_name = forms.CharField(label='Имя', widget=forms.TextInput(attrs={'class': 'form-input'}))
    last_name = forms.CharField(label='Фамиля', widget=forms.TextInput(attrs={'class': 'form-input'}))
    email = forms.EmailField(label='Email', widget=forms.TextInput(attrs={'class': 'form-input'}))
    password1 = forms.CharField(label='Пароль', widget=forms.TextInput(attrs={'class': 'form-input'}))
    password2 = forms.CharField(label='Повтор пароля', widget=forms.TextInput(attrs={'class': 'form-input'}))
    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2')


# class LoginUserForm(AuthenticationForm):
#     username = forms.CharField(label='Логин', widget=forms.TextInput(attrs={'class': 'form-input'}))
#     password = forms.CharField(label='Пароль', widget=forms.PasswordInput(attrs={'class': 'form-input'}))