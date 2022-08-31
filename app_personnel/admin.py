from django.contrib import admin

from app_personnel.models import *



admin.site.register(PersonalData)


# @admin.register(Personnel)
class PersonnelAdmin(admin.ModelAdmin):
    list_display = ('id', 'last_name', 'first_name', 'fathers_name')
    list_display_links = ('id', 'last_name', 'first_name', 'fathers_name')
    search_fields = ('last_name',)
    prepopulated_fields = {"slug": ("last_name", "first_name")}


admin.site.register(Personnel, PersonnelAdmin)

# @admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display =['id', 'employee', 'function', 'departament']
    list_display_links = ('id', 'employee', 'function', 'departament')
    search_fields = ('employee',)
    prepopulated_fields = {"slug": ("employee",)}


@admin.register(Employment)
class EmploymentAdmin(admin.ModelAdmin):
    list_display = ['employee', 'employment_date_beginning', 'employment_date_ending']



# @admin.register(Education)
# class EducationAdmin(admin.ModelAdmin):
#     list_display = ['employee', 'education']
#     # list_filter = ['qualifications',]
#     # filter_horizontal = ['qualifications',]
#
#
# @admin.register(Superiors)
# class SuperiorsAdmin(admin.ModelAdmin):
#     list_display = ['departament', 'superior']
#
#
# @admin.register(Assignment)
# class AssignmentAdmin(admin.ModelAdmin):
#     list_display = ['level',]
#
