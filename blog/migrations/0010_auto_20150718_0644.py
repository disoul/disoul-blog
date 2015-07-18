# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0009_update_timetuple'),
    ]

    operations = [
        migrations.AlterField(
            model_name='update_timetuple',
            name='time',
            field=models.FloatField(),
        ),
    ]
