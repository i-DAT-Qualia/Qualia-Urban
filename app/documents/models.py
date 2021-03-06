from django.db import models
from django.forms import ModelForm
from django.contrib.postgres.fields import ArrayField, HStoreField
from django.conf import settings
import uuid


class Document(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(db_index=True, max_length=250)

    # meta
    info = models.TextField(blank=True, null=True)
    added = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    updated = models.DateTimeField(auto_now=True, blank=True, null=True)
    tags = ArrayField(models.CharField(max_length=200), blank=True, null=True)
    owner = models.ForeignKey(settings.AUTH_USER_MODEL)

    # data
    content = HStoreField()

    def __unicode__(self):
        return self.name
