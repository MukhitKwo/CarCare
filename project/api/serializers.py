from rest_framework import serializers
from .models import *

class CarroSerializer(serializers.ModelSerializer):
    class Meta:
        model = Carro
        fields = '__all__'