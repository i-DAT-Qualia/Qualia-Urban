from django.core.management.base import BaseCommand, CommandError
import json
import requests
import time
from django.contrib.gis.geos import Point

from django.conf import settings
from trees.models import *


class Command(BaseCommand):
    args = ''
    help = 'Imports Tree Data'

    def handle(self, *args, **options):
        print "importing"
        print "ancient trees"

        ancient_data = Dataset(
            name='Ancient Trees Import',
            info='From PCC and Simon\'s tool',
            source='http://odtp.herokuapp.com/?target=ancient_trees.zip&translations=PNT2LL'
        )
        data = requests.get(ancient_data.source)
        ancient_data.data = data.json()
        ancient_data.save()
        #print ancient_data.json()

        for tree in ancient_data.data["features"]:
            species_obj, created = Species.objects.get_or_create(name=tree["properties"]["SPECIES"], data={})
            species_obj.save()

            org_obj, created = Org.objects.get_or_create(name=tree["properties"]["ORGANISATI"], data={})
            org_obj.save()

            new_tree = Tree(
                name=tree["properties"]["TREE_LOCAT"],
                data=tree["properties"],
                dataset=ancient_data,
                age=tree["properties"]["AGE_ESTIMA"],
                species=species_obj,
                org=org_obj,
                info=str(tree["properties"]["COMMENTS_O"]) + '\n' + str(tree["properties"]["TREE_PUBLI"]) + '\n\n' + str(tree["properties"]["STANDING_O"]) + '\n' + str(tree["properties"]["LIVING_STA"]) + '\n' + str(tree["properties"]["TREE_CONDI"]),
                gps=Point(tree["geometry"]["coordinates"][0][0], tree["geometry"]["coordinates"][0][1])
            )
            new_tree.save()

        print "importing"
        print "pear trees"

        pear_data = Dataset(
            name='Plymouth Pears Import',
            info='From PCC and Simon\'s tool',
            source='http://odtp.herokuapp.com/?target=plymouth_pear.zip&translations=PNT2LL'
        )
        data = requests.get(pear_data.source)
        pear_data.data = data.json()
        pear_data.save()

        species_obj, created = Species.objects.get_or_create(name="Plymouth Pear", data={})
        species_obj.save()

        org_obj, created = Org.objects.get_or_create(name="Plymouth City Council", data={})
        org_obj.save()

        for pear in pear_data.data["features"]:
            for loc in pear["geometry"]["coordinates"]:
                new_tree = Tree(
                    name=pear["properties"]["LOCATION"],
                    data=pear["properties"],
                    dataset=pear_data,
                    species=species_obj,
                    org=org_obj,
                    info=str(pear["properties"]["NOTES"]),
                    gps=Point(loc[0], loc[1])
                )
                new_tree.save()
