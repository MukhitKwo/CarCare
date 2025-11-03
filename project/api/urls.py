from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import *

router = DefaultRouter()
router.register(r'carinfo', CarroViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('cronicIssues/', getCarCronicIssues),
    path('tabelaCarro/', tabelaCarro),  # POST
    path('tabelaCarro/<int:carro_id>/', tabelaCarro),  # GET, PUT, DELETE
]
