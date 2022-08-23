from django.contrib import admin
from django.urls import path, include

from app_personnel.views import *


urlpatterns = [
    path('', LoginUser.as_view(), name='login'),
    path('', logout_user, name='logout'),
    path('home/', HomeView.as_view(), name='home'),
    path('personnel/', ListObjectView.as_view(), name='personnel'),
    path('create_employee/', CreateEmployeeView.as_view(), name='create_employee'),
]