from django.urls import path
from . import views

urlpatterns = [
    path('bd/', views.covid19_bd, name="bd" ),
    path('world/', views.covid19_world, name="world"),
    path('cases/', views.country_cases, name="cases"),
    path('AT/', views.all_treatments, name="AT" ),
    path('AV/', views.all_vaccines, name="AV" ),
    path('ambulance/', views.ambulance, name="ambulance"), 
    path('oc/', views.oxygen_cylinder, name="oc"), 
    path('tp/', views.test_place, name="tp"),
    path('tc/', views.test_center, name="tc"),
    path('ib/', views.icu_bed, name="ib"), 
    path('ch/', views.covid_hotline, name="ch"), 
  
]