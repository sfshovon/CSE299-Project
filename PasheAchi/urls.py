"""PasheAchi URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from login_register import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.login, name="login"),
    path('post_login/', views.post_login, name="post_login"),
    path('home/', views.home, name="home"),
    path('google_login/', views.google_login, name="google_login"),
    path('user_signup/', views.user_signup, name="user_signup"),
    path('user_post_signup/', views.user_post_signup, name="user_post_signup"),
    path('logout/', views.logout, name="logout"), 
    path('forget_password/', views.forget_password, name = "forget_password"),   
    path('scrapper/', include('scrapper.urls')),
    path('vprofile/', include('view_profile.urls')),
]
