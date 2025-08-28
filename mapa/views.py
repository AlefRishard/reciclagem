from django.shortcuts import render
from django.contrib.auth.decorators import login_required 
# Create your views here.

@login_required
def mostrar_mapa(request):
    return render(request, 'mapa/mapa.html')