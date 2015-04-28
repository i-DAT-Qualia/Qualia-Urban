# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import qualia.tools.uploads


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Photo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('image', models.ImageField(null=True, upload_to=qualia.tools.uploads.get_image_path, blank=True)),
            ],
        ),
    ]
