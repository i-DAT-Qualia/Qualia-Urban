from django.shortcuts import render, get_object_or_404, render_to_response, redirect
from models import *

from django.http import JsonResponse
from django.contrib.gis.geos import Point

from django.template import Context, loader, RequestContext

import datetime
import json
import numpy

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
                "coordinates": [reading.gps.x, reading.gps.y]
            }
        })

    return JsonResponse(response, safe=False)


def return_geojson_mean(request):
    date = datetime.datetime.strptime(request.GET.get('date'), '%Y-%m-%d').date()
    analyses = Analysis.objects.all()

    response = {
        "type": "FeatureCollection",
        "features": []
    }

    for analysis in analyses:
        readings = Reading.objects.filter(
            added__date=date,
            gps__within=analysis.poly
        )

        pm10count = []
        pm10con = []
        pm2point5count = []
        pm2point5con = []

        for reading in readings:
            pm10count.append(reading.pm10count)
            pm10con.append(reading.pm10con)
            pm2point5count.append(reading.pm2point5count)
            pm2point5con.append(reading.pm2point5con)

        response["features"].append({
            "type": "Feature",
            "properties": {
                "description": 'average',
                "icon": "reading",
                "id": analysis.id,
                "pm10count": numpy.mean(pm10count),
                "pm10con": numpy.mean(pm10con),
                "pm2point5count": numpy.mean(pm2point5count),
                "pm2point5con": numpy.mean(pm2point5con),
            },
            "geometry": json.loads(analysis.poly.json) # bit of a hack
        })

    return JsonResponse(response, safe=False)
