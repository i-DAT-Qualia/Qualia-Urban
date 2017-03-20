from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.template import Context, loader, RequestContext
from django.template.loader import render_to_string
from django.contrib.auth.models import User
from django.conf import settings
from django.shortcuts import render_to_response, get_object_or_404, redirect
from django.utils import timezone
from django.views.decorators.clickjacking import xframe_options_exempt

from sensors.models import *
from media.models import *
from trees.models import *
from airquality.models import *

import numpy
import datetime
import json

from qualia.tools.decorators import dashboard_level_required


def front_page(request):
    return render_to_response('map/index.html', {
        "devices": Thing.objects.all(),
        "photos": Photo.objects.all(),
        "links": FileLink.objects.all()
    }, context_instance=RequestContext(request))


def tree_map(request):
    return render_to_response('map/trees.html', {
        # "trees": Tree.objects.all(),
    }, context_instance=RequestContext(request))


def aqs_map_mean(request):
    return render_to_response('map/aqs_mean.html', {
        'date': request.GET.get('date')
    }, context_instance=RequestContext(request))

def aqs_map(request, id=None, localid=None):
    if localid:
        return render_to_response('map/aqs.html', {
            "id": get_object_or_404(Device, identifier=localid).id
        }, context_instance=RequestContext(request))
    elif id:
        return render_to_response('map/aqs.html', {
            "id": id
        }, context_instance=RequestContext(request))
    else:
        return render_to_response('map/aqs.html', {
        }, context_instance=RequestContext(request))

@xframe_options_exempt
def aqs_map_widget(request, id=None, localid=None):
    if localid:
        return render_to_response('map/aqs_widget.html', {
            "id": get_object_or_404(Device, identifier=localid).id
        }, context_instance=RequestContext(request))
    elif id:
        return render_to_response('map/aqs_widget.html', {
            "id": id
        }, context_instance=RequestContext(request))
    else:
        return render_to_response('map/aqs_widget.html', {
        }, context_instance=RequestContext(request))

@xframe_options_exempt
def tree_map_widget(request):
    return render_to_response('map/tree_widget.html', {
        # "trees": Tree.objects.all(),
    }, context_instance=RequestContext(request))


def draft_page(request):
    return render_to_response('draft/index.html', {
    }, context_instance=RequestContext(request))


def props_page(request):
    return render_to_response('props/index.html', {
    }, context_instance=RequestContext(request))


@dashboard_level_required
def api_info(request):
    return render_to_response('info/api.html', {
    }, context_instance=RequestContext(request))
