from django.conf.urls import url
from django.urls import path
from . import views

urlpatterns =[
    path('DoctorList/',views.doctor_list, name="DoctorList"),
]

























