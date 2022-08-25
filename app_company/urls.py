from django.urls import path, include
from .views import *

urlpatterns = [
    path('', ListObjectView.as_view(), name='structure'),
    path('function/', ListFunctionView.as_view(), name='function'),
    path('create_structure/', CreateOrgView.as_view(), name='create_structure'),
    path('create_function/', CreateFunctionView.as_view(), name='create_function'),
    path('update_structure/<int:pk>', UpdateOrgView.as_view(), name='update_structure'),
    path('update_function/<int:pk>', UpdateFunctionView.as_view(), name='update_function'),
    path('delete_structure/<int:pk>', DeleteOrganizationView.as_view(), name='delete_structure'),
    path('delete_function/<int:pk>', DeleteFunctionView.as_view(), name='delete_function'),

    # path('qualifications/', ListQualificationView.as_view(), name='qualifications'),
    # path('vacation/', ListVacationView.as_view(), name='vacation'),
    # path('create_qualifications/', CreateQualificationsView.as_view(), name='create_qualifications'),
    # path('create_vacation/', CreateVacationView.as_view(), name='create_vacation'),
    # path('update_vacation/<int:pk>', UpdateVacationView.as_view(), name='update_vacation'),
    # path('update_qualifications/<int:pk>', UpdateQualificationView.as_view(), name='update_qualifications'),
    # path('delete_qualifications/<int:pk>', DeleteQualificationView.as_view(), name='delete_qualifications'),
    # path('delete_vacation/<int:pk>', DeleteVacationView.as_view(), name='delete_vacation'),
]