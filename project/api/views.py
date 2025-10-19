from django import views
from django.http import JsonResponse
from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import *
from .serializers import *
import requests

# # Create your views here.
def hello(request):
    return JsonResponse({'message': 'Isto é uma mensage retornada por api.views.hello'})

class CarInfoViewSet(viewsets.ModelViewSet):
    queryset = CarInfo.objects.all()
    serializer_class = CarInfoSerializer
    # print("HEY: ",serializer_class)

@api_view(['GET'])
def getinfo(request):
    resp = requests.get("http://127.0.0.1:8001/api/carinfo/")
    data = resp.json()
    print(data)
    return Response(data)

