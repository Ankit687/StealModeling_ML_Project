from django.urls import path

from Alloy import views

urlpatterns = [
    path('', views.index),
    path('signup/', views.register),
    path('login/', views.login),
    path('logout/', views.logout)
]