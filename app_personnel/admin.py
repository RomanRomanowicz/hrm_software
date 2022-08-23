from django.contrib import admin

from app_personnel.models import *


@admin.register(Personnel)
class PersonnelAdmin(admin.ModelAdmin):
    list_display = ['last_name', 'first_name', 'fathers_name']


@admin.register(Employment)
class EmploymentAdmin(admin.ModelAdmin):
    list_display = ['employee', 'employment_date_beginning', 'employment_date_ending']


@admin.register(Education)
class EducationAdmin(admin.ModelAdmin):
    list_display = ['employee', 'education']
    # list_filter = ['qualifications',]
    # filter_horizontal = ['qualifications',]


@admin.register(Superiors)
class SuperiorsAdmin(admin.ModelAdmin):
    list_display = ['departament', 'superior']


@admin.register(Assignment)
class AssignmentAdmin(admin.ModelAdmin):
    list_display = ['level',]

