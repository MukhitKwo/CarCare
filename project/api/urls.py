from django.urls import path
from .views import ProcessItemView

urlpatterns = [
    path('process-item/', ProcessItemView.as_view(), name='process-item'), # (da ctrl + click no 'ProcessItemView)
]