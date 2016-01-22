from django.shortcuts import render
from .models import Flight
from .models import Passenger
from .models import StartLane
from .models import StartLaneScheduleField
from .helpers import validate_password
from .helpers import validate_user
from .helpers import string_to_int_list
from .helpers import update_personal_data
from .helpers import update_pw
from .helpers import add_reservation
from .helpers import remove_reservation
from .helpers import up_flight
from .helpers import get_user_tickets
from .helpers import pay_for_ticket
from .helpers import validate_if_flights_arent_coliding
from .helpers import validate_flight_to_start_lane_assignment
from datetime import datetime
from datetime import timedelta
from datetime import time
from datetime import date
from django.db import models
from django.http import HttpResponse
from django.db.models import Q
import json
from time import sleep

# Create your views here.


def lotnisko_test(request):
    print "Django say something"
    return render(request, "lotnisko/lotnisko_main_page.html", {})


def get_unassigned_flights(request):
    limit = int(request.GET.get("limit"))
    flights = Flight.objects.filter(models.Q(start_lane__isnull=True) | models.Q(start_lane=None)).order_by('flight_date')[:limit]
    data = []
    for flight in flights:
        data.append({'pk': flight.flight_number,
                     'flight_date': str(flight.flight_date),
                     'destination': flight.destination,
                     })
    return HttpResponse(json.dumps(data))


def get_flights(request):
    date = request.GET.get("date")
    if not date:
        py_date = datetime.now()
    else:
        YYMMDD = date.split("-")
        py_date = datetime.now().replace(year=int(YYMMDD[0]), month=int(YYMMDD[1]), day=int(YYMMDD[2]))
    dest = request.GET.get("dest")
    if not dest:
        dest = ".*"
    flights = Flight.objects.filter(destination__iregex=dest, flight_date__gte=py_date).order_by('flight_date')[:5]
    print "HERE"
    return render(request, "lotnisko/flightsForm.html", {'flights': flights, 'date': py_date})


def get_current_departues(request):
    print "get current departues"
    date = datetime.now()
    flights = Flight.objects.filter(flight_date__gt=date).order_by('flight_date')[:5]
    return render(request, "lotnisko/nextFlights.html", {'flights': flights})


def reservation_test(request):
    print "Reservation testing"
    return render(request, "lotnisko/reservation_page.html", {})


def user_login(request):
    flight_pk = request.GET.get("flight_pk")
    if flight_pk is None:
        flight_pk = ''
    flights_to_reserve = request.GET.get("flights_to_reserve")
    print flights_to_reserve
    if flights_to_reserve is None:
        flights_to_reserve = ''
    return render(request, "lotnisko/user_login.html", {'flight_pk': flight_pk, 'flights_to_reserve': flights_to_reserve, 'login_fail': False})


def flight_coordination(request):
    return render(request, "lotnisko/flight_coordination_dashboard.html")


def user_dashboard(request):
    login = request.GET.get("login")
    password = request.GET.get("password")
    flight_pk = request.GET.get("flight_pk")
    flights_to_reserve = request.GET.get("flights_to_reserve")
    if validate_password(login, password):
        passenger = Passenger.objects.filter(nickname=login)[0]
        return render(request, "lotnisko/user_dashboard.html", {'flight_pk': flight_pk, 'flights_to_reserve': flights_to_reserve, 'passenger': passenger})
    else:
        return render(request, "lotnisko/user_login.html", {'flight_pk': flight_pk, 'flights_to_reserve': flights_to_reserve, 'login_fail': True})


def registration_page(request):
    flight_pk = request.GET.get("flight_pk")
    if flight_pk is None:
        flight_pk = ''
    return render(request, "lotnisko/registration_page.html", {'flight_pk': flight_pk})


def add_passenger(request):
    print "adding passenger"
    data = {
        'nickname': request.GET.get("nickname"),
        'password': request.GET.get("password"),
        'name': request.GET.get("name"),
        'surname': request.GET.get("surname"),
        'email': request.GET.get("email"),
    }
    return_msg = validate_user(data)
    return HttpResponse(json.dumps({'status': return_msg,
                                    'flight_pk': request.GET.get("flight_pk"),
                                    'passenger': request.GET.get("nickname"),
                                    'pw': request.GET.get("password"),
                                    }))


def show_seats(request):
    flight_pk = request.GET.get("flight_pk")
    flight = Flight.objects.filter(flight_number=flight_pk)
    return render(request, "lotnisko/seatsForm.html", {'flight': flight[0],
                                                       'ec': range(1, flight[0].plane.economic_class_seats+1),
                                                       'bc': range(1, flight[0].plane.business_class_seats+1),
                                                       'fc': range(1, flight[0].plane.first_class_seats+1),
                                                       'rec': string_to_int_list(flight[0].reserved_economic_class_seats_numbers),
                                                       'rbc': string_to_int_list(flight[0].reserved_business_class_seats_numbers),
                                                       'rfc': string_to_int_list(flight[0].reserved_first_class_seats_numbers)
                                                       })


