from django.urls import path
from . import views

urlpatterns = [
    path('cad_endereco/', views.cad_endereco, name='cad_endereco'),
    path('novo/', views.criar_endereco, name='criar_endereco'),
]