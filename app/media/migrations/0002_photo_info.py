# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('media', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='photo',
            name='info',
            field=models.TextField(null=True, blank=True),
        ),
    ]
