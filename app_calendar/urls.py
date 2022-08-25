from django.urls import path, include

from . import views
from .views import *

urlpatterns = [
    # path('delegation/', ListDelegationView.as_view(), name='delegation'),
    path('delegation/', views.your_delegation, name='delegation'),
    path('create_delegation/', CreateDelegationView.as_view(), name='create_delegation'),
    path('update_delegation/', UpdateDelegation.as_view(), name='update_delegation'),
    # path(r'delegation/$', LoanedDelegationUserListView.as_view(), name='delegation')
]