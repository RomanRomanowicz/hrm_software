from django.contrib.auth import logout
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, DetailView
from app_personnel.forms import *
from app_personnel.models import *

from django.http import HttpResponse

# def login_user(request):
#     return render(request, 'login.html')

menu = [
        {'title': 'вход', 'url_name': 'login'},
        {'title': 'Список сотрудников', 'url_name': 'personnel'},
        ]


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
    success_url = reverse_lazy('create_employee')


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
    template_name = 'calendarapp/events_list.html'
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


# def personnel_id_view(request, personnel_id_id):
#     # if request.id.filter(id=id).exists():
#     personnel_id = Personnel.object.all()
#     return render(request, 'app_personnel/personnel_id.html', {'personnel_id': personnel_id})


class CreatePersonnelView(CreateView):
    form_class = AddPersonnelForm
    template_name = 'app_personnel/add_personnel.html'
    context_object_name = 'create_personnel'
    success_url = reverse_lazy('create_employee')


class CreateEmployeeView(CreateView):
    form_class = AddEmployeeForm
    template_name = 'app_personnel/create.html'
    context_object_name = 'create_employee'
    success_url = reverse_lazy('create_employment')


class CreateEmploymentView(CreateView):
    form_class = AddEmploymentForm
    template_name = 'app_personnel/create.html'
    context_object_name = 'create_employment'
    success_url = reverse_lazy('')
