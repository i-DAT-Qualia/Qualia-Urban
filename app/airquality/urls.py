from django.conf.urls import include, url

import airquality.views
import dashboard.views

urlpatterns = [
    url(r'^$', dashboard.views.aqs_map),
    url(r'^geojson/', airquality.views.return_geojson),
    #url(r'^embed/', dashboard.views.tree_map_widget),
    #url(r'^(?P<id>[^/]+)/json/', trees.views.return_tree_json),
    #url(r'^(?P<id>[^/]+)/readings/(?P<type>[^/]+)/', trees.views.return_reading_chart),
    #url(r'^(?P<id>[^/]+)/add/photo/', trees.views.add_photo),
    #url(r'^(?P<id>[^/]+)/add/reading/', trees.views.add_reading),
    #url(r'^(?P<id>[^/]+)/add/report/', trees.views.add_report),
    #url(r'^(?P<id>[^/]+)/add/story/', trees.views.add_story),
    #url(r'^add/', trees.views.add_tree),
    #url(r'^(?P<id>[^/]+)/', trees.views.detail),
]
