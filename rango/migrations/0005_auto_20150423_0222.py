# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rango', '0004_remove_category_views'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='views',
            field=models.IntegerField(default=0),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='category',
            name='slug',
            field=models.SlugField(),
        ),
    ]
