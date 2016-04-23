__author__ = 'edek437'
from .models import Passenger
from .models import Flight
from .models import Reservation
from .models import StartLaneScheduleField
from .models import StartLane
from django.core.exceptions import ValidationError
from django.db import transaction
from django.core.validators import validate_email
from django.db.models import Q
from datetime import time
from datetime import timedelta


def validate_password(login, password):
    return Passenger.objects.filter(password=password, nickname=login)


def validate_user(data):
    if not data["nickname"]:
        return "Nazwa uzytkownika jest wymagana"
    if not data["password"]:
        return "Haslo jest wymagane"
    if len(data["password"]) < 4:
        return "Haslo musi miec co najmniej 4 znaki"
    if not data["name"]:
        return "Imie nie zostalo podane"
    if not data["surname"]:
        return "Nazwisko nie zostalo podane"
    if len(Passenger.objects.filter(nickname=data["nickname"])):
        return "Uzytkownik %s juz istnieje" % data["nickname"]
    try:
        validate_email(data["email"])
    except ValidationError as e:
        return "Podano zly format adresu email"
    return add_user(data)


def add_user(data):
    fail_error_msg = 'OK'
    user = Passenger(nickname=data["nickname"],
                     password=data["password"],
                     name=data["name"],
                     surname=data["surname"],
                     email=data["email"],
    )
    try:
        user.save()
    except ValidationError, e:
        fail_error_msg = '; '.join(e.messages)
    finally:
        return fail_error_msg


def string_to_int_list(reserved_seats_string):
    if not reserved_seats_string:
        return []
    else:
        return map(int, filter(None, reserved_seats_string.split(",")))


def update_personal_data(login, new_name, new_surname, new_email):
    user = Passenger.objects.filter(nickname=login)
    if len(user) == 0:
        return {'status': 'NOK', 'error_msg': 'Login nie istnieje'}
    if len(user) > 1:
        return {'status': 'NOK', 'error_msg': 'Dude! We have big fail over there'}
    try:
        validate_email(new_email)
    except ValidationError as e:
        return {'status': 'NOK', 'error_msg':"Podano zly format adresu email"}
    user = user[0]
    user.name = new_name
    user.surname = new_surname
    user.email = new_email
    try:
        user.save()
    except ValidationError, e:
        return {'status': 'NOK', 'error_msg': '; '.join(e.messages)}
    return {'status': 'OK'}


def update_pw(login, old_pw, new_pw, confirm_new_pw):
    user = Passenger.objects.filter(nickname=login)
    if len(user) == 0:
        return {'status': 'NOK', 'error_msg': 'Login nie istnieje'}
    if len(user) > 1:
        return {'status': 'NOK', 'error_msg': 'Dude! We have big fail over there'}
    user = user[0]
    if user.password != old_pw:
        return {'status': 'NOK', 'error_msg': 'Zle haslo'}
    if new_pw != confirm_new_pw:
        return {'status': 'NOK', 'error_msg': 'Wpisano haslo oraz potwierdzenie haslo sa rozne'}
    if len(new_pw) < 4:
        return {'status': 'NOK', 'error_msg': "Haslo musi miec co najmniej 4 znaki"}
    user.password = new_pw
    try:
        user.save()
    except ValidationError, e:
        return {'status': 'NOK', 'error_msg': '; '.join(e.messages)}
    return {'status': 'OK'}


def validate_flight_to_start_lane_assignment(start_lane, fpk, start_time, end_time):
    if not StartLane.objects.filter(name=start_lane):
        return {'status': 'Podanyu pas startowy nie istnieje'}
    if not Flight.objects.filter(flight_number=fpk):
        return {'status': 'Podany lot nie istnieje'}
    if start_time[0] > 23 or end_time[0] > 23 or end_time[0] < 0 or start_time[0] < 0:
        return {'status': 'Podana godzina nie istnieje'}
    if start_time[1] > 59 or end_time[1] > 59 or end_time[1] < 0 or start_time[1] < 0:
        return {'status': 'Zle podana godzina'}
    flight_date = Flight.objects.filter(flight_number=fpk)[0].flight_date
    if not (time(start_time[0], start_time[1]) > time(end_time[0], end_time[1])) or (flight_date.hour < start_time[0] or (flight_date.hour == start_time[0] and flight_date.minute < start_time[1])) and (flight_date.hour > end_time[0] or (flight_date.hour == end_time[0] and flight_date.minute > end_time[1])):
        return {'status': 'Przydzilony czas nie zawiera godziny odlotu'}
    return {'status': 'OK'}


