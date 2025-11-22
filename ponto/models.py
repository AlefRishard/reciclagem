from django.contrib.gis.db import models

class Ponto(models.Model):
    nmunic = models.CharField(max_length=40)
    globalid = models.CharField(max_length=38)
    geom = models.PointField(srid=4326)

    def __str__(self):
        return f"{self.nmunic} - {self.globalid}"
    
    @property
    def popup_content(self):
        popup = f"<b>Município:</b> {self.nmunic}"
        popup += f"<br><b>Global ID:</b> {self.globalid}"

        if hasattr(self, 'endereco'):
            popup += f"<hr style='margin: 5px 0;'>"
            popup += f"<b>Rua:</b> {self.endereco.rua}"
            popup += f"<br><b>Número:</b> {self.endereco.numero}"
            popup += f"<br><b>Bairro:</b> {self.endereco.bairro}"
            
        return popup