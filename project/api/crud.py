from django.http import JsonResponse
import json


def crud(request, model, serializer, id=None):
    """
    O CRUD deteta automaticamente o tipo de request e retorna o json correspondente
    """

    if request.method == "POST":
        return create_object(request, serializer)  # valores necessarios para o POST

    elif request.method == "GET":
        return get_object(model, serializer, id)  # valores necessarios para o GET

    elif request.method == "PUT":
        return update_object(request, model, serializer, id)  # valores necessarios para o PUT

    elif request.method == "DELETE":
        return delete_object(model, id)  # valores necessarios para o DELETE

    return JsonResponse({"error": "Method not allowed"}, status=405)


#! ================== Funções CRUD ==================

def create_object(request, Serializer):

    data = json.loads(request.body)  # recebe o json enviado no request
    serializer = Serializer(data=data)  # converte o json para o objeto do serializer

    if serializer.is_valid():  # verifica se os dados são válidos
        obj = serializer.save()  # guarda no BD
        return JsonResponse({"status": "created"}, status=201)  # resposta ok
    return JsonResponse(serializer.errors, status=400)  # erros de validação


def get_object(Model, Serializer, id):

    if id:  # se foi passado um id, significa que quer um objeto específico

        try:
            pk_id = Model._meta.pk.name
            obj = Model.objects.get(**{pk_id: id})  # procura o objeto com a chave primária correta
        except Model.DoesNotExist:
            return JsonResponse({"error": f"{Model.__name__} not found"}, status=404)  # não encontrou

        serializer = Serializer(obj)  # converte o objeto para json
        return JsonResponse(serializer.data, status=200)  # devolve o json

    objects = Model.objects.all()[:100] # busca todos os primeiros 100 registos
    serializer = Serializer(objects, many=True)  # converte todos para json
    return JsonResponse(serializer.data, safe=False, status=200)  # devolve lista de jsons


def update_object(request, Model, Serializer, id):

    if not id:  # sem id não há como atualizar
        return JsonResponse({"error": f"Primary key required"}, status=400)

    try:
        pk_id = Model._meta.pk.name
        obj = Model.objects.get(**{pk_id: id})  # procura o objeto
    except Model.DoesNotExist:
        return JsonResponse({"error": f"{Model.__name__} not found"}, status=404)

    data = json.loads(request.body)  # recebe o json com os dados a atualizar
    serializer = Serializer(obj, data=data, partial=True)  # atualiza só os campos fornecidos
    if serializer.is_valid():  # valida
        serializer.save()  # guarda alterações
        return JsonResponse({"status": "updated"}, status=200)  # resposta ok
    else:
        return JsonResponse(serializer.errors, status=400)  # erro de validação


def delete_object(Model, id):

    if not id:  # sem id não há o que apagar
        return JsonResponse({"error": f"Primary key required"}, status=400)

    try:
        pk_id = Model._meta.pk.name
        obj = Model.objects.get(**{pk_id: id})  # procura o objeto
    except Model.DoesNotExist:
        return JsonResponse({"error": f"{Model.__name__} not found"}, status=404)

    obj.delete()  # apaga o registo
    return JsonResponse({"status": "deleted"}, status=200)  # confirma eliminação
