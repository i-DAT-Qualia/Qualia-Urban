from django.db import models
from django.contrib.gis.db import models
from django.forms import ModelForm
from django.contrib.postgres.fields import ArrayField
from django.conf import settings
import uuid


class SensorMeta(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(db_index=True, max_length=250)
    info = models.TextField(blank=True, null=True)
    added = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    updated = models.DateTimeField(auto_now=True, blank=True, null=True)
    tags = ArrayField(models.CharField(max_length=200), blank=True, null=True)

    class Meta:
        abstract = True


class Thing(SensorMeta):
    owner = models.ForeignKey(settings.AUTH_USER_MODEL)

    def __unicode__(self):
        return self.name

    def location_list(self):
        return Location.objects.filter(thing=self).order_by('-added')

    def last_location(self):
        return Location.objects.filter(thing=self).order_by('added').last()

    def channel_list(self):
        return Channel.objects.filter(thing=self).order_by('-added')


class Channel(SensorMeta):
    thing = models.ForeignKey(Thing)

    def __unicode__(self):
        return self.name

    def reading_list(self):
        return Reading.objects.filter(channel=self).order_by('-added')


class Reading(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    channel = models.ForeignKey(Channel)
    added = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    value = models.FloatField()

    def __unicode__(self):
        return self.channel.name


class Location(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    thing = models.ForeignKey(Thing)
    added = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    gps = models.PointField()
    objects = models.GeoManager()

    def __unicode__(self):
        return self.thing.name
