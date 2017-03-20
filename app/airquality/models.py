from __future__ import unicode_literals

from django.db import models
from django.contrib.gis.db import models
from django.contrib.postgres.fields import ArrayField
from django.contrib.postgres.fields import JSONField
import uuid

from django.db.models.signals import post_save
from django.dispatch import receiver

import pusher



class AirQualMeta(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    info = models.TextField(blank=True, null=True)
    added = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    updated = models.DateTimeField(auto_now=True, blank=True, null=True)
    tags = ArrayField(models.CharField(max_length=200), blank=True, null=True)
    data = JSONField(blank=True, null=True)

    class Meta:
        abstract = True


class Device(AirQualMeta):
    identifier = models.CharField(max_length=250)

    def __unicode__(self):
        return self.identifier


class Reading(AirQualMeta):
    device = models.ForeignKey(Device, blank=True, null=True)
    gps = models.PointField()
    objects = models.GeoManager()

    pm10count = models.FloatField()
    pm10con = models.FloatField()
    pm2point5count = models.FloatField()
    pm2point5con = models.FloatField()
    recorded = models.DateTimeField(blank=True, null=True)

    def __unicode__(self):
        # return self.device.identifier
        return str(self.added)


class Analysis(AirQualMeta):
    poly = models.PolygonField()
    objects = models.GeoManager()

    def __unicode__(self):
        # return self.device.identifier
        return str(self.poly)



@receiver(post_save, sender=Reading, dispatch_uid="refresh_aqs_data")
def update_stock(sender, instance, **kwargs):
    pusher_client = pusher.Pusher(
        app_id='228273',
        key='69fd7ece64cc89e58187',
        secret='0d766ecef1bd29ef8ae3',
        cluster='eu',
        ssl=True
    )

    pusher_client.trigger('refresh_aqs_data', 'refresh_aqs_data_now', {})
