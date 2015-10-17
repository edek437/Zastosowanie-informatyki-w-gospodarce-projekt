from django.db import models

# Create your models here.


class Passaager(models.Model):
    name = models.CharField(max_length=254)
    surname = models.CharField(max_length=254)
    email = models.EmailField()


class Reservation(models.Model):
    RESERVATION_STATUS_CHOICES = (
        ('Paid', 'Paid'),
        ('Canceled', 'Canceled'),
    )

    reservation_id = models.CharField(max_length=254, primary_key=True)
    passenger = models.ForeignKey(Passaager)
    status = models.CharField(max_length=254, choices=RESERVATION_STATUS_CHOICES)


class Plane(models.Model):
    economic_class_seats = models.IntegerField()
    reserved_economic_class_seats = models.IntegerField()
    business_class_seats = models.IntegerField()
    reserved_business_class_seats = models.IntegerField()
    first_class_seats = models.IntegerField()
    reserved_first_class_seats = models.IntegerField()
    # TODO: przerzucić do lotu
    luggage_weight_limit = models.IntegerField()
    weight_reserved_for_luggage = models.IntegerField()


class Flight(models.Model):
    BOARDING_STATE_CHOICES = (
        ('Pending', 'Pending'),
        ('Boarding Over', 'Boarding Over'),
        ('Plane started', 'Plane started'),
        # TODO: dodac jeszcze trylion tego (np. lot odwołany itp.)
    )

    AIRLINES_CHOICES = (
        ('LOT', 'LOT'),
        # TODO: dodac jeszcze jakies
    )

    flight_number = models.CharField(max_length=254)
    flight_date = models.DateTimeField()
    plane = models.ForeignKey(Plane)
    status = models.CharField(max_length=254, choices=BOARDING_STATE_CHOICES)
    destination = models.CharField(max_length=254)
    airlines = models.CharField(max_length=254, choices=AIRLINES_CHOICES)
#    class Meta:
#        sorting = [flight_date]


class Stuff(models.Model):
    name = models.CharField(max_length=254)
    surname = models.CharField(max_length=254)
    phone = models.IntegerField(blank=True)
    email = models.EmailField(blank=True)


class Auth(models.Model):
    login = models.CharField(max_length=254)
    password = models.CharField(max_length=254)
    stuff = models.ForeignKey(Stuff)
