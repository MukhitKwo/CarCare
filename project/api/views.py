from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework import viewsets
from .models import *
from .serializers import *
from .gemini import geminiCronicIssues
import json


class CarInfoViewSet(viewsets.ModelViewSet):
    queryset = Carro.objects.all()
    serializer_class = CarInfoSerializer


def getCarCronicIssues(request):
    car = request.GET.get("car")
    # print("Car:", car)
    data = geminiCronicIssues(car)
    if data is None:
        return JsonResponse({"error": "Failed to get car issues"}, status=500)
    return JsonResponse(data, safe=False, json_dumps_params={"ensure_ascii": False, "indent": 2})

# ! para enviar para basedados
#  res = requests.post('http://127.0.0.1:8001/api/carinfo/', json=data)


@csrf_exempt
def adicionarCarro(request):
    if request.method == "POST":
        try:
            # Parse JSON body
            data = json.loads(request.body)
            print(data)  # prints the received data
        except json.JSONDecodeError:
            return JsonResponse({"error": "Invalid JSON"}, status=400)
        return JsonResponse({"status": "received"}, status=201)
    return JsonResponse({"error": "Only POST allowed"}, status=405)
