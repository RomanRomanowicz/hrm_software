from django.contrib import admin

from app_calendar.models import *
from app_personnel.models import *


@admin.register(Delegation)
class DelegationAdmin(admin.ModelAdmin):
    list_display = ('employee', 'borrower', 'delegation', 'id')
    list_filter = ('delegation', )
    # fields = (
    #     (None, {'fields': ('employee', 'id')}),
    #     ('Availability', {'fields': ('delegation', 'borrower')})
    # )

# @admin.register(DepartamentE)
# class DepartamentEAdmin(admin.ModelAdmin):
#     list_display = ['dep', 'superior', 'function']
