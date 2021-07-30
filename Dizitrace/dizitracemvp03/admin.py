from import_export.admin import ImportExportModelAdmin
from django.contrib import admin
from .models import bulkdata

@admin.register(bulkdata)
class PersonAdmin(ImportExportModelAdmin):
    list_display = ('product_name', 'manufacturer_name', 'product_group')
