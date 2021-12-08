from os import name
from django.urls import path
from .views import *

urlpatterns = [
    path('dashboard/',employ,name='dashboard'),
    path('',main,name='home'),
    path("signup/", SignUp.as_view(), name="signup"),
]
