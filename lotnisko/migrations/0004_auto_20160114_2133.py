# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lotnisko', '0003_passenger_password'),
    ]

    operations = [
        migrations.AddField(
            model_name='flight',
            name='business_class_seat_price',
            field=models.IntegerField(default=150),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='flight',
            name='economic_class_seat_price',
            field=models.IntegerField(default=90),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='flight',
            name='first_class_seat_price',
            field=models.IntegerField(default=500),
            preserve_default=False,
        ),
    ]
