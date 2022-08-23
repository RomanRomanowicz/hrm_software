from django import forms
from django.contrib.auth.forms import AuthenticationForm

from .models import *


class DateInput(forms.DateInput):
    input_type = 'date'


class AddEmployeeForm(forms.Form, forms.ModelForm, forms.DateInput):
    employment_date = forms.DateField(widget=DateInput)
    class Meta:
        model = Personnel
        fields = ['last_name', 'first_name']
        widget = {'employment_date': DateInput()}


class LoginUserForm(AuthenticationForm):
    username = forms.CharField(label='Логин', widget=forms.TextInput(attrs={'class': 'form-input'}))
    password = forms.CharField(label='Пароль', widget=forms.PasswordInput(attrs={'class': 'form-input'}))