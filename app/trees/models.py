from __future__ import unicode_literals

from django.db import models
from django.contrib.gis.db import models
from django.contrib.postgres.fields import ArrayField
from django.contrib.postgres.fields import JSONField
import uuid

from qualia.tools.uploads import get_image_path

from imagekit.models import ImageSpecField
from imagekit.processors import Thumbnail, ResizeToFit



class TreesMeta(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(blank=True, null=True, max_length=250)
    info = models.TextField(blank=True, null=True)
    added = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    updated = models.DateTimeField(auto_now=True, blank=True, null=True)
    tags = ArrayField(models.CharField(max_length=200), blank=True, null=True)
    data = JSONField()

    class Meta:
        abstract = True


class Dataset(TreesMeta):
    source = models.URLField()

    def __unicode__(self):
        return self.name


class Species(TreesMeta):
    more_info = models.URLField(blank=True, null=True)

    '''
    common_name
    botanical_name
    variety
    '''

    def __unicode__(self):
        return self.name

class Org(TreesMeta):
    more_info = models.URLField(blank=True, null=True)

    def __unicode__(self):
        return self.name

class Tree(TreesMeta):
    dataset = models.ForeignKey(Dataset, blank=True, null=True)
    species = models.ForeignKey(Species, blank=True, null=True)
    org = models.ForeignKey(Org, blank=True, null=True)
    age = models.CharField(blank=True, null=True, max_length=250)

    gps = models.PointField()
    objects = models.GeoManager()

    def __unicode__(self):
        return self.name


class DataPoint(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    tree = models.ForeignKey(Tree)

    added = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    updated = models.DateTimeField(auto_now=True, blank=True, null=True)
    recorded = models.DateTimeField()

    author = models.CharField(blank=True, null=True, max_length=250, default="Anon.")

    class Meta:
        abstract = True


class Reading(DataPoint):
    type_choices = (
        ('A', 'Height of Tree'),
        ('B', 'Spread of Crown'),
        ('C', 'Diameter at Breast Height'),
        ('D', 'Clear Stem Height'),
        ('O', 'Other'),
    )

    type = models.CharField(
        default='O',
        choices=type_choices,
        max_length=1
    )

    value = models.FloatField()

    def __unicode__(self):
        return self.tree.name


class Photo(DataPoint):
    image = models.ImageField(upload_to=get_image_path, blank=True, null=True)
    large = ImageSpecField(
        source='image',
        processors=[Thumbnail(width=640, height=440, upscale=True)],
        format='JPEG',
        options={'quality': 100}
    )
    thumb = ImageSpecField(
        source='image',
        processors=[Thumbnail(width=320, height=220, upscale=True)],
        format='JPEG',
        options={'quality': 100}
    )

    def __unicode__(self):
        return self.tree.name


class Story(DataPoint):
    info = models.TextField(blank=True, null=True)

    def __unicode__(self):
        return self.tree.name


class Report(DataPoint):
    type_choices = (
        ('A', 'Site History'),
        ('B', 'Form'),
        ('C', 'Condition'),
        ('D', 'Nearby Obstructions'),
        ('E', 'Past Management'),
        ('F', 'Recommendations'),
        ('O', 'Other'),
    )

    type = models.CharField(
        default='O',
        choices=type_choices,
        max_length=1
    )

    info = models.TextField(blank=True, null=True)

    def __unicode__(self):
        return self.tree.name



'''
class TreesMeta:

class Tree:
    ptp_number

    common_name
    botanical_name
    variety

    year_planted
    date_planted

class conservationArea:

class Status:


class Owner:
    tree

class PreservationOrder:
    tree

class Inspector:
class Inspection:
'''
