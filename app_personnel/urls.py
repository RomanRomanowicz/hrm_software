from django.contrib import admin
from django.urls import path, include

from app_personnel.views import *


urlpatterns = [
    path('home/', HomeView.as_view(), name='home'),
    path('personnel/', ListObjectView.as_view(), name='personnel'),
    path('personnel/<slug:slug>/', PersonnelIdDetail.as_view(), name='human'),
    path('create_personnel/', CreatePersonnel.as_view(), name='create_personnel'),
    path('create_data/', CreatePersonnelData.as_view(), name='create_data'),
    path('add_employment/', CreateEmployment.as_view(), name='add_employment'),
    path('delegation/', your_delegation, name='delegation'),
    # path('create_delegation/', add_delegation, name='create_delegation'),
    path('create_delegation/', CreateDelegation.as_view(), name='create_delegation'),
    path('update_delegation/<int:pk>/', UpdateDelegation.as_view(), name='update_delegation'),
    path('delete_delegation/<int:pk>/', DeleteDelegation.as_view(), name='delete_delegation'),
    path('vacation/', your_vacation, name='vacation'),
    path('create_vacation/', CreateVacation.as_view(), name='create_vacation'),
    path('update_vacation/<int:pk>/', UpdateVacation.as_view(), name='update_vacation'),
    path('delete_vacation/<int:pk>/', DeleteVacation.as_view(), name='delete_vacation'),
    path('daily_report/', your_daily_report, name='daily_report'),
    path('create_daily_report/', CreateDailyReport.as_view(), name='create_daily_report'),
    path('update_daily_report/<int:pk>/', UpdateDailyReport.as_view(), name='update_daily_report'),
    path('delete_daily_report/<int:pk>/', DeleteDailyReport.as_view(), name='delete_daily_report'),
    path('detail_report/<int:pk>/', DetailDailyReport.as_view(), name='detail_report'),
    path('create_employee/', CreateEmployee.as_view(), name='create_employee'),
]

urlpatterns += [
    path('accounts/', include('django.contrib.auth.urls')),
]

# urlpatterns += [
#     path(r'^delegation/$', DelegationUserListView.as_view(), name='my-user'),
# ]