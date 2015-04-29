from django.http import HttpResponse, HttpResponseRedirect
from django.template import Context, loader, RequestContext
from django.template.loader import render_to_string
from django.contrib.auth.models import User
from django.conf import settings
from django.shortcuts import render_to_response, get_object_or_404, redirect
from django.utils import timezone

from qualia.tools.decorators import dashboard_level_required

from leaflet.forms.widgets import LeafletWidget

from media.models import *

import numpy
import datetime
import json

from PIL import Image
from PIL.ExifTags import TAGS, GPSTAGS

from django.contrib.gis.geos import Point


class PhotoForm(ModelForm):

    class Meta:
        model = Photo
        fields = ['tags', 'image']

        widgets = {
        }

# based on example: http://eran.sandler.co.il/2011/05/20/extract-gps-latitude-and-longitude-data-from-exif-using-python-imaging-library-pil/


def get_gps(f):
    gps_data = {}
    i = Image.open(f)
    info = i._getexif()
    for tag, value in info.items():
        decoded = TAGS.get(tag, tag)
        if decoded == "GPSInfo":
            for t in value:
                sub_decoded = GPSTAGS.get(t, t)
                gps_data[sub_decoded] = value[t]
    return gps_data


def _get_if_exist(data, key):
    if key in data:
        return data[key]

    return None


def _convert_to_degress(value):
    d0 = value[0][0]
    d1 = value[0][1]
    d = float(d0) / float(d1)

    m0 = value[1][0]
    m1 = value[1][1]
    m = float(m0) / float(m1)

    s0 = value[2][0]
    s1 = value[2][1]
    s = float(s0) / float(s1)

    return d + (m / 60.0) + (s / 3600.0)


def get_lat_lon(gps_info):
    lat = None
    lon = None

    if gps_info:
        gps_latitude = _get_if_exist(gps_info, "GPSLatitude")
        gps_latitude_ref = _get_if_exist(gps_info, 'GPSLatitudeRef')
        gps_longitude = _get_if_exist(gps_info, 'GPSLongitude')
        gps_longitude_ref = _get_if_exist(gps_info, 'GPSLongitudeRef')

        if gps_latitude and gps_latitude_ref and gps_longitude and gps_longitude_ref:
            lat = _convert_to_degress(gps_latitude)
            if gps_latitude_ref != "N":
                lat = 0 - lat

            lon = _convert_to_degress(gps_longitude)
            if gps_longitude_ref != "E":
                lon = 0 - lon

    return Point(lon, lat)


def success(request):
    return render_to_response('media/photos/success.html', {
    }, context_instance=RequestContext(request))


def upload(request):
    photo_form = PhotoForm()
    success = False

    if request.method == "POST":
        photo_form = PhotoForm(request.POST, request.FILES)
        if photo_form.is_valid():
            item = photo_form.save(commit=False)
            item.gps = get_lat_lon(get_gps(request.FILES['image']))
            item.save()
            success = True

    if success:
        return redirect('/dashboard/media/photos/success/')

    return render_to_response('media/photos/add.html', {
        'form': photo_form,
        'success': success,
    }, context_instance=RequestContext(request))
