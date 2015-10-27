from django.contrib import admin
from .models import Flight
from .models import Passenger
from .models import Reservation
from .models import ReservedSeat
from .models import StartLane
from .models import StartLaneScheduleField
from .models import AirLines
from .models import Plane
from .models import Pilot

# Register your models here.


class AirLinesAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Name', {'fields': ['name']}),
    ]

    list_display = [
        'name'
    ]


class FlightAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Pilot', {'fields': ['pilot']}),
        ('Flight number', {'fields': ['flight_number']}),
        ('Date', {'fields': ['flight_date']}),
        ('Plane', {'fields': ['plane']}),
        ('Destination', {'fields': ['destination']}),
        ('Lane', {'fields': ['start_lane']}),
        ('Status', {'fields': ['status']}),
        ('EClassReserved', {'fields': ['reserved_economic_class_seats']}),
        ('BClassReserved', {'fields': ['reserved_business_class_seats']}),
        ('1stClassReserved', {'fields': ['reserved_first_class_seats']}),
    ]

    list_display = [
        'flight_number',
        'flight_date',
        'pilot',
        'destination',
        'start_lane',
        'status',
        'reserved_economic_class_seats',
        'reserved_business_class_seats',
        'reserved_first_class_seats',
    ]

    list_filter = ['flight_date']

    search_fields = [
        'flight_number',
        'destination',
        'flight_date',
        'pilot',
    ]


class PassengerAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Name', {'fields': ['name']}),
        ('Surname', {'fields': ['surname']}),
        ('Email', {'fields': ['email']}),
    ]

    list_display = [
        'name',
        'surname',
    ]

    list_filter = [
        'name',
        'surname',
    ]

    search_fields = [
        'name',
        'surname',
    ]


class PilotAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Name', {'fields': ['name']}),
        ('Surname', {'fields': ['surname']}),
        ('Airlines', {'fields': ['airlines']}),
    ]

    list_display = [
        'name',
        'surname',
        'airlines',
    ]

    list_filter = [
        'name',
        'surname',
        'airlines',
    ]

    search_fields = [
        'name',
        'surname',
        'airlines',
    ]


class PlaneAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Name', {'fields': ['name']}),
        ('Airlines', {'fields': ['airlines']}),
        ('EClassLimit', {'fields': ['economic_class_seats']}),
        ('BClassLimit', {'fields': ['business_class_seats']}),
        ('1stClassLimit', {'fields': ['first_class_seats']}),
    ]

    list_display = [
        'name',
        'airlines',
        'economic_class_seats',
        'business_class_seats',
        'first_class_seats',
    ]

    list_filter = [
        'airlines',
    ]

    search_fields = [
        'name',
        'airlines',
    ]


class ReservationAdmin(admin.ModelAdmin):
    fieldsets = [
        ('ID', {'fields': ['reservation_id']}),
        ('Passenger', {'fields': ['passenger']}),
        ('Status', {'fields': ['status']}),
        ('Seat', {'fields': ['seat']}),
        ('Hand Luggage Surcharge', {'fields': ['hand_luggage_surcharge']}),
        ('Hold Luggage Surcharge', {'fields': ['hold_luggage_surcharge']}),
    ]

    list_display = [
        'passenger',
        'status',
        'reservation_id',
        'hand_luggage_surcharge',
        'hold_luggage_surcharge',
    ]

    list_filter = [
        'passenger',
        'status',
        'reservation_id',
    ]

    search_fields = [
        'passenger',
        'status',
        'reservation_id',
        'hand_luggage_surcharge',
        'hold_luggage_surcharge',
    ]


class ReservedSeatAdmin(admin.ModelAdmin):
    list_filter = [
        'flight',
        'seat_type',
    ]

    search_fields = [
        'flight',
        'seat_type',
    ]


class StartLaneAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Name', {'fields': ['name']}),
    ]

    list_display = [
        'name'
    ]


class StartLaneScheduleAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Day', {'fields': ['date']}),
        ('From', {'fields': ['start_time']}),
        ('To', {'fields': ['end_time']}),
        ('Name', {'fields': ['lane']}),
    ]

    list_display = [
        'date',
        'lane',
        'start_time',
        'end_time',
    ]

    list_filter = [
        'date',
        'lane',
        'start_time',
        'end_time',
    ]

    search_fields = [
        'date',
        'lane',
        'start_time',
        'end_time',
    ]


admin.site.register(AirLines, AirLinesAdmin)
admin.site.register(Flight, FlightAdmin)
admin.site.register(Passenger, PassengerAdmin)
admin.site.register(Pilot, PilotAdmin)
admin.site.register(Plane, PlaneAdmin)
admin.site.register(Reservation, ReservationAdmin)
admin.site.register(ReservedSeat, ReservedSeatAdmin)
admin.site.register(StartLaneScheduleField, StartLaneScheduleAdmin)
admin.site.register(StartLane, StartLaneAdmin)
