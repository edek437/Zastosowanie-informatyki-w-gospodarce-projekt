# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lotnisko', '0002_auto_20160113_2246'),
    ]

    operations = [
        migrations.AddField(
            model_name='passenger',
            name='password',
            field=models.CharField(default='OKO\u0143', max_length=254),
            preserve_default=False,
        ),
    ]
