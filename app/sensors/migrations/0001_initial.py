# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.contrib.gis.db.models.fields
import django.contrib.postgres.fields
from django.conf import settings
import uuid


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Channel',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, serialize=False, editable=False, primary_key=True)),
                ('name', models.CharField(max_length=250, db_index=True)),
                ('info', models.TextField(null=True, blank=True)),
                ('added', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated', models.DateTimeField(auto_now=True, null=True)),
                ('tags', django.contrib.postgres.fields.ArrayField(size=None, null=True, base_field=models.CharField(max_length=200), blank=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, serialize=False, editable=False, primary_key=True)),
                ('added', models.DateTimeField(auto_now_add=True, null=True)),
                ('gps', django.contrib.gis.db.models.fields.PointField(srid=4326)),
            ],
        ),
        migrations.CreateModel(
            name='Reading',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, serialize=False, editable=False, primary_key=True)),
                ('added', models.DateTimeField(auto_now_add=True, null=True)),
                ('value', models.FloatField()),
                ('channel', models.ForeignKey(to='sensors.Channel')),
            ],
        ),
        migrations.CreateModel(
            name='Thing',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, serialize=False, editable=False, primary_key=True)),
                ('name', models.CharField(max_length=250, db_index=True)),
                ('info', models.TextField(null=True, blank=True)),
                ('added', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated', models.DateTimeField(auto_now=True, null=True)),
                ('tags', django.contrib.postgres.fields.ArrayField(size=None, null=True, base_field=models.CharField(max_length=200), blank=True)),
                ('owner', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='location',
            name='thing',
            field=models.ForeignKey(to='sensors.Thing'),
        ),
        migrations.AddField(
            model_name='channel',
            name='thing',
            field=models.ForeignKey(to='sensors.Thing'),
        ),
    ]
