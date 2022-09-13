from django.urls import path, include

from .views import *


app_name = 'cal'
urlpatterns = [
    path('calendar/', CalendarView.as_view(), name='calendar'),
    path('event/new/', event, name='event_new'),
    path('event/edit/(?P<event_id>\d+)/', event, name='event_edit'),
]
