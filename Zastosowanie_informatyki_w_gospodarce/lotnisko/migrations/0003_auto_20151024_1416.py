# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('lotnisko', '0002_auto_20151024_1348'),
    ]

    operations = [
        migrations.AlterField(
            model_name='passenger',
            name='email',
            field=models.EmailField(max_length=254, blank=True),
        ),
    ]
