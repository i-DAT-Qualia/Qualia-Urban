from django.contrib.gis import admin
from models import *

from imagekit.admin import AdminThumbnail

class MetaAdmin(admin.OSMGeoAdmin):
    search_fields = ['id']
    list_display = ('__str__', 'thumbnail', 'gps')
    thumbnail = AdminThumbnail(image_field='thumb')


class LinkAdmin(admin.OSMGeoAdmin):
    search_fields = ['id']

admin.site.register(Photo, MetaAdmin)
admin.site.register(FileLink, LinkAdmin)
