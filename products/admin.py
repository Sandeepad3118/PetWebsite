from django.contrib import admin
from .models import *
from django.contrib import admin
from import_export.admin import ImportExportModelAdmin

admin.site.register(Profile)

admin.site.register(Signup)

class ViewAdmin(ImportExportModelAdmin):
    pass
