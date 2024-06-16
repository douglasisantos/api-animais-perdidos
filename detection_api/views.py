from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse("Olá, mundo. Esta é a página inicial da minha API.")