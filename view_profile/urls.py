from django.urls import path
from . import views

urlpatterns = [
    path('VP/', views.view_profile, name = "VP"),
    path('DP/', views.delete_profile, name = "DP"),
    path('update_profile',views.update_profile, name="update_profile"),
    path('update_img_url',views.update_img_url, name="update_img_url"),
    path('EP/', views.edit_profile, name = "EP"),
]