from django.urls import path
from .views import *
from project.api import views

urlpatterns = [
    path('process-item/', ProcessItemView.as_view(), name='process-item'), # (da ctrl + click no 'ProcessItemView)
    path('hello/', views.hello_world),
]