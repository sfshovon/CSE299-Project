from django.urls import path
from . import views

urlpatterns = [
    path('bd/', views.covid19_bd, name="bd" ),
    path('world/', views.covid19_world, name="world"),
    path('news/', views.news, name="news"),
    path('FAv/', views.FDA_approved_vaccines, name="FAv"),
    path('FAt/', views.FDA_approved_treatments, name="FAt"),
    path('AT/', views.all_treatments, name="AT" ),
    path('AV/', views.all_vaccines, name="AV" ),
  
]