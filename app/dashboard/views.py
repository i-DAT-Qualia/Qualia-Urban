from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.template import Context, loader, RequestContext
from django.template.loader import render_to_string
from django.contrib.auth.models import User
from django.conf import settings
from django.shortcuts import render_to_response, get_object_or_404, redirect
from django.utils import timezone

from sensors.models import *
from media.models import *

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
