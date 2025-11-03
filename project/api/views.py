from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import requests
from rest_framework import viewsets
from .models import *
from .serializers import *
from .gemini import geminiCronicIssues
import json


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

# TODO Tornar a função universal (todas as tabelas)
@csrf_exempt
def tabelaCarro(request, carro_id=None):

    if request.method == "POST":
        # ----- CREATE -----
        data = json.loads(request.body)  # obtem as informações todas necessarias para criar um carro em json
        serializer = CarroSerializer(data=data)  # converte json para Objeto
        if serializer.is_valid():
            carro = serializer.save() # salva o carro na tabela
            return JsonResponse({"status": "created", "carro_id": carro.carro_id}, status=201)
        else:
            return JsonResponse(serializer.errors, status=400)

    elif request.method == "GET":
        # ----- READ -----
        if carro_id:  # verifica se carro_id tem valor, caso tenha, significa que procura um valor especifico
            try:
                carro = Carro.objects.get(carro_id=carro_id)  # tenta encotrar o carro com tal id
            except Carro.DoesNotExist:
                return JsonResponse({"error": "Car not found"}, status=404)  # caso nao encotre, dá erro

            serializer = CarroSerializer(carro)  # converte para json
            return JsonResponse(serializer.data, status=200)  # retorna o json com os valores todos
        else:
            carros = Carro.objects.all()  # retorna todos os carros
            serializer = CarroSerializer(carros, many=True)  # converte os carros todos para jsons
            return JsonResponse(serializer.data, safe=False, status=200)  # retorna os jsons todos

    elif request.method == "PUT":
        # ----- UPDATE -----
        if not carro_id:
            return JsonResponse({"error": "carro_id required"}, status=400)  # caso não tenha id, dá erro
        try:
            carro = Carro.objects.get(carro_id=carro_id)  # tenta encotrar o carro com tal id
        except Carro.DoesNotExist:
            return JsonResponse({"error": "Car not found"}, status=404)  # caso não encontre, dá erro

        data = json.loads(request.body)  # recebe o json do request
        serializer = CarroSerializer(carro, data=data, partial=True)  # converte json para Objeto
        if serializer.is_valid():
            updated_carro = serializer.save()  # salva por cima do carro antigo
            return JsonResponse({"status": "updated", "carro_id": updated_carro.carro_id}, status=200)
        else:
            return JsonResponse(serializer.errors, status=400)

    elif request.method == "DELETE":
        # ----- DELETE -----
        if not carro_id:
            return JsonResponse({"error": "carro_id required"}, status=400)  # caso não tenha id, dá erro
        try:
            carro = Carro.objects.get(carro_id=carro_id)  # tenta encotrar o carro com tal id
        except Carro.DoesNotExist:
            return JsonResponse({"error": "Car not found"}, status=404)

        carro.delete()  # apaga o carro na tabela
        return JsonResponse({"status": "deleted", "carro_id": carro_id}, status=200)

    else:
        return JsonResponse({"error": "Method not allowed"}, status=405)
