from tastypie.resources import ModelResource
from tastypie.contrib.gis.resources import ModelResource
from tastypie import fields
from tastypie import utils
from tastypie.authentication import ApiKeyAuthentication
from tastypie.authorization import DjangoAuthorization
from tastypie.validation import Validation, FormValidation
from tastypie.constants import ALL, ALL_WITH_RELATIONS
from django import forms
from django.forms import ModelForm
from datetime import datetime, timedelta
from django.db.models import Q
from tastypie.serializers import Serializer
from django.utils.timezone import is_naive

from qualia.tools.api import *

from sensors.models import *


class ThingList(ModelResource):

    channels = fields.ToManyField('sensors.api.resources.ChannelList', 'channel_set', full=True, null=True)
    location = fields.ToManyField('sensors.api.resources.LocationList', 'location_set', full=True, null=True)

    class Meta:
        queryset = Thing.objects.all()
        resource_name = 'thing'
        allowed_methods = ['get']
        authentication = KeyOnlyAuthentication()
        authorization = DjangoAuthorization()
        always_return_data = True
        detail_uri_name = 'id'

        filtering = {
            'name': ALL,
        }

    def dehydrate_tags(self, bundle):
        return bundle.obj.tags


class ChannelList(ModelResource):

    readings = fields.ToManyField('sensors.api.resources.ReadingList', 'reading_set', full=True, null=True)

    class Meta:
        queryset = Channel.objects.all()
        resource_name = 'channel'
        allowed_methods = ['get']
        authentication = KeyOnlyAuthentication()
        authorization = DjangoAuthorization()
        always_return_data = True
        detail_uri_name = 'id'

        filtering = {
            'name': ALL,
        }

    def dehydrate_tags(self, bundle):
        return bundle.obj.tags


class ReadingList(ModelResource):

    class Meta:
        queryset = Reading.objects.all()
        resource_name = 'reading'
        allowed_methods = ['get']
        authentication = KeyOnlyAuthentication()
        authorization = DjangoAuthorization()
        always_return_data = True
        detail_uri_name = 'id'

        filtering = {
            'name': ALL,
        }


class LocationList(ModelResource):

    class Meta:
        queryset = Location.objects.all()
        resource_name = 'location'
        allowed_methods = ['get']
        authentication = KeyOnlyAuthentication()
        authorization = DjangoAuthorization()
        always_return_data = True
        detail_uri_name = 'id'

        filtering = {
            'name': ALL,
        }
