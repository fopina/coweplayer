# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cowepl', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='music',
            old_name='link',
            new_name='stream_link',
        ),
        migrations.AddField(
            model_name='music',
            name='video_id',
            field=models.CharField(default='', max_length=20),
            preserve_default=False,
        ),
    ]
