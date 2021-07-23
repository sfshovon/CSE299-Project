from django.conf.urls import url
from django.urls import path
from . import views

urlpatterns =[
    path('docList/',views.doctor_list, name="doc_list"),
    path('docProfile/',views.doctor_profile_view, name="doc_profile"),
]

























