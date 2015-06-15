# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20150611_1221'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='articletags',
            name='tag_color',
        ),
        migrations.AlterField(
            model_name='article',
            name='date',
            field=models.DateField(),
        ),
    ]
