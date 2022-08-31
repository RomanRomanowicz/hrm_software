from django.contrib import admin
from django.urls import path, include

from app_personnel.views import *


urlpatterns = [
    path('', LoginUser.as_view(), name='login'),
    path('', logout_user, name='logout'),
    path('register/', RegisterUser.as_view(), name='register'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('home/', HomeView.as_view(), name='home'),
    path('personnel/', ListObjectView.as_view(), name='personnel'),
    path('personnel/<slug:slug>/', PersonnelIdDetail.as_view(), name='human'),
    # path('personnel_id/<int:personnel_id_id>/', personnel_id_view, name='personnel_id'),
    path('create_personnel/', CreatePersonnelView.as_view(), name='create_personnel'),
    path('create_employee/', CreateEmployeeView.as_view(), name='create_employee'),
    path('create_employment/', CreateEmploymentView.as_view(), name='create_employment'),
]