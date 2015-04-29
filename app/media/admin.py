from django.contrib.gis import admin
from models import *


class MetaAdmin(admin.OSMGeoAdmin):
    search_fields = ['id']

admin.site.register(Photo, MetaAdmin)
