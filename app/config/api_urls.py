from django.conf.urls import patterns, include, url

from sensors.api.resources import *
from documents.api.resources import *
from media.api.resources import *

from tastypie.api import Api

from django.conf import settings

v3_api = Api(api_name='v3')
v3_api.register(ThingList())
v3_api.register(ChannelList())
v3_api.register(ReadingList())
v3_api.register(LocationList())
v3_api.register(DocumentList())
v3_api.register(PhotoList())

urlpatterns = [

    # authentication
    url(r'^v2/auth/', include('provider.oauth2.urls', namespace='oauth2')),
    url(r'^v2/register/', 'accounts.api.register.register_user'),
    url(r'^v2/login/', 'accounts.api.register.login_user'),
    url(r'^v2/logout/', 'accounts.api.register.logout_user'),

    # API Collectors
    url(r'^v3/collector/reading/', 'sensors.api.collectors.collect_reading'),
    url(r'^v3/collector/location/', 'sensors.api.collectors.collect_location'),


    # Tastypie API
    url(r'', include(v3_api.urls)),

    # url(r'/doc/', include('tastypie_swagger.urls', namespace='tastypie_swagger')),


]
