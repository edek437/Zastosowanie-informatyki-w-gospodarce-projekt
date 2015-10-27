# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('django_bootstrap_calendar', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='calendarevent',
            name='url',
        ),
        migrations.AddField(
            model_name='calendarevent',
            name='person',
            field=models.ForeignKey(default=10, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='calendarevent',
            name='css_class',
            field=models.CharField(default=b'Normal', max_length=20, verbose_name='Priority', blank=True, choices=[(b'', 'Normal'), (b'event-warning', 'Warning'), (b'event-info', 'Info'), (b'event-success', 'Success'), (b'event-inverse', 'Inverse'), (b'event-special', 'Special'), (b'event-important', 'Important')]),
        ),
        migrations.AlterField(
            model_name='calendarevent',
            name='title',
            field=models.CharField(default=b'Work Time', max_length=255, verbose_name='Title'),
        ),
    ]
