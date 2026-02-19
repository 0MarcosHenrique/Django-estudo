from django.shortcuts import render
from django.http import HttpResponse

def ver_treinamentos(request):
    nome = 'Marcos'
    return render (request, 'ver_treinamentos.html', {'nome': nome})

def inserir_treinamentos(request):
    return HttpResponse ("Estou no inserir")