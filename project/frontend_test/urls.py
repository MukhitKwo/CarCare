from django.urls import path
from .views import hello

urlpatterns = [
    path('car/', hello, name='display-values'),
]
