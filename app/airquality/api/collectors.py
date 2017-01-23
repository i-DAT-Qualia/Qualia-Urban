from airquality.models import *
from django import forms
import json
import datetime

from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods

from django.http import JsonResponse
from django.contrib.gis.geos import Point


def process_reading(data):
    response = {
        "success": False,
        "message": ""
    }

    print data["reading"]["pm10"]["count"]

    try:
        device, created = Device.objects.get_or_create(identifier=data["uuid"])
        device.save()
        reading = Reading(
            device=device,
            pm10count=data["reading"]["pm10"]["count"],
            pm10con=data["reading"]["pm10"]["concentration"],
            pm2point5count=data["reading"]["pm2point5"]["count"],
            pm2point5con=data["reading"]["pm2point5"]["concentration"],
            gps=Point(data["location"]["longitude"], data["location"]["latitude"]),
            data=data
        )
        reading.save()
        response['success'] = True
    # this is horrible. Don't do this. I made a puppy sad.
    except Exception as e:
        response['message'] = str(e)

    return response


@require_http_methods(["POST"])
@csrf_exempt
def collect_reading(request):
    return JsonResponse(process_reading(json.loads(request.body)), safe=False)
