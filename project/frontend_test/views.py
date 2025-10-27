from django.shortcuts import render
import requests
from .forms import CarInfoForm


def addCar(request):

    if request.method == "POST":
        form = CarInfoForm(request.POST)

        if form.is_valid():
            dataForm = form.cleaned_data

            brand = dataForm["brand"].capitalize()
            model = dataForm["model"].capitalize()
            year = dataForm["year"]
            car_model = f"{brand} {model} {year}"

            cronicIssues = requests.get(
                'http://127.0.0.1:8001/api/cronicIssues/',
                params={'car': car_model}
            )

            data = {
                "brand": brand,
                "model": model,
                "year": year,
                "cronic": cronicIssues.json()
            }
            # print("Data:", data)

            res = requests.post('http://127.0.0.1:8001/api/carinfo/', json=data)

            if cronicIssues.status_code == 200:
                print("Cronic Issues Status: 200 (Gemini data retrieved)")
            else:
                print(f"Cronic Issues Status: Failed ({cronicIssues.status_code})")

            if res.status_code == 201:
                print("Car Info Status: 201 (Database received data)")
            else:
                print(f"Car Info Status: Failed ({res.status_code})")

    else:
        form = CarInfoForm()

    return render(request, 'addCars.html', {'form': form})


def showCar(request):

    res = requests.get('http://127.0.0.1:8001/api/carinfo/')
    res.raise_for_status()
    cars = res.json()

    return render(request, 'showCars.html', {'cars': cars})
