from django.shortcuts import render
from django.http import HttpResponseNotFound, HttpResponseServerError


def MainView(request):
    return render(request, 'tours/index.html')


def DepartureView(request, departure):
    departures = {"msk": "Из Москвы", "spb": "Из Петербурга",
                  "nsk": "Из Новосибирска", "ekb": "Из Екатеринбурга",
                  "kazan": "Из Казани"}
    if departure not in departures:
        return HttpResponseNotFound(f"Нет тура с направлением {departure}")
    return render(request, "tours/departure.html", context=departures)


def TourView(request, id):
    return render(request, 'tours/tour.html')
