from django.contrib import admin

from app_calendar.models import *
from app_personnel.models import *


# @admin.register(DepartamentE)
# class DepartamentEAdmin(admin.ModelAdmin):
#     list_display = ['dep', 'superior', 'function']


admin.site.register(Event)