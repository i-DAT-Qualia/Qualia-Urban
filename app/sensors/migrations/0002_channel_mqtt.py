# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sensors', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='channel',
            name='mqtt',
            field=models.CharField(max_length=250, null=True, blank=True),
        ),
    ]
