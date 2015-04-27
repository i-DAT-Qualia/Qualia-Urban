from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.template import Context, loader, RequestContext
from django.template.loader import render_to_string
from django.contrib.auth.models import User
from django.conf import settings
from django.shortcuts import render_to_response, get_object_or_404, redirect
from django.utils import timezone

from sensors.models import *

import numpy
import datetime
import json

from qualia.tools.decorators import dashboard_level_required


def can_edit(thing, user):
    if (user.level >= 4) or (thing.owner == user):
        return True
    else:
        return False


@dashboard_level_required
def list(request):
    return render_to_response('content/devices/list.html', {
        'mine': Thing.objects.filter(owner=request.user),
        'all': Thing.objects.all()
    }, context_instance=RequestContext(request))


@dashboard_level_required
def detail(request, id):
    device = get_object_or_404(Thing, id=id)
    #loc = Location.objects.filter(thing=device).order_by('-added')
    channel = Channel.objects.filter(thing=device).order_by('-added')
    #lastloc = loc.last()

    return render_to_response('content/devices/detail.html', {
        'device': device,
        #'lastloc': device.last_location(),
        #'loc': device.location_list(),
        'can_edit': can_edit(device, request.user),
    }, context_instance=RequestContext(request))
