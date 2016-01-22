# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lotnisko', '0005_auto_20160117_1041'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='reservedseat',
            name='flight',
        ),
        migrations.RemoveField(
            model_name='reservation',
            name='hand_luggage_surcharge',
        ),
        migrations.RemoveField(
            model_name='reservation',
            name='hold_luggage_surcharge',
        ),
        migrations.RemoveField(
            model_name='reservation',
            name='seat',
        ),
        migrations.AddField(
            model_name='reservation',
            name='seat_number',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='reservation',
            name='seat_type',
            field=models.CharField(default='Economic Class', max_length=254, choices=[(b'Economic Class', b'Economic Class'), (b'Business Class', b'Business Class'), (b'First Class', b'First Class')]),
            preserve_default=False,
        ),
        migrations.DeleteModel(
            name='ReservedSeat',
        ),
    ]
