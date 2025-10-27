from django.http import JsonResponse
from rest_framework import viewsets
from .models import CarInfo
from .serializers import CarInfoSerializer
from django.http import JsonResponse
from .gemini import geminiCronicIssues

# # Create your views here.


def hello(request):
    return JsonResponse({'message': 'Isto é uma mensage retornada por api.views.hello'})


class CarInfoViewSet(viewsets.ModelViewSet):
    queryset = CarInfo.objects.all()
    serializer_class = CarInfoSerializer


def getCarCronicIssues(request):
    car = request.GET.get("car")
    # print("Car:", car)
    data = geminiCronicIssues(car)
    if data is None:
        return JsonResponse({"error": "Failed to get car issues"}, status=500)
    return JsonResponse(data, safe=False, json_dumps_params={"ensure_ascii": False, "indent": 2})
