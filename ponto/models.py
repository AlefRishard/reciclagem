from django.contrib.gis.db import models

class Ponto(models.Model):
    nmunic = models.CharField(max_length=40)
    globalid = models.CharField(max_length=38)
    geom = models.PointField(srid=4326)

    def __str__(self):
        return f"{self.nmunic} - {self.globalid}"
    
    @property
    def popup_content(self):
        popup = f"<span>Município:</span> {self.nmunic}"
        popup += f"<br><span>Global ID:</span> {self.globalid}"
        return popup
