from django import views
from django.urls import path
from .views import hello

from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import *

router = DefaultRouter()
router.register(r'carinfo', CarInfoViewSet)

urlpatterns = [
    path('hello/', hello),
    path('', include(router.urls)),
    path('getinfo/', getinfo)
]