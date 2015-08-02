# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0010_auto_20150718_0644'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='article_id',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]
