from django.contrib.auth import logout
from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView
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


class HomeView(LoginView):
    model = Personnel
    # template_name = 'app_personnel/index.html'
    template_name = 'app_personnel/base.html'
    context_object_name = 'home'

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
    template_name = 'app_personnel/list.html'
    context_object_name = 'personnel'
    extra_context = {'title': 'Главнвя страница'}

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['menu'] = menu
        return context

    def get_queryset(self):
        return Personnel.objects.filter(is_acceptance=True)


class CreateEmployeeView(CreateView):
    form_class = AddEmployeeForm
    template_name = 'app_personnel/create_employee.html'
    context_object_name = 'create_employee'
    success_url = reverse_lazy('home')

