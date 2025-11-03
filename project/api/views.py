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


#! isto é uma tentativa para ter o crud para todas as tabelas sem estar a criar 5 funções enormes
#! e parace que funciona por agora
@csrf_exempt
def tabelaUtilizador(request, id=None):
    if request.method == "POST":
        return create_object(request, UtilizadorSerializer)

    elif request.method == "GET":
        return get_object(Utilizador, UtilizadorSerializer, "utilizador_id", id)

    elif request.method == "PUT":
        return update_object(request, Utilizador, UtilizadorSerializer, "utilizador_id", id)

    elif request.method == "DELETE":
        return delete_object(Utilizador, "utilizador_id", id)

    return JsonResponse({"error": "Method not allowed"}, status=405)


@csrf_exempt
def tabelaGaragem(request, id=None):
    if request.method == "POST":
        return create_object(request, GaragemSerializer)

    elif request.method == "GET":
        return get_object(Garagem, GaragemSerializer, "garagem_id", id)

    elif request.method == "PUT":
        return update_object(request, Garagem, GaragemSerializer, "garagem_id", id)

    elif request.method == "DELETE":
        return delete_object(Garagem, "garagem_id", id)

    return JsonResponse({"error": "Method not allowed"}, status=405)


@csrf_exempt
def tabelaCarro(request, id=None):
    if request.method == "POST":
        return create_object(request, CarroSerializer)

    elif request.method == "GET":
        return get_object(Carro, CarroSerializer, "carro_id", id)

    elif request.method == "PUT":
        return update_object(request, Carro, CarroSerializer, "carro_id", id)

    elif request.method == "DELETE":
        return delete_object(Carro, "carro_id", id)

    return JsonResponse({"error": "Method not allowed"}, status=405)


def create_object(request, Serializer):
    data = json.loads(request.body)  # recebe o json enviado no request
    serializer = Serializer(data=data)  # converte o json para o objeto do serializer
    if serializer.is_valid():  # verifica se os dados são válidos
        obj = serializer.save()  # guarda no BD
        return JsonResponse({"status": "created"}, status=201)  # resposta ok
    return JsonResponse(serializer.errors, status=400)  # erros de validação


def get_object(Model, Serializer, key_id, id):
    if id:  # se foi passado um id, significa que quer um objeto específico

        try:
            obj = Model.objects.get(**{key_id: id})  # procura o objeto com a chave primária correta
        except Model.DoesNotExist:
            return JsonResponse({"error": f"{Model.__name__} not found"}, status=404)  # não encontrou

        serializer = Serializer(obj)  # converte o objeto para json
        return JsonResponse(serializer.data, status=200)  # devolve o json

    objects = Model.objects.all()  # busca todos os registos
    serializer = Serializer(objects, many=True)  # converte todos para json
    return JsonResponse(serializer.data, safe=False, status=200)  # devolve lista de jsons


def update_object(request, Model, Serializer, key_id, id):
    if not id:  # sem id não há como atualizar
        return JsonResponse({"error": f"{key_id} required"}, status=400)

    try:
        obj = Model.objects.get(**{key_id: id})  # procura o objeto
    except Model.DoesNotExist:
        return JsonResponse({"error": f"{Model.__name__} not found"}, status=404)

    data = json.loads(request.body)  # recebe o json com os dados a atualizar
    serializer = Serializer(obj, data=data, partial=True)  # atualiza só os campos fornecidos
    if serializer.is_valid():  # valida
        serializer.save()  # guarda alterações
        return JsonResponse({"status": "updated"}, status=200)  # resposta ok

    return JsonResponse(serializer.errors, status=400)  # erro de validação


def delete_object(Model, key_id, id):
    if not id:  # sem id não há o que apagar
        return JsonResponse({"error": f"{key_id} required"}, status=400)

    try:
        obj = Model.objects.get(**{key_id: id})  # procura o objeto
    except Model.DoesNotExist:
        return JsonResponse({"error": f"{Model.__name__} not found"}, status=404)

    obj.delete()  # apaga o registo
    return JsonResponse({"status": "deleted"}, status=200)  # confirma eliminação
