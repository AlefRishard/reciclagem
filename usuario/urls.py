# Em usuario/urls.py

from django.urls import path
from . import views
from django.contrib.auth import views as auth_views


urlpatterns = [
    
    # Rota para PROCESSAR o formulário de cadastro
    path('cadastrar/', views.cadastrar, name='cadastrar'),
    
    # Rota para o LOGIN, usando a SUA view customizada
    path('login/', views.login_view, name='login'),
    
    # Rota para o LOGOUT, usando a view pronta do Django
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
]