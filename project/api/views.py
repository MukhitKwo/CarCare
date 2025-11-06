from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework import viewsets
from .models import *
from .serializers import *
from .gemini import geminiCronicIssues
from .crud import crud


class CarroViewSet(viewsets.ModelViewSet):
    queryset = Carro.objects.all()
    serializer_class = CarroSerializer


def getCarCronicIssues(request):
    car = request.GET.get("car")
    # print("Car:", car)
    data = geminiCronicIssues(car)
    if data is None:
        return JsonResponse({"error": "Failed to get car issues"}, status=500)
    return JsonResponse(data, safe=False, json_dumps_params={"ensure_ascii": False, "indent": 2})


@csrf_exempt
def tabelaCarro(request, id=None):
    return crud(request, Carro, CarroSerializer, id)


@csrf_exempt
def tabelaGaragem(request, id=None):
    return crud(request, Garagem, GaragemSerializer, id)
    # garagem__user=request.user


@csrf_exempt
def tabelaUtilizador(request, id=None):
    return crud(request, Utilizador, UtilizadorSerializer, id)
