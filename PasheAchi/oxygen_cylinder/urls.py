from django.conf.urls import url
from django.urls import path
from . import views

urlpatterns =[
    path('view_oxygen_cylinders/',views.view_oxygen_cylinders, name="view_oxygen_cylinders"),
    
]