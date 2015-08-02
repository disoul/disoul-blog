# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0011_article_article_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='article',
            name='article_id',
        ),
    ]
