from django.urls import path
from . import views

urlpatterns = [
    path('appForm/', views.appointment_form, name = "appForm"),
    path('createAppointment/', views.create_appointment, name = "createAppointment"),
]