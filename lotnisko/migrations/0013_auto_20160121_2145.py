# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('lotnisko', '0012_auto_20160121_2013'),
    ]

    operations = [
        migrations.RenameField(
            model_name='startlaneschedulefield',
            old_name='date',
            new_name='start_date',
        ),
        migrations.AddField(
            model_name='startlaneschedulefield',
            name='end_date',
            field=models.DateField(default=datetime.date(2015, 5, 22)),
        ),
    ]
