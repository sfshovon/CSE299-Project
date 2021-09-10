from django.conf.urls import url
from django.urls import path
from . import views

urlpatterns =[
    path('search_page/',views.search_page, name="search_page"),
    path('search_blog_post/',views.search_blog_post, name="search_blog_post"),
    path('searchnotfound/',views.search_not_found, name="searchnotfound"),
    path('search_doctors/',views.search_doctors, name="search_doctors"),
]

