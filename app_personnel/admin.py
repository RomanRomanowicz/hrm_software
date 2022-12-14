from django.contrib import admin
from django.utils.safestring import mark_safe

from app_company.forms import RegisterUserForm
from app_personnel.models import *


class PersonnelDataAdmin(admin.ModelAdmin):
    list_display = ['employee', 'born', 'birth_place']


admin.site.register(PersonnelData, PersonnelDataAdmin)


class EmployeeInline(admin.TabularInline):
    model = Employee
    verbose_name = 'Пользователь'


@admin.register(Personnel)
class PersonnelAdmin(admin.ModelAdmin):
    list_display = ('last_name', 'first_name', 'fathers_name', 'get_html_image', 'is_acceptance')
    list_display_links = ('last_name', 'first_name', 'fathers_name')
    search_fields = ('last_name',)
    prepopulated_fields = {"slug": ("last_name", "first_name")}
    list_editable = ('is_acceptance',)
    list_filter = ('last_name', 'is_acceptance')
    inlines = [EmployeeInline, ]
    # readonly_fields = ('last_name',)

    def get_html_image(self, object):
        if object.image:
            return mark_safe(f"<img src='{object.image.url}' width=50>")
    get_html_image.short_description = "Миниятюра"


@admin.register(Employment)
class EmploymentAdmin(admin.ModelAdmin):
    list_display = ['employee', 'employment_date_beginning', 'employment_date_ending']


@admin.register(Delegation)
class DelegationAdmin(admin.ModelAdmin):
    list_display = ['username', 'cause', 'date_start', 'date_end']
    # fields = ['username', 'cause', ('date_start', 'date_end')]
    list_filter = ('cause',)
    fieldsets = (
        (None, {'fields': ('employee', 'username', 'date_start', 'date_end', 'departure_reason', 'scan_of_documents')}),
        ('Availability', {'fields': ('cause', )},)
    )


@admin.register(Vacation)
class VacationAdmin(admin.ModelAdmin):
    list_display = ['username', 'employee', 'date_start', 'date_end']
    list_filter = ('date_start',)


@admin.register(DailyReport)
class DailyReportAdmin(admin.ModelAdmin):
    list_display = ['username', 'employee', 'date_start', 'date_end']
    # fields = ['username', 'employee', ('date_start', 'date_end')]
    list_filter = ('date_start',)
    fieldsets = (
        (None, {'fields': ('username', 'employee', 'date_start', 'date_end')}),
        ('Ежедневный отчет', {'fields': ('report',)},)
    )


@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ['user', 'employee', 'function', 'departament']
    list_filter = ('employee', 'function', 'departament')
    list_display_links = ('user', 'employee', 'function', 'departament')
