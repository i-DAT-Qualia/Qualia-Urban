# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.contrib.postgres.fields
import qualia.tools.uploads
import uuid
import django.contrib.gis.db.models.fields


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Photo',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, serialize=False, editable=False, primary_key=True)),
                ('added', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated', models.DateTimeField(auto_now=True, null=True)),
                ('tags', django.contrib.postgres.fields.ArrayField(size=None, null=True, base_field=models.CharField(max_length=200), blank=True)),
                ('gps', django.contrib.gis.db.models.fields.PointField(srid=4326, null=True, blank=True)),
                ('image', models.ImageField(null=True, upload_to=qualia.tools.uploads.get_image_path, blank=True)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
