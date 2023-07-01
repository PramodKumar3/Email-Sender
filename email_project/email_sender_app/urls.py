from django.urls import path, include
from rest_framework import routers
from . import views

urlpatterns = [
    path('email', views.email,name="email"),
    path('',views.index,name="index"),
]