from django.db import models

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


class Staff(Person):
    JOB_TITLE_CHOICES = (
        ('HR', 'HR'),
        ('Manager', 'Manager'),
        ('Receptionist', 'Receptionist'),
        ('Flight Coordinator', 'Flight Coordinator'),
        ('Cleaner', 'Cleaner'),
    )

    phone = models.IntegerField(blank=True)
    email = models.EmailField(blank=True)
    job_title = models.CharField(max_length=254, choices=JOB_TITLE_CHOICES)
    salary = models.IntegerField()

    def __str__(self):
        return self.name + ' ' + self.surname


class ScheduleField(models.Model):  # TODO: make start and end time unique for day
    date = models.DateField()
    start_time = models.TimeField()
    end_time = models.TimeField()

    class Meta:
        abstract = True


class StaffScheduleField(ScheduleField):
    staff = models.ForeignKey(Staff)

    def __str__(self):
        return self.staff + ': ' + self.start_time + '-' + self.end_time


class AirLines(models.Model):
    name = models.CharField(max_length=254)

    def __str__(self):
        return self.name


class Pilot(Person):  # Pilot is not airport worker, HE's hired by airlines
    airlines = models.ForeignKey(AirLines)

    def __str__(self):
        return self.name + ' ' + self.surname + '(' + self.airlines + ')'


class Luggage(models.Model):  # TODO: poki co gowno robie z tym bagazem trza to gdzies dodac
    LUGGAGE_TYPE_CHOICES = (
        ('hand luggage', 'hand luggage'),
        ('hold luggage', 'hold luggage'),
    )

    type = models.CharField(max_length=254, choices=LUGGAGE_TYPE_CHOICES)
    weight = models.IntegerField(default=0)

    def __str__(self):
        return self.type + ' (' + self.weight + ')'


class Passenger(Person):
    email = models.EmailField()

    def __str__(self):
        return self.name + ' ' + self.surname


class Plane(models.Model):  # TODO: przeniesc reserved do flight
    name = models.CharField(max_length=254)
    airlines = models.ForeignKey(AirLines)
    economic_class_seats = models.IntegerField()
    reserved_economic_class_seats = models.IntegerField(default=0)
    business_class_seats = models.IntegerField()
    reserved_business_class_seats = models.IntegerField(default=0)
    first_class_seats = models.IntegerField()
    reserved_first_class_seats = models.IntegerField(default=0)

    def __str__(self):
        return self.name


class StartLane(models.Model):
    name = models.CharField(max_length=254)

    def __str__(self):
        return self.name


class StartLaneScheduleField(ScheduleField):
    lane = models.ForeignKey(StartLane)

    def __str__(self):
        return self.lane + ': ' + self.start_time + '-' + self.end_time


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

    def __str__(self):
        return self.flight_number


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
        field_list = [self.flight, self.seat_type, self.seat_number]
        return '/'.join(str(x) for x in field_list)


class Reservation(models.Model):
    RESERVATION_STATUS_CHOICES = (
        ('Paid', 'Paid'),
        ('Canceled', 'Canceled'),
    )

    reservation_id = models.CharField(max_length=254, primary_key=True)  # TODO: a moze to wyjebac i dac atuo id?
    passenger = models.ForeignKey(Passenger)
    status = models.CharField(max_length=254, choices=RESERVATION_STATUS_CHOICES)
    seat = models.ForeignKey(ReservedSeat)
    luggage = models.ForeignKey(Luggage)
    # luggage = models.ManyToManyField(Luggage)

    def __str__(self):
        return self.reservation_id + ': ' + self.passenger + '(' + self.seat + ')'
