# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_auto_20150614_0529'),
    ]

    operations = [
        migrations.AddField(
            model_name='articletags',
            name='tag_color',
            field=models.CharField(default='#000', max_length=10),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='article',
            name='date',
            field=models.DateTimeField(),
        ),
    ]
