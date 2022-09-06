from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views import generic
from django.shortcuts import render
from django.views.generic import ListView, CreateView, UpdateView

from app_calendar.forms import AddDelegationForm, EventForm
from app_calendar.models import Delegation
from django.contrib.auth.models import User, Group

import calendar
from datetime import datetime, timedelta, date
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.views import generic
from django.urls import reverse
from django.utils.safestring import mark_safe
from .models import *
from .utils import Calendar



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
    # template_name = 'app_calendar/delegation.html'
    template_name = 'calendarapp/test.html'
    context_object_name = 'delegation'




# class CreateDelegationView(CreateView):
#     form_class = AddDelegationForm
#     template_name = 'app_calendar/create.html'
#     context_object_name = 'create_delegation'
#     success_url = reverse_lazy('delegation')
#
#
# class UpdateDelegation(UpdateView):
#     model = Delegation
#     fields = ['employee', 'delegation', 'destination', 'date_start', 'date_end']
#     template_name = 'app_calendar/update.html'
#     context_object_name = 'update_delegation'
#     success_url = reverse_lazy('delegation')


# class LoanedDelegationUserListView(LoginRequiredMixin, generic.ListView):
#     model = Delegation
#     template_name = 'app_calendar/delegation.html'
#     paginate_by = 10
#
#     def get_queryset(self):
#         return

# Delegation.objects.filter(borrower=self.request.user).filter(status__exact='o').order_by('due_back')


class CalendarView(generic.ListView):
    model = Event
    template_name = 'cal/calendar.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        # use today's date for the calendar
        d = get_date(self.request.GET.get('month', None))

        # Instantiate our calendar class with today's year and date
        cal = Calendar(d.year, d.month)

        # Call the formatmonth method, which returns our calendar as a table
        html_cal = cal.formatmonth(withyear=True)
        context['calendar'] = mark_safe(html_cal)
        context['prev_month'] = prev_month(d)
        context['next_month'] = next_month(d)
        return context


def get_date(req_day):
    if req_day:
        year, month = (int(x) for x in req_day.split('-'))
        return date(year, month, day=1)
    return datetime.today()


def prev_month(d):
    first = d.replace(day=1)
    prev_month = first - timedelta(days=1)
    month = 'month=' + str(prev_month.year) + '-' + str(prev_month.month)
    return month


def next_month(d):
    days_in_month = calendar.monthrange(d.year, d.month)[1]
    last = d.replace(day=days_in_month)
    next_month = last + timedelta(days=1)
    month = 'month=' + str(next_month.year) + '-' + str(next_month.month)
    return month


def event(request, event_id=None):
    instance = Event()
    if event_id:
        instance = get_object_or_404(Event, pk=event_id)
    else:
        instance = Event()

    form = EventForm(request.POST or None, instance=instance)
    if request.POST and form.is_valid():
        form.save()
        return HttpResponseRedirect(reverse('cal:calendar'))
    return render(request, 'cal/event.html', {'form': form})
