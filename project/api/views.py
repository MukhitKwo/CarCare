from django.http import JsonResponse
from django.shortcuts import render

# # Create your views here.
def hello(request):
    return JsonResponse({'message': 'Isto é uma mensage retornada por api.views.hello'})

# from rest_framework.views import APIView
# from rest_framework.response import Response
# from .models import Item
# from .serializers import ItemSerializer
# from .utils import process_values

# def hello_world(request):
#     return JsonResponse({"message":"Hello from Django brother"})

# class ProcessItemView(APIView):
#     def post(self, request):

#         values = request.data.get('values', [])  # recebe os valores em json
#         values = [int(v) for v in values]  # transfroma em lista

#         processed = process_values(values)  # dobra os valores (da ctrl + click na funçaõ)

#         # salva no novo valor na base dados (db.spqlite3), tabela Item (api_item)
#         items = [Item.objects.create(value=v) for v in processed]

#         serializer = ItemSerializer(items, many=True)  # converte o objeto Item com o valor dobrado para JSON
#         return Response(serializer.data)  # retorna o JSON
