# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AirLines',
            fields=[
                ('name', models.CharField(max_length=254, serialize=False, primary_key=True)),
            ],
        ),
        migrations.CreateModel(
            name='Flight',
            fields=[
                ('flight_number', models.CharField(max_length=254, serialize=False, primary_key=True)),
                ('flight_date', models.DateTimeField()),
                ('status', models.CharField(max_length=254, choices=[(b'Scheduled', b'Scheduled'), (b'Boarding started', b'Boarding started'), (b'Boarding Over', b'Boarding Over'), (b'Plane started', b'Plane started'), (b'Flight canceled', b'Flight canceled')])),
                ('destination', models.CharField(max_length=254)),
                ('reserved_economic_class_seats', models.IntegerField(default=0)),
                ('reserved_business_class_seats', models.IntegerField(default=0)),
                ('reserved_first_class_seats', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Passenger',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=254)),
                ('surname', models.CharField(max_length=254)),
                ('nickname', models.CharField(max_length=254)),
                ('is_registered', models.BooleanField()),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Pilot',
            fields=[
                ('name', models.CharField(max_length=254)),
                ('surname', models.CharField(max_length=254)),
                ('nickname', models.CharField(max_length=8, serialize=False, primary_key=True)),
                ('airlines', models.ForeignKey(to='lotnisko.AirLines')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Plane',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=254)),
                ('economic_class_seats', models.IntegerField()),
                ('business_class_seats', models.IntegerField()),
                ('first_class_seats', models.IntegerField()),
                ('airlines', models.ForeignKey(to='lotnisko.AirLines')),
            ],
        ),
        migrations.CreateModel(
            name='Reservation',
            fields=[
                ('reservation_id', models.CharField(max_length=254, serialize=False, primary_key=True)),
                ('hand_luggage_surcharge', models.IntegerField(default=0)),
                ('hold_luggage_surcharge', models.IntegerField(default=0)),
                ('status', models.CharField(max_length=254, choices=[(b'Paid', b'Paid'), (b'Not paid', b'Not paid'), (b'Canceled', b'Canceled')])),
                ('passenger', models.ForeignKey(to='lotnisko.Passenger')),
            ],
        ),
        migrations.CreateModel(
            name='ReservedSeat',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('seat_type', models.CharField(max_length=254, choices=[(b'Business class', b'Business class'), (b'Economic class', b'Economic class'), (b'First class', b'First class')])),
                ('seat_number', models.IntegerField()),
                ('flight', models.ForeignKey(to='lotnisko.Flight')),
            ],
        ),
        migrations.CreateModel(
            name='StartLane',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=254)),
            ],
        ),
        migrations.CreateModel(
            name='StartLaneScheduleField',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('date', models.DateField()),
                ('start_time', models.TimeField()),
                ('end_time', models.TimeField()),
                ('flight', models.ForeignKey(to='lotnisko.Flight')),
                ('lane', models.ForeignKey(to='lotnisko.StartLane')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='reservation',
            name='seat',
            field=models.ForeignKey(to='lotnisko.ReservedSeat'),
        ),
        migrations.AddField(
            model_name='flight',
            name='pilot',
            field=models.ForeignKey(to='lotnisko.Pilot'),
        ),
        migrations.AddField(
            model_name='flight',
            name='plane',
            field=models.ForeignKey(to='lotnisko.Plane'),
        ),
        migrations.AddField(
            model_name='flight',
            name='start_lane',
            field=models.ForeignKey(to='lotnisko.StartLane'),
        ),
    ]
