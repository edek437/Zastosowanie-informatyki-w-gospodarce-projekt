# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('lotnisko', '0004_auto_20151024_1503'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='staffschedulefield',
            name='staff',
        ),
        migrations.DeleteModel(
            name='StaffScheduleField',
        ),
    ]
