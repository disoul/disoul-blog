# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0007_auto_20150615_1513'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='preview_line',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]
