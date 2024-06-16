# detection_api/serializers.py

from rest_framework import serializers
from .models import AnimalPerdido

class AnimalPerdidoSerializer(serializers.ModelSerializer):
    class Meta:
        model = AnimalPerdido
        fields = ['nome', 'tipo', 'foto']