def reserve_tickets(request):
    fpk_snbr_sclass = request.GET.get("ticket").split('-')
    login = request.GET.get("login")
    error_msg = ''
    print fpk_snbr_sclass
    while True:
        try:
            up_flight(fpk_snbr_sclass)
            break
        except Exception as e:
            error_msg += str(e)
            print str(e)

    data = add_reservation({'login': login, 'fpk_snbr_sclass': request.GET.get("ticket")})
    return HttpResponse(json.dumps(data))


def cancel_reservation(request):
    print request.GET.get("ticket")
    remove_reservation({
        'fpk_snbr_sclass': request.GET.get("ticket")
    })
    return HttpResponse("OK!")


def get_my_tickets(request):
    return HttpResponse(json.dumps(get_user_tickets(request.GET.get("login"))))


def change_personal_data(request):
    login = request.GET.get("login")
    new_name = request.GET.get("new_name")
    new_surname = request.GET.get("new_surname")
    new_email = request.GET.get("new_email")
    # status has fields status and error_msg
    status = update_personal_data(login, new_name, new_surname, new_email)
    return HttpResponse(json.dumps(status))


def change_pw(request):
    login = request.GET.get("login")
    old_pw = request.GET.get("old_pw")
    new_pw = request.GET.get("new_pw")
    confirm_new_pw = request.GET.get("confirm_new_pw")
    # status has fields status and error_msg
    status = update_pw(login, old_pw, new_pw, confirm_new_pw)
    return HttpResponse(json.dumps(status))


def purchase_reservation(request):
    pay_for_ticket(request.GET.get("ticket"))
    return HttpResponse("OK!")


# fc stands for flight coordinator
def get_fc_flights(request):
    print "get_flights 100 closest flights"
    return HttpResponse(json.dumps([{'status': "OK!"}]))


def get_flights_for_given_date(request):
    YYMMDD = request.GET.get("date").split('-')
    py_date = date(int(YYMMDD[0]), int(YYMMDD[1]), int(YYMMDD[2]))
    print "get flights to for given date"
    slsfs = StartLaneScheduleField.objects.filter(Q(start_date=py_date) | Q(end_date=py_date))
    data = []
    print slsfs
    for slsf in slsfs:
        data.append({
            "start_time": str(slsf.start_time),
            "end_time": str(slsf.end_time),
            "fpk": slsf.flight.flight_number,
            "start_lane_name": slsf.flight.start_lane.name
        })
    return HttpResponse(json.dumps(data))


def assign_flight_to_start_lane(request):
    print "assign start lane"
    fr = request.GET.get("from")
    fr = fr if len(fr) == 5 else '0'+fr
    to = request.GET.get("to")
    to = to if len(to) == 5 else '0'+to
    start_lane = request.GET.get("start_lane")
    fpk = request.GET.get("fpk")
    start_time = map(int, request.GET.get("from").split(':'))
    end_time = map(int, request.GET.get("to").split(':'))
    flight_date = Flight.objects.filter(flight_number=fpk)[0].flight_date
    print "validate request and return error"
    print (fr < to)
    status = validate_flight_to_start_lane_assignment(start_lane, fpk, start_time, end_time)
    print "validated"
    if status['status'] != "OK":
        return HttpResponse(json.dumps(status))
    status = validate_if_flights_arent_coliding(fr, to, flight_date, start_lane)
    if status['status'] != "OK":
        return HttpResponse(json.dumps(status))
    print "saving start_lane_schedule_field"
    try:
        slsf = StartLaneScheduleField(
                start_date=flight_date,
                start_time=time(start_time[0], start_time[1]),
                end_date=(flight_date if fr < to else (flight_date + timedelta(days=1))),
                end_time=time(end_time[0], end_time[1]),
                lane=StartLane.objects.filter(name=start_lane)[0],
                flight=Flight.objects.filter(flight_number=fpk)[0]
        )
        slsf.save()
        f = Flight.objects.filter(flight_number=fpk)[0]
        f.start_lane = StartLane.objects.filter(name=start_lane)[0]
        f.save()
    except Exception, e:
        return HttpResponse(json.dumps({'status': '; '.join(e.message)}))
    finally:
        return HttpResponse(json.dumps({'status':"OK"}))


def remove_flight_from_start_lane(request):
    fpk = request.GET.get("fpk")
    # remove slsf and flight lane from flight
    f = Flight.objects.filter(flight_number=fpk)[0]
    f.start_lane = None
    f.save()
    StartLaneScheduleField.objects.filter(flight=fpk).delete()
    return HttpResponse(json.dumps({'status':"OK"}))


def get_flight_lanes(request):
    lane_array = []
    start_lanes = StartLane.objects.all()
    for lane in start_lanes:
        lane_array.append(str(lane))
    return HttpResponse(json.dumps(lane_array))
