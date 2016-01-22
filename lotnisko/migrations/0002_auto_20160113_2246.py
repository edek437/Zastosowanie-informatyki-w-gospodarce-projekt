# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lotnisko', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='passenger',
            name='id',
        ),
        migrations.AddField(
            model_name='passenger',
            name='email',
            field=models.EmailField(default='aa@aa.com', max_length=254),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='passenger',
            name='nickname',
            field=models.CharField(max_length=254, serialize=False, primary_key=True),
        ),
    ]
