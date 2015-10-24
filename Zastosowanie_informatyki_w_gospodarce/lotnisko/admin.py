from django.contrib import admin
from .models import Flight
from .models import Staff
from .models import Reservation
from .models import StartLane
from .models import StaffScheduleField
from .models import StartLaneScheduleField
from .models import AirLines
from .models import Plane
from .models import Pilot

# Register your models here.


class FlightAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Pilot', {'fields': ['pilot']}),
        ('Flight number', {'fields': ['flight_number']}),
        ('Date', {'fields': ['flight_date']}),
        ('Plane', {'fields': ['plane']}),
        ('Destination', {'fields': ['destination']}),
        ('Lane', {'fields': ['start_lane']}),
        ('Status', {'fields': ['status']}),
    ]

    list_display = [
        'flight_number',
        'flight_date',
        'pilot',
        'destination',
        'start_lane',
        'status',
    ]

    list_filter = ['flight_date']

    search_fields = [
        'flight_number',
        'destination',
        'flight_date',
        'pilot',
    ]


class StaffAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Name', {'fields': ['name']}),
        ('Surname', {'fields': ['surname']}),
        ('Phone', {'fields': ['phone']}),
        ('Email', {'fields': ['email']}),
        ('Who is he?', {'fields': ['job_title']}),
    ]

    list_display = [
        'name',
        'surname',
        'job_title',
    ]

    list_filter = [
        'job_title',
        'surname',
        'name'
    ]

    search_fields = [
        'name',
        'surname',
        'job_title',
    ]


class ReservationAdmin(admin.ModelAdmin):
    fieldsets = [
        ('ID', {'fields': ['reservation_id']}),
        ('Passenger', {'fields': ['passenger']}),
        ('Status', {'fields': ['status']}),
        ('Seat', {'fields': ['seat']}),
        ('Luggage', {'fields': ['luggage']}),
    ]

    list_display = [
        'passenger',
        'status',
        'reservation_id',
        'luggage',
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
    ]


class StartLaneAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Name', {'fields': ['name']}),
    ]

    list_display = [
        'name'
    ]


class StaffScheduleAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Day', {'fields': ['date']}),
        ('From', {'fields': ['start_time']}),
        ('To', {'fields': ['end_time']}),
        ('Name', {'fields': ['staff']}),
    ]

    list_display = [
        'date',
        'staff',
        'start_time',
        'end_time',
    ]

    list_filter = [
        'date',
        'staff',
        'start_time',
        'end_time',
    ]

    search_fields = [
        'date',
        'staff',
        'start_time',
        'end_time',
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


class AirLinesAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Name', {'fields': ['name']}),
    ]

    list_display = [
        'name'
    ]


class PlaneAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Airlines', {'fields': ['airlines']}),
        ('EClassLimit', {'fields': ['economic_class_seats']}),
        ('EClassReserved', {'fields': ['reserved_economic_class_seats']}),
        ('BClassLimit', {'fields': ['business_class_seats']}),
        ('BClassReserved', {'fields': ['reserved_business_class_seats']}),
        ('1stClassLimit', {'fields': ['first_class_seats']}),
        ('1stClassReserved', {'fields': ['reserved_first_class_seats']}),
    ]

    list_display = [
        'airlines',
        'economic_class_seats',
        'reserved_economic_class_seats',
        'business_class_seats',
        'reserved_business_class_seats',
        'first_class_seats',
        'reserved_first_class_seats',
    ]

    list_filter = [
        'airlines',
    ]

    search_fields = [
        'airlines',
    ]


class PilotAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Name', {'fields': ['name']}),
        ('Surname', {'fields': ['surname']}),
        ('Pilot', {'fields': ['airlines']}),
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


admin.site.register(Flight, FlightAdmin)
admin.site.register(Staff, StaffAdmin)
admin.site.register(Pilot, PilotAdmin)
admin.site.register(Plane, PlaneAdmin)
admin.site.register(AirLines, AirLinesAdmin)
admin.site.register(StartLaneScheduleField, StartLaneScheduleAdmin)
admin.site.register(StaffScheduleField, StaffScheduleAdmin)
admin.site.register(StartLane, StartLaneAdmin)
admin.site.register(Reservation, ReservationAdmin)
