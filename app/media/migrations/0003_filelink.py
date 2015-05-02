# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.contrib.postgres.fields
import uuid
import django.contrib.gis.db.models.fields


class Migration(migrations.Migration):

    dependencies = [
        ('media', '0002_photo_info'),
    ]

    operations = [
        migrations.CreateModel(
            name='FileLink',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, serialize=False, editable=False, primary_key=True)),
                ('added', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated', models.DateTimeField(auto_now=True, null=True)),
                ('tags', django.contrib.postgres.fields.ArrayField(size=None, null=True, base_field=models.CharField(max_length=200), blank=True)),
                ('info', models.TextField(null=True, blank=True)),
                ('gps', django.contrib.gis.db.models.fields.PointField(srid=4326, null=True, blank=True)),
                ('link', models.URLField(null=True, blank=True)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
