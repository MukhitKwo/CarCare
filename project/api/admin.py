from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(Utilizador)
admin.site.register(Garagem)
admin.site.register(Carro)
admin.site.register(Manutencao)
admin.site.register(Cronico)