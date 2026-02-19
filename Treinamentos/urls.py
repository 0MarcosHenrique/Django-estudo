from django.urls import path
from . import views

urlpatterns = [
    path('ver_treinamentos/', views.ver_treinamentos, name="ver_treinamentoS"),
    path('inserir_treinamentos/', views.inserir_treinamentos, name="inserir_treinamentos")

]