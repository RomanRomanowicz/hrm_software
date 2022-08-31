from django.contrib import admin
from django.contrib.auth.models import Permission
from app_company.models import *


admin.site.register(Permission)

@admin.register(OrgStructure)
class OrgStructureAdmin(admin.ModelAdmin):
    list_display = ('departament', )


@admin.register(Function)
class FunctionAdmin(admin.ModelAdmin):
    list_display = ('function', )


# @admin.register(Qualifications)
# class QualificationsAdmin(admin.ModelAdmin):
#     list_display = ('qualifications', )
#
#
# @admin.register(Vacation)
# class VacationAdmin(admin.ModelAdmin):
#     list_display = ['function', 'vacation_limit', 'remote_work_limit']


# @admin.register(Delegation)
# class DelegationAdmin(admin.ModelAdmin):
#     list_display = ['function', 'delegation', 'limit_journey', 'limit_hotel', 'limit_payment_on_account']