from django.shortcuts import render
import requests
from .forms import CarInfoForm


def addCar(request):

    if request.method == "POST":

        form = CarInfoForm(request.POST)

        if form.is_valid():

            carInfo = form.cleaned_data
            res = requests.post('http://127.0.0.1:8001/api/adicionarCarro/', json=carInfo)
            print(f"AdicionarCarro Status: {res.status_code}")
    else:
        form = CarInfoForm()

    return render(request, 'addCars.html', {'form': form})


def showCar(request):

    res = requests.get('http://127.0.0.1:8001/api/carinfo/')
    res.raise_for_status()
    cars = res.json()

    return render(request, 'showCars.html', {'cars': cars})
