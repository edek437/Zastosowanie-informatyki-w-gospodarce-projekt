from django.contrib import admin
from .models import Flight
from .models import Passenger
from .models import Reservation
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
        ('Status', {'fields': ['status']}),
        ('EClassPrice', {'fields': ['economic_class_seat_price']}),
        ('BClassPrice', {'fields': ['business_class_seat_price']}),
        ('1stClassPrice', {'fields': ['first_class_seat_price']}),
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
        'economic_class_seat_price',
        'business_class_seat_price',
        'first_class_seat_price',
    ]

    list_filter = ['flight_date']

    search_fields = [
        'flight_number',
        'destination',
        'flight_date',
        'pilot',
        'destination',
        'start_lane',
    ]


class PassengerAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Nickname', {'fields': ['nickname']}),
        ('Password', {'fields': ['password']}),
        ('Name', {'fields': ['name']}),
        ('Surname', {'fields': ['surname']}),
        ('Email', {'fields': ['email']}),
    ]

    list_display = [
        'nickname',
        'name',
        'surname',
    ]

    list_filter = [
        'nickname',
        'name',
        'surname',
    ]

    search_fields = [
        'nickname',
        'name',
        'surname',
    ]


class PilotAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Nickname', {'fields': ['nickname']}),
        ('Name', {'fields': ['name']}),
        ('Surname', {'fields': ['surname']}),
        ('Airlines', {'fields': ['airlines']}),
    ]

    list_display = [
        'nickname',
        'name',
        'surname',
        'airlines',
    ]

    list_filter = [
        'nickname',
        'name',
        'surname',
        'airlines',
    ]

    search_fields = [
        'nickname',
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
        ('Seat Type', {'fields': ['seat_type']}),
        ('Seat Number', {'fields': ['seat_number']}),
    ]

    list_display = [
        'passenger',
        'status',
        'reservation_id',
        'seat_type',
        'seat_number',
    ]

    list_filter = [
        'passenger',
        'status',
        'reservation_id',
        'seat_type',
    ]

    search_fields = [
        'passenger',
        'status',
        'reservation_id',
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
        ('Start Day', {'fields': ['start_date']}),
        ('End Day', {'fields': ['end_date']}),
        ('From', {'fields': ['start_time']}),
        ('To', {'fields': ['end_time']}),
        ('Name', {'fields': ['lane']}),
        ('Flight', {'fields': ['flight']}),
    ]
    list_display = [
        'lane',
        'flight',
        'start_date',
        'start_time',
        'end_date',
        'end_time',
    ]


    list_filter = [
        'lane',
        'flight',
        'start_date'
    ]

    search_fields = [
        'start_date',
        'flight',
        'lane',
    ]


admin.site.register(AirLines, AirLinesAdmin)
admin.site.register(Flight, FlightAdmin)
admin.site.register(Passenger, PassengerAdmin)
admin.site.register(Pilot, PilotAdmin)
admin.site.register(Plane, PlaneAdmin)
admin.site.register(Reservation, ReservationAdmin)
admin.site.register(StartLaneScheduleField, StartLaneScheduleAdmin)
admin.site.register(StartLane, StartLaneAdmin)
