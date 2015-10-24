# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('lotnisko', '0003_auto_20151024_1416'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='reservation',
            name='luggage',
        ),
        migrations.AddField(
            model_name='reservation',
            name='hand_luggage_surcharge',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='reservation',
            name='hold_luggage_surcharge',
            field=models.IntegerField(default=0),
        ),
        migrations.DeleteModel(
            name='Luggage',
        ),
    ]
