from django.urls import path
from .views import *

urlpatterns = [
    path('addcar/', addCar, name='addCar'),
    path('showcar/', showCar, name='showCar'),
]
