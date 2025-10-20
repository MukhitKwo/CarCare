from django.shortcuts import render
import requests
from .forms import CarInfoForm


def hello(request):

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

    return render(request, 'display.html', {'form': form})
