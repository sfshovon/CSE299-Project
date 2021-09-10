from django.conf.urls import url
from django.urls import path
from . import views

urlpatterns =[
    path('doc_list/',views.doctor_list, name="doc_list"),
    path('/doc_profile/?P<keyy>[\w+]+',views.doctor_profile_view, name="doc_profile"),
]



























