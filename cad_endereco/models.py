from django.db import models
from django.contrib.gis.geos import Point
from geopy.geocoders import ArcGIS
from ponto.models import Ponto 

class Endereco(models.Model):
    ponto = models.OneToOneField(Ponto, on_delete=models.CASCADE, null=True, blank=True)
    
    rua = models.CharField(max_length=200)
    numero = models.CharField(max_length=10)
    bairro = models.CharField(max_length=100)
    cidade = models.CharField(max_length=100, default='Manaus')
    cep = models.CharField(max_length=20, blank=True)

    def __str__(self):
        return f"{self.rua}, {self.numero}"

    def save(self, *args, **kwargs):
        if self.ponto_id is None:
            try:
                cep_limpo = self.cep.replace('-', '').replace('.', '').strip() if self.cep else ""

                busca_prioritaria = f"{self.rua} {self.numero}, {self.bairro}, {self.cidade}, {cep_limpo}, Brasil"
                
                #print(f"busca: {busca_prioritaria}")
                geolocator = ArcGIS(timeout=10)
                location = geolocator.geocode(busca_prioritaria)

                if not location:
                     #print("busca sem cep")
                     busca_secundaria = f"{self.rua}, {self.numero}, {self.bairro}, {self.cidade}, Amazonas"
                     location = geolocator.geocode(busca_secundaria)


                if location:
                    geom_final = Point(location.longitude, location.latitude)
                    #print(f" Coordenada: {location.latitude}, {location.longitude}")
                    
                    novo_ponto = Ponto.objects.create(
                        geom=geom_final,
                        nmunic=self.cidade
                    )
                    self.ponto = novo_ponto
                
                
            except Exception as e:
                print(f"Erro: {e}")

        super(Endereco, self).save(*args, **kwargs)