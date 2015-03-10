# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=100, verbose_name=b'Title')),
                ('status', models.CharField(default=b'draft', max_length=15, verbose_name=b'Status', choices=[(b'draft', b'Draft'), (b'published', b'Published')])),
                ('lead', models.TextField(null=True, verbose_name=b'Lead', blank=True)),
                ('content', models.TextField(null=True, verbose_name=b'Content', blank=True)),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name=b'Created at')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name=b'Updated at')),
                ('user', models.ForeignKey(verbose_name=b'User', to=settings.AUTH_USER_MODEL)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
