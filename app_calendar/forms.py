from django import forms
from app_calendar.models import *


class DateInput(forms.DateInput):
    input_type = 'date'


class AddDelegationForm(forms.Form, forms.ModelForm, forms.DateInput):
    date_start = forms.DateField(widget=DateInput)
    date_end = forms.DateField(widget=DateInput)
    class Meta:
        model = Delegation
        fields = ['destination', 'date_start', 'date_end', 'departure_reason', 'scan_of_documents']
        widget = {'date_start': DateInput()}, {'date_end': DateInput()}