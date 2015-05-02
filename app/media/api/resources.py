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

from media.models import *


class PhotoList(ModelResource):

    large = fields.FileField('large')
    thumb = fields.FileField('thumb')

    class Meta:
        queryset = Photo.objects.all()
        resource_name = 'photo'
        allowed_methods = ['get']
        authentication = KeyOnlyAuthentication()
        authorization = DjangoAuthorization()
        always_return_data = True
        detail_uri_name = 'id'

        filtering = {
            'tag': ALL,
        }

    def dehydrate_tags(self, bundle):
        return bundle.obj.tags


class FileLinkList(ModelResource):

    class Meta:
        queryset = FileLink.objects.all()
        resource_name = 'file'
        allowed_methods = ['get']
        authentication = KeyOnlyAuthentication()
        authorization = DjangoAuthorization()
        always_return_data = True
        detail_uri_name = 'id'

        filtering = {
            'tag': ALL,
        }

    def dehydrate_tags(self, bundle):
        return bundle.obj.tags
