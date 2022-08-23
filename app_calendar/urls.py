from django.urls import path, include
from .views import *

urlpatterns = [
    # path('delegation/', ListDelegationView.as_view(), name='delegation'),
    path(r'delegation/$', LoanedDelegationUserListView.as_view(), name='delegation')
]