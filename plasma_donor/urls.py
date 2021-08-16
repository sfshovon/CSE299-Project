from django.urls import path
from . import views

urlpatterns = [
    path('become_donor/', views.become_donor, name = "become_donor"),
    path('eligibility/', views.eligibility, name = "eligibility"),
    path('add_donor/', views.add_donor, name = "add_donor"),
]