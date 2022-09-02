from django.urls import path, include
from .views import *

urlpatterns = [
    path('', LoginUser.as_view(), name='login'),
    path('', logout_user, name='logout'),
    path('register/', RegisterUser.as_view(), name='register'),
    path('structure/', DepartamentView.as_view(), name='structure'),
    # path('employee_list/', employee_list, name='employee_list'),
    path('function_group/', function_group, name='function_group'),
    # path('add_group/add/', function_group_add, name='add_group_add'),
    path('create_structure/', CreateDepartament.as_view(), name='create_structure'),
    # path('create_function/', CreateFunctionView.as_view(), name='create_function'),
    path('update_departament/<int:pk>/', UpdateDepartament.as_view(), name='update_departament'),
    # path('update_function/<int:pk>', UpdateFunctionView.as_view(), name='update_function'),
    path('delete_structure/<int:pk>/', DeleteDepartament.as_view(), name='delete_structure'),
    # path('delete_function/<int:pk>', DeleteFunctionView.as_view(), name='delete_function'),

    # path('qualifications/', ListQualificationView.as_view(), name='qualifications'),
    # path('vacation/', ListVacationView.as_view(), name='vacation'),
    # path('create_qualifications/', CreateQualificationsView.as_view(), name='create_qualifications'),
    # path('create_vacation/', CreateVacationView.as_view(), name='create_vacation'),
    # path('update_vacation/<int:pk>', UpdateVacationView.as_view(), name='update_vacation'),
    # path('update_qualifications/<int:pk>', UpdateQualificationView.as_view(), name='update_qualifications'),
    # path('delete_qualifications/<int:pk>', DeleteQualificationView.as_view(), name='delete_qualifications'),
    # path('delete_vacation/<int:pk>', DeleteVacationView.as_view(), name='delete_vacation'),
]