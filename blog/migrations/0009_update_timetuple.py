# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0008_article_preview_line'),
    ]

    operations = [
        migrations.CreateModel(
            name='update_timetuple',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('time', models.IntegerField()),
                ('update_type', models.CharField(max_length=100)),
            ],
        ),
    ]
