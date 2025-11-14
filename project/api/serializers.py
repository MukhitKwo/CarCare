from rest_framework import serializers
from .models import *
from django.contrib.auth import get_user_model

User = get_user_model()


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
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
