from django.urls import path
from . import views

urlpatterns = [
    path('appoints/', views.appointments, name = "viewAppointments"),
    path('cancelAppointments/<int:appointmentIdList>/',views.cancel_appointment, name = "cancelAppointments")
]