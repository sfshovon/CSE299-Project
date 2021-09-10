from django.urls import path
from . import views
urlpatterns =[
    path('view_oxygen_cylinders/',views.view_oxygen_cylinders, name="view_oxygen_cylinders"),
    path('cylinder_details/?P<keyy>[\w+]+',views.cylinder_details, name="cylinder_details"),
    path('request_form/?P<keyy>[\w+]+',views.request_form,name="request_form"),
    path('oxygen_request/',views.oxygen_request, name="oxygen_request"),      
]