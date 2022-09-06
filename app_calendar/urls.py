from django.urls import path, include

from .views import *


urlpatterns = [
    path('delegation/', ListDelegationView.as_view(), name='delegation'),
    # path('delegation/', your_delegation, name='delegation'),
    # path('create_delegation/', CreateDelegationView.as_view(), name='create_delegation'),
    # path('update_delegation/', UpdateDelegation.as_view(), name='update_delegation'),
    # path(r'delegation/$', LoanedDelegationUserListView.as_view(), name='delegation')
]

app_name = 'cal'
urlpatterns += [
    path('calendar/', CalendarView.as_view(), name='calendar'),
    path('event/new/', event, name='event_new'),
    path('event/edit/(?P<event_id>\d+)/', event, name='event_edit'),
]
