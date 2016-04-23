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
from django.http import JsonResponse
from django.db.models import Q
import json
from time import sleep

# Create your views here.


def lotnisko_test(request):
    print "Django say something"
    return render(request, "lotnisko/lotnisko_main_page.html", {})


def get_unassigned_flights(request):
    '''Used by filghcoordination page to get filghts unassigned to flight lanes'''
    limit = int(request.GET.get("limit"))
    flights = Flight.objects.filter(models.Q(start_lane__isnull=True) | models.Q(start_lane=None)).order_by('flight_date')[:limit]
    data = []
    for flight in flights:
        data.append({'pk': flight.flight_number,
                     'flight_date': str(flight.flight_date),
                     'destination': flight.destination,
                     })
    return HttpResponse(json.dumps(data))


def get_flights_mobile(request):
    date = request.GET.get("date")
    if not date:
        py_date = datetime.now()
    else:
        YYMMDD = date.split("-")
        py_date = datetime.now().replace(year=int(YYMMDD[0]), month=int(YYMMDD[1]), day=int(YYMMDD[2]))
    dest = request.GET.get("dest")
    if not dest:
        dest = ".*"
    limit = request.GET.get("limit")
    if not limit:
        limit = 5
    flights = Flight.objects.filter(destination__iregex=dest, flight_date__gte=py_date).order_by('flight_date')[:limit]
    print "HERE"
    flights_dict = {}
    flights_arr = []
    for f in flights:
        flights_arr.append({
          "flight_number": f.flight_number,
          "flight_date": f.flight_date,
          "destination": f.destination,
          "status": f.status
        })
    flights_dict['flights'] = flights_arr
    flights_dict['date'] = py_date
    return JsonResponse(flights_dict)
    return render(request, "lotnisko/flightsForm.html", {'flights': flights, 'date': py_date})

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

def get_news_mobile(request):
    print "Should return json"
    news_dict = {}
    news_arr = []
    for i in range(1,5):
        news_arr.append({
          "title": "string tytul (fake not implemented yet)",
          "content": "strong tresc newsa (fake not implemented yet)",
          "photo": "trzeba sie zastanowic albo to olac (fake not implemented yet)"
        })
    news_dict["news"] = news_arr
    return JsonResponse(news_dict)


def get_current_departues_mobile(request):
    print "Should return json"
    date = datetime.now()
    nbr_of_flights = request.GET.get("nbr_of_flights")
    if not nbr_of_flights:
        nbr_of_flights = 5
    flights = Flight.objects.filter(flight_date__gt=date).order_by('flight_date')[:nbr_of_flights]
    flights_dict = {}
    json_flights = []
    for f in flights:
        json_flights.append({
          "flight_number": f.flight_number,
          "flight_date": f.flight_date,
          "destination": f.destination,
          "status": f.status
        })
    flights_dict["flights"] = json_flights
    return JsonResponse(flights_dict)

def get_current_departues(request):
    print "Should render table"
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

def user_dashboard_mobile(request):
    print "should return json"
    login = request.GET.get("login")
    password = request.GET.get("password")
    flight_pk = request.GET.get("flight_pk")
    flights_to_reserve = request.GET.get("flights_to_reserve")
    if validate_password(login, password):
        passenger = Passenger.objects.filter(nickname=login)[0]
        return JsonResponse({
            'status': 'OK',
            'flight_pk': flight_pk,
            'flights_to_reserve': flights_to_reserve,
            'passenger': {
                "login": passenger.nickname,
                "password": passenger.password,
                "email": passenger.email,
                "name": passenger.name,
                "surname": passenger.surname
            }
        })
    else:
        return JsonResponse({'status': 'NOK', "errorr_msg": "Credential validation failed"})

def user_dashboard(request):
    print "should render page"
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


def add_passenger_mobile(request):
    print "adding passenger mobile"
    data = {
        'nickname': request.GET.get("nickname"),
        'password': request.GET.get("password"),
        'name': request.GET.get("name"),
        'surname': request.GET.get("surname"),
        'email': request.GET.get("email"),
    }
    return_msg = validate_user(data)
    return JsonResponse({
            'status': return_msg,
            'flight_pk': request.GET.get("flight_pk"),
            'passenger': request.GET.get("nickname"),
            'pw': request.GET.get("password"),
        })

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


