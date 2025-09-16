from django.urls import path, include
from . import views

urlpatterns = [
    path('mapa/',views.mostrar_mapa, name='mapa'),
    path('ponto/', include('ponto.urls')),

]