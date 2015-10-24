from django.conf.urls import url
from . import views

urlpatterns = [
    # TODO: add test url
    url(r'^$', views.lotnisko_test, name='index'),
]

