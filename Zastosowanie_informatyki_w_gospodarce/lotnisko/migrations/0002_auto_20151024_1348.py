# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('lotnisko', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='plane',
            name='reserved_business_class_seats',
        ),
        migrations.RemoveField(
            model_name='plane',
            name='reserved_economic_class_seats',
        ),
        migrations.RemoveField(
            model_name='plane',
            name='reserved_first_class_seats',
        ),
        migrations.AddField(
            model_name='flight',
            name='reserved_business_class_seats',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='flight',
            name='reserved_economic_class_seats',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='flight',
            name='reserved_first_class_seats',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='startlaneschedulefield',
            name='flight',
            field=models.ForeignKey(default='something', to='lotnisko.Flight'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='reservation',
            name='luggage',
            field=models.ForeignKey(to='lotnisko.Luggage', blank=True),
        ),
        migrations.AlterField(
            model_name='reservation',
            name='status',
            field=models.CharField(max_length=254, choices=[(b'Paid', b'Paid'), (b'Not paid', b'Not paid'), (b'Canceled', b'Canceled')]),
        ),
        migrations.AlterField(
            model_name='staffschedulefield',
            name='staff',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL),
        ),
        migrations.DeleteModel(
            name='Staff',
        ),
    ]
