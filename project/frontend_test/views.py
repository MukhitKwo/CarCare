from django.shortcuts import render

# Create your views here.

from api.utils import process_values  # reuse API logic
from api.models import Item  # importar o modelo Item

def display_values(request):
    
    # Item.objects acede à tabela Items na base de dados
    # .all() diz para devolver todas as linhas da tabela
    # order_by('-id) ordernar por id decrescente ( '-' diz recente -> antigo)
    processed = Item.objects.all().order_by('-id')

    return render(request, 'frontend_test/display.html', {'processed': processed})
