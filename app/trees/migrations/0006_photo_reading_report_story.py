# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-07-21 22:15
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import qualia.tools.uploads
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('trees', '0005_auto_20160719_1901'),
    ]

    operations = [
        migrations.CreateModel(
            name='Photo',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('added', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated', models.DateTimeField(auto_now=True, null=True)),
                ('recorded', models.DateTimeField()),
                ('author', models.CharField(blank=True, default='Anon.', max_length=250, null=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to=qualia.tools.uploads.get_image_path)),
                ('tree', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='trees.Tree')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Reading',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('added', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated', models.DateTimeField(auto_now=True, null=True)),
                ('recorded', models.DateTimeField()),
                ('author', models.CharField(blank=True, default='Anon.', max_length=250, null=True)),
                ('type', models.CharField(choices=[('A', 'Height of Tree'), ('B', 'Spread of Crown'), ('C', 'Diameter at Breast Height'), ('D', 'Clear Stem Height'), ('O', 'Other')], default='O', max_length=1)),
                ('value', models.FloatField()),
                ('tree', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='trees.Tree')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Report',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('added', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated', models.DateTimeField(auto_now=True, null=True)),
                ('recorded', models.DateTimeField()),
                ('author', models.CharField(blank=True, default='Anon.', max_length=250, null=True)),
                ('type', models.CharField(choices=[('A', 'Site History'), ('B', 'Form'), ('C', 'Condition'), ('D', 'Nearby Obstructions'), ('E', 'Past Management'), ('F', 'Recommendations'), ('O', 'Other')], default='O', max_length=1)),
                ('info', models.TextField(blank=True, null=True)),
                ('tree', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='trees.Tree')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Story',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('added', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated', models.DateTimeField(auto_now=True, null=True)),
                ('recorded', models.DateTimeField()),
                ('author', models.CharField(blank=True, default='Anon.', max_length=250, null=True)),
                ('info', models.TextField(blank=True, null=True)),
                ('tree', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='trees.Tree')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
