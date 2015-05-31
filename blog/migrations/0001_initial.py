# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=100)),
                ('content', models.TextField()),
                ('date', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='ArticleTags',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('tag_name', models.CharField(max_length=100)),
                ('tag_color', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='BlogTheme',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('theme_name', models.CharField(max_length=100)),
                ('icon', models.ImageField(upload_to=b'')),
                ('title_text', models.CharField(max_length=100)),
                ('title_img', models.ImageField(upload_to=b'')),
                ('body_img', models.ImageField(upload_to=b'')),
            ],
        ),
        migrations.AddField(
            model_name='article',
            name='tag',
            field=models.ForeignKey(to='blog.ArticleTags'),
        ),
    ]
