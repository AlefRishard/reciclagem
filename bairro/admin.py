from django.contrib import admin
from .models import Bairro 
from leaflet.admin import LeafletGeoAdmin

@admin.register(Bairro)
class BairroAdmin(LeafletGeoAdmin):
    list_display = ('nome', 'globalid', 'geom',)
    search_fields = ('nome', 'globalid')