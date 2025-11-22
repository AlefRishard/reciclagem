from django.contrib import admin
from .models import Endereco

@admin.register(Endereco)
class EnderecoAdmin(admin.ModelAdmin):
    # Mostra colunas úteis na lista
    list_display = ('rua', 'numero', 'bairro', 'cidade', 'status_ponto')
    
    # Barra de busca
    search_fields = ('rua', 'bairro', 'cidade')
    
    # Filtro lateral
    list_filter = ('cidade',)

    # Cria uma coluna calculada para mostrar se o Ponto foi criado
    def status_ponto(self, obj):
        if obj.ponto:
            return "Gerado"
        return "Pendente"
    status_ponto.short_description = "Geometria"