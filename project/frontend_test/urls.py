from django.urls import path
from frontend_test.views import display_values

urlpatterns = [
    path('', display_values, name='display-values'),
]
