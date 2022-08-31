from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.models import User

from .models import *


class AddPersonnelForm(forms.Form, forms.ModelForm):
    class Meta:
        model = Personnel
        fields = ['last_name', 'first_name', 'fathers_name', 'image', 'gender', 'email', 'phone', 'is_acceptance']


class AddEmployeeForm(forms.Form, forms.ModelForm):
    class Meta:
        model = Employee
        fields = ['username', 'employee', 'function', 'departament']


class DateInput(forms.DateInput):
    input_type = 'date'


class AddEmploymentForm(forms.Form, forms.ModelForm, forms.DateInput):
    employment_date_beginning = forms.DateField(widget=DateInput)
    employment_date_ending = forms.DateField(widget=DateInput)
    deadline = forms.DateField(widget=DateInput)
    class Meta:
        model = Employment
        fields = ['employee', 'function', 'departament',
                  'contract', 'employment_date_beginning', 'employment_date_ending',
                  'salary', 'uploadedFile', 'uploadedFile_date', 'education_remarks', 'deadline']
        widget = ({'employment_date_beginning': DateInput()},
                  {'employment_date_ending': DateInput()},
                  {'deadline': DateInput()})


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