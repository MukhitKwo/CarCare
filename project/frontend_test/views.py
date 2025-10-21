from django.shortcuts import render
import requests
from .forms import CarInfoForm


def addCar(request):

    if request.method == "POST":
        form = CarInfoForm(request.POST)

        if form.is_valid():
            data = form.cleaned_data

            data['brand'] = data['brand'].capitalize()
            data['model'] = data['model'].capitalize()

            print("Data:", data)

            res = requests.post('http://127.0.0.1:8001/api/carinfo/', json=data)

            if res.status_code == 201:
                print("Status: good")
            else:
                print("Status: bad")
    else:
        form = CarInfoForm()

    return render(request, 'addCars.html', {'form': form})

def showCar(request):
    try:
        res = requests.get('http://127.0.0.1:8001/api/carinfo/', timeout=5)
        res.raise_for_status()
        cars = res.json()
        print(cars)
    except requests.RequestException as e:
        print("Request error:", e)
        cars = []
    except ValueError as e:
        print("JSON decode error:", e)
        cars = []

    

    return render(request, 'showCars.html', {'cars': cars})
