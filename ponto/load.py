import os
from django.contrib.gis.utils import LayerMapping
from .models import Ponto

ponto_mapping = {
    'nmunic': 'nmunic',
    'globalid': 'globalid',
    'geom': 'POINT',
}



shp = os.path.abspath(os.path.join('data', 'pontos.shp'))


def run_pontos(verbase=True):
    lm = LayerMapping(Ponto, shp, ponto_mapping)
    lm.save(strict=True, verbose=True)