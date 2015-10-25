from django.conf.urls import url
from . import views

urlpatterns = [
    # TODO: add test url
    url(r'^$', views.lotnisko_test, name='index'),
    url(r'^mySchedule', views.schedule_test, name='schedule'),
    url(r'^reservation', views.reservation_test, name='reservation'),
]

