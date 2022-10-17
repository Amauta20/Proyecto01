from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def saludar(request): #Consulta o petición
    return HttpResponse("Hola Mi primer app")

def saludar2(request):
    return HttpResponse("Mi segundo saludo")

def saluda_a(request, nombre):
    return HttpResponse(f"Hola como te va {nombre}")

def mostrartemplate(request):
    return render(request, 'modulo01/index.html')
