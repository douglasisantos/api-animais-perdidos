from django import forms
from .models import AnimalPerdido

class AnimalPerdidoForm(forms.ModelForm):
    class Meta:
        model = AnimalPerdido
        fields = ['nome', 'raca', 'tipo', 'foto','endereco']

