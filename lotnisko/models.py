from django.db import models
from datetime import date

# Create your models here.


class Person(models.Model):
    name = models.CharField(max_length=254)
    surname = models.CharField(max_length=254)

    class Meta:
        abstract = True


class ScheduleField(models.Model):  # TODO: make start and end time unique for day
    start_date = models.DateField()
    start_time = models.TimeField()
    end_date = models.DateField()
    end_time = models.TimeField()

    class Meta:
        abstract = True


class AirLines(models.Model):
    name = models.CharField(max_length=254, primary_key=True)

    def __str__(self):
        return self.name


class Pilot(Person):  # Pilot is not airport worker, HE's hired by airlines
    nickname = models.CharField(max_length=8, primary_key=True)
    airlines = models.ForeignKey(AirLines)

    def __str__(self):
        return '%s %s(%s)' % (self.name, self.surname, self.airlines)


class Passenger(Person):
    nickname = models.CharField(max_length=56, primary_key=True)
    password = models.CharField(max_length=56)
    email = models.EmailField(max_length=56)

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
    name = models.CharField(max_length=254, primary_key=True)

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
    start_lane = models.ForeignKey(StartLane, null=True, blank=True)
    status = models.CharField(max_length=254, choices=BOARDING_STATE_CHOICES)
    destination = models.CharField(max_length=254)
    reserved_economic_class_seats = models.IntegerField(default=0)
    reserved_business_class_seats = models.IntegerField(default=0)
    reserved_first_class_seats = models.IntegerField(default=0)
    reserved_economic_class_seats_numbers = models.CharField(max_length=1000000, default='', blank=True)
    reserved_business_class_seats_numbers = models.CharField(max_length=1000000, default='', blank=True)
    reserved_first_class_seats_numbers = models.CharField(max_length=1000000, default='', blank=True)
    economic_class_seat_price = models.IntegerField()
    business_class_seat_price = models.IntegerField()
    first_class_seat_price = models.IntegerField()

    def __str__(self):
        return self.flight_number


class StartLaneScheduleField(ScheduleField):
    lane = models.ForeignKey(StartLane)
    flight = models.ForeignKey(Flight, unique=True)

    def __str__(self):
        return '%s: %s-%s' % (self.lane, self.start_time, self.end_time)


class Reservation(models.Model):
    RESERVATION_STATUS_CHOICES = (
        ('Paid', 'Paid'),
        ('Not Paid', 'Not Paid'),
        ('Canceled', 'Canceled'),
    )

    SEAT_CLASS_CHOICES = (
        ('economic', 'economic'),
        ('business', 'business'),
        ('first', 'first'),
    )

    reservation_id = models.CharField(max_length=254, primary_key=True)
    passenger = models.ForeignKey(Passenger)
    status = models.CharField(max_length=254, choices=RESERVATION_STATUS_CHOICES)
    seat_type = models.CharField(max_length=254, choices=SEAT_CLASS_CHOICES)
    seat_number = models.IntegerField()

    def __str__(self):
        return '%s: %s-%s-%s' % (self.reservation_id, self.passenger, self.seat_type, self.seat_number)
