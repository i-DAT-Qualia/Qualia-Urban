from django.contrib.gis import admin
from models import *

class MetaAdmin(admin.OSMGeoAdmin):
    search_fields = ['name', 'id']

admin.site.register(Dataset)
admin.site.register(Tree, MetaAdmin)
admin.site.register(Org)
admin.site.register(Species)
admin.site.register(Reading)
admin.site.register(Photo)
admin.site.register(Story)
admin.site.register(Report)
