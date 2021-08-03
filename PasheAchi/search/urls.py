from django.conf.urls import url
from django.urls import path
from . import views

urlpatterns =[
    path('search_blog_post/',views.search_blog_post, name="search_blog_post"),
    path('searchnotfound/',views.search_not_found, name="searchnotfound"),
]

