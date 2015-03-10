# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='ingredients',
            field=models.TextField(null=True, verbose_name=b'Ingredients', blank=True),
            preserve_default=True,
        ),
    ]
