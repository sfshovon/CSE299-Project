from django.urls import path
from . import views
urlpatterns =[
    path('BDnews/',views.news, name="BDnews"),
    path('vaccine/',views.vaccine_news, name="vaccine_news"),   
]