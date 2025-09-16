
from .models import Ponto
from djgeojson.views import GeoJSONLayerView
from django.shortcuts import render


class PontoGeojson(GeoJSONLayerView):
    model = Ponto
    properties = ('popup_content',)


def pontos_js(request):
    pontos = Ponto.objects.all()

    context = {
        'object_list' : pontos,
    }
    return render(request, 'ponto/pontos_js.html', context, content_type='application/javascript')