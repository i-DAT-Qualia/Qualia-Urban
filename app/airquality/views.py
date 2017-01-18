from django.shortcuts import render, get_object_or_404, render_to_response, redirect
from models import *

from django.http import JsonResponse
from django.contrib.gis.geos import Point

from django.template import Context, loader, RequestContext

import json
#from forms import *

from django.conf import settings


def return_geojson(request):
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
                "id": reading.id
            },
            "geometry": {
                "type": "Point",
                "coordinates": [reading.gps.x,reading.gps.y]
            }
        })

    return JsonResponse(response, safe=False)
