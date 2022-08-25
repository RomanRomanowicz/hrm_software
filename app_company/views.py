from django.shortcuts import render
from django.http import HttpResponse
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView

from app_company.forms import *
from app_company.models import *


class ListObjectView(ListView):
    model = OrgStructure
    fields = ['departament', ]
    template_name = 'app_company/structure.html'
    context_object_name = 'structure'


class ListFunctionView(ListView):
    model = Function
    fields = ['function', ]
    template_name = 'app_company/function.html'
    context_object_name = 'function'


class CreateOrgView(CreateView):
    form_class = AddOrgForm
    template_name = 'app_company/create.html'
    context_object_name = 'create_structure'
    success_url = reverse_lazy('structure')


class CreateFunctionView(CreateView):
    form_class = AddFunctionForm
    template_name = 'app_company/create.html'
    context_object_name = 'create_function'
    success_url = reverse_lazy('function')


class UpdateOrgView(UpdateView):
    model = OrgStructure
    fields = ['departament', ]
    template_name = 'app_company/update.html'
    context_object_name = 'update_structure'
    success_url = reverse_lazy('structure')


class UpdateFunctionView(UpdateView):
    model = Function
    fields = ['function', ]
    template_name = 'app_company/update.html'
    context_object_name = 'update_function'
    success_url = reverse_lazy('function')


class DeleteOrganizationView(DeleteView):
    model = OrgStructure
    fields = ['departament', ]
    template_name = 'app_company/delete.html'
    context_object_name = 'delete_structure'
    success_url = reverse_lazy('structure')


class DeleteFunctionView(DeleteView):
    model = Function
    fields = ['function', ]
    template_name = 'app_company/delete.html'
    context_object_name = 'delete_function'
    success_url = reverse_lazy('function')





# class ListQualificationView(ListView):
#     model = Qualifications
#     fields = ['qualifications',]
#     template_name = 'app_company/qualifications.html'
#     context_object_name = 'qualifications'


# class ListVacationView(ListView):
#     model = Vacation
#     fields = ['function', 'vacation_limit', 'remote_work_limit']
#     template_name = 'app_company/vacation.html'
#     context_object_name = 'vacation'


# class CreateQualificationsView(CreateView):
#     form_class = AddQualificationsForm
#     template_name = 'app_company/create.html'
#     context_object_name = 'create_qualifications'
#     success_url = reverse_lazy('qualifications')


# class CreateVacationView(CreateView):
#     form_class = AddVacationForm
#     template_name = 'app_company/create.html'
#     context_object_name = 'create_vacation'
#     success_url = reverse_lazy('vacation')


# class UpdateQualificationView(UpdateView):
#     model = Qualifications
#     fields = ['qualifications', ]
#     template_name = 'app_company/update.html'
#     context_object_name = 'update_qualifications'
#     success_url = reverse_lazy('qualifications')
#
#
# class UpdateVacationView(UpdateView):
#     model = Vacation
#     fields = ['function', 'vacation_limit', 'remote_work_limit']
#     template_name = 'app_company/update.html'
#     context_object_name = 'update_vacation'
#     success_url = reverse_lazy('vacation')


# class DeleteQualificationView(DeleteView):
#     model = Qualifications
#     fields = ['qualifications', ]
#     template_name = 'app_company/delete.html'
#     context_object_name = 'delete_qualifications'
#     success_url = reverse_lazy('qualifications')


# class DeleteVacationView(DeleteView):
#     model = Vacation
#     fields = ['function', 'vacation_limit', 'remote_work_limit']
#     template_name = 'app_company/delete.html'
#     context_object_name = 'delete_vacation'
#     success_url = reverse_lazy('vacation')