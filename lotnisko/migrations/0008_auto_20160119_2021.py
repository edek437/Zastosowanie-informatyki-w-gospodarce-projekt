# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lotnisko', '0007_remove_passenger_is_registered'),
    ]

    operations = [
        migrations.AlterField(
            model_name='flight',
            name='start_lane',
            field=models.ForeignKey(blank=True, to='lotnisko.StartLane', null=True),
        ),
        migrations.AlterField(
            model_name='reservation',
            name='seat_type',
            field=models.CharField(max_length=254, choices=[(b'economic', b'economic'), (b'business', b'business'), (b'first', b'first')]),
        ),
        migrations.AlterField(
            model_name='reservation',
            name='status',
            field=models.CharField(max_length=254, choices=[(b'Paid', b'Paid'), (b'Not Paid', b'Not Paid'), (b'Canceled', b'Canceled')]),
        ),
    ]
