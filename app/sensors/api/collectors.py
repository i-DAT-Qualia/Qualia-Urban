from sensors.models import *
from django import forms
import json

from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods

from django.http import JsonResponse
from django.contrib.gis.geos import Point

class ReadingForm(forms.ModelForm):
    channel_uuid = forms.UUIDField()
    # reading = forms.FloatField()
    api_key = forms.CharField()
    # added = forms.DateTimeField()

    class Meta:
        model = Reading
        fields = ['value']


def process_reading(data):
    response = {
        "success": False,
        "message": ""
    }

    form = ReadingForm(data)

    if form.is_valid():
        new_item = form.save(commit=False)
        new_item.channel = Channel.objects.get(id=form.cleaned_data['channel_uuid'])
        new_item.save()
        response['success'] = True

    return response


def process_location(data):
    response = {
        "success": False,
        "message": ""
    }
    try:
        loaded_data = json.loads(data)
        new_item = Location()
        new_item.thing = Thing.objects.get(id=loaded_data['device_uuid'])
        new_item.gps = Point(loaded_data['longitude'], loaded_data['latitude'])
        new_item.save()
        response['success'] = True

    # this is horrible. Don't do this. I made a puppy sad.
    except Exception as e:
        response['message'] = str(e)

    return response


@require_http_methods(["POST"])
@csrf_exempt
def collect_reading(request):
    return JsonResponse(process_reading(json.loads(request.body)), safe=False)


@require_http_methods(["POST"])
@csrf_exempt
def collect_location(request):
    return JsonResponse(process_location(request.body), safe=False)
