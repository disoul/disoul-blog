# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_auto_20150615_0353'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='articletags',
            name='tag_color',
        ),
    ]
