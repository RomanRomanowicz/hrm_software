from django.contrib import admin
from django.contrib.auth.models import Permission
from app_company.models import *


admin.site.register(Permission)

@admin.register(Departament)
class DepartamentAdmin(admin.ModelAdmin):
    list_display = ('departament', )