from django.contrib.gis import admin
from models import *


class MetaAdmin(admin.OSMGeoAdmin):
    search_fields = ['name', 'id']

admin.site.register(Location, MetaAdmin)
admin.site.register(Thing)
admin.site.register(Channel)
admin.site.register(Reading)
