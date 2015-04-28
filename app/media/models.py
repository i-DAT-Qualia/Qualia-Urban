from django.db import models
from django.contrib.gis.db import models
from django.forms import ModelForm
from django.contrib.postgres.fields import ArrayField
from django.conf import settings
import uuid

from qualia.tools.uploads import get_image_path

from imagekit.models import ImageSpecField
from imagekit.processors import Thumbnail, ResizeToFit


class MediaMeta(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    added = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    updated = models.DateTimeField(auto_now=True, blank=True, null=True)
    tags = ArrayField(models.CharField(max_length=200), blank=True, null=True)

    gps = models.PointField()
    objects = models.GeoManager()

    class Meta:
        abstract = True


class Photo(models.Model):
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
        return self.id
