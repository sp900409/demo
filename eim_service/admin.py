from django.contrib import admin
from eim_service.models import KcsInfo, UnitInfo


# admin.site.register(UnitInfo)

# class KcsInfoInline(admin.TabularInline):
#     model = KcsInfo
#
# class MyModelAdmin(admin.ModelAdmin):
#     inlines = [UnitInfo]
#     fk_name = 'create_unit'

admin.site.register(KcsInfo)
admin.site.register(UnitInfo)
