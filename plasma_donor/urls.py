from django.urls import path
from . import views

urlpatterns = [
    path('become_donor/', views.become_donor, name = "become_donor"),
    path('eligibility/', views.eligibility, name = "eligibility"),
    path('add_donor/', views.add_donor, name = "add_donor"),
    path('donor_list/', views.donor_list, name = "donor_list"),
    path('a_positive/', views.a_positive, name = "a_positive"),
    path('a_negative/', views.a_negative, name = "a_negative"),
    path('b_positive/', views.b_positive, name = "b_positive"),
    path('b_negative/', views.b_negative, name = "b_negative"),
    path('ab_positive/', views.ab_positive, name = "ab_positive"),
    path('ab_negative/', views.ab_negative, name = "ab_negative"),
    path('o_positive/', views.o_positive, name = "o_positive"),
    path('o_negative/', views.o_negative, name = "o_negative"),
    path('add_donor/', views.add_donor, name = "add_donor"),
    path('donor_details/', views.donor_details, name = "donor_details"),
]