def validate_if_flights_arent_coliding(start_time, end_time, flight_date, start_lane):
    lane = StartLane.objects.filter(name=start_lane)[0]
    slsf = StartLaneScheduleField.objects.filter(lane=lane)
    if not slsf:
        return {'status': 'OK'}
    stime = map(int, start_time.split(':'))
    etime = map(int, end_time.split(':'))
    if start_time > end_time:
        # flight start and end in 2 different days
        flight_date_end = flight_date + timedelta(days=1)
        slsf.filter(start_date=flight_date, start_time__gte=time(stime[0], stime[1]), end_date=flight_date_end, end_time__lte=time(etime[0],etime[1]))
    else:
        # flight start and end in the same day
        slsf = slsf.filter(start_date=flight_date, start_time__gte=time(stime[0], stime[1]), end_time__lte=time(etime[0],etime[1]))

    if not slsf:
        return {'status': 'OK'}
    else:
        return {'status': 'Nie mozna przydzielic samolutu gdyz koliduje to z innym samolotem'}


@transaction.atomic
def up_flight(fpk_snbr_sclass):
    flight = Flight.objects.filter(flight_number=fpk_snbr_sclass[0])[0]
    seat_num = getattr(flight, 'reserved_'+fpk_snbr_sclass[2]+'_class_seats')
    if seat_num > getattr(flight.plane, fpk_snbr_sclass[2]+'_class_seats'):
        return "Nie ma wiecej wolnych miejsc dla klasy %s" % fpk_snbr_sclass[2]
    setattr(flight, 'reserved_'+fpk_snbr_sclass[2]+'_class_seats', int(seat_num)+1)
    res_seats = getattr(flight, 'reserved_'+fpk_snbr_sclass[2]+'_class_seats_numbers')
    if fpk_snbr_sclass[1] in string_to_int_list(res_seats):
        return "Miejsce %s zostalo zarezerwowane. Sproboj wybrac inne." % fpk_snbr_sclass
    setattr(flight, 'reserved_'+fpk_snbr_sclass[2]+'_class_seats_numbers', res_seats+fpk_snbr_sclass[1]+',')
    flight.save()


@transaction.atomic
def remove_from_flight(fpk_snbr_sclass):
    flight = Flight.objects.filter(flight_number=fpk_snbr_sclass[0])[0]
    seat_num = getattr(flight, 'reserved_'+fpk_snbr_sclass[2]+'_class_seats')
    setattr(flight, 'reserved_'+fpk_snbr_sclass[2]+'_class_seats', int(seat_num)-1)
    res_seats = string_to_int_list(getattr(flight, 'reserved_'+fpk_snbr_sclass[2]+'_class_seats_numbers'))
    res_seats.remove(int(fpk_snbr_sclass[1]))
    setattr(flight, 'reserved_'+fpk_snbr_sclass[2]+'_class_seats_numbers', ','.join(str(i) for i in res_seats))
    flight.save()


@transaction.atomic
def add_reservation(data):
    fpk_snbr_sclass = data["fpk_snbr_sclass"].split('-')
    passenger=Passenger.objects.filter(nickname=data['login'])
    if len(passenger) == 0:
        msg='login %s does not exist' % (data['login'])
        return {'status': 'NOK', 'error_msg': msg }
    reservation = Reservation(
         reservation_id=data["fpk_snbr_sclass"],
         passenger=Passenger.objects.filter(nickname=data['login'])[0],
         status='Not Paid',
         seat_type=fpk_snbr_sclass[2],
         seat_number=int(fpk_snbr_sclass[1]),
    )
    try:
        reservation.save()
        flight = Flight.objects.filter(flight_number=fpk_snbr_sclass[0])[0]
        data = {
            'status': "OK",
            'flight_info': {
                'status': 'Not Paid',
                'res_num': data["fpk_snbr_sclass"],
                'destination': flight.destination,
                'date': flight.flight_date.strftime("%Y-%m-%d %H:%M:%S"),
                'seat_class': fpk_snbr_sclass[2],
                'seat_number': fpk_snbr_sclass[1],
                'price': getattr(flight, fpk_snbr_sclass[2]+'_class_seat_price'),
            }
        }
        return data
    except ValidationError, e:
        remove_from_flight(fpk_snbr_sclass)
        return {'status': 'NOK', 'error_msg': '; '.join(e.messages)}


@transaction.atomic
def remove_reservation(data):
    Reservation.objects.filter(reservation_id=data["fpk_snbr_sclass"]).delete()
    remove_from_flight(data["fpk_snbr_sclass"].split('-'))
    return {'status': 'OK'}


@transaction.atomic
def get_user_tickets(login):
    data = []
    user_reservations = Reservation.objects.filter(passenger=login)
    for res in user_reservations:
        fpk_snbr_sclass = res.reservation_id.split('-')
        flight = Flight.objects.filter(flight_number=fpk_snbr_sclass[0])[0]
        data.append({
            'status': res.status,
            'res_num': res.reservation_id,
            'destination': flight.destination,
            'date': flight.flight_date.strftime("%Y-%m-%d %H:%M:%S"),
            'seat_class': fpk_snbr_sclass[2],
            'seat_number': int(fpk_snbr_sclass[1]),
            'price': getattr(flight, fpk_snbr_sclass[2]+'_class_seat_price'),
        })
    return data


@transaction.atomic
def pay_for_ticket(ticket):
    reservation = Reservation.objects.filter(reservation_id=ticket)[0]
    reservation.status = 'Paid'
    reservation.save()
