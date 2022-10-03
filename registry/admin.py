from django.contrib import admin

from .models import Hospital, Purchase

from import_export.admin import ImportExportActionModelAdmin
from import_export import resources
from import_export import fields
from import_export.widgets import ForeignKeyWidget

class PurchaseResource(resources.ModelResource):
    hospital = fields.Field(column_name='hospital', attribute='hospital', widget=ForeignKeyWidget(Hospital, 'name'))

    class Meta:
        model = Hospital


class HospitalAdmin (ImportExportActionModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug': ('name',)}


admin.site.register(Hospital, HospitalAdmin)


class PurchaseAdmin(ImportExportActionModelAdmin):
    list_display = ['hospital', 'name', 'price', 'signed', 'returned', 'transferred']
    prepopulated_fields = {'slug': ('name',)}


admin.site.register(Purchase, PurchaseAdmin)





#class PurchaseAdmin(admin.ModelAdmin):
#    list_display = ['hospital', 'name', 'price', 'signed', 'returned', 'transferred']
#    prepopulated_fields = {'slug': ('name',)}

# admin.site.register(Purchase, PurchaseAdmin)

#class HospitalAdmin(admin.ModelAdmin):
#   list_display = ['name', 'slug']
#   prepopulated_fields = {'slug': ('name',)}

#admin.site.register(Hospital, HospitalAdmin)
