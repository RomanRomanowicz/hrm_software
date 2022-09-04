from django.contrib import admin
from django.urls import path, include

from app_personnel.views import *


urlpatterns = [
    path('accounts/', include('django.contrib.auth.urls')),
    path('home/', HomeView.as_view(), name='home'),
    path('personnel/', ListObjectView.as_view(), name='personnel'),
    path('personnel/<slug:slug>/', PersonnelIdDetail.as_view(), name='human'),
    path('create_personnel/', CreatePersonnel.as_view(), name='create_personnel'),
    path('create_personnel_data/', CreatePersonalData.as_view(), name='create_personnel_data'),
    path('add_employment/', CreateEmployment.as_view(), name='add_employment'),
]