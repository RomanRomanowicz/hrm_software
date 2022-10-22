from django.contrib.auth import logout
from django.contrib.auth.decorators import permission_required, login_required
from django.contrib.auth.views import LoginView
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import PermissionRequiredMixin
from app_company.forms import *
from django.contrib.auth.models import User, Group, Permission
from app_personnel.models import *


class LoginUser(LoginView):
    form_class = AuthenticationForm
    template_name = 'accounts/login.html'
    # template_name = 'login.html'
    context_object_name = 'login'
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


@login_required
@permission_required('app_company.user_list', raise_exception=True)
def user_list(request):
    users = Employee.objects.all()
    return render(request, 'app_company/user_list.html', {'users': users})


@login_required
@permission_required('app_company.function_group', raise_exception=True)
def function_group(request):
    perm = 0
    for i in request.user.groups.all():
        if i.name == 'masteruser': perm = 1

    if perm == 0:
        error = "Доступ запрещен"
        return render(request, 'app_company/error.html', {'error': error})

    group = Group.objects.all().exclude(name='masteruser')
    return render(request, 'app_company/add_function.html', {'group': group})


def function_group_add(request):
    perm = 0
    for i in request.user.groups.all():
        if i.name == 'masteruser': perm = 1
    if perm == 0:
        error = "Доступ запрещен"
        return render(request, 'app_company/error.html', {'error': error})
    if request.method == 'POST':
        name = request.POST.get('name')
        if name != "":
            if len(Group.objects.filter(name=name)) == 0:
                group = Group(name=name)
                group.save()
    return redirect('function_group')


class FunctionUpdate(UpdateView):
    model = Group
    fields = ['name', ]
    template_name = 'app_company/update_function.html'
    context_object_name = 'function_update'
    success_url = reverse_lazy('function_group')


class FunctionDelete(DeleteView):
    model = Group
    fields = ['name', ]
    template_name = 'app_company/delete_function.html'
    context_object_name = 'function_del'
    success_url = reverse_lazy('function_group')


class DepartamentView(PermissionRequiredMixin, ListView):
    permission_required = 'app_company.views'
    model = Departament
    fields = ['departament', ]
    template_name = 'app_company/add_departament.html'
    context_object_name = 'structure'


class CreateDepartament(PermissionRequiredMixin, CreateView):
    permission_required = 'app_company.views'
    form_class = AddDepartamentForm
    template_name = 'app_company/add_departament.html'
    context_object_name = 'create_structure'
    success_url = reverse_lazy('structure')


class UpdateDepartament(PermissionRequiredMixin, UpdateView):
    permission_required = 'app_company.views'
    model = Departament
    fields = ['departament', ]
    template_name = 'app_company/update_departament.html'
    context_object_name = 'update_departament'
    success_url = reverse_lazy('structure')


class DeleteDepartament(PermissionRequiredMixin, DeleteView):
    permission_required = 'app_company.views'
    model = Departament
    fields = ['departament', ]
    template_name = 'app_company/delete_structure.html'
    context_object_name = 'delete_structure'
    success_url = reverse_lazy('structure')


def function_perms(request):
    perm = 0
    for i in request.user.groups.all():
        if i.name == 'masteruser': perm = 1

    if perm == 0:
        error = "Доступ запрещен"
        return render(request, 'app_company/error.html', {'error': error})

    perms = Permission.objects.all().exclude(name='masteruser')
    return render(request, 'app_company/Permission_list.html', {'perms': perms})


def users_perms(request, pk):
    perm = 0
    for i in request.user.groups.all():
        if i.name == 'masteruser': perm = 1

    if perm == 0:
        error = "Доступ запрещен"
        return render(request, 'app_company/error.html', {'error': error})

    perms = Permission.objects.all().exclude(name='masteruser')
    return render(request, 'app_company/Permission_list.html', {'perms': perms})