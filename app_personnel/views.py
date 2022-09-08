from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.views import generic
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView
from pyexpat.errors import messages

from app_personnel.forms import *
from app_personnel.models import *
from django.contrib.auth.models import User, Group


menu = [
        {'title': 'вход', 'url_name': 'login'},
        {'title': 'Список сотрудников', 'url_name': 'personnel'},
        ]


class HomeView(LoginView):
    model = Personnel
    paginate_by = 10
    # template_name = 'app_personnel/index.html'
    template_name = 'calendarapp/dashboard.html'
    context_object_name = 'personnel'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['menu'] = menu
        context['title'] = 'Главнвя страница'
        return context

    def get_queryset(self):
        return Personnel.objects.filter(is_acceptance=True)


class ListObjectView(ListView):
    model = Personnel
    fields = ['__all__']
    template_name = 'calendarapp/personnel_list.html'
    context_object_name = 'personnel'
    extra_context = {'title': 'Главнвя страница'}

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['menu'] = menu
        return context

    def get_queryset(self):
        return Personnel.objects.filter(is_acceptance=True)


class PersonnelIdDetail(DetailView):
    model = Personnel
    #fields = ['last_name', 'first_name']
    template_name = 'calendarapp/human.html'
    slug_url_kwarg = 'slug'  ### tu mogę nadać swoją nazwę "slug"
    context_object_name = 'human'


class CreateEmployee(CreateView):
    form_class = AddEmployeeForm
    template_name = 'calendarapp/create_employee.html'
    context_object_name = 'create_employee'
    success_url = reverse_lazy('create_employee')


class CreatePersonnel(CreateView):
    form_class = AddPersonnelForm
    template_name = 'calendarapp/add_human.html'
    context_object_name = 'create_personnel'
    slug_url_kwarg = 'slug'
    success_url = reverse_lazy('create_data')


class CreatePersonnelData(CreateView):
    form_class = AddPersonnelDataForm
    template_name = 'calendarapp/add_personnel_data.html'
    context_object_name = 'create_data'
    success_url = reverse_lazy('add_employment')


class CreateEmployment(CreateView):
    form_class = AddEmploymentForm
    template_name = 'calendarapp/add_employment.html'
    context_object_name = 'add_employment'
    success_url = reverse_lazy('human')


class EmployeeView(ListView):
    model = Employee
    fields = ['user', 'employee']
    template_name = 'calendarapp/test.html'
    context_object_name = 'employee'


class EmployeeCreate(CreateView):
    form_class = AddPersonnelForm
    template_name = 'calendarapp/test.html'
    context_object_name = 'create_employee'
    success_url = reverse_lazy('employee')


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


# def add_delegation(request):
#     form = AddDelegationForm(request.POST or None)
#     if request.method == "POST":
#         if form.is_valid():
#             new_delegation = form.save(commit=False)
#             new_delegation.author = request.user
#             new_delegation.save()
#             return redirect('home')
#     return render(request, 'calendarapp/delegation_list.html.html', locals())


# class DelegationUserListView(LoginRequiredMixin, generic.ListView):
#     model = Delegation
#     template_name = 'calendarapp/delegation_list_user.html'
#     paginate_by = 10
#
#     def get_queryset(self):
#         return Delegation.objects.filter(username=self.request.user) #.filter(status__exact='o').order_by('date_start')


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