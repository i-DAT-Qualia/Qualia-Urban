from django.conf.urls import include, url

urlpatterns = [

    url(r'content/devices/(?P<id>[^/]+)/location', 'dashboard.content.devices.update_location'),
    url(r'content/devices/(?P<id>[^/]+)/', 'dashboard.content.devices.detail'),
    url(r'content/devices/', 'dashboard.content.devices.list'),

    url(r'information/api/', 'dashboard.views.api_info'),


]
