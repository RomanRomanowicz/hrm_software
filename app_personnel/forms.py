from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.models import User

from .models import *


class AddPersonnelForm(forms.Form, forms.ModelForm):
    class Meta:
        model = Personnel
        fields = ['last_name', 'first_name',
                  'fathers_name', 'slug', 'image',
                  'gender', 'email', 'phone', 'is_acceptance']


class AddEmployeeForm(forms.Form, forms.ModelForm):
    class Meta:
        model = Employee
        fields = ['user', 'employee', 'function', 'departament']


class DateInput(forms.DateInput):
    input_type = 'date'


class AddPersonnelDataForm(forms.Form, forms.ModelForm, forms.DateInput):
    born = forms.DateField(widget=DateInput)
    uploadedFile_date = forms.DateField(widget=DateInput)
    class Meta:
        model = PersonnelData
        fields = ['employee', 'born', 'birth_place', 'birth_country',
                  'country', 'city', 'post_code', 'street', 'street_number', 'house_number',
                  'education', 'uploadedFile', 'uploadedFile_date', 'is_acceptance']
        widget = ({'born': DateInput()},
                  {'uploadedFile_date': DateInput()})


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


class AddDelegationForm(forms.ModelForm, forms.DateInput):
    # cause = models.TextField()
    date_start = forms.DateField(widget=DateInput)
    date_end = forms.DateField(widget=DateInput)
    # departure_reason = models.CharField()
    # scan_of_documents = models.FileField()

    class Meta:
        model = Delegation
        # exclude = ['username',]
        # fields = '__all__'
        fields = ['employee', 'username', 'cause', 'date_start', 'date_end', 'departure_reason', 'scan_of_documents']
        widget = {'date_start': DateInput()}, {'date_end': DateInput()}


class AddVacationForm(forms.ModelForm, forms.DateInput):
    date_start = forms.DateField(widget=DateInput)
    date_end = forms.DateField(widget=DateInput)

    class Meta:
        model = Vacation
        fields = ['employee', 'username', 'date_start', 'date_end', 'is_acceptance']
        widget = {'date_start': DateInput()}, {'date_end': DateInput()}


class DateTimeInput(forms.DateTimeInput):
    input_type = 'datetime-local'


class AddDailyReportForm(forms.ModelForm, forms.DateTimeInput):
    date_start = forms.DateTimeField(widget=DateTimeInput)
    date_end = forms.DateTimeField(widget=DateTimeInput)

    class Meta:
        model = DailyReport
        fields = ['employee', 'username', 'date_start', 'date_end', 'report']
        widget = {'date_start': DateTimeInput()}, {'date_end': DateTimeInput()}