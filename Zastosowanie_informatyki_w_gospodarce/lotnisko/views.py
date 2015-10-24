from django.shortcuts import render

# Create your views here.


def lotnisko_test(request):
    print "Django say something"
    return render(request, "lotnisko/test.html", {})
