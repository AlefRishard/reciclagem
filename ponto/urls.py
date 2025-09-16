from django.urls import path
from . import views as v

app_name = 'ponto'

urlpatterns = [
    path('geojson/', v.PontoGeojson.as_view(), name='ponto-geojson'),
    path('pontos.js/', v.pontos_js, name='pontos_js'),
]