from django import forms
from app_company.models import *
from django.contrib.auth.models import Group


# class AddOrgForm(forms.ModelForm):
#     class Meta:
#         model = OrgStructure
#         fields = ['departament',]


class AddFunctionForm(forms.ModelForm):
    class Meta:
        model = Function
        fields = ['function', ]






# class AddQualificationsForm(forms.ModelForm):
#     class Meta:
#         model = Qualifications
#         fields = ['qualifications',]


# class AddVacationForm(forms.ModelForm):
#     class Meta:
#         model = Vacation
#         fields = ['function', 'vacation_limit', 'remote_work_limit']