# -*- coding: utf-8 -*-
# Generated by Django 1.9a1 on 2016-01-14 18:25
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('django_bootstrap_calendar', '0003_calendarevent_url'),
    ]

    operations = [
        migrations.AlterField(
            model_name='calendarevent',
            name='css_class',
            field=models.CharField(blank=True, choices=[(b'', 'Normal'), (b'event-warning', 'Warning'), (b'event-info', 'Info'), (b'event-success', 'Success'), (b'event-inverse', 'Inverse'), (b'event-special', 'Special'), (b'event-important', 'Important')], max_length=20, verbose_name='Priority'),
        ),
    ]