def show_seats_mobile(request):
    flight_pk = "AAAAAA" #request.GET.get("flight_pk")
    print flight_pk
    flight = Flight.objects.filter(flight_number=flight_pk)
    if not flight:
        return JsonResponse({"error": "flight with this identifier doesn't exist"})
    else:
        return JsonResponse({
               'flight': {
                    'number': flight[0].flight_number,
                    'date': flight[0].flight_date,
                    'destination': flight[0].destination,
                    'economic_price': flight[0].economic_class_seat_price,
                    'bussiness_price': flight[0].business_class_seat_price,
                    'first_price': flight[0].first_class_seat_price,
               },
               'ec': range(1, flight[0].plane.economic_class_seats+1),
               'bc': range(1, flight[0].plane.business_class_seats+1),
               'fc': range(1, flight[0].plane.first_class_seats+1),
               'rec': string_to_int_list(flight[0].reserved_economic_class_seats_numbers),
               'rbc': string_to_int_list(flight[0].reserved_business_class_seats_numbers),
               'rfc': string_to_int_list(flight[0].reserved_first_class_seats_numbers)
           })

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


def reserve_tickets_mobile(request):
    fpk_snbr_sclass = request.GET.get("ticket").split('-')
    fpk_snbr_sclass = fpk_snbr_sclass.split('-')
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
            return JsonResponse({
              "status": "NOK",
              "error_msg": str(e)
            })
    print "up filght passed"
    data = add_reservation({'login': login, 'fpk_snbr_sclass': "AAAAAA-2-first" })
    return JsonResponse(data)


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


def cancel_reservation_mobile(request):
    try:
        remove_reservation({
            'fpk_snbr_sclass': request.GET.get("ticket")
        })
    except Exception as e:
        return  JsonResponse({"status": "NOK!", "error_msg": str(e)})
    return JsonResponse({"status": "OK!"})


def cancel_reservation(request):
    try:
        remove_reservation({
            'fpk_snbr_sclass': request.GET.get("ticket")
        })
    except Exception as e:
        return  HttpResponse("NOK!")
    return HttpResponse("OK!")


def get_my_tickets_mobile(request):
    return JsonResponse({"reservations" : get_user_tickets(request.GET.get("login"))})


def get_my_tickets(request):
    return HttpResponse(json.dumps(get_user_tickets(request.GET.get("login"))))


def change_personal_data_mobile(request):
    login = request.GET.get("login")
    new_name = request.GET.get("new_name")
    new_surname = request.GET.get("new_surname")
    new_email = request.GET.get("new_email")
    # status has fields status and error_msg
    status = update_personal_data(login, new_name, new_surname, new_email)
    return JsonResponse(status)

def change_personal_data(request):
    login = request.GET.get("login")
    new_name = request.GET.get("new_name")
    new_surname = request.GET.get("new_surname")
    new_email = request.GET.get("new_email")
    # status has fields status and error_msg
    status = update_personal_data(login, new_name, new_surname, new_email)
    return HttpResponse(json.dumps(status))


def change_pw_mobile(request):
    login = request.GET.get("login")
    old_pw = request.GET.get("old_pw")
    new_pw = request.GET.get("new_pw")
    confirm_new_pw = request.GET.get("confirm_new_pw")
    # status has fields status and error_msg
    status = update_pw(login, old_pw, new_pw, confirm_new_pw)
    return JsonResponse(status)


def change_pw(request):
    login = request.GET.get("login")
    old_pw = request.GET.get("old_pw")
    new_pw = request.GET.get("new_pw")
    confirm_new_pw = request.GET.get("confirm_new_pw")
    # status has fields status and error_msg
    status = update_pw(login, old_pw, new_pw, confirm_new_pw)
    return HttpResponse(json.dumps(status))


def purchase_reservation_mobile(request):
    try:
        pay_for_ticket(request.GET.get("ticket"))
    except Exception as e:
        return JsonResponse({"status": "NOK!", "error_msg": str(e)})
    return JsonResponse({"status": "OK!"})


def purchase_reservation(request):
    try:
        pay_for_ticket(request.GET.get("ticket"))
    except:
        return HttpResponse({"status": "NOK!"})
    return HttpResponse({"status": "OK!"})


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


def log_out(request):
    return JsonResponse({
      "status": "OK",
      "goodbye_msg": "jakas wiadomosc pozegnalna"
    })
