# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('django_bootstrap_calendar', '0002_auto_20151025_1536'),
    ]

    operations = [
        migrations.AddField(
            model_name='calendarevent',
            name='url',
            field=models.URLField(null=True, verbose_name='URL', blank=True),
        ),
    ]
