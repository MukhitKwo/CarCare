from django.shortcuts import render
from httpx import get
import requests
from .forms import *
from utils.res_status import *


def createCarroView(request):

    form = createCarroForm(request.POST or None)

    if form.is_valid():

        carInfo = form.cleaned_data
        carInfo["garagem"] = "1"

        res = requests.post('http://127.0.0.1:8001/api/tabelaCarro/', json=carInfo)
        print_status(res)

    return render(request, 'demo/createCarro.html', {'form': form})


def getCarroView(request):
    oneCar = None
    multipleCars = None

    form = getCarroForm(request.POST or None)

    if form.is_valid():
        car_id = request.POST.get("id")
        if car_id:
            res = requests.get(f'http://127.0.0.1:8001/api/tabelaCarro/{car_id}/')
            oneCar = res.json()
        else:
            res = requests.get('http://127.0.0.1:8001/api/tabelaCarro/')
            multipleCars = res.json()

    return render(request, 'demo/getCarro.html', {"form": form, 'oneCar': oneCar, "multipleCars": multipleCars})


def updateCarroView(request):
    pass


def deleteCarroView(request):
    pass
