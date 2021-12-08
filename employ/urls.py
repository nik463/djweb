from os import name
from django.urls import path
from .views import *

urlpatterns = [
    path('dashboard/',employ,name='employlogin'),
    path('',main,name='sigin')
]
