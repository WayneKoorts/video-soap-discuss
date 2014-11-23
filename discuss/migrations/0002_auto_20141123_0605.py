# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('discuss', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='mediaUrl',
            field=models.URLField(blank=True, null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='post',
            name='text',
            field=models.TextField(blank=True, null=True),
            preserve_default=True,
        ),
    ]
