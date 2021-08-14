from django.conf.urls import url
from django.urls import path
from . import views

urlpatterns =[
    path('view_icu_beds/',views.view_icu_beds, name="view_icu_beds"),
    
]