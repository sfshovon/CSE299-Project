from django.urls import path
from . import views

urlpatterns = [
    path('bd/', views.covid19_bd, name="bd" ),
    path('world/', views.covid19_world, name="world"),
]