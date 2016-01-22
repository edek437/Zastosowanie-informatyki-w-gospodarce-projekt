# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lotnisko', '0013_auto_20160121_2145'),
    ]

    operations = [
        migrations.AlterField(
            model_name='startlaneschedulefield',
            name='end_date',
            field=models.DateField(),
        ),
    ]
