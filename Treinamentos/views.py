from django.shortcuts import render
from django.http import HttpResponse

def ver_treinamentos(request):
    return HttpResponse('Olá mundo!')