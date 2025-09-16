from django.contrib import admin
from .models import Ponto
from leaflet.admin import LeafletGeoAdmin

@admin.register(Ponto)
class PontoAdmin(LeafletGeoAdmin):
    list_display = ('nmunic', 'globalid', 'geom')
    search_fields = ('nmunic', 'globalid')

