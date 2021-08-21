"""PasheAchi URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from DoctorList import views

urlpatterns = [
    path('admin/', admin.site.urls), 
    path('',views.home,name="home"),
    path('doc_list/',views.doctor_list, name="doc_list"),
    path('doc_profile/?P<keyy>[\w+]+',views.doctor_profile_view, name="doc_profile"),  
    path('search/', include('search.urls')),
    path('covidnews/', include('news.urls')),
    path('icubed/',include('icubed.urls')),
    path('oxygen_cylinder/',include('oxygen_cylinder.urls')),

]





























