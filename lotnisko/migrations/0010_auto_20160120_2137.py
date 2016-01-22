# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lotnisko', '0009_auto_20160119_2242'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='startlane',
            name='id',
        ),
        migrations.AlterField(
            model_name='startlane',
            name='name',
            field=models.CharField(max_length=254, serialize=False, primary_key=True),
        ),
    ]
