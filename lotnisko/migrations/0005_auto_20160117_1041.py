# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lotnisko', '0004_auto_20160114_2133'),
    ]

    operations = [
        migrations.AddField(
            model_name='flight',
            name='reserved_business_class_seats_numbers',
            field=models.CharField(default=b'', max_length=1000000),
        ),
        migrations.AddField(
            model_name='flight',
            name='reserved_economic_class_seats_numbers',
            field=models.CharField(default=b'', max_length=1000000),
        ),
        migrations.AddField(
            model_name='flight',
            name='reserved_first_class_seats_numbers',
            field=models.CharField(default=b'', max_length=1000000),
        ),
    ]
