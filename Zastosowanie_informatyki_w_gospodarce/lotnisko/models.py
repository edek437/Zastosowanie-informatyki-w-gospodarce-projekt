from django.db import models
from django.contrib.auth.models import User

# Create your models here.

# TODO: pilot dla lotu, pas startowy, typ przewozonego towaru, pensje, grafik pracy,

'''
grafiki:
-grafik pracy pracownikow
-grafik kiedy jaki pas startowy jest wolny
'''


class Person(models.Model):
    name = models.CharField(max_length=254)
    surname = models.CharField(max_length=254)

    class Meta:
        abstract = True


class ScheduleField(models.Model):  # TODO: make start and end time unique for day
    date = models.DateField()
    start_time = models.TimeField()
    end_time = models.TimeField()

    class Meta:
        abstract = True


class StaffScheduleField(ScheduleField):
    staff = models.ForeignKey(User)

    def __str__(self):
        return '%s: %s-%s' % (self.staff, self.start_time, self.end_time)


class AirLines(models.Model):
    name = models.CharField(max_length=254)

    def __str__(self):
        return self.name


class Pilot(Person):  # Pilot is not airport worker, HE's hired by airlines
    airlines = models.ForeignKey(AirLines)

    def __str__(self):
        return '%s %s(%s)' % (self.name, self.surname, self.airlines)


class Passenger(Person):
    email = models.EmailField(blank=True)

    def __str__(self):
        return '%s %s' % (self.name, self.surname)


class Plane(models.Model):
    name = models.CharField(max_length=254)
    airlines = models.ForeignKey(AirLines)
    economic_class_seats = models.IntegerField()
    business_class_seats = models.IntegerField()
    first_class_seats = models.IntegerField()

    def __str__(self):
        return '%s: %s' % (self.airlines, self.name)


class StartLane(models.Model):
    name = models.CharField(max_length=254)

    def __str__(self):
        return self.name


class Flight(models.Model):
    BOARDING_STATE_CHOICES = (
        ('Scheduled', 'Scheduled'),
        ('Boarding started', 'Boarding started'),
        ('Boarding Over', 'Boarding Over'),
        ('Plane started', 'Plane started'),
        ('Flight canceled', 'Flight canceled'),
    )

    flight_number = models.CharField(max_length=254, primary_key=True)
    flight_date = models.DateTimeField()
    pilot = models.ForeignKey(Pilot)
    plane = models.ForeignKey(Plane)
    start_lane = models.ForeignKey(StartLane)
    status = models.CharField(max_length=254, choices=BOARDING_STATE_CHOICES)
    destination = models.CharField(max_length=254)
    reserved_economic_class_seats = models.IntegerField(default=0)
    reserved_business_class_seats = models.IntegerField(default=0)
    reserved_first_class_seats = models.IntegerField(default=0)

    def __str__(self):
        return self.flight_number


class StartLaneScheduleField(ScheduleField):
    lane = models.ForeignKey(StartLane)
    flight = models.ForeignKey(Flight)

    def __str__(self):
        return '%s: %s-%s' % (self.lane, self.start_time, self.end_time)


class ReservedSeat(models.Model):
    SEAT_TYPE_CHOICES = (
        ('Business class', 'Business class'),
        ('Economic class', 'Economic class'),
        ('First class', 'First class'),
    )

    flight = models.ForeignKey(Flight)
    seat_type = models.CharField(max_length=254, choices=SEAT_TYPE_CHOICES)
    seat_number = models.IntegerField()

    def __str__(self):
        return '%s/%s/%s' % (self.flight, self.seat_type, self.seat_number)


class Reservation(models.Model):
    RESERVATION_STATUS_CHOICES = (
        ('Paid', 'Paid'),
        ('Not paid', 'Not paid'),
        ('Canceled', 'Canceled'),
    )

    reservation_id = models.CharField(max_length=254, primary_key=True)  # TODO: a moze to wyjebac i dac atuo id? Ablo jakas auto genrated value
    passenger = models.ForeignKey(Passenger)
    hand_luggage_surcharge = models.IntegerField(default=0)
    hold_luggage_surcharge = models.IntegerField(default=0)
    status = models.CharField(max_length=254, choices=RESERVATION_STATUS_CHOICES)
    seat = models.ForeignKey(ReservedSeat)

    def __str__(self):
        return '%s: %s-%s' % (self.reservation_id, self.passenger, self.seat)
