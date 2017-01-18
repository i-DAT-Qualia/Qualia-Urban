from django.contrib.gis import admin
from models import *

class MetaAdmin(admin.OSMGeoAdmin):
    search_fields = ['name', 'id']

admin.site.register(Device)
admin.site.register(Reading, MetaAdmin)
