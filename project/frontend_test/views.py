from django.shortcuts import render
import requests
from .forms import CarInfoForm
from utils.res_status import *


def addCar(request):

    if request.method == "POST":

        form = CarInfoForm(request.POST)

        if form.is_valid():

            carInfo = form.cleaned_data
            carInfo["garagem"] = "1"

            res = requests.post('http://127.0.0.1:8001/api/tabelaCarro/', json=carInfo)
            print_status(res)
            print(res.text)
    else:
        form = CarInfoForm()

    return render(request, 'addCars.html', {'form': form})


def showCar(request):

    res = requests.get('http://127.0.0.1:8001/api/tabelaCarro/1/')
    print_status(res)
    cars = res.json()
    

    return render(request, 'showCars.html', {'cars': cars})
