# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lotnisko', '0006_auto_20160117_2111'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='passenger',
            name='is_registered',
        ),
    ]
