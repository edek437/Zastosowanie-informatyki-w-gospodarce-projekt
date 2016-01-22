from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.lotnisko_test, name='index'),
    url(r'^reservation', views.reservation_test, name='reservation'),
    url(r'^flights', views.get_flights, name='flights'),
    url(r'^current_departues', views.get_current_departues, name='current_departues'),
    url(r'^user_login', views.user_login, name='user_login'),
    url(r'^user_dashboard', views.user_dashboard, name='user_dashboard'),
    url(r'^registration_page', views.registration_page, name='registration_page'),
    url(r'^add_passenger', views.add_passenger, name='add_passenger'),
    url(r'^flight_coordination', views.flight_coordination, name='flight_coordination'),
    url(r'^show_seats', views.show_seats, name='show_seats'),
    url(r'^reserve_tickets', views.reserve_tickets, name='reserve_tickets'),
    url(r'^change_personal_data', views.change_personal_data, name='change_personal_data'),
    url(r'^change_pw', views.change_pw, name='change_pw'),
    url(r'^get_my_tickets', views.get_my_tickets, name='get_my_tickets'),
    url(r'^cancel_reservation', views.cancel_reservation, name='cancel_reservation'),
    url(r'^purchase_reservation', views.purchase_reservation, name='purchase_reservation'),
    url(r'^get_fc_flights', views.get_fc_flights, name='get_fc_flights'),
    url(r'^get_flights_for_given_date', views.get_flights_for_given_date, name='get_flights_for_given_date'),
    url(r'^assign_flight_to_start_lane', views.assign_flight_to_start_lane, name='assign_flight_to_start_lane'),
    url(r'^remove_flight_from_start_lane', views.remove_flight_from_start_lane, name='remove_flight_from_start_lane'),
    url(r'^get_flight_lanes', views.get_flight_lanes, name='get_flight_lanes'),
    url(r'^get_unassigned_flights', views.get_unassigned_flights, name='get_unassigned_flights'),
]
