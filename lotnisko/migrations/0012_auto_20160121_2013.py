# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lotnisko', '0011_auto_20160120_2351'),
    ]

    operations = [
        migrations.AlterField(
            model_name='passenger',
            name='email',
            field=models.EmailField(max_length=56),
        ),
        migrations.AlterField(
            model_name='passenger',
            name='nickname',
            field=models.CharField(max_length=56, serialize=False, primary_key=True),
        ),
        migrations.AlterField(
            model_name='passenger',
            name='password',
            field=models.CharField(max_length=56),
        ),
    ]
