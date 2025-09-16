# bairro/models.py
from django.contrib.gis.db import models

class Bairro(models.Model):
    objectid = models.BigIntegerField()
    nome = models.CharField(max_length=50)
    shape_leng = models.FloatField()
    globalid = models.CharField(max_length=38)
    shape_le_1 = models.FloatField()
    shape_area = models.FloatField()
    geom = models.MultiPolygonField(srid=4326)

    def __str__(self):
        return self.nome