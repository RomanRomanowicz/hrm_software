from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.contrib.auth.views import LoginView
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.views import generic
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView
from pyexpat.errors import messages

from app_personnel.forms import *
from app_personnel.models import *
from django.contrib.auth.models import User, Group


class HomeView(LoginView):
    model = Personnel
    paginate_by = 10
    template_name = 'calendarapp/personnel_list.html'
    # template_name = 'calendarapp/dashboard.html'
    context_object_name = 'personnel'

    def get_queryset(self):
        return Personnel.objects.filter(is_acceptance=True)


class ListPersonnelView(ListView):
    model = Personnel
    fields = ['__all__']
    template_name = 'calendarapp/personnel_list.html'
    context_object_name = 'personnel'
    extra_context = {'title': 'Главнвя страница'}

    def get_queryset(self):
        return Personnel.objects.filter(is_acceptance=True)


class CreatePersonnel(CreateView):
    form_class = AddPersonnelForm
    template_name = 'calendarapp/add_human.html'
    context_object_name = 'create_personnel'
    slug_url_kwarg = 'slug'
    success_url = reverse_lazy('create_data')


class PersonnelIdDetail(PermissionRequiredMixin, DetailView):
    permission_required = 'app_personnel.views'
    model = Personnel
    template_name = 'calendarapp/human.html'
    slug_url_kwarg = 'slug'  ### tu mogę nadać swoją nazwę "slug"
    context_object_name = 'human'

    def get_context_data(self, **kwargs):
        context = super(PersonnelIdDetail, self).get_context_data(**kwargs)
        context['employee'] = Employee.objects.filter(employee=self.get_object())
        return context


class CreatePersonnelData(PermissionRequiredMixin, CreateView):
    permission_required = 'app_personnel.views'
    form_class = AddPersonnelDataForm
    template_name = 'calendarapp/add_personnel_data.html'
    context_object_name = 'create_data'
    success_url = reverse_lazy('add_employment')


class PersonnelDataDetail(PermissionRequiredMixin, DetailView):
    permission_required = 'app_personnel.views'
    model = PersonnelData
    template_name = 'calendarapp/personnel_data_detail.html'
    # slug_url_kwarg = 'slug'
    context_object_name = 'personnel_data_detail'


class EmploymentCreate(PermissionRequiredMixin, CreateView):
    permission_required = 'app_personnel.views'
    form_class = AddEmploymentForm
    template_name = 'calendarapp/add_employment.html'
    context_object_name = 'add_employment'
    success_url = reverse_lazy('register')


class EmploymentDetail(PermissionRequiredMixin, DetailView):
    permission_required = 'app_personnel.views'
    model = Employment
    template_name = 'calendarapp/employment_detail.html'
    context_object_name = 'employment_detail'


''' ------------------------- сотрудник ------------------------'''


class ListEmployeeView(ListView):
    permission_required = 'app_personnel.views'
    model = Employee
    template_name = 'calendarapp/nowy_personnel_list.html'
    context_object_name = 'employee_list'


class EmployeeDetail(PermissionRequiredMixin, DetailView):
    permission_required = 'app_personnel.views'
    model = Employee
    template_name = 'calendarapp/nowy_test.html'
    context_object_name = 'employee_detail'


class CreateEmployee(PermissionRequiredMixin, CreateView):
    permission_required = 'app_personnel.views'
    form_class = AddEmployeeForm
    template_name = 'calendarapp/create_employee.html'
    context_object_name = 'create_employee'
    success_url = reverse_lazy('personnel')


''' ------------------------------------koniec przerabiania---------------------------------'''


'''------------- zmiana stanowiska --------------------'''
# class EmployeeUpdate(UpdateView):
#     model = Employee
#     fields = ['user', 'employee', 'function', 'departament']
#     template_name = 'calendarapp/login.html'
#     context_object_name = 'create_employee'
#     success_url = reverse_lazy('employee')


""" ----------------------------- командировка ------------------------------------"""


def your_delegation(request):
    if request.user.groups.filter().exists():
        context = Delegation.objects.filter(username=request.user)
        return render(request, 'calendarapp/delegation_list.html', {'delegation': context})
    else:
        context = Delegation.objects.all()
        return render(request, 'calendarapp/delegation_list.html', {'delegation': context})


'''это если чётко прописать группу'''
# def your_delegation(request):
#     if request.user.groups.filter(name='masteruser').exists():
#         context = Delegation.objects.filter(username=request.user)
# return render(request, 'calendarapp/delegation_list.html', {'delegation': context})


class CreateDelegation(CreateView):
    form_class = AddDelegationForm
    template_name = 'calendarapp/create_delegation.html'
    context_object_name = 'create_delegation'
    success_url = reverse_lazy('delegation')


class UpdateDelegation(UpdateView):
    model = Delegation
    fields = ['employee', 'username', 'cause', 'date_start', 'date_end', 'departure_reason', 'scan_of_documents']
    template_name = 'calendarapp/update.html'
    context_object_name = 'update_delegation'
    success_url = reverse_lazy('delegation')


class DeleteDelegation(DeleteView):
    model = Delegation
    fields = ['cause', ]
    template_name = 'calendarapp/delete.html'
    context_object_name = 'delete_delegation'
    success_url = reverse_lazy('delegation')


""" ---------------------- Отпуск ------------------------------ """


def your_vacation(request):
    if request.user.groups.filter().exists():
        context = Vacation.objects.filter(username=request.user)
        return render(request, 'calendarapp/vacation_list.html', {'vacation': context})
    else:
        context = Vacation.objects.all()
        return render(request, 'calendarapp/vacation_list.html', {'vacation': context})


class CreateVacation(CreateView):
    form_class = AddVacationForm
    template_name = 'calendarapp/create_vacation.html'
    context_object_name = 'create_vacation'
    success_url = reverse_lazy('vacation')


class UpdateVacation(UpdateView):
    model = Vacation
    fields = ['date_start', 'date_end']
    template_name = 'calendarapp/update.html'
    context_object_name = 'update_vacation'
    success_url = reverse_lazy('vacation')


class DeleteVacation(DeleteView):
    model = Vacation
    fields = ['date_start', 'date_end']
    template_name = 'calendarapp/delete.html'
    context_object_name = 'delete_vacation'
    success_url = reverse_lazy('vacation')


'''----------- Ежедневный отчет -----------------'''


def your_daily_report(request):
    if request.user.groups.filter().exists():
        context = DailyReport.objects.filter(username=request.user)
        return render(request, 'calendarapp/daily_report_list.html', {'daily_report': context})
    else:
        context = DailyReport.objects.all()
        return render(request, 'calendarapp/daily_report_list.html', {'daily_report': context})


class CreateDailyReport(CreateView):
    form_class = AddDailyReportForm
    template_name = 'calendarapp/create_daily_report.html'
    context_object_name = 'create_daily_report'
    success_url = reverse_lazy('daily_report')


class DetailDailyReport(DetailView):
    model = DailyReport
    template_name = 'calendarapp/detail_report.html'
    context_object_name = 'detail_report'


class UpdateDailyReport(UpdateView):
    model = DailyReport
    fields = ['date_start', 'date_end']
    template_name = 'calendarapp/update.html'
    context_object_name = 'update_daily_report'
    success_url = reverse_lazy('daily_report')


class DeleteDailyReport(DeleteView):
    model = DailyReport
    fields = ['date_start', 'date_end']
    template_name = 'calendarapp/delete.html'
    context_object_name = 'delete_daily_report'
    success_url = reverse_lazy('daily_report')
