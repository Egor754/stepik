from django.shortcuts import render
from django.http import HttpResponseNotFound, HttpResponseServerError


def MainView(request):
    return render(request, 'tours/index.html')


def DepartureView(request, departure):
    return render(request, "tours/departure.html")


def TourView(request, id):
    return render(request, 'tours/tour.html')


def pageNotFound(request, exception):
    return HttpResponseNotFound('<h1>Страница не найдена</h1>')


def ServerError(request):
    return HttpResponseServerError('<h1>Извините, произошел '
                                   'внутрисистемный сбой</h1>')
