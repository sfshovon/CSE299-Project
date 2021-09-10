from django.urls import path
from . import views
urlpatterns =[
    path('view_icu_beds/',views.view_icu_beds, name="view_icu_beds"),
    path('icu_details/?P<keyy>[\w+]+',views.icu_details, name="icu_details"),   
]