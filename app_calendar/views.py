from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views import generic
from django.shortcuts import render
from django.views.generic import ListView, CreateView, UpdateView

from app_calendar.forms import AddDelegationForm
from app_calendar.models import Delegation
from django.contrib.auth.models import User


def your_delegation(request):
    if request.user.groups.filter(name='Kierownictwo').exists():
        context = Delegation.objects.filter(username=request.user)
        return render(request, 'app_calendar/delegation.html', {'delegation': context})
    else:
        context = Delegation.objects.all()
        return render(request, 'app_calendar/delegation.html', {'delegation': context})

'''to dla grupy'''
# def your_delegation(request):
#     if request.user.groups.filter(name=request.user.groups).exists():
#         context = Delegation.objects.filter(username=request.user)
#         return render(request, 'app_calendar/delegation.html', {'delegation': context})
#     else:
#         context = Delegation.objects.all()
#         return render(request, 'app_calendar/delegation.html', {'delegation': context})



# class ListDelegationView(ListView):
#     model = Delegation
#     fields = ['employee', 'delegation', 'destination', 'date_start', 'date_end']
#     template_name = 'app_calendar/delegation.html'
#     context_object_name = 'delegation'




class CreateDelegationView(CreateView):
    form_class = AddDelegationForm
    template_name = 'app_calendar/create.html'
    context_object_name = 'create_delegation'
    success_url = reverse_lazy('delegation')


class UpdateDelegation(UpdateView):
    model = Delegation
    fields = ['employee', 'delegation', 'destination', 'date_start', 'date_end']
    template_name = 'app_calendar/update.html'
    context_object_name = 'update_delegation'
    success_url = reverse_lazy('delegation')


# class LoanedDelegationUserListView(LoginRequiredMixin, generic.ListView):
#     model = Delegation
#     template_name = 'app_calendar/delegation.html'
#     paginate_by = 10
#
#     def get_queryset(self):
#         return

# Delegation.objects.filter(borrower=self.request.user).filter(status__exact='o').order_by('due_back')
