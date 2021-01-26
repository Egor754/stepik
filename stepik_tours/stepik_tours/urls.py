from django.contrib import admin
from django.urls import path
from tours.views import MainView, DepartureView,\
    TourView, pageNotFound, ServerError

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', MainView),
    path('departure/<str:departure>/', DepartureView),
    path('tour/<int:id>/', TourView),
]
handler404 = pageNotFound
handler500 = ServerError
