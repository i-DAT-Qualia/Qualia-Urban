from django.shortcuts import render, get_object_or_404, render_to_response, redirect
from models import *

from django.http import JsonResponse
from django.contrib.gis.geos import Point

from django.template import Context, loader, RequestContext

import json
from forms import *

from django.conf import settings



def detail(request, id):
    tree = get_object_or_404(Tree, id=id)
    photos = Photo.objects.filter(tree=tree)
    reports = Report.objects.filter(tree=tree)
    stories = Story.objects.filter(tree=tree)

    return render_to_response('trees/detail.html', {
        'tree': tree,
        'photos': photos,
        'reports': reports,
        'stories': stories,
    }, context_instance=RequestContext(request))


def add_photo(request, id):
    photo_form = PhotoForm()
    tree = get_object_or_404(Tree, id=id)
    success = False

    if request.method == "POST":
        photo_form = PhotoForm(request.POST, request.FILES)
        if photo_form.is_valid():
            item = photo_form.save(commit=False)
            item.tree = tree
            item.save()
            success = True

    if success:
        return redirect('/trees/' + id + '/')

    return render_to_response('trees/add/photo.html', {
        'form': photo_form,
        'success': success,
        'tree': tree,
    }, context_instance=RequestContext(request))


def add_reading(request, id):
    reading_form = ReadingForm()
    tree = get_object_or_404(Tree, id=id)
    success = False

    if request.method == "POST":
        reading_form = ReadingForm(request.POST)
        if reading_form.is_valid():
            item = reading_form.save(commit=False)
            item.tree = tree
            item.save()
            success = True

    if success:
        return redirect('/trees/' + id + '/')

    return render_to_response('trees/add/reading.html', {
        'form': reading_form,
        'success': success,
        'tree': tree,
    }, context_instance=RequestContext(request))


def add_report(request, id):
    report_form = ReportForm()
    tree = get_object_or_404(Tree, id=id)
    success = False

    if request.method == "POST":
        report_form = ReportForm(request.POST)
        if report_form.is_valid():
            item = report_form.save(commit=False)
            item.tree = tree
            item.save()
            success = True

    if success:
        return redirect('/trees/' + id + '/')

    return render_to_response('trees/add/report.html', {
        'form': report_form,
        'success': success,
        'tree': tree,
    }, context_instance=RequestContext(request))


def add_story(request, id):
    story_form = StoryForm()
    tree = get_object_or_404(Tree, id=id)
    success = False

    if request.method == "POST":
        story_form = StoryForm(request.POST)
        if story_form.is_valid():
            item = story_form.save(commit=False)
            item.tree = tree
            item.save()
            success = True

    if success:
        return redirect('/trees/' + id + '/')

    return render_to_response('trees/add/story.html', {
        'form': story_form,
        'success': success,
        'tree': tree,
    }, context_instance=RequestContext(request))

def add_tree(request):
    tree_form = TreeForm()
    success = False

    id = None

    if request.method == "POST":
        tree_form = TreeForm(request.POST)
        if tree_form.is_valid():
            item = tree_form.save(commit=False)
            item.save()
            id = item.id
            success = True

    if success:
        return redirect('/trees/' + str(id) + '/')

    return render_to_response('trees/add/tree.html', {
        'form': tree_form,
        'success': success,
    }, context_instance=RequestContext(request))


def return_reading_chart(request, id, type):
    tree = get_object_or_404(Tree, id=id)
    readings = Reading.objects.filter(tree=tree,type=type).order_by("added")

    return_list = {
        'x': [],
        'Value': [],
    }

    for reading in readings:
        return_list['x'].append(reading.added.strftime("%Y-%m-%d %H:%M:%S"))
        return_list['Value'].append(reading.value)

    return JsonResponse(return_list, safe=False)


def return_geojson(request):
    trees = Tree.objects.all()

    response = {
        "type": "FeatureCollection",
        "features": []
    }

    for tree in trees:
        response["features"].append({
            "type":"Feature",
            "properties": {
                "description": '<a href="'+tree.name+'"><h3>'+tree.name+'</h3></a>',
                "icon": "tree",
                "id": tree.id
            },
            "geometry": {
                "type": "Point",
                "coordinates": [tree.gps.x,tree.gps.y]
            }
        })

    return JsonResponse(response, safe=False)


def return_tree_json(request, id):
    tree = get_object_or_404(Tree, id=id)
    photos = Photo.objects.filter(tree=tree).order_by("added")

    photo = None

    if photos:
        photo = photos[0].image.url

    '''if not tree.org:
        tree.org.id = None
        tree.org.name = None
    '''

    return JsonResponse({
        "id": tree.id,
        "name": tree.name,
        "info": tree.info,
        "added": tree.added,
        "updated": tree.updated,
        "data": tree.data,
        "org": {
            "id": tree.org.id,
            "name": tree.org.name,
        },
        "dataset": {
            "id": tree.dataset.id,
            "name": tree.dataset.name,
        },
        "species": {
            "id": tree.species.id,
            "name": tree.species.name,
        },
        "age": tree.age,
        "geometry": {
            "type": "Point",
            "coordinates": [tree.gps.x,tree.gps.y]
        },
        "photo": photo
    }, safe=False)
