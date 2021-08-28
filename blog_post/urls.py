from django.urls import path
from . import views

urlpatterns = [
    path('home_page/', views.home_page, name = "home_page"),
    path('add_post/', views.add_post, name = "add_post"),
    path('post_details/<int:timeStampList>/', views.post_details, name = "post_details"),
    path('comment/<int:timeStampList>/', views.comment, name = "comment"),
    path('like/<int:timeStampList>/', views.like, name = "like"),
    path('timeline/', views.timeline, name = "timeline"),
    path('delete_post/<int:postIdList>/', views.delete_post, name = "delete_post"),
]
