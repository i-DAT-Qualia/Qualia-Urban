from django.shortcuts import render
from models import *

from django.http import JsonResponse
from django.contrib.gis.geos import Point

from django.shortcuts import get_object_or_404

import json

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
        }
    }, safe=False)
