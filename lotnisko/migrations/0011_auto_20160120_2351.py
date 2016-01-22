# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lotnisko', '0010_auto_20160120_2137'),
    ]

    operations = [
        migrations.AlterField(
            model_name='startlaneschedulefield',
            name='flight',
            field=models.ForeignKey(to='lotnisko.Flight', unique=True),
        ),
    ]
