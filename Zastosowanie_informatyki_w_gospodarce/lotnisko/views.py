from django.shortcuts import render

# Create your views here.


def lotnisko_test(request):
    print "Django say something"
    return render(request, "lotnisko/lotnisko_main_page.html", {})


def schedule_test(request):
    name = 'Adrian'  # Test passing variables to html
    print "Schedule testing"
    return render(request, "lotnisko/schedule.html", {'name': name, 'user': request.user})  # TODO: w klamrach powiniem podac uzytkownika ktory chce zobaczyc schdule


def reservation_test(request):
    print "Reservation testing"
    return render(request, "lotnisko/reservation_page.html", {})
