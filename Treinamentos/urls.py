from django.urls import path
from . import views

urlpatterns = [
    path('ver_Treinamentos/', views.ver_treinamentos, name="ver_TreinamentoS")



]