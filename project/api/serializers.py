from rest_framework import serializers
from .models import *


class UtilizadorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Utilizador
        fields = '__all__'


class GaragemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Garagem
        fields = '__all__'


class CarroSerializer(serializers.ModelSerializer):
    class Meta:
        model = Carro
        fields = '__all__'


class ManutencaoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Manutencao
        fields = '__all__'


class CronicoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cronico
        fields = '__all__'
