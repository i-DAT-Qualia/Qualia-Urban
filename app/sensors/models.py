from django.db import models
from django.contrib.gis.db import models
from django.forms import ModelForm
from django.contrib.postgres.fields import ArrayField
from django.conf import settings


class SensorMeta(models.Model):
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


class Channel(SensorMeta):
    thing = models.ForeignKey(Thing)

    def __unicode__(self):
        return self.name


class Reading(models.Model):
    channel = models.ForeignKey(Channel)
    added = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    value = models.FloatField()

    def __unicode__(self):
        return self.channel.name


class Location(models.Model):
    thing = models.ForeignKey(Thing)
    added = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    gps = models.PointField()
    objects = models.GeoManager()

    def __unicode__(self):
        return self.thing.name
