from django import forms
from app_calendar.models import *



class DateInput(forms.DateInput):
    input_type = 'date'


class AddDelegationForm(forms.Form, forms.ModelForm, forms.DateInput):
    date_start = forms.DateField(widget=DateInput)
    date_end = forms.DateField(widget=DateInput)

    class Meta:
        model = Delegation
        fields = ['employee', 'username', 'destination', 'date_start', 'date_end', 'departure_reason', 'scan_of_documents']
        widget = {'date_start': DateInput()}, {'date_end': DateInput()}


from django.forms import ModelForm, DateInput
from .models import Event


class EventForm(ModelForm):
    class Meta:
        model = Event
        # datetime-local is a HTML5 input type, format to make date time show on fields
        widgets = {
          'start_time': DateInput(attrs={'type': 'datetime-local'}, format='%Y-%m-%dT%H:%M'),
          'end_time': DateInput(attrs={'type': 'datetime-local'}, format='%Y-%m-%dT%H:%M'),
        }
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(EventForm, self).__init__(*args, **kwargs)
        # input_formats to parse HTML5 datetime-local input to datetime field
        self.fields['start_time'].input_formats = ('%Y-%m-%dT%H:%M',)
        self.fields['end_time'].input_formats = ('%Y-%m-%dT%H:%M',)