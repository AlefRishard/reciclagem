import os
from django.contrib.gis.utils import LayerMapping
from .models import Bairro

bairro_mapping = {
    'objectid': 'objectid',
    'nome': 'nome',
    'shape_leng': 'shape_leng',
    'globalid': 'globalid',
    'shape_le_1': 'Shape_Le_1',
    'shape_area': 'Shape_Area',
    'geom': 'MULTIPOLYGON',
}


shp = os.path.abspath(os.path.join('data', 'bairros.shp'))


def run_bairros(verbase=True):
    lm = LayerMapping(Bairro, shp, bairro_mapping)
    lm.save(strict=True, verbose=True)