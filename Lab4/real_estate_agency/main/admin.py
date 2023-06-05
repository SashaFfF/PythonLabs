from django.contrib import admin
from .models import *

class RealEstateAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'area')
    list_display_links = ('id', 'title')
    search_fields = ('title',)
    list_filter = ('type', 'service_type')

admin.site.register(PropertyType)
admin.site.register(ServiceType)
admin.site.register(RealEstate, RealEstateAdmin)
admin.site.register(Client)
admin.site.register(Owner)
admin.site.register(Employee)
admin.site.register(Deal)


