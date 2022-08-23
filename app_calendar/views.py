from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import generic
from django.shortcuts import render
from django.views.generic import ListView
from app_calendar.models import Delegation


# class ListDelegationView(ListView):
#     model = Delegation
#     fields = ['delegation', ]
#     template_name = 'app_calendar/delegation.html'
#     context_object_name = 'delegation'


class LoanedDelegationUserListView(LoginRequiredMixin, generic.ListView):
    model = Delegation
    template_name = 'app_calendar/delegation.html'
    paginate_by = 10

    def get_queryset(self):
        return

Delegation.objects.filter(borrower=self.request.user).filter(status__exact='o').order_by('due_back')
