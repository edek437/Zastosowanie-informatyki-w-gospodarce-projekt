# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lotnisko', '0008_auto_20160119_2021'),
    ]

    operations = [
        migrations.AlterField(
            model_name='flight',
            name='reserved_business_class_seats_numbers',
            field=models.CharField(default=b'', max_length=1000000, blank=True),
        ),
        migrations.AlterField(
            model_name='flight',
            name='reserved_economic_class_seats_numbers',
            field=models.CharField(default=b'', max_length=1000000, blank=True),
        ),
        migrations.AlterField(
            model_name='flight',
            name='reserved_first_class_seats_numbers',
            field=models.CharField(default=b'', max_length=1000000, blank=True),
        ),
    ]
