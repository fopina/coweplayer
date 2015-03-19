# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cowepl', '0002_music_duration'),
    ]

    operations = [
        migrations.AlterField(
            model_name='music',
            name='stream_link',
            field=models.CharField(max_length=1000),
            preserve_default=True,
        ),
    ]
