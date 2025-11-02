from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import *

router = DefaultRouter()
router.register(r'carinfo', CarInfoViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('cronicIssues/', getCarCronicIssues),
    path('adicionarCarro/', adicionarCarro),
]
