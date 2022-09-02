from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.models import User

from .models import *


class AddPersonnelForm(forms.Form, forms.ModelForm):
    class Meta:
        model = Personnel
        fields = ['id', 'last_name', 'first_name',
                  'fathers_name', 'slug', 'image',
                  'gender', 'email', 'phone', 'is_acceptance']


class AddPersonalDataForm(forms.Form, forms.ModelForm):
    class Meta:
        model = PersonalData
        fields = ['employee', 'born', 'birth_place', 'birth_country',
                  'country', 'city', 'post_code', 'street', 'street_number', 'house_number',
                  'education', 'uploadedFile', 'uploadedFile_date', 'is_acceptance']


class DateInput(forms.DateInput):
    input_type = 'date'


class AddEmploymentForm(forms.Form, forms.ModelForm, forms.DateInput):
    employment_date_beginning = forms.DateField(widget=DateInput)
    employment_date_ending = forms.DateField(widget=DateInput)
    uploadedFile_date = forms.DateField(widget=DateInput)
    deadline = forms.DateField(widget=DateInput)
    class Meta:
        model = Employment
        fields = ['employee',
                  'contract', 'employment_date_beginning', 'employment_date_ending',
                  'salary', 'uploadedFile', 'uploadedFile_date', 'education_remarks', 'deadline']
        widget = ({'employment_date_beginning': DateInput()},
                  {'employment_date_ending': DateInput()},
                  {'uploadedFile_date': DateInput()},
                  {'deadline': DateInput()})





