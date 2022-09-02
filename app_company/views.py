from django.contrib.auth import logout
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.views import LoginView
from django.shortcuts import render, redirect, get_object_or_404
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from app_company.forms import *
from app_company.models import *

from django.contrib.auth.models import User, Group, Permission

from app_personnel.models import *


class LoginUser(LoginView):
    form_class = AuthenticationForm
    template_name = 'login.html'
    extra_context = {'title': 'Вход в HRM Sofware'}

    def get_success_url(self):
        return reverse_lazy('home')


def logout_user(request):
    logout(request)
    return redirect('login')


class RegisterUser(CreateView):
    form_class = RegisterUserForm
    template_name = 'app_personnel/register.html'
    context_object_name = 'register'
    success_url = reverse_lazy('home')


# def employee_list(request):
#     employee = Employee.objects.all()
#     return render(request, 'app_company/employee_list.html', {'employee': employee})


def function_group(request):
    group = Group.objects.all()
    return render(request, 'app_company/function_group.html', {'group': group})


class DepartamentView(ListView):
    model = Departament
    fields = ['departament', ]
    template_name = 'calendarapp/add_departament.html'
    context_object_name = 'structure'


class CreateDepartament(CreateView):
    form_class = AddDepartamentForm
    template_name = 'calendarapp/add_departament.html'
    context_object_name = 'create_structure'
    success_url = reverse_lazy('structure')


class UpdateDepartament(UpdateView):
    model = Departament
    fields = ['departament', ]
    template_name = 'calendarapp/update_departament.html'
    context_object_name = 'update_departament'
    success_url = reverse_lazy('structure')


class DeleteDepartament(DeleteView):
    model = Departament
    fields = ['departament', ]
    template_name = 'calendarapp/delete_structure.html'
    context_object_name = 'delete_structure'
    success_url = reverse_lazy('structure')


# class UpdateFunction(UpdateView):
#     model = Function
#     fields = ['function', ]
#     template_name = 'app_company/update.html'
#     context_object_name = 'update_function'
#     success_url = reverse_lazy('function')
#
#
# class DeleteFunction(DeleteView):
#     model = Function
#     fields = ['function', ]
#     template_name = 'app_company/delete.html'
#     context_object_name = 'delete_function'
#     success_url = reverse_lazy('function')











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