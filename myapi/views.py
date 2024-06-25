
# views.py
from django.shortcuts import render, redirect
from django.http import HttpResponse
from detection_api.forms import AnimalPerdidoForm
from .detecao_objetos_yolo import detectar_objetos  # Importe a função detectar_objetos
from detection_api.models import AnimalPerdido
from detection_api.serializers import AnimalPerdidoSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from django.views.decorators.http import require_POST
from rest_framework.views import APIView
from django.db.models import Q


def index(request):
    # Busque todos os animais perdidos no banco de dados
    animais_perdidos = AnimalPerdido.objects.all()
    # Passe os animais perdidos para o template
    return render(request, 'index.html', {'animais_perdidos': animais_perdidos})

def limpar_animais_perdidos(request):
    # Verifique se o método da solicitação é POST
    if request.method == 'POST':
        # Limpar os dados dos animais perdidos
        AnimalPerdido.objects.all().delete()
        return HttpResponse('Os dados dos animais perdidos foram limpos com sucesso.')
    else:
        # Se a solicitação não for POST, retorne um erro
        return HttpResponse('A solicitação deve ser do tipo POST.')  


def enviar_animal_perdido(request):
    if request.method == 'POST':
        form = AnimalPerdidoForm(request.POST, request.FILES)
        if form.is_valid():
            nome = form.cleaned_data['nome']
            tipo = form.cleaned_data['tipo']
            foto = form.cleaned_data['foto']

            # Chama a função para detectar objetos na imagem
            resultados = detectar_objetos(foto)

            # Salva o novo animal perdido no banco de dados
            novo_animal = AnimalPerdido(nome=nome, raca=resultados['objetos_detectados'][0], tipo=tipo, foto=foto)
            novo_animal.save()

            # Verifica se há animais detectados na imagem e se há animais perdidos semelhantes
            if 'objetos_detectados' in resultados and resultados['objetos_detectados']:
                animais_perdidos_semelhantes = []
                for animal_detectado in resultados['objetos_detectados']:
                    # Busca animais perdidos semelhantes com base no tipo de animal detectado
                    animais_encontrados = AnimalPerdido.objects.filter(raca=animal_detectado, tipo=tipo)
                    animais_perdidos_semelhantes.extend(animais_encontrados)

                # Remove o novo animal da lista de animais semelhantes, se estiver presente
                animais_perdidos_semelhantes = [animal for animal in animais_perdidos_semelhantes if animal != novo_animal]

                # Retorna para a página de sucesso com a lista de animais semelhantes
                return render(request, 'envio_sucesso.html', {'animais_perdidos_semelhantes': animais_perdidos_semelhantes})

            # Retorna para a página de sucesso sem a lista de animais semelhantes
            return render(request, 'envio_sucesso.html', {'novo_animal': novo_animal})
    else:
        form = AnimalPerdidoForm()
    return render(request, 'enviar_animal_perdido.html', {'form': form})



