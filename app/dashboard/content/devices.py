from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.template import Context, loader, RequestContext
from django.template.loader import render_to_string
from django.contrib.auth.models import User
from django.conf import settings
from django.shortcuts import render_to_response, get_object_or_404, redirect
from django.utils import timezone

from sensors.models import *

from django.forms import ModelForm

import numpy
import datetime
import json

from qualia.tools.decorators import dashboard_level_required

from leaflet.forms.widgets import LeafletWidget


class LocationUpdateForm(ModelForm):

    class Meta:
        model = Location
        fields = ['gps']

        widgets = {
            'gps': LeafletWidget(),
        }


def can_edit(thing, user):
    if not user.is_anonymous():
        if (user.level >= 4) or (thing.owner == user):
            return True

    return False


@dashboard_level_required
def list(request):
    return render_to_response('content/devices/list.html', {
        'mine': Thing.objects.filter(owner=request.user),
        'all': Thing.objects.all()
    }, context_instance=RequestContext(request))


# @dashboard_level_required
def detail(request, id):
    device = get_object_or_404(Thing, id=id)
    channel = Channel.objects.filter(thing=device).order_by('-added')

    return render_to_response('content/devices/detail.html', {
        'device': device,
        'can_edit': can_edit(device, request.user),
    }, context_instance=RequestContext(request))


@dashboard_level_required
def update_location(request, id):
    device = get_object_or_404(Thing, id=id)
    form = LocationUpdateForm()
    success = False

    if request.method == "POST":
        form = LocationUpdateForm(request.POST)

        if form.is_valid():
            new_item = form.save(commit=False)
            new_item.thing = device
            new_item.save()
            success = True

        if success:
            return redirect('/dashboard/content/devices/'+str(id)+'/')

    return render_to_response('content/devices/update_location.html', {
        'device': device,
        'form': form,
        'success': success
    }, context_instance=RequestContext(request))
