from django import forms
from app_company.models import *
from django.contrib.auth.models import Group
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.models import User


class AddDepartamentForm(forms.ModelForm):
    class Meta:
        model = Departament
        fields = ['departament',]


class RegisterUserForm(UserCreationForm):
    username = forms.CharField(label='Логин', widget=forms.TextInput(attrs={'class': 'form-input'}))
    first_name = forms.CharField(label='Имя', widget=forms.TextInput(attrs={'class': 'form-input'}))
    last_name = forms.CharField(label='Фамиля', widget=forms.TextInput(attrs={'class': 'form-input'}))
    email = forms.EmailField(label='Email', widget=forms.TextInput(attrs={'class': 'form-input'}))
    password1 = forms.CharField(label='Пароль', widget=forms.TextInput(attrs={'class': 'form-input'}))
    password2 = forms.CharField(label='Повтор пароля', widget=forms.TextInput(attrs={'class': 'form-input'}))
    class Meta:
        model = User
        fields = ('last_name', 'first_name', 'username', 'email', 'password1', 'password2')

    def __str__(self):
        return f"{self.first_name}, {self.last_name}"



# class LoginUserForm(AuthenticationForm):
#     username = forms.CharField(label='Логин', widget=forms.TextInput(attrs={'class': 'form-input'}))
#     password = forms.CharField(label='Пароль', widget=forms.PasswordInput(attrs={'class': 'form-input'}))










# class AddQualificationsForm(forms.ModelForm):
#     class Meta:
#         model = Qualifications
#         fields = ['qualifications',]


# class AddVacationForm(forms.ModelForm):
#     class Meta:
#         model = Vacation
#         fields = ['function', 'vacation_limit', 'remote_work_limit']