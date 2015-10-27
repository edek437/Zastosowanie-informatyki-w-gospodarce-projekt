__author__ = 'edek437'

from django.contrib import admin
from .models import CalendarEvent

# Register your models here.


class CalendarEventAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Person', {'fields': ['person']}),
        ('Title', {'fields': ['title']}),
        ('Type', {'fields': ['css_class']}),
        ('From', {'fields': ['start']}),
        ('To', {'fields': ['end']}),
    ]
    list_display = [
        'person',
        'title',
        'start',
        'end',
    ]

    list_filter = [
        'person',
        'title',
        'start',
        'end',
    ]


admin.site.register(CalendarEvent, CalendarEventAdmin)
