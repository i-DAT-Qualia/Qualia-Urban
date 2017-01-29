from django.shortcuts import render, get_object_or_404, render_to_response, redirect
from models import *

from django.http import JsonResponse
from django.contrib.gis.geos import Point

from django.template import Context, loader, RequestContext

import json
#from forms import *

from django.conf import settings


def return_geojson(request, id=None, localid=None):
    readings = None

    if localid:
        device = get_object_or_404(Device, identifier=localid)
        readings = Reading.objects.filter(device=device)
    elif id:
        device = get_object_or_404(Device, id=id)
        readings = Reading.objects.filter(device=device)
    else:
        readings = Reading.objects.all()

    response = {
        "type": "FeatureCollection",
        "features": []
    }

    for reading in readings:
        response["features"].append({
            "type":"Feature",
            "properties": {
                "description": 'reading',
                "icon": "reading",
                "id": reading.id,
                "pm10count": reading.pm10count,
                "pm10con": reading.pm10con,
                "pm2point5count": reading.pm2point5count,
                "pm2point5con": reading.pm2point5con,
            },
            "geometry": {
                "type": "Point",
                "coordinates": [reading.gps.x,reading.gps.y]
            }
        })

    return JsonResponse(response, safe=False)
