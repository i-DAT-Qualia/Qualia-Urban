from sensors.models import *
from django import forms
import json

from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods

from django.http import JsonResponse


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


@require_http_methods(["POST"])
@csrf_exempt
def collect_reading(request):
    return JsonResponse(process_reading(json.loads(request.body)), safe=False)
