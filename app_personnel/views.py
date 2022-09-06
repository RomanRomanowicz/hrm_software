from django.contrib.auth import logout
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, DetailView
from app_personnel.forms import *
from app_personnel.models import *


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


class CreatePersonnel(CreateView):
    form_class = AddPersonnelForm
    template_name = 'calendarapp/add_human.html'
    context_object_name = 'create_personnel'
    slug_url_kwarg = 'slug'
    # success_url = reverse_lazy('create_employee')
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




# def your_delegation(request):
#     if request.user.groups.filter(name='Kierownictwo').exists():
#         context = Delegation.objects.filter(username=request.user)
#         return render(request, 'app_calendar/delegation.html', {'delegation': context})
#     else:
#         context = Delegation.objects.all()
#         return render(request, 'app_calendar/delegation.html', {'delegation': context})

'''to dla grupy'''
# def your_delegation(request):
#     if request.user.groups.filter(name=request.user.groups).exists():
#         context = Delegation.objects.filter(username=request.user)
#         return render(request, 'app_calendar/delegation.html', {'delegation': context})
#     else:
#         context = Delegation.objects.all()
#         return render(request, 'app_calendar/delegation.html', {'delegation': context})


class ListDelegationView(ListView):
    model = Delegation
    fields = ['employee', 'delegation', 'destination', 'date_start', 'date_end']
    template_name = 'calendarapp/delegation_list.html'
    context_object_name = 'delegation'


class CreateDelegation(CreateView):
    form_class = AddDelegationForm
    template_name = 'calendarapp/test.html'
    context_object_name = 'create_delegation'
    success_url = reverse_lazy('delegation')


# class UpdateDelegation(UpdateView):
#     model = Delegation
#     fields = ['employee', 'delegation', 'destination', 'date_start', 'date_end']
#     template_name = 'app_calendar/update.html'
#     context_object_name = 'update_delegation'
#     success_url = reverse_lazy('delegation